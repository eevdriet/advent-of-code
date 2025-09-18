import re
import sys

from attrs import define

from aoc.io import read_file
from aoc.util import timed
from aoc.util.re import find_nums

Conversion = tuple[str, list[tuple[int, int, int]]]


@define
class Production:
    seeds: list[int]
    conversions: dict[str, Conversion]


def parse(input: str) -> Production:
    seeds_block, *conversion_blocks = input.split("\n\n")
    seeds = find_nums(seeds_block)
    conversions = {}

    for block in conversion_blocks:
        conversion_line, *range_lines = block.splitlines()

        match = re.match(r"(\w+)-to-(\w+) map", conversion_line)
        from_str, to_str = match.groups()

        ranges = []

        for line in range_lines:
            dst, src, size = find_nums(line)
            ranges.append((src, dst, size))

        conversions[from_str] = to_str, ranges

    return Production(seeds, conversions)


def find_min_location(production: Production, seed_ranges: list[range]) -> int:
    min_location = sys.maxsize

    for seeds in seed_ranges:
        for val in seeds:
            category = "seed"

            while category != "location":
                category, ranges = production.conversions[category]

                for src, dst, size in ranges:
                    if src <= val <= src + size - 1:
                        val = dst + (val - src)
                        break

            min_location = min(val, min_location)

    return min_location


def part1(production: Production) -> int:
    seed_ranges = [range(seed, seed + 1) for seed in production.seeds]

    return find_min_location(production, seed_ranges)


def part2(production: Production) -> int:
    seed_ranges = []

    for idx in range(0, len(production.seeds), 2):
        start = production.seeds[idx]
        size = production.seeds[idx + 1]

        seed_range = range(start, start + size)
        seed_ranges.append(seed_range)

    return find_min_location(production, seed_ranges)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2023, 5, "example")
    part1(parse(example))
