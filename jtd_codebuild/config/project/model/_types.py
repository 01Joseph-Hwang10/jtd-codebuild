from typing import Literal, TypeAlias

DuplicatePolicy: TypeAlias = Literal["error", "allow"]
PropertyFormat: TypeAlias = Literal["snake", "camel", "pascal"]
Language: TypeAlias = Literal[
    "python",
    "typescript",
    "go",
    "rust",
    "csharp-system-text",
    "ruby",
    "java-jackson",
]
