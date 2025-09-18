import re
import sys

from aoc.io import read_file
from aoc.util import timed


def parse(input: str) -> list[str]:
    return input.strip().splitlines()


def digit_sum(lines: list[str], with_letters: bool = False) -> int:
    LETTER_DIGITS = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    pattern = r"\d" if not with_letters else rf"(?=(\d|{'|'.join(LETTER_DIGITS)}))"

    def find_digits(text: str) -> list[str]:
        return [
            digit if digit and digit.isdigit() else str(LETTER_DIGITS.index(digit) + 1)
            for digit in re.findall(pattern, text)
        ]

    result = 0

    for line in lines:
        digits = find_digits(line)

        match len(digits):
            case 0:
                raise ValueError(f"Cannot find any digits in '{line}'")
            case 1:
                first = last = digits[0]
            case _:
                first, *_, last = digits

        num = int(f"{first}{last}")
        result += num

    return result


def part1(lines: list[str]) -> int:
    return digit_sum(lines, with_letters=False)


def part2(lines: list[str]) -> int:
    return digit_sum(lines, with_letters=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2023, 1, "example2")
    part2(parse(example))
