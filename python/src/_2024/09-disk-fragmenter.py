from typing import TextIO

from aoc.io import FileType, open_file
from attrs import define

YEAR = 2024
DAY = 9


@define
class FileSystem:
    disk_map: str


def parse(file: TextIO) -> FileSystem:
    return file.read().splitlines()


def part1(fs: FileSystem) -> int:
    pass


def part2(fs: FileSystem) -> int:
    pass


def main():
    with open_file(YEAR, DAY, FileType.INPUT) as file:
        fs = parse(file)

    print(f"Part 1: {part1(fs)}")
    print(f"Part 2: {part2(fs)}")


if __name__ == "__main__":
    main()
