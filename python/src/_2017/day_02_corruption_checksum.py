import sys
from itertools import combinations


def parse(input: str) -> list[list[int]]:
    return [[int(cell) for cell in row.split()] for row in input.splitlines()]


def part1(spreadsheet: list[list[int]]) -> int:
    return sum(max(row) - min(row) for row in spreadsheet)


def part2(spreadsheet: list[list[int]]) -> int:
    return sum(
        first // second
        for row in spreadsheet
        for first, second in combinations(sorted(row), 2)
        if first % second == 0
    )


if __name__ == "__main__":
    # input = sys.stdin.read()
    # parsed = parse(input)
    #
    # result1, elapsed = timed(part1, parsed)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, parsed)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    part2([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
