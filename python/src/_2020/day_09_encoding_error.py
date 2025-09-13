import sys

from _2020.day_01_report_repair import part1 as two_sum
from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.splitlines()]


def part1(nums: list[int], preamble: int = 25) -> int:
    for idx in range(preamble, len(nums)):
        target = nums[idx]
        prev_nums = nums[idx - preamble : idx]

        if two_sum(prev_nums, target) is None:
            return target

    raise RuntimeError(
        f"No number after a preamble isn't a 2-sum of the previous {preamble} numbers"
    )


def part2(nums: list[int], preamble: int = 25) -> int:
    target = part1(nums, preamble)

    left, right = 0, 0
    cont_sum = nums[left]

    while left <= right < len(nums):
        if cont_sum == target:
            cont_nums = nums[left : right + 1]
            return min(cont_nums) + max(cont_nums)

        if cont_sum > target:
            cont_sum -= nums[left]
            left += 1
        else:
            right += 1
            cont_sum += nums[right]

    raise RuntimeError(f"No contiguous subarray of {nums} can sum to {target}")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
