import sys
from collections import defaultdict

from aoc.util import timed

CAPACITY = 150


def parse(input: str) -> list[int]:
    return [int(container) for container in input.splitlines()]


def part1(containers: list[int], capacity: int = CAPACITY) -> int:
    def backtrack(pos: int, remaining: int) -> int:
        if remaining < 0:
            return 0
        if remaining == 0:
            return 1

        return sum(
            backtrack(next_pos + 1, remaining - containers[next_pos])
            for next_pos in range(pos, len(containers))
        )

    return backtrack(0, capacity)


def part2(containers: list[int], capacity: int = CAPACITY) -> int:
    counts = defaultdict(int)

    def backtrack(pos: int, n_chosen: int, remaining: int):
        if remaining < 0:
            return
        if remaining == 0:
            counts[n_chosen] += 1
            return

        for next_pos in range(pos, len(containers)):
            backtrack(next_pos + 1, n_chosen + 1, remaining - containers[next_pos])

    backtrack(0, 0, capacity)

    min_chosen = min(counts.keys())
    return counts[min_chosen]


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
