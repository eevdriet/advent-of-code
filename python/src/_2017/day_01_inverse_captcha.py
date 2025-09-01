import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def part1(digits: str) -> int:
    return sum(
        int(digits[idx])
        for idx in range(len(digits))
        if digits[idx] == digits[(idx + 1) % len(digits)]
    )


def part2(digits: str) -> int:
    return sum(
        int(digits[idx])
        for idx in range(len(digits))
        if digits[idx] == digits[(idx + len(digits) // 2) % len(digits)]
    )


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    part1("1122")
