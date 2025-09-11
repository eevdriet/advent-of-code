import sys

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Coord = tuple[int, int]
Slope = tuple[int, int]


@define
class Toboggan:
    trees: set[Coord]
    n_rows: int
    n_cols: int

    @classmethod
    def parse(cls, input: str) -> "Toboggan":
        cells = [[cell for cell in row] for row in input.splitlines()]

        n_rows = len(cells)
        n_cols = len(cells[0])
        trees = {
            (r, c)
            for r, row in enumerate(cells)
            for c, cell in enumerate(row)
            if cell == "#"
        }

        return cls(trees, n_rows, n_cols)

    def count_trees(self, slopes: list[Slope]) -> int:
        total_count = 1

        for dc, dr in slopes:
            count = 0
            row, col = 0, 0

            while row < self.n_rows:
                count += (row, col) in self.trees
                row += dr
                col = (col + dc) % self.n_cols

            total_count *= count

        return total_count


def parse(input: str) -> Toboggan:
    return Toboggan.parse(input)


def part1(toboggan: Toboggan) -> int:
    return toboggan.count_trees([(3, 1)])


def part2(toboggan: Toboggan) -> int:
    return toboggan.count_trees([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2020, 3, "example1")
    part1(parse(input))
