from collections.abc import Generator
from typing import Generic, TypeVar

from aoc.util import Coord2D, adjacent4, adjacent8

T = TypeVar("T")
S = TypeVar("S")


class Grid(dict[tuple[int, ...], T], Generic[T]):
    @property
    def min_dims(self) -> tuple[int | None, ...]:
        if not self:
            return tuple()

        n_dims = len(next(iter(self)))

        return tuple(
            min((coord[dim] for coord in self), default=None) for dim in range(n_dims)
        )

    @property
    def max_dims(self) -> tuple[int | None, ...]:
        if not self:
            return tuple()

        n_dims = len(next(iter(self)))

        return tuple(
            max((coord[dim] for coord in self), default=None) for dim in range(n_dims)
        )

    def in_bounds(self, coord: tuple[int, ...]) -> bool:
        min_dims = self.min_dims
        max_dims = self.max_dims

        return all(
            min_ and max_ and axis in range(min_, max_ + 1)
            for axis, min_, max_ in zip(coord, min_dims, max_dims)
        )

    def neighbors4(self, coord: tuple[int, ...]) -> Generator[tuple[int, ...]]:
        for neighbor in adjacent4(coord):
            if self.in_bounds(neighbor):
                yield neighbor

    def neighbors8(self, coord: tuple[int, ...]) -> Generator[tuple[int, ...]]:
        for neighbor in adjacent8(coord):
            if self.in_bounds(neighbor):
                yield neighbor


class Grid2D(Grid[T]):
    @classmethod
    def _coord_to_rc(cls, coord: Coord2D) -> tuple[int, int]:
        if isinstance(coord, complex):
            return int(coord.imag), int(coord.real)

        return coord

    @property
    def min_row(self) -> int | None:
        min_row, _ = self.min_dims
        return min_row

    @property
    def min_col(self) -> int | None:
        _, min_col = self.min_dims
        return min_col

    @property
    def max_row(self) -> int | None:
        max_row, _ = self.max_dims
        return max_row

    @property
    def max_col(self) -> int | None:
        _, max_col = self.max_dims
        return max_col

    @property
    def n_rows(self) -> int:
        min_ = self.min_row
        max_ = self.max_row

        return (max_ - min_ + 1) if min_ and max_ else 0

    @property
    def n_cols(self) -> int:
        min_ = self.min_col
        max_ = self.max_col

        return (max_ - min_ + 1) if min_ and max_ else 0
