import re
import sys
from typing import Callable

from aoc.util import timed

Assignment = tuple[range, range]


def parse(input: str) -> list[Assignment]:
    assignments = []

    for line in input.splitlines():
        start1, stop1, start2, stop2 = map(int, re.findall(r"(\d+)", line))
        range1 = range(start1, stop1 + 1)
        range2 = range(start2, stop2 + 1)

        assignment = range1, range2
        assignments.append(assignment)

    return assignments


def count_overlaps(
    assignments: list[Assignment], overlaps: Callable[[range, range], bool]
) -> int:
    return sum(
        1
        for range1, range2 in assignments
        if overlaps(range1, range2) or overlaps(range2, range1)
    )


def part1(assignments: list[Assignment]) -> int:
    def overlap(range1: range, range2: range) -> bool:
        return range1.start <= range2.start and range2.stop <= range1.stop

    return count_overlaps(assignments, overlap)


def part2(assignments: list[Assignment]) -> int:
    def overlap(range1: range, range2: range) -> bool:
        return range1.start < range2.stop and range1.stop > range2.start

    return count_overlaps(assignments, overlap)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
