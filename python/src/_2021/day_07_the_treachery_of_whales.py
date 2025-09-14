import sys
from math import ceil, floor

from numpy import mean, median

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",")]


def part1(nums: list[int]) -> int:
    med = int(median(nums))
    return sum(abs(num - med) for num in nums)


def part2(nums: list[int]) -> int:
    mu = mean(nums)

    def fuel_to_mean(src: int, dst: int) -> int:
        n = abs(src - dst)
        return (n * (n + 1)) // 2

    opt1 = sum(fuel_to_mean(num, floor(mu)) for num in nums)
    opt2 = sum(fuel_to_mean(num, ceil(mu)) for num in nums)

    return min(opt1, opt2)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
