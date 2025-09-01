import time
from itertools import chain, combinations, product
from math import floor, log10
from typing import (Callable, Generator, Iterable, Iterator, Optional,
                    ParamSpec, Tuple, TypeVar, overload)

Point = tuple[int, ...]

P = ParamSpec("P")
R = TypeVar("R")


@overload
def timed(func: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> tuple[R, str]: ...


@overload
def timed(func: Callable[P, R]) -> Callable[P, tuple[R, str]]: ...


def timed(func, *args, **kwargs):
    def format_duration(seconds: float) -> str:
        if seconds >= 1:
            return f"{seconds:.3f} s"
        elif seconds >= 1e-3:
            return f"{seconds * 1e3:.3f} ms"
        elif seconds >= 1e-6:
            return f"{seconds * 1e6:.3f} µs"
        else:
            return f"{seconds * 1e9:.3f} ns"

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = format_duration(end - start)
        return result, elapsed

    return wrapper(*args, **kwargs) if args or kwargs else wrapper


def minmax(*items):
    return min(items), max(items)


def sign(num: int | float) -> int | float:
    ans = 1.0 if num > 0 else -1.0 if num < 0 else 0
    ans = int(ans) if isinstance(num, int) else ans

    return ans


def n_digits(num: int) -> int:
    return floor(log10(num)) + 1


def ends_with(target: int, right: int) -> bool:
    return (target - right) % (10 ** n_digits(right)) == 0


def partitions(total: int, n: int) -> Generator[Tuple[int, ...], None, None]:
    if n == 2:
        for amount in range(total + 1):
            yield (amount, total - amount)
    else:
        for amount in range(total + 1):
            for partition in partitions(total - amount, n - 1):
                yield (amount,) + partition


def pairwise_sum(x: Point, y: Point) -> Point:
    """
    Compute the pairwise sum of two points

    :param x: First point
    :param y: Second point
    :return: Pairwise sum of the points
    """
    assert len(x) == len(y)

    return tuple(map(sum, zip(x, y)))


def adjacent4(point: Point) -> Iterator[Point]:
    """
    Generate points horizontally or vertically adjacent to a given point with variable dimension

    :param point: Point to find neighbors for
    :yield: Points adjacent to the given point
    """
    for deltas in product((-1, 0, 1), repeat=len(point)):
        if sum(delta != 0 for delta in deltas) != 1:
            continue

        yield pairwise_sum(point, deltas)


def adjacent8(point: Point, *, bounds: Optional[Point] = None) -> Iterator[Point]:
    """
    Generate points horizontally, vertically or diagonally adjacent to a given point with variable dimension

    :param point: Point to find neighbors for
    :yield: Points adjacent to the given point
    """
    for deltas in product((-1, 0, 1), repeat=len(point)):
        if all(delta == 0 for delta in deltas):
            continue

        result = pairwise_sum(point, deltas)
        if bounds is None or all(0 <= dim < bound for dim, bound in zip(result, bounds)):
            yield result


def combinations_xy(iterable: Iterable, rs: range) -> Iterator[tuple]:
    return chain.from_iterable(combinations(iterable, r) for r in rs)
