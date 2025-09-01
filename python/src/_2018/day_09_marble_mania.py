import sys
from collections import deque

import parse as ps

from aoc.types.list import ListNode
from aoc.util import timed


def parse(input: str) -> tuple[int, int]:
    return ps.parse("{:d} players; last marble is worth {:d} points", input)


def marble_game(n_players: int, last_marble: int) -> int:
    """
    - Place 0 in the circle, becomes CURR
    - Every normal turn
    - * Place lowest-remaining marble between marbles 1 and 2 clockwise from CURR
    - * That lowest-remaining becomes CURR
    - Every turn where lowest-remaining % 23 == 0
    - * Player keeps that marble and adds it to score
    - * Marble that is 7 counter-clockwise from CURR is removed and also added to score
    - * Marble clockwise of removed marble becomes CURR
    """
    scores = [0] * n_players
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        elf = marble % n_players

        if marble % 23 == 0:
            # Add the marble to the current elf's score if it divides 23
            scores[elf] += marble

            # Then add the marble 7 places counter-clockwise too and remove it
            circle.rotate(7)
            scores[elf] += circle.pop()

            # Continue with the elf clockwise from the removed marble
            circle.rotate(-1)
        else:
            # Add the marble inbetween the marble 1 and 2 steps clockwise
            circle.rotate(-1)
            circle.append(marble)

    return max(scores)


def part1(n_players: int, last_marble: int) -> int:
    return marble_game(n_players, last_marble)


def part2(n_players: int, last_marble: int) -> int:
    return marble_game(n_players, 100 * last_marble)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part1(9, 25)
