from collections.abc import Generator, Iterable, Iterator
from itertools import chain, combinations
from math import floor, log10


def minmax(a: int, b: int):
    return min([a, b]), max([a, b])


def sign(num: int | float) -> int | float:
    ans = 1.0 if num > 0 else -1.0 if num < 0 else 0
    ans = int(ans) if isinstance(num, int) else ans

    return ans


def n_digits(num: int) -> int:
    return floor(log10(num)) + 1


def ends_with(target: int, right: int) -> bool:
    return (target - right) % (10 ** n_digits(right)) == 0


def partitions(total: int, n: int) -> Generator[tuple[int, ...], None, None]:
    if n == 2:
        for amount in range(total + 1):
            yield (amount, total - amount)
    else:
        for amount in range(total + 1):
            for partition in partitions(total - amount, n - 1):
                yield (amount,) + partition


def pairwise_sum(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    """
    Compute the pairwise sum of two points

    :param x: First point
    :param y: Second point
    :return: Pairwise sum of the points
    """
    assert len(x) == len(y)

    return tuple(map(sum, zip(x, y)))


def combinations_xy(iterable: Iterable, rs: range) -> Iterator[tuple]:
    return chain.from_iterable(combinations(iterable, r) for r in rs)
