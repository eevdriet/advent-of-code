import sys
from collections.abc import Generator
from math import prod

from attrs import define

from aoc.util import timed


@define
class Treehouse:
    grid: list[list[int]]

    @property
    def n_rows(self) -> int:
        return len(self.grid)

    @property
    def n_cols(self) -> int:
        return len(self.grid[0])

    def heights(self, row: int, col: int) -> Generator[list[int]]:
        yield [self.grid[row][c] for c in reversed(range(col))]
        yield [self.grid[row][c] for c in range(col + 1, self.n_cols)]
        yield [self.grid[r][col] for r in reversed(range(row))]
        yield [self.grid[r][col] for r in range(row + 1, self.n_rows)]

    def __iter__(self) -> Generator[tuple[int, int]]:
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                yield row, col


def parse(input: str) -> Treehouse:
    grid = [[int(num) for num in row] for row in input.splitlines()]

    return Treehouse(grid)


def part1(treehouse: Treehouse) -> int:
    n_visible = 0

    for row, col in treehouse:
        root = treehouse.grid[row][col]

        is_visible = any(
            all(height < root for height in heights)
            for heights in treehouse.heights(row, col)
        )
        if is_visible:
            n_visible += 1

    return n_visible


def part2(treehouse: Treehouse) -> int:
    def count_trees(heights: list[int], root: int) -> int:
        n_trees = 0

        for height in heights:
            n_trees += 1
            if height >= root:
                break

        return n_trees

    max_score = 0

    for row, col in treehouse:
        root = treehouse.grid[row][col]

        score = prod(
            count_trees(heights, root) for heights in treehouse.heights(row, col)
        )
        if score > max_score:
            max_score = score

    return max_score


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
