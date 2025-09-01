from collections import defaultdict
from itertools import combinations
from typing import TextIO

from aoc.io import FileType, open_file
from aoc.util import Point, pairwise_sum
from attrs import define

YEAR = 2024
DAY = 8


@define
class Grid:
    antennas: dict[str, set[Point]]
    n_rows: int
    n_cols: int

    def contains(self, point: Point):
        return 0 <= point[0] < self.n_rows and 0 <= point[1] < self.n_cols


def parse(file: TextIO) -> Grid:
    lines = file.read().splitlines()

    n_rows = len(lines)
    n_cols = len(lines[0])
    antennas = defaultdict(set)

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            if cell != ".":
                pos = (row, col)
                antennas[cell].add(pos)

    return Grid(antennas, n_rows, n_cols)


def part1(grid: Grid) -> int:
    nodes: set[Point] = set()

    for coords in grid.antennas.values():
        for (row1, col1), (row2, col2) in combinations(coords, r=2):
            node1 = (2 * row1 - row2, 2 * col1 - col2)
            if grid.contains(node1):
                nodes.add(node1)

            node2 = (2 * row2 - row1, 2 * col2 - col1)
            if grid.contains(node2):
                nodes.add(node2)

    return len(nodes)


def part2(grid: Grid) -> int:
    nodes: set[Point] = set()

    for coords in grid.antennas.values():
        for (row1, col1), (row2, col2) in combinations(coords, r=2):
            node1 = (row1, col1)

            while grid.contains(node1):
                nodes.add(node1)
                node1 = (node1[0] + row1 - row2, node1[1] + col1 - col2)

            node2 = (row2, col2)

            while grid.contains(node2):
                nodes.add(node2)
                node2 = (node2[0] + row2 - row1, node2[1] + col2 - col1)

    return len(nodes)


def main():
    with open_file(YEAR, DAY, FileType.INPUT) as file:
        grid = parse(file)

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    main()
