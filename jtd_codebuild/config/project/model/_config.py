from pydantic import BaseModel
from ._types import DuplicatePolicy
from ._target import (
    PythonTarget,
    TypescriptTarget,
    GoTarget,
    JavaTarget,
    CSharpTarget,
    RustTarget,
    RubyTarget,
)
from jtd_codebuild.utils.mapping import Subscriptable


class ProjectConfig(BaseModel, Subscriptable):
    include: list[str]
    references: list[str]
    targets: list[
        PythonTarget
        | TypescriptTarget
        | GoTarget
        | JavaTarget
        | CSharpTarget
        | RustTarget
        | RubyTarget
    ]
    jtdBundlePath: str = "gen/schema.jtd.json"
    duplicate: DuplicatePolicy = "error"
