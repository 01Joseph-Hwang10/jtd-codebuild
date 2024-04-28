import os
from typing import Any, AnyStr


def file_is_yaml(file: AnyStr) -> bool:
    """Check if a file is a YAML file.

    Args:
        file: The file name.

    Returns:
        True if the file is a YAML file, False otherwise.
    """
    return file.endswith((".yaml", ".yml"))


def file_is_json(file: AnyStr) -> bool:
    """Check if a file is a JSON file.

    Args:
        file: The file name.

    Returns:
        True if the file is a JSON file, False otherwise.
    """
    return file.endswith(".json")


def safe_mkdir(path: AnyStr) -> None:
    """Create a directory with creating its parent directories if they do not exist.

    Args:
        path: The directory path.
    """
    os.makedirs(path, exist_ok=True)


def safe_open(file_path: AnyStr, mode: AnyStr) -> Any:
    """Open a file with creating its parent directories if they do not exist.

    Args:
        file_path: The file path.
        mode: The file open mode.

    Returns:
        The opened file.
    """
    safe_mkdir(os.path.dirname(file_path))
    return open(file_path, mode)
