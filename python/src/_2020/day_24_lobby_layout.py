import re
import sys
from collections import defaultdict
from collections.abc import Generator

from aoc.util import timed


class HexGrid:
    __DIRECTIONS: dict[str, complex] = {
        "e": 2 + 0j,
        "w": -2 + 0j,
        "ne": 1 - 2j,
        "nw": -1 - 2j,
        "se": 1 + 2j,
        "sw": -1 + 2j,
    }

    def __init__(self, pos: complex = 0):
        self.pos: complex = pos
        self.flipped_tiles: set[complex] = set()

    def move(self, dir_str: str):
        dir = self.__DIRECTIONS[dir_str]

        self.pos += dir

    def flip(self, pos: complex | None = None):
        pos = self.pos if pos is None else pos

        self.flipped_tiles ^= {pos}

    def flip_tiles(self, tiles_dirs: list[list[str]]):
        for dirs in tiles_dirs:
            # Start from the center and move to the tile to flip
            self.pos = 0

            for dir_str in dirs:
                self.move(dir_str)

            # Flip the tile
            self.flip()

    def evolve_tiles(self, n_days: int):
        for _ in range(n_days):
            # Count how many (flipped) neighbors each tile has
            neighbor_counts = defaultdict(int)

            for tile in self.flipped_tiles:
                for neighbor in self.neighbors(tile):
                    neighbor_counts[neighbor] += 1

            # Determine which tiles stay flipped and will flip
            stay_flipped = {
                tile for tile in self.flipped_tiles if neighbor_counts[tile] in (1, 2)
            }
            turn_flipped = {
                tile
                for tile, count in neighbor_counts.items()
                if tile not in self.flipped_tiles and count == 2
            }

            self.flipped_tiles = stay_flipped | turn_flipped

    def neighbors(self, pos: complex | None = None) -> Generator[complex]:
        pos = self.pos if pos is None else pos

        for dir in self.__DIRECTIONS.values():
            yield pos + dir


def parse(input: str) -> list[list[str]]:
    return [
        [dir_str for dir_str in re.findall(r"(se|sw|nw|ne|e|w)", line.strip())]
        for line in input.splitlines()
    ]


def part1(tiles_dirs: list[list[str]]) -> int:
    grid = HexGrid()
    grid.flip_tiles(tiles_dirs)

    return len(grid.flipped_tiles)


def part2(tiles_dirs: list[list[str]], n_days: int = 100) -> int:
    grid = HexGrid()
    grid.flip_tiles(tiles_dirs)
    grid.evolve_tiles(n_days)

    return len(grid.flipped_tiles)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
