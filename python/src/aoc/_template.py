from typing import TextIO

from aoc.io import FileType, open_file

YEAR = 2015
DAY = None


def parse(file: TextIO):
    return file.read().splitlines()


def part1(lines: list[str]) -> int:
    pass


def part2(lines: list[str]) -> int:
    pass


def main():
    with open_file(YEAR, DAY, FileType.INPUT) as file:
        lines = parse(file)

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
