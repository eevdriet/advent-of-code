import sys
from collections import deque
from collections.abc import Sequence

from attrs import define

from aoc.util import timed

Cards = deque[int]


@define
class CrabGame:
    player1: list[int]
    player2: list[int]

    @classmethod
    def parse(cls, text: str) -> "CrabGame":
        player1_text, player2_text = text.split("\n\n")

        def get_player(text: str) -> list[int]:
            _, *card_lines = text.splitlines()
            return [int(card) for card in card_lines]

        return cls(get_player(player1_text), get_player(player2_text))

    def score(self, winning_cards: Sequence[int]) -> int:
        return sum(
            (len(winning_cards) - idx) * card for idx, card in enumerate(winning_cards)
        )

    def combat(self) -> int:
        cards1 = Cards(self.player1)
        cards2 = Cards(self.player2)

        while cards1 and cards2:
            card1 = cards1.popleft()
            card2 = cards2.popleft()

            if card1 > card2:
                cards1.extend([card1, card2])
            elif card2 > card1:
                cards2.extend([card2, card1])
            else:
                raise RuntimeError("Must be a winner in every hand")

        player1_wins = len(cards1) > 0
        return self.score(cards1 if player1_wins else cards2)

    def recursive_combat(self) -> int:
        def combat(cards1: Cards, cards2: Cards) -> bool:
            seen = set()

            while cards1 and cards2:
                # Player 1 wins if current cards state has been seen before
                if (state := (tuple(cards1), tuple(cards2))) in seen:
                    return True

                seen.add(state)

                # Otherwise each play a card to determine a winner
                card1 = cards1.popleft()
                card2 = cards2.popleft()

                # Play a recursive subgame if enough cards are present for it
                if card1 <= len(cards1) and card2 <= len(cards2):
                    sub_cards1 = deque(tuple(cards1)[:card1])
                    sub_cards2 = deque(tuple(cards2)[:card2])

                    player1_wins = combat(sub_cards1, sub_cards2)

                # Otherwise decide the round winner normally
                else:
                    player1_wins = card1 > card2

                # Distribute winning cards in the same way as before
                if player1_wins:
                    cards1.extend([card1, card2])
                else:
                    cards2.extend([card2, card1])

            return len(cards1) > 0

        # Play the recursive game
        cards1 = Cards(self.player1)
        cards2 = Cards(self.player2)
        player1_wins = combat(cards1, cards2)

        return self.score(cards1 if player1_wins else cards2)


def parse(input: str) -> CrabGame:
    return CrabGame.parse(input)


def part1(game: CrabGame) -> int:
    return game.combat()


def part2(game: CrabGame) -> int:
    return game.recursive_combat()


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
