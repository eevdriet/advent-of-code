import re
import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def part1(format: str) -> int:
    len_decompressed = 0
    idx = 0

    while idx < len(format):
        letter = format[idx]

        if letter.isalpha():
            len_decompressed += 1
            idx += 1
        elif match := re.match(r"\((\d+)x(\d+)\)", format[idx:]):
            n_chars, repeat = map(int, match.groups())

            len_decompressed += n_chars * repeat

            _, len_marker = match.span(0)
            idx += len_marker + n_chars

    return len_decompressed


def part2(format: str) -> int:
    def helper(text: str) -> int:
        len_decompressed = 0
        idx = 0

        while idx < len(text):
            letter = text[idx]

            if letter.isalpha():
                len_decompressed += 1
                idx += 1
            elif match := re.match(r"\((\d+)x(\d+)\)", text[idx:]):
                n_chars, repeat = map(int, match.groups())
                _, len_marker = match.span(0)

                idx += len_marker
                len_decompressed += helper(text[idx : idx + n_chars]) * repeat
                idx += n_chars

        return len_decompressed

    return helper(format)


def main():
    input = sys.stdin.read()
    format = parse(input)

    result1, elapsed = timed(part1, format)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, format)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part2("X(8x2)(3x3)ABCY")
