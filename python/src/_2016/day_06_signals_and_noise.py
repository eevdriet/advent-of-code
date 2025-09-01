import sys
from collections import defaultdict

from aoc.util import timed


def parse(input: str) -> list[str]:
    return input.splitlines()


def find_message(grid: list[str], *, use_max: bool) -> str:
    n_rows = len(grid)
    n_cols = len(grid[0])
    message = ""

    for col in range(n_cols):
        letter_counts = defaultdict(int)

        for row in range(n_rows):
            letter = grid[row][col]
            letter_counts[letter] += 1

        message += (
            max(letter_counts, key=letter_counts.get)
            if use_max
            else min(letter_counts, key=letter_counts.get)
        )

    return message


def part1(grid: list[str]) -> str:
    return find_message(grid, use_max=True)


def part2(grid: list[str]) -> str:
    return find_message(grid, use_max=False)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(find_message, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
