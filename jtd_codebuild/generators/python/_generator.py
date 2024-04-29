import ast
from ast import (
    ClassDef,
    Name,
    Load,
    AnnAssign,
    Constant,
    Import,
    ImportFrom,
    FunctionDef,
    Expr,
    Call,
    alias,
)
from os.path import dirname, join
from io import TextIOWrapper
from typing import Type, Any
from toolz import pipe
from toolz.curried import filter, map, first, complement, curry
from jtd_codebuild.config.project.model import PythonTarget
from jtd_codebuild.utils.io import read
from jtd_codebuild.utils.string import caseconverter
from jtd_codebuild.utils.function import replace, chain
from .._values import ROOT_SCHEMA_NAMES
from .._generator import JTDCodeGenerator

SUBSCRIPTABLE_SOURCE_CODE = read(
    join(
        dirname(__file__),
        "..",
        "utils/mapping/_subscriptable.py",
    )
)


class PythonJTDCodeGenerator(JTDCodeGenerator):
    """Generate Python code from the JSON Type Definition files."""

    def generate(self, target: PythonTarget) -> None:  # noqa: C901
        # Generate the target
        super().generate(target)

        # Open the schema file
        with self._open_schema_file(target, "r") as f:
            code = f.read()

        # Parse the schema file
        parsed = ast.parse(code)

        imports: list[Import] = select_nodes_with_type(Import, parsed.body)
        importfroms: list[ImportFrom] = select_nodes_with_type(ImportFrom, parsed.body)
        classes: list[ClassDef] = select_nodes_with_type(ClassDef, parsed.body)
        functions: list[FunctionDef] = select_nodes_with_type(FunctionDef, parsed.body)
        calls: list[Call] = []

        should_remove_dataclass_decorator = target.typingBackend in [
            "pydantic",
            "typed-dictionary",
        ]
        should_remove_dataclass_imports = target.typingBackend in [
            "pydantic",
            "pydantic-dataclass",
            "typed-dictionary",
        ]
        should_add_json_codec_methods = target.typingBackend in [
            "dataclass",
            "pydantic-dataclass",
        ]

        # Remove root schema from the file if the option is set
        if target.removeRootSchema:
            classes = pipe(
                classes,
                filter(lambda node: node.name in ROOT_SCHEMA_NAMES),
                list,
            )

        if should_remove_dataclass_imports:
            importfroms = remove_dataclass_imports(importfroms)

        if target.typingBackend == "pydantic-dataclass":
            # Add pydantic dataclass imports if the option is set
            importfroms.append(
                create_importfrom_directive(
                    "pydantic.dataclasses",
                    ["dataclass", "rebuild_directive"],
                )
            )

            # Add rebuild_dataclass directives for all classes
            for class_ in classes:
                calls.append(create_call_directive("rebuild_dataclass", [class_.name]))

        if target.typingBackend == "pydantic":
            # Add pydantic BaseModel imports
            importfroms.append(create_importfrom_directive("pydantic", ["BaseModel"]))

        if target.typingBackend == "typed-dictionary":
            # Add TypedDict imports
            typing_imports = find_import_from_node(importfroms, "typing")
            typing_imports.names.append(alias(name="TypedDict"))

        for node in classes:
            # Remove json codec methods
            node = remove_json_codec(node)

            if target.typingBackend == "pydantic":
                # Inherit from BaseModel if typing backend is pydantic
                node.bases.append(Name(id="BaseModel", ctx=Load()))

            if target.typingBackend == "typed-dictionary":
                # Inherit from TypedDict if typing backend is typed-dictionary
                node.bases.append(Name(id="TypedDict", ctx=Load()))

            if should_remove_dataclass_decorator:
                node.decorator_list = remove_dataclass_decorator(node.decorator_list)

            # Inherit from Subscriptable if the option is set
            if target.subscriptable:
                node.bases.append(Name(id="Subscriptable", ctx=Load()))

            properties: list[AnnAssign] = select_nodes_with_type(AnnAssign, node.body)
            for property in properties:
                # Change type annotations to actual implementations
                annotation: str = property.annotation.value
                property.annotation.value = pipe(
                    annotation,
                    replace("Dict", "dict"),
                    replace("Any", "object"),
                    replace("List", "list"),
                )

                # Add `None` to optional fields
                if annotation.startswith("Optional"):
                    property.value = Constant(value=None)

                # Convert property names to given format if given
                if target.propertyFormat:
                    property.target.id = caseconverter(
                        target.propertyFormat,
                        property.target.id,
                    )

            if should_add_json_codec_methods:
                node = create_json_codec_methods(node)

        # Add subscriptable code if the option is set
        if target.subscriptable:
            subscriptable = ast.parse(SUBSCRIPTABLE_SOURCE_CODE)
            classes = subscriptable.body + classes

        # Merge every nodes
        nodes = imports + importfroms + classes + functions + calls

        # Write back the code
        code = (
            "# Code generated by jtd-codebuild\n"
            + "# flake8: noqa\n"
            + "# pylint: skip-file\n"
            + ast.unparse(nodes)
        )
        with self._open_schema_file(target, "w") as f:
            f.write(code)

    def _open_schema_file(self, target: PythonTarget, mode: str) -> TextIOWrapper:
        output_dir = join(self.get_target_path(target), "__init__.py")
        return open(output_dir, mode)


def create_importfrom_directive(
    module: str,
    names: list[str] = [],
) -> ImportFrom:
    return ast.parse(f'from {module} import {", ".join(names)}').body[0]


def create_call_directive(
    func: str,
    args: list[str] = [],
    kwargs: dict[str, str] = {},
) -> Expr:
    return ast.parse(
        func
        + "("
        + ", ".join(args)
        + ", "
        + ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        + ")"
    ).body[0]


def select_nodes_with_type(type: Type, nodes: list[Any]) -> list[Any]:
    return pipe(
        nodes,
        filter(lambda node: isinstance(node, type)),
        list,
    )


def find_import_from_node(importfroms: list[ImportFrom], module: str) -> ImportFrom:
    return pipe(
        importfroms,
        filter(lambda node: node.module == module),
        list,
        first,
    )


def space(level: int, code: str) -> str:
    return "\n".join([f"{' ' * level}{line}" for line in code.split("\n")])


def create_json_codec_methods(class_: ClassDef) -> ClassDef:
    properties = select_nodes_with_type(AnnAssign, class_.body)
    methods = "\n".join(
        [
            # `from_json_data`_ method
            "@classmethod" f"def from_json_data(cls, data: Any) -> '{class_.name}':",
            space(
                4,
                "return cls(",
            ),
            *pipe(
                properties,
                map(
                    lambda property: (
                        f"_from_json_data({property.annotation.value}, "
                        f"data.get('{property.target.id}'))",
                    )
                ),
                map(curry(space)(8)),
            ),
            space(4, ")"),
            # `to_json_data`_ method
            "def to_json_data(self) -> Any:",
            space(4, r"data: dict[str, Any] = {}"),
            *pipe(
                properties,
                map(
                    lambda property: (
                        f"if self.{property.target.id} is not None:",
                        (
                            f"    data['{property.target.id}'] "
                            f"= _to_json_data(self.{property.target.id})"
                        ),
                    ),
                ),
                map(map(curry(space)(8))),
                chain,
            ),
            space(4, "return data"),
        ]
    )
    class_.body.extend(ast.parse(methods).body)
    return class_


def remove_dataclass_imports(importfroms: list[ImportFrom]):
    return pipe(
        importfroms,
        filter(lambda node: node.module != "dataclasses"),
        list,
    )


def remove_dataclass_decorator(decorator_list: list[Name]):
    return pipe(
        decorator_list,
        filter(lambda node: node.id != "dataclass"),
        list,
    )


def is_json_codec_method(node: Any) -> bool:
    return isinstance(node, FunctionDef) and node.name in [
        "from_json_data",
        "to_json_data",
    ]


def remove_json_codec(class_: ClassDef):
    class_.body = pipe(
        class_.body,
        filter(complement(is_json_codec_method)),
        list,
    )
    return class_
