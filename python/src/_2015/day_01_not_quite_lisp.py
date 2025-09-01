import sys
from typing import Optional

from aoc.util import timed


def parse(input: str) -> str:
    return input


def part1(steps: str) -> int:
    floor = 0

    for step in steps:
        match step:
            case "(":
                floor += 1
            case ")":
                floor -= 1

    return floor


def part2(steps: str) -> Optional[int]:
    BASEMENT = -1
    floor = 0

    for pos, step in enumerate(steps, start=1):
        match step:
            case "(":
                floor += 1
            case ")":
                floor -= 1

        if floor == BASEMENT:
            return pos

    return None


def main():
    input = sys.stdin.read()
    steps = parse(input)

    result1, elapsed = timed(part1, steps)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, steps)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
