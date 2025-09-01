import re
from typing import List

from aoc.io import File, open_file


def part1(lines: List[str]) -> int:
    total = 0

    for line in lines:
        digits = [ch for ch in line if ch.isdigit()]
        total += int(digits[0] + digits[-1])

    return total


numbers = "one two three four five six seven eight nine".split()
numbers09 = "|".join(numbers) + "|\\d"
rexp = f"(?=({numbers09}))"  # lookaround instead of consuming


def numeric(x: str) -> str:
    if x in numbers:
        return str(numbers.index(x) + 1)

    return x


def part2(lines: List[str]) -> int:
    total = 0

    for line in lines:
        digits = tuple(map(numeric, re.findall(rexp, line)))
        total += int(digits[0] + digits[-1])

    return total


def main():
    lines = open_file(2023, 1, File.INPUT).read().strip().splitlines()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
