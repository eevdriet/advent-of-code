from collections import Counter
from itertools import pairwise

from aoc.io import FileType, open_file
from aoc.util import timed


def parse(input: str) -> list[str]:
    return input.splitlines()


def is_nice_1(line: str) -> bool:
    # At least three vowels
    vowels = "aeiou"
    letters = Counter(line)

    if sum(letters[vowel] for vowel in vowels) < 3:
        return False

    # Letter appears twice in a row
    has_equal_pair = False

    for cur, nxt in pairwise(line):
        if cur == nxt:
            has_equal_pair = True
            break

    if not has_equal_pair:
        return False

    # Has no forbidden strings
    forbidden_words = ["ab", "cd", "pq", "xy"]
    for idx in range(len(line)):
        for word in forbidden_words:
            if line[idx : idx + len(word)] == word:
                return False

    return True


def is_nice_2(line: str) -> bool:
    # Pair of letters that appears twice
    has_pair = False

    pairs = {}
    for pos in range(len(line) - 1):
        pair = line[pos : pos + 2]

        if pair in pairs:
            if pos - pairs[pair] > 1:
                has_pair = True
                break
        else:
            pairs[pair] = pos

    if not has_pair:
        return False

    # Letter repeats with one between
    has_letter_repeat = False

    for pos in range(len(line) - 2):
        first, _, third = line[pos : pos + 3]
        if first == third:
            has_letter_repeat = True
            break

    if not has_letter_repeat:
        return False

    return True


def part1(lines: list[str]) -> int:
    return sum(1 for line in lines if is_nice_1(line))


def part2(lines: list[str]) -> int:
    return sum(1 for line in lines if is_nice_2(line))


def main():
    with open_file(2015, 5, FileType.INPUT) as file:
        lines = file.read().splitlines()

    result1, elapsed = timed(part1, lines)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, lines)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
