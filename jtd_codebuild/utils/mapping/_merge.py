from typing import Dict, AnyStr, Any


def shallow_merge(
    a: Dict[AnyStr, Any],
    b: Dict[AnyStr, Any],
) -> Dict[AnyStr, Any]:
    """Merge two dictionaries shallowly.

    Note that `b` will override `a` if there are duplicate keys.
    """
    return {**a.copy(), **b.copy()}


def deep_merge(
    a: Dict[AnyStr, Any],
    b: Dict[AnyStr, Any],
) -> Dict[AnyStr, Any]:
    """Merge two dictionaries deeply.

    Note that `b` will override `a` if there are duplicate keys.
    """
    merged = a.copy()
    for key, value in b.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged
