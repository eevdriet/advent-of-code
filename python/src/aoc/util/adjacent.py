from collections.abc import Generator
from functools import partial
from itertools import product
from typing import Callable, overload

from aoc.util.func import pairwise_sum

Coord2D = complex | tuple[int, int]
Coord = complex | tuple[int, ...]
Direction = complex | tuple[int, ...]


@overload
def directions4(coord: complex, include_zero: bool = False) -> Generator[complex]: ...
@overload
def directions4(
    coord: tuple[int, int], include_zero: bool = False
) -> Generator[tuple[int, int]]: ...
@overload
def directions4(
    coord: tuple[int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int]]: ...
@overload
def directions4(
    coord: tuple[int, int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int, int]]: ...
@overload
def directions4(
    coord: tuple[int, ...], include_zero: bool = False
) -> Generator[tuple[int, ...]]: ...


def directions4(coord: Coord, include_zero: bool = False) -> Generator[Direction]:
    if isinstance(coord, complex):
        yield from [-1 + 0j, 1 + 0j, -1j, 1j] + ([0j] if include_zero else [])

    elif isinstance(coord, tuple):
        for deltas in product((-1, 0, 1), repeat=len(coord)):
            match sum(delta != 0 for delta in deltas):
                case 1:
                    yield deltas
                case 0 if len(coord) and include_zero:
                    yield deltas
                case _:
                    continue
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
def adjacent4(coord: complex, include_zero: bool = False) -> Generator[complex]: ...
@overload
def adjacent4(
    coord: tuple[int, int], include_zero: bool = False
) -> Generator[tuple[int, int]]: ...
@overload
def adjacent4(
    coord: tuple[int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int]]: ...
@overload
def adjacent4(
    coord: tuple[int, int, int, int], include_zero: bool = False
) -> Generator[tuple[int, int, int, int]]: ...
@overload
def adjacent4(
    coord: tuple[int, ...], include_zero: bool = False
) -> Generator[tuple[int, ...]]: ...


def adjacent4(coord: Coord, include_zero: bool = False) -> Generator[Coord]:
    return adjacent(coord, partial(directions4, include_zero=include_zero))


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
