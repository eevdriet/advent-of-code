import sys
from itertools import pairwise

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def reduce_polymer(polymer: str) -> str:
    reduced = list(polymer)

    while True:
        prev_len = len(reduced)
        idx = 0

        while idx + 1 < len(reduced):
            left = reduced[idx]
            right = reduced[idx + 1]

            # Already reduced
            if left == "" or right == "":
                idx += 1
                continue

            # Different letter or same casing
            if left.lower() != right.lower() or left.islower() == right.islower():
                idx += 1
                continue

            # Reduce unit pair
            reduced[idx] = ""
            reduced[idx + 1] = ""
            idx += 2

        # Try to reduce the polymer and stop if nothing could be done
        reduced = [unit for unit in reduced if unit]

        if len(reduced) == prev_len:
            break

    return "".join(reduced)


def part1(polymer: str) -> int:
    return len(reduce_polymer(polymer))


def part2(polymer: str) -> int:
    units = set((ch.lower() for ch in polymer))
    min_len = len(polymer)

    for unit in units:
        candidate = "".join((ch for ch in polymer if ch.lower() != unit))
        reduced = reduce_polymer(candidate)
        min_len = min(len(reduced), min_len)

    return min_len


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    reduce_polymer("dabAcCaCBAcCcaDA")
