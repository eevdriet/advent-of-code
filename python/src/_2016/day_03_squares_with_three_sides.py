import re
import sys
from itertools import combinations

from attr import define

from aoc.util import timed


@define
class Triangle:
    first: int
    second: int
    third: int

    def is_valid(self) -> bool:
        return (
            self.first + self.second > self.third
            and self.second + self.third > self.first
            and self.third + self.first > self.second
        )


def parse(input: str) -> list[int]:
    return [int(num) for num in re.findall(r"(\d+)", input)]


def part1(nums: list[int]) -> int:
    triangles = [
        Triangle(nums[idx], nums[idx + 1], nums[idx + 2])
        for idx in range(0, len(nums), 3)
    ]

    return sum(1 for triangle in triangles if triangle.is_valid())


def part2(nums: list[int]) -> int:
    n_rows = len(nums) // 3

    triangles = [
        Triangle(
            nums[3 * row + col], nums[3 * (row + 1) + col], nums[3 * (row + 2) + col]
        )
        for col in range(3)
        for row in range(0, n_rows, 3)
    ]

    return sum(1 for triangle in triangles if triangle.is_valid())


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
