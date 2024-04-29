from typing import Generator, Tuple
from toolz import pipe
from jtd_codebuild.config.project.model import TypescriptTarget
from jtd_codebuild.utils.io import read_json, write_json, read, write
from jtd_codebuild.utils.function import replace
from jtd_codebuild.utils.string import caseconverter
from .._generator import JTDCodeGenerator


class TypescriptJTDCodeGenerator(JTDCodeGenerator):
    """Generate Typescript code from the JSON Type Definition files."""

    def generate(self, target: TypescriptTarget) -> None:
        jtd_schema_path = self.get_schema_path(target)

        jtd_schema = read_json(jtd_schema_path)
        definitions: dict = jtd_schema.get("definitions", {})

        def convert_schema_definition_keys(
            properties: dict,
        ) -> Generator[Tuple[str, dict], None, None]:
            for property_name, property_definition in properties.items():
                yield caseconverter(
                    target.propertyFormat, property_name
                ), property_definition

        for class_name in definitions.keys():
            definition = definitions[class_name]
            definition["properties"] = pipe(
                definition.get("properties", {}),
                convert_schema_definition_keys,
                dict,
            )
            definition["optionalProperties"] = pipe(
                definition.get("optionalProperties", {}),
                convert_schema_definition_keys,
                dict,
            )

        write_json(jtd_schema_path, jtd_schema)

        # Generate the target
        super().generate(target)

        target_path = self.get_target_path(target)
        schema = read(jtd_schema_path)

        if target.removeRootSchema:
            schema = pipe(
                schema,
                replace("export type Schema = any;"),
                replace("export type JtdSchema = any;"),
            )

        write(target_path, schema)
