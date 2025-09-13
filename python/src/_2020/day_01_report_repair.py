import sys

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.splitlines()]


def part1(nums: list[int], target: int = 2020) -> int | None:
    remainders = set()

    for num in nums:
        remainder = target - num
        if remainder in remainders:
            return num * remainder

        remainders.add(num)

    return None


def part2(nums: list[int], target: int = 2020) -> int:
    nums.sort()

    for idx, first in enumerate(nums):
        if idx > 0 and first == nums[idx - 1]:
            continue

        left = idx + 1
        right = len(nums) - 1

        while left < right:
            second = nums[left]
            third = nums[right]
            three_sum = first + second + third

            if three_sum == target:
                return first * second * third

            if three_sum < target:
                left += 1
            else:
                right -= 1

    raise RuntimeError(f"Could not create {target} from three numbers in {nums}")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
