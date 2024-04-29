from typing import Literal, Self
from pydantic import BaseModel, model_validator
from ._types import PropertyFormat, Language
from jtd_codebuild.utils.mapping import Subscriptable


class Target(BaseModel, Subscriptable):
    language: Language
    path: str
    propertyFormat: PropertyFormat | None = None
    removeRootSchema: bool = True


PythonTypingBackend = Literal[
    "pydantic",
    "pydantic-dataclass",
    "dataclass",
    "typed-dictionary",
]


class PythonTarget(Target):
    language: Literal["python"]
    typingBackend: PythonTypingBackend = "dataclass"
    subscriptable: bool = False

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.typingBackend == "typed-dictionary" and self.subscriptable:
            raise ValueError("Typed dictionaries do not support subscriptable")
        return self


class TypescriptTarget(Target):
    language: Literal["typescript"]


class GoTarget(Target):
    language: Literal["go"]
    package: str


class JavaTarget(Target):
    language: Literal["java"]
    package: str


class CSharpTarget(Target):
    language: Literal["csharp"]
    namespace: str


class RustTarget(Target):
    language: Literal["rust"]


class RubyTarget(Target):
    language: Literal["ruby"]
    module: str
