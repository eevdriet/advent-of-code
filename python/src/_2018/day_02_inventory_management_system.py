import sys
from collections import Counter
from itertools import combinations

from aoc.constant import MISSING_STR
from aoc.util import timed


def parse(input: str) -> list[str]:
    return input.splitlines()


def part1(words: list[str]) -> int:
    exactly2 = 0
    exactly3 = 0

    for word in words:
        letters = Counter(word)

        exactly2 += any(letter for letter, count in letters.items() if count == 2)
        exactly3 += any(letter for letter, count in letters.items() if count == 3)

    return exactly2 * exactly3


def part2(words: list[str]) -> str:
    for first, second in combinations(words, r=2):
        if len(first) != len(second):
            continue

        in_common = ""
        n_diff = 0

        for letter1, letter2 in zip(first, second):
            if letter1 != letter2:
                n_diff += 1
            else:
                in_common += letter1

            if n_diff > 1:
                break

        if n_diff == 1:
            return in_common

    return MISSING_STR


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
