import sys

from aoc.util import timed

CHOICES = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3,
}
OUTCOMES = {
    "X": -1,
    "Y": 0,
    "Z": 1,
}
SCORES = {0: 3, 1: 6, 2: 0}


def parse(input: str) -> list[list[str]]:
    return [line.split() for line in input.splitlines()]


def part1(rounds: list[list[str]]) -> int:
    score = 0

    for opponent, player in rounds:
        # Count choice score
        score += CHOICES[player]

        # Count outcome score
        outcome = (CHOICES[player] - CHOICES[opponent]) % 3
        score += SCORES[outcome]

    return score


def part2(rounds: list[list[str]]) -> int:
    score = 0

    for opponent, player in rounds:
        # Count outcome score
        outcome_diff = OUTCOMES[player]
        score += SCORES[outcome_diff % 3]

        # Count choice score
        choice = 1 + ((CHOICES[opponent] - 1) + outcome_diff) % 3
        score += choice

    return score


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
