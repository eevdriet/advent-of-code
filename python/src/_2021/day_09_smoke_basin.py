import sys
from math import prod

from aoc.util import adjacent4, timed

HeightMap = dict[complex, int]


def parse(input: str) -> HeightMap:
    return {
        complex(x, y): int(height)
        for y, row in enumerate(input.strip().splitlines())
        for x, height in enumerate(row.strip())
    }


def part1(heights: HeightMap) -> int:
    return sum(
        height + 1
        for coord, height in heights.items()
        if all(
            heights[neighbor] > height
            for neighbor in adjacent4(coord)
            if neighbor in heights
        )
    )


def part2(heights: HeightMap) -> int:
    visited = set()

    def flood_fill(coord: complex) -> int:
        if coord in visited or coord not in heights:
            return 0

        visited.add(coord)

        if heights[coord] == 9:
            return 0

        return 1 + sum(flood_fill(neighbor) for neighbor in adjacent4(coord))

    height_counts = [flood_fill(coord) for coord in heights]
    height_counts.sort()

    return prod(height_counts[-3:])


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
