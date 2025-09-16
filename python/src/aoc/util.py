import time
from collections.abc import Generator, Iterable, Iterator
from functools import partial
from itertools import chain, combinations, product
from math import floor, log10
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    overload,
)

Coord2D = complex | tuple[int, int]
Coord = complex | tuple[int, ...]
Direction = complex | tuple[int, ...]

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")


@overload
def timed(func: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> tuple[R, str]: ...


@overload
def timed(func: Callable[P, R]) -> Callable[P, tuple[R, str]]: ...


def timed(func: Callable, *args, **kwargs):
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


@overload
def directions4(coord: complex) -> Generator[complex]: ...
@overload
def directions4(coord: tuple[int, int]) -> Generator[tuple[int, int]]: ...
@overload
def directions4(coord: tuple[int, int, int]) -> Generator[tuple[int, int, int]]: ...
@overload
def directions4(
    coord: tuple[int, int, int, int],
) -> Generator[tuple[int, int, int, int]]: ...
@overload
def directions4(coord: tuple[int, ...]) -> Generator[tuple[int, ...]]: ...


def directions4(coord: Coord) -> Generator[Direction]:
    if isinstance(coord, complex):
        yield from [-1 + 0j, 1 + 0j, -1j, 1j]

    elif isinstance(coord, tuple):
        for deltas in product((-1, 0, 1), repeat=len(coord)):
            if sum(delta != 0 for delta in deltas) != 1:
                continue

            yield deltas
    else:
        raise TypeError(f"Unsupported coordinate type: {type(coord)}")


@overload
def directions8(coord: complex, include_zero: bool = False) -> Generator[complex]: ...
@overload
def directions8(
    coord: tuple[int, int], include_zero: bool = False
) -> Generator[tuple[int, int]]: ...
@overload
def directions8(
    coord: tuple[int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int]]: ...
@overload
def directions8(
    coord: tuple[int, int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int, int]]: ...
@overload
def directions8(
    coord: tuple[int, ...], include_zero: bool = False
) -> Generator[tuple[int, ...]]: ...


def directions8(coord: Coord, include_zero: bool = False) -> Generator[Direction]:
    if isinstance(coord, complex):
        for deltas in product([-1j, 0j, 1j], [-1, 0, 1]):
            if not include_zero and all(delta == 0 for delta in deltas):
                continue

            yield sum(deltas)

    elif isinstance(coord, tuple):
        for deltas in product((-1, 0, 1), repeat=len(coord)):
            if not include_zero and all(delta == 0 for delta in deltas):
                continue

            yield deltas
    else:
        raise TypeError(f"Unsupported coordinate type: {type(coord)}")


@overload
def adjacent(
    coord: complex, directions: Callable[[complex], Generator[complex]]
) -> Generator[complex]: ...


@overload
def adjacent(
    coord: tuple[int, int],
    directions: Callable[[tuple[int, int]], Generator[tuple[int, int]]],
) -> Generator[tuple[int, int]]: ...


@overload
def adjacent(
    coord: tuple[int, int, int],
    directions: Callable[[tuple[int, int, int]], Generator[tuple[int, int, int]]],
) -> Generator[tuple[int, int, int]]: ...


@overload
def adjacent(
    coord: tuple[int, int, int, int],
    directions: Callable[
        [tuple[int, int, int, int]], Generator[tuple[int, int, int, int]]
    ],
) -> Generator[tuple[int, int, int, int]]: ...


def adjacent(
    coord: Coord, directions: Callable[[Coord], Generator[Direction]]
) -> Generator[Coord]:
    for dir in directions(coord):
        if isinstance(coord, complex) and isinstance(dir, complex):
            yield coord + dir

        elif isinstance(coord, tuple) and isinstance(dir, tuple):
            yield pairwise_sum(coord, dir)

        else:
            raise TypeError(
                f"Unsupported coordinate ({type(coord)}) and direction ({type(dir)}) type pair: "
            )


@overload
def adjacent4(coord: complex) -> Generator[complex]: ...
@overload
def adjacent4(coord: tuple[int, int]) -> Generator[tuple[int, int]]: ...
@overload
def adjacent4(coord: tuple[int, int, int]) -> Generator[tuple[int, int, int]]: ...
@overload
def adjacent4(
    coord: tuple[int, int, int, int],
) -> Generator[tuple[int, int, int, int]]: ...
@overload
def adjacent4(coord: tuple[int, ...]) -> Generator[tuple[int, ...]]: ...


def adjacent4(coord: Coord) -> Generator[Coord]:
    return adjacent(coord, directions4)


@overload
def adjacent8(coord: complex, include_zero: bool = False) -> Generator[complex]: ...
@overload
def adjacent8(
    coord: tuple[int, int], include_zero: bool = False
) -> Generator[tuple[int, int]]: ...
@overload
def adjacent8(
    coord: tuple[int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int]]: ...
@overload
def adjacent8(
    coord: tuple[int, int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int, int]]: ...
@overload
def adjacent8(coord: tuple[int, ...]) -> Generator[tuple[int, ...]]: ...


def adjacent8(coord: Coord, include_zero: bool = False) -> Generator[Coord]:
    return adjacent(coord, partial(directions8, include_zero=include_zero))


def combinations_xy(iterable: Iterable, rs: range) -> Iterator[tuple]:
    return chain.from_iterable(combinations(iterable, r) for r in rs)
