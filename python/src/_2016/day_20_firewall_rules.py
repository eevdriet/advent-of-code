import sys

from aoc.util import timed

Range = list[int]
MAX_VAL = 4294967295


def parse(input: str) -> list[Range]:
    ranges = []

    for line in input.splitlines():
        rang = [int(num) for num in line.split("-")]
        ranges.append(rang)

    return ranges


def merge_ranges(ranges: list[Range]) -> list[Range]:
    if not ranges:
        return []

    # Sort ranges for easier merging
    ranges.sort(key=lambda r: r[0])

    # Merge the ranges to reduce the computations
    merged = [ranges[0]]

    for curr in ranges[1:]:
        prev = merged[-1]

        if curr[0] > prev[1] + 1:
            merged.append(curr)
        else:
            prev[1] = max(prev[1], curr[1])

    return merged


def part1(ranges: list[Range], max_val: int = MAX_VAL) -> int:
    merged = merge_ranges(ranges)

    # Then search for the lowest non-blocked IP
    return next(
        (
            ip
            for ip in range(max_val + 1)
            if not any(blocked[0] <= ip <= blocked[1] for blocked in merged)
        ),
        -1,
    )


def part2(ranges: list[Range], max_val: int = MAX_VAL) -> int:
    merged = merge_ranges(ranges)

    n_total = max_val + 1
    n_blocked = sum(blocked[1] - blocked[0] + 1 for blocked in merged)

    return n_total - n_blocked


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    lines = """
5-8
0-2
4-7
    """.strip()

    part1(parse(lines))
