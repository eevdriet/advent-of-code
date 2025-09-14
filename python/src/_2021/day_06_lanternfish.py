import sys
from collections import Counter

from aoc.util import timed

MAX_N_FISHES = 8


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",")]


def simulate(fishes: list[int], *, n_days: int) -> Counter:
    fish_counts = Counter(fishes)

    for _ in range(n_days):
        new_counts = Counter()

        for fish, count in fish_counts.items():
            if fish == 0:
                new_counts[8] += count
                new_counts[6] += count
            else:
                new_counts[fish - 1] += count

        fish_counts = new_counts

    return fish_counts


def part1(fishes: list[int]) -> int:
    fish_counts = simulate(fishes, n_days=80)
    return sum(count for count in fish_counts.values())


def part2(fishes: list[int]) -> int:
    fish_counts = simulate(fishes, n_days=256)
    return sum(count for count in fish_counts.values())


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
