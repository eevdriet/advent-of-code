import sys

from aoc.constant import MISSING_INT
from aoc.io import open_file
from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(line) for line in input.splitlines()]


def part1(nums: list[int]) -> int:
    return sum(nums)


def part2(nums: list[int]) -> int:
    curr = 0
    seen = set()

    while True:
        for num in nums:
            if curr in seen:
                return curr

            seen.add(curr)
            curr += num


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part2([-6, 3, 8, 5, -6])
