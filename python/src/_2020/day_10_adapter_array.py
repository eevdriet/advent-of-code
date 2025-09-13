import sys
from collections import Counter, defaultdict
from itertools import pairwise

from aoc.util import timed


def parse(input: str) -> list[int]:
    jolts = [int(num) for num in input.splitlines()]
    jolts = sorted(jolts)
    jolts = [0] + jolts + [3 + jolts[-1]]

    return jolts


def part1(jolts: list[int]) -> int:
    diff_counts = Counter(curr - prev for prev, curr in pairwise(jolts))

    return diff_counts[1] * diff_counts[3]


def part2(jolts: list[int]) -> int:
    counts = defaultdict(int, {jolts[-1]: 1})

    for jolt in reversed(jolts[:-1]):
        counts[jolt] = sum(counts[jolt + offset] for offset in range(1, 4))

    return counts[0]


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
