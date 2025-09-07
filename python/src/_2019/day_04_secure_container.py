import sys
from typing import Optional

from aoc.util import timed


def parse(input: str) -> range:
    left, right = map(int, input.strip().split("-"))
    return range(left, right + 1)


def is_valid(password: int, *, max_adj_digits: Optional[int] = None) -> bool:
    digits = str(password)
    max_adj_digits = max_adj_digits if max_adj_digits else len(digits)
    if len(digits) == 0:
        return False

    seen = set()
    n_adj_digits = 1

    for idx in range(1, len(digits)):
        if digits[idx] < digits[idx - 1]:
            return False

        if digits[idx] == digits[idx - 1]:
            n_adj_digits += 1
        else:
            seen.add(n_adj_digits)
            n_adj_digits = 1

    seen.add(n_adj_digits)
    return any(n_digits in range(2, max_adj_digits + 1) for n_digits in seen)


def part1(nums: range) -> int:
    return sum(is_valid(password) for password in nums)


def part2(nums: range) -> int:
    return sum(is_valid(password, max_adj_digits=2) for password in nums)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    is_valid(111122, max_adj_digits=2)
