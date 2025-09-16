import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def part1(input: str) -> int:
    return 0


def part2(input: str) -> int:
    return 0


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
