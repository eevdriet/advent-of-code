import sys
from collections import Counter

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Card = int
FACE_CARD_RANKS: dict[str, int] = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


@define
class Hand:
    cards: list[Card]

    @classmethod
    def _find_category(cls, counts: list[int]) -> int:
        match counts:
            case [5]:
                return 7
            case [4, 1]:
                return 6
            case [3, 2]:
                return 5
            case [3, 1, 1]:
                return 4
            case [2, 2, 1]:
                return 3
            case [2, 1, 1, 1]:
                return 2
            case _:
                return 1

    def rank_no_joker(self) -> tuple[int, ...]:
        card_counts = Counter(self.cards)
        counts = sorted(card_counts.values(), reverse=True)

        return (self._find_category(counts), *self.cards)

    def rank_joker(self) -> tuple[int, ...]:
        # Determine how many jokers there are and rank normally if there are none
        joker = FACE_CARD_RANKS["J"]
        n_jokers = self.cards.count(joker)

        if n_jokers == 0:
            return self.rank_no_joker()

        # Count every J as a joker instead of a jack
        cards = [card if card != joker else 1 for card in self.cards]

        # If there are only jokers (no normal card counts, return right away)
        card_counts = Counter(card for card in self.cards if card != joker)

        if len(card_counts) == 0:
            return (7, *cards)

        # Otherwise, let every joker count as the most common card
        most_common_card = max(card_counts, key=lambda card: (card_counts[card], card))
        card_counts[most_common_card] += n_jokers

        counts = sorted(card_counts.values(), reverse=True)
        return (self._find_category(counts), *cards)


def parse(input: str) -> list[tuple[Hand, int]]:
    hands = []

    for line in input.splitlines():
        hand_str, bid = line.split()

        cards = [
            int(card) if card.isdigit() else FACE_CARD_RANKS[card] for card in hand_str
        ]

        hand = Hand(cards), int(bid)
        hands.append(hand)

    return hands


def part1(hands: list[tuple[Hand, int]]) -> int:
    hands.sort(key=lambda hand: hand[0].rank_no_joker())

    return sum(rank * bid for rank, (_, bid) in enumerate(hands, start=1))


def part2(hands: list[tuple[Hand, int]]) -> int:
    hands.sort(key=lambda hand: hand[0].rank_joker())

    return sum(rank * bid for rank, (_, bid) in enumerate(hands, start=1))


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    example = read_file(2023, 7, "example")
    part1(parse(example))
