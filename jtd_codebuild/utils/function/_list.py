import itertools
from typing import Iterable
from toolz import pipe
from toolz.curried import filter


def filterlist(predicate, source):
    return pipe(
        source,
        filter(predicate),
        list,
    )


def chain(iterable: Iterable):
    return itertools.chain(*iterable)
