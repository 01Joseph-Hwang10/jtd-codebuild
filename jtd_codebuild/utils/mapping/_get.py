from typing import Dict, AnyStr, Any, List


def get_items(obj: Dict[AnyStr, Any]) -> List[Any]:
    return obj.items()


def get_values(obj: Dict[AnyStr, Any]) -> List[Any]:
    return obj.values()


def get_keys(obj: Dict[AnyStr, Any]) -> List[Any]:
    return obj.keys()
