from functools import cmp_to_key
from typing import TextIO

from aoc.io import FileType, open_file

Page = int
Order = tuple[Page, Page]
Rules = dict[Order, bool]
Update = list[Page]


def parse(file: TextIO) -> tuple[Rules, list[Update]]:
    rules_str, updates_str = file.read().split("\n\n")

    rules = {}
    for line in rules_str.splitlines():
        x, y = map(int, line.split("|"))

        # Read the rules as an -1, 0, 1 ordering right away
        rules[(x, y)] = -1
        rules[(y, x)] = 1

    updates = [list(map(int, line.split(","))) for line in updates_str.splitlines()]

    return rules, updates


def is_in_order(update: Update, rules: Rules):
    """
    Verify whether an update is in order according to the given rules

    :param update: Update to verify
    :param rules: Rules which the update has to satisfy
    :return: Whether the update is in order
    """
    for left in range(len(update)):
        for right in range(left + 1, len(update)):
            key = (update[left], update[right])

            if key in rules and rules[key] != -1:
                return False

    return True


def part1(updates: list[Update], rules: Rules) -> int:
    # Count the middle element of each update that is in order according to the rules
    return sum(
        update[len(update) // 2] for update in updates if is_in_order(update, rules)
    )


def part2(updates: list[Update], rules: Rules) -> int:
    # Comparison function to sort each update
    def cmp(x, y):
        return rules.get((x, y), 0)

    total = 0

    for update in updates:
        # Skip already in-order update
        if is_in_order(update, rules):
            continue

        # Correct the update and count the middle element
        update.sort(key=cmp_to_key(cmp))
        total += update[len(update) // 2]

    return total


def main():
    with open_file(2024, 5, FileType.INPUT) as file:
        rules, updates = parse(file)

    print(f"Part 1: {part1(updates, rules)}")
    print(f"Part 2: {part2(updates, rules)}")


if __name__ == "__main__":
    main()
