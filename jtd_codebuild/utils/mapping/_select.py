from typing import Any, AnyStr, Dict


def select(key: AnyStr):
    """Create a selector function that selects a value from a dictionary."""

    def selector(obj: Dict[AnyStr, Any]) -> Any:
        return obj[key]

    return selector
