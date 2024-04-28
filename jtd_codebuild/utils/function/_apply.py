from typing import Callable, Any, Iterable, TypeAlias, Generator, TypeVar

Predicate: TypeAlias = Callable[[Any], bool]
Callback: TypeAlias = Callable[[Any], Any]


def applyif(
    predicate: Predicate,
    callback: Callback,
):
    T = TypeVar("T")

    def applier(items: Iterable[T]) -> Generator[T, None, None]:
        for i, item in enumerate(items):
            if predicate(item):
                yield callback(item)
            else:
                yield item

    return applier
