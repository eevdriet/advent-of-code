import re

from aoc.io import FileType, open_file


def mull(mull_str: str) -> int:
    print(mull_str)
    left, right = map(int, mull_str[4:-1].split(","))
    return left * right


def part1(memory: str) -> int:
    REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"

    total = 0

    for instruction in re.finditer(REGEX, memory):
        left, right = map(int, instruction.groups())
        total += left * right

    return total


def part2(memory: str) -> int:
    REGEX = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"

    total = 0
    do = True

    for instruction in re.finditer(REGEX, memory):
        match instruction.group(1):
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                if do:
                    left, right = map(int, instruction.groups()[1:])
                    total += left * right

    return total


def main():
    with open_file(2024, 3, FileType.INPUT, "example2") as file:
        memory = file.read()

    print(f"Part 1: {part1(memory)}")
    print(f"Part 2: {part2(memory)}")


if __name__ == "__main__":
    main()
