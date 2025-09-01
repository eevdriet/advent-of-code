import sys
from itertools import groupby

from aoc.util import timed


def parse(input: str) -> str:
    return input


def look_and_say(num: str, *, n_looks_and_says: int = 1) -> str:
    def find_next(num: str) -> str:
        if len(num) == 0:
            return ""

        return "".join(f"{len(tuple(group))}{digit}" for digit, group in groupby(num))

    for _ in range(n_looks_and_says):
        num = find_next(num)

    return num


def part1(num: str) -> int:
    return len(look_and_say(num, n_looks_and_says=40))


def part2(num: str) -> int:
    return len(look_and_say(num, n_looks_and_says=50))


def main():
    input = sys.stdin.read()
    num = parse(input)

    result1, elapsed = timed(part1, num)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, num)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
