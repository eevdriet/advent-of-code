import sys

from aoc.util import timed

Rucksack = str


def parse(input: str) -> list[Rucksack]:
    return input.splitlines()


def part1(rucksacks: list[Rucksack]) -> int:
    total = 0

    for rucksack in rucksacks:
        # Split the rucksack into equal parts
        mid = len(rucksack) // 2
        left = rucksack[:mid]
        right = rucksack[mid:]

        # Verify which item is packed in both halves
        items = set(left) & set(right)
        assert len(items) == 1
        item = next(iter(items))

        # Add the item priority to the total
        total += (
            (ord(item) - ord("a") + 1)
            if item.islower()
            else (ord(item) - ord("A") + 27)
        )

    return total


def part2(rucksacks: list[Rucksack]) -> int:
    total = 0

    for idx in range(0, len(rucksacks), 3):
        first, second, third = rucksacks[idx : idx + 3]

        # Verify which item is packed in both halves
        items = set(first) & set(second) & set(third)
        assert len(items) == 1
        item = next(iter(items))

        # Add the item priority to the total
        total += (
            (ord(item) - ord("a") + 1)
            if item.islower()
            else (ord(item) - ord("A") + 27)
        )

    return total


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
