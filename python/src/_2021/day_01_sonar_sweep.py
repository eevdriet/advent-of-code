import sys
from itertools import pairwise

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.splitlines()]


def part1(nums: list[int]) -> int:
    return sum(1 for prev, curr in pairwise(nums) if curr > prev)


def part2(nums: list[int]) -> int:
    num_sum = sum(nums[:3])
    n_increasing_sums = 0

    for idx, num in enumerate(nums[3:], start=3):
        if num > nums[idx - 3]:
            n_increasing_sums += 1

        num_sum -= nums[idx - 3]
        num_sum += num

    return n_increasing_sums


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
