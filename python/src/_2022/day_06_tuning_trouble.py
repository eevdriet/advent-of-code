import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def count_processed_chars(chars: str, *, stride: int) -> int:
    for idx in range(stride, len(chars)):
        seen = set(chars[idx - stride : idx])

        if len(seen) == stride:
            return idx

    raise RuntimeError("Cannot found number of processed characters")


def part1(chars: str) -> int:
    return count_processed_chars(chars, stride=4)


def part2(chars: str) -> int:
    return count_processed_chars(chars, stride=14)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
