import operator
import sys
from functools import reduce
from itertools import combinations
from math import prod

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(line) for line in input.splitlines()]


def min_entanglement(packages: list[int], target: int) -> int:
    packages = sorted(packages)
    min_len = float("inf")
    min_entangle = sys.maxsize

    def backtrack(start, current, total):
        nonlocal min_len, min_entangle

        # Prune: if current length already exceeds best found, stop
        if len(current) > min_len:
            return

        # Found exact sum: try to minimize entanglement
        if total == target:
            entangle = prod(current)

            if len(current) < min_len:
                min_len = len(current)
                min_entangle = entangle

            elif len(current) == min_len and entangle < min_entangle:
                min_entangle = entangle
            return

        # Overshot the target, stop
        if total > target:
            return

        for pos in range(start, len(packages)):
            current.append(packages[pos])
            backtrack(pos + 1, current, total + packages[pos])
            current.pop()

    backtrack(0, [], 0)
    return min_entangle


def part1(packages: list[int]) -> int:
    target = sum(packages) // 3
    return min_entanglement(packages, target)


def part2(packages: list[int]) -> int:
    target = sum(packages) // 4
    return min_entanglement(packages, target)


if __name__ == "__main__":
    # input = sys.stdin.read()
    packages = [
        1,
        2,
        3,
        7,
        11,
        13,
        17,
        19,
        23,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
    ]

    result1, elapsed = timed(part1, packages)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, packages)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
