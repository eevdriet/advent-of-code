import sys

import parse as ps

from aoc.io import read_file
from aoc.util import timed

REGION_TYPES = [".", "=", "|"]
MOD = 20_183

Coord2D = tuple[int, int]


def parse(input: str) -> tuple[int, Coord2D]:
    depth, x_max, y_max = ps.parse("depth: {:d}\ntarget: {:d},{:d}", input.strip())
    target = x_max, y_max

    return depth, target


def create_indices(target: Coord2D) -> dict[Coord2D, int]:
    geo_indices: dict[Coord2D, int] = {}
    x_max, y_max = target

    for y in range(y_max + 1):
        for x in range(x_max + 1):
            match (x, y):
                case (0, 0):
                    idx = 0
                case (x, 0):
                    idx = (x * 16_807) % MOD
                case (0, y):
                    idx = (y * 48_271) % MOD
                case _:
                    idx = (
                        0
                        if (x, y) == (x_max, y_max)
                        else (geo_indices[(x - 1, y)] * geo_indices[(x, y - 1)]) % MOD
                    )

            geo_indices[(x, y)] = idx

    return geo_indices


def part1(depth: int, target: Coord2D) -> int:
    geo_indices = create_indices(target)

    return sum(((depth + idx) % MOD) % 3 for idx in geo_indices.values())


def part2(depth: int, target: Coord2D) -> int:
    return 0


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2018, 22)
    depth = 510
    target = 10, 10

    print(part1(*parse(f"depth: {depth}\ntarget: {target[0]},{target[1]}")))
