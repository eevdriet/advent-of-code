import sys

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.splitlines()]


def part1(nums: list[int]) -> int:
    return sum(num // 3 - 2 for num in nums)


def part2(nums: list[int]) -> int:
    total = 0

    for num in nums:
        fuel = num

        while fuel >= 9:
            fuel = fuel // 3 - 2
            total += max(fuel, 0)

    return total


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
