import sys
from collections import defaultdict, deque
from typing import Optional

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",")]


def part1(memory: list[int]) -> Optional[int]:
    program = IntCode(memory)
    out, _ = program.run_until_output([1])

    return out


def part2(memory: list[int]) -> Optional[int]:
    program = IntCode(memory)
    out, _ = program.run_until_output([2])

    return out


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
