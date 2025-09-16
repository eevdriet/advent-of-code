import sys
from collections import defaultdict
from itertools import accumulate

from aoc.util import timed

FileSystem = dict[str, int]


def parse(input: str) -> list[str]:
    return input.splitlines()


def search_file_system(lines: list[str]) -> FileSystem:
    dirs = defaultdict(int)
    path = []

    for line in lines:
        match line.split():
            # Change directory
            case "$", "cd", "/":
                path = ["/"]
            case "$", "cd", "..":
                path.pop()
            case "$", "cd", dir:
                path.append(dir + "/")

            # List files
            case "$", "ls":
                pass
            case "dir", _:
                pass

            case size, _:
                for p in accumulate(path):
                    dirs[p] += int(size)

            case _:
                raise ValueError(f"Found invalid command '{line}'")

    return dirs


def part1(lines: list[str]) -> int:
    fs = search_file_system(lines)

    return sum(size for size in fs.values() if size <= 100_000)


def part2(lines: list[str]) -> int:
    fs = search_file_system(lines)
    root_size = fs["/"]

    return min(size for size in fs.values() if size + 40_000_000 >= root_size)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
