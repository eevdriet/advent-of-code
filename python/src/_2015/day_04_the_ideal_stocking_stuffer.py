import sys
from hashlib import md5

from aoc.util import timed


def parse(input: str) -> str:
    return input


def find_hash_number(key: str, *, n_leading_zeroes: int) -> int:
    result = "0" * n_leading_zeroes
    n = 1
    hash = ""

    while hash[:n_leading_zeroes] != result:
        data = f"{key}{n}"
        hash = md5(data.encode()).hexdigest()
        n += 1

    return n - 1


def part1(key: str) -> int:
    return find_hash_number(key, n_leading_zeroes=5)


def part2(key: str) -> int:
    return find_hash_number(key, n_leading_zeroes=6)


def main():
    input = sys.stdin.read()
    key = parse(input)

    result1, elapsed = timed(part1, key)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, key)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
