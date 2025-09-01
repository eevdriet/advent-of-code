import sys
from typing import Optional

from aoc.constant import MISSING_STR
from aoc.util import timed


def parse(input: str) -> int:
    return int(input.strip())


def find_max_square(serial: int, sizes: Optional[range] = None) -> tuple[int, int, int]:
    width = 300
    sizes = sizes if sizes else range(1, width + 1)

    # Build summed-area table
    sums = [[0] * (width + 1) for _ in range(width + 1)]

    for y in range(1, width + 1):
        for x in range(1, width + 1):
            rack_id = x + 10
            power = rack_id * y
            power += serial
            power *= rack_id
            power = (power // 100) % 10
            power -= 5

            sums[y][x] = power + sums[y - 1][x] + sums[y][x - 1] - sums[y - 1][x - 1]

    max_power = -sys.maxsize
    result = (-1, -1, 0)

    # Search all square sizes
    for size in sizes:
        for y in range(size, width + 1):
            for x in range(size, width + 1):
                power = (
                    sums[y][x]
                    - sums[y - size][x]
                    - sums[y][x - size]
                    + sums[y - size][x - size]
                )
                if power > max_power:
                    max_power = power
                    result = (x - size + 1, y - size + 1, size)  # top-left corner

    return result


def part1(serial: int) -> str:
    x, y, _ = find_max_square(serial, range(3, 3 + 1))
    return f"{x},{y}"


def part2(serial: int) -> str:
    x, y, size = find_max_square(serial)
    return f"{x},{y},{size}"


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part1(18)
