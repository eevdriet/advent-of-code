import sys
from functools import cmp_to_key

from aoc.util import timed

Item = list | int
Pair = tuple[Item, Item]


def parse(input: str) -> list[Pair]:
    pairs = []

    for block in input.split("\n\n"):
        first_line, second_line = block.splitlines()

        left = eval(first_line)
        right = eval(second_line)

        pair = left, right
        pairs.append(pair)

    return pairs


def cmp(left: Item, right: Item) -> int:
    match (left, right):
        # Compare numbers directly
        case int(), int():
            return (left > right) - (left < right)

        # Compare item by item for lists if they have the same length
        case list(), list():
            for left_item, right_item in zip(left, right):
                res = cmp(left_item, right_item)

                if res != 0:
                    return res

            return cmp(len(left), len(right))

        # Convert number to list and compare
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])


def part1(pairs: list[Pair]) -> int:
    return sum(
        idx
        for idx, (left, right) in enumerate(pairs, start=1)
        if cmp(left, right) == -1
    )


def part2(pairs: list[Pair]) -> int:
    # Unpack the items from all pairs and add the additional ones
    items: list[Item] = [[[2]], [[6]]]

    for left, right in pairs:
        items.append(left)
        items.append(right)

    # Sort by the custom compare function
    items.sort(key=cmp_to_key(cmp))

    return (1 + items.index([[2]])) * (1 + items.index([[6]]))


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
