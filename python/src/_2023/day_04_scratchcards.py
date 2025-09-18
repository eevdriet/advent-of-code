import sys

from attrs import define

from aoc.util import timed
from aoc.util.re import find_nums


@define
class Scratchcard:
    nums: list[int]
    winning_nums: list[int]


def parse(input: str) -> list[Scratchcard]:
    cards = []

    for line in input.splitlines():
        nums_text, winning_text = line.split(" | ")

        nums = find_nums(nums_text)[1:]
        winning_nums = find_nums(winning_text)

        card = Scratchcard(nums, winning_nums)
        cards.append(card)

    return cards


def part1(cards: list[Scratchcard]) -> int:
    total = 0

    for card in cards:
        winning_nums = set(card.nums) & set(card.winning_nums)
        if winning_nums:
            total += 2 ** (len(winning_nums) - 1)

    return total


def part2(cards: list[Scratchcard]) -> int:
    card_counts = {idx: 1 for idx in range(len(cards))}

    for idx, card in enumerate(cards):
        count = card_counts[idx]
        winning_nums = set(card.nums) & set(card.winning_nums)
        if not winning_nums:
            continue

        n_wins = len(winning_nums)

        for offset in range(1, n_wins + 1):
            other_idx = (idx + offset) % len(cards)
            card_counts[other_idx] += count

    return sum(card_counts.values())


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
