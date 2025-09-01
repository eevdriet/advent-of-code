from aoc.io import FileType, open_file
from aoc.util import timed


def parse(input: str) -> list[str]:
    return input.splitlines()


def find_n_chars_1(line: str):
    n_literal_chars = len(line)
    n_memory_chars = 0

    idx = 1
    while idx != len(line) - 1:
        char = line[idx]

        if char != "\\":
            n_memory_chars += 1
            idx += 1
        else:
            match tuple(line[idx + 1 : idx + 4]):
                case ("\\", *_) | ('"', *_):
                    n_memory_chars += 1
                    idx += 2
                case ("x", *_):
                    n_memory_chars += 1
                    idx += 4

    return n_literal_chars, n_memory_chars


def part1(lines: list[str]) -> int:
    n_chars = [find_n_chars_1(line) for line in lines]
    return sum(a - b for a, b in n_chars)


def find_n_chars_2(line: str):
    n_literal_chars = len(line)
    n_encoded_chars = 2 + sum(2 if ch in ["\\", '"'] else 1 for ch in line)

    return n_literal_chars, n_encoded_chars


def part2(lines: list[str]):
    n_chars = [find_n_chars_2(line) for line in lines]
    return sum(b - a for a, b in n_chars)


def main():
    with open_file(2015, 8, FileType.INPUT) as file:
        lines = file.read().splitlines()

    result1, elapsed = timed(part1, lines)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, lines)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
