import sys


def parse(input: str) -> ...:
    pass


def part1(input: ...) -> ...:
    pass


def part2(input: ...) -> ...:
    pass


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = part1(parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = part2(parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
