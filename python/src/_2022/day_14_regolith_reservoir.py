import sys
from collections import defaultdict
from itertools import pairwise

from attrs import define, field

from aoc.io import read_file
from aoc.util import minmax, timed


@define
class Tiles:
    filled: dict[tuple[int, int], str]
    spring: tuple[int, int] = field(default=(500, 0))


def parse(input: str) -> Tiles:
    filled = defaultdict(lambda: ".")

    for line in input.splitlines():
        for left, right in pairwise(line.split(" -> ")):
            x1, y1 = map(int, left.split(","))
            x2, y2 = map(int, right.split(","))

            x_min, x_max = minmax(x1, x2)
            y_min, y_max = minmax(y1, y2)

            if x1 == x2:
                tiles = [(x1, y) for y in range(y_min, y_max + 1)]
            elif y1 == y2:
                tiles = [(x, y1) for x in range(x_min, x_max + 1)]
            else:
                tiles = []

            for tile in tiles:
                filled[tile] = "#"

    return Tiles(filled)


def drop_sand(tiles: Tiles, *, with_infinite_floor: bool = False):
    y_max = max(y for (_, y), fill in tiles.filled.items() if fill == "#")
    y_floor = y_max + 2 if with_infinite_floor else y_max

    while True:
        # Create the sand grain just below the spring
        x, y = tiles.spring

        while y <= y_floor:
            # Drop sand on the infinite floor if enabled
            if with_infinite_floor and y + 1 == y_floor:
                tiles.filled[(x, y)] = "O"
                break

            # Otherwise, drop the sand normally until it falls to rest
            if (down := (x, y + 1)) not in tiles.filled:
                x, y = down
            elif (left := (x - 1, y + 1)) not in tiles.filled:
                x, y = left
            elif (right := (x + 1, y + 1)) not in tiles.filled:
                x, y = right
            else:
                tiles.filled[(x, y)] = "O"
                break

        # Sand was dropped into the abyss
        else:
            break

        # Sand could not be dropped anymore
        if (x, y) == tiles.spring:
            break


def part1(tiles: Tiles) -> int:
    drop_sand(tiles, with_infinite_floor=False)

    return sum(1 for tile in tiles.filled.values() if tile == "O")


def part2(tiles: Tiles) -> int:
    drop_sand(tiles, with_infinite_floor=True)

    return sum(1 for tile in tiles.filled.values() if tile == "O")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2022, 14, "example")
    part2(parse(example))
