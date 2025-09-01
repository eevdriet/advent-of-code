from collections import Counter
from typing import TextIO

from aoc.io import FileType, open_file


def parse(file: TextIO) -> tuple[list[int], list[int]]:
    left, right = [], []

    for line in file.readlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    return left, right


def part1(left: list[int], right: list[int]):
    return sum(abs(l - r) for l, r in zip(left, right))


def part2(left: list[int], right: list[int]):
    counts = Counter(right)

    return sum(l * counts[l] for l in left)


def main():
    with open_file(2024, 1, FileType.EXAMPLE) as file:
        left, right = parse(file)

    left.sort()
    right.sort()

    print(f"Part 1: {part1(left, right)}")
    print(f"Part 2: {part2(left, right)}")


if __name__ == "__main__":
    main()
