from collections import Counter
from itertools import pairwise
from typing import TextIO

from aoc.io import FileType, open_file
from aoc.util import sign

Report = list[int]


def parse(file: TextIO) -> list[Report]:
    return [list(map(int, line.split())) for line in file.readlines()]


def is_safe(report: Report) -> bool:
    level_diffs = {
        curr_level - next_level for curr_level, next_level in pairwise(report)
    }

    return level_diffs <= {1, 2, 3} or level_diffs <= {-1, -2, -3}


def part1(reports: list[Report]):
    return sum(is_safe(report) for report in reports)


def part2(reports: list[Report]):
    """
    Check if how many reports are safe by removing at most one level from each report

    :param reports: _description_
    :return: _description_
    """
    return sum(
        is_safe(report)
        | any(is_safe(report[:idx] + report[idx + 1 :]) for idx in range(len(report)))
        for report in reports
    )


def main():
    with open_file(2024, 2, FileType.INPUT) as file:
        reports = parse(file)

    print(f"Part 1: {part1(reports)}")
    print(f"Part 2: {part2(reports)}")


if __name__ == "__main__":
    main()
