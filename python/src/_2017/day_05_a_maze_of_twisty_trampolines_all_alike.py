import sys

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(line) for line in input.splitlines()]


def part1(jumps: list[int]) -> int:
    idx = 0
    n_steps = 0

    while idx < len(jumps):
        jump = jumps[idx]
        jumps[idx] += 1

        idx += jump
        n_steps += 1

    return n_steps


def part2(jumps: list[int]) -> int:
    idx = 0
    n_steps = 0

    while idx in range(len(jumps)):
        jump = jumps[idx]
        jumps[idx] += 1 if jump < 3 else -1

        idx += jump
        n_steps += 1

    return n_steps


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
