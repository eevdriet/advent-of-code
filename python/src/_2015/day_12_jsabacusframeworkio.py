import json
import sys

from aoc.util import timed


def parse(input: str) -> dict:
    return json.loads(input)


def sum_numbers(doc: dict, *, ignore_red: bool) -> int:
    def count(var) -> int:
        match var:
            case dict():
                return (
                    sum(count(val) for val in var.values())
                    if not (ignore_red and "red" in var.values())
                    else 0
                )
            case list():
                return sum(count(item) for item in var)
            case int():
                return var
            case _:
                return 0

    return count(doc)


def part1(doc: dict) -> int:
    return sum_numbers(doc, ignore_red=False)


def part2(doc: dict) -> int:
    return sum_numbers(doc, ignore_red=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    doc = parse(input)

    result1, elapsed = timed(part1, doc)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, doc)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
