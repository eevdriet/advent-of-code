import sys

from aoc.util import timed


def parse(input: str) -> list[list[str]]:
    return [line.split() for line in input.splitlines()]


def part1(passphrases: list[list[str]]) -> int:
    return sum(1 for phrase in passphrases if len(phrase) == len(set(phrase)))


def is_valid(phrase: list[str]) -> bool:
    letter_counts = set()

    for word in phrase:
        count = [0] * 26

        for letter in word:
            idx = ord(letter) - ord("a")
            count[idx] += 1

        key = tuple(count)
        if key in letter_counts:
            return False

        letter_counts.add(key)

    return True


def part2(passphrases: list[list[str]]) -> int:
    return sum(1 for phrase in passphrases if is_valid(phrase))


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    is_valid(["abcde", "xyz", "ecdab"])
