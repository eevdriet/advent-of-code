import sys
from collections import deque

from aoc.util import timed


def parse(input: str) -> str:
    return input.strip()


def str_recipes(recipes: list[int]):
    return "".join(str(digit) for digit in recipes)


def part1(recipe_str: str) -> str:
    n_recipes = int(recipe_str)
    score = "37"
    elves = [0, 1]

    while len(score) < n_recipes + 10:
        # Determine the new recipe(s) score and add them
        score += str(sum(int(score[elf]) for elf in elves))

        # Move the elves forward through the recipes
        for idx, elf in enumerate(elves):
            elves[idx] = (elf + 1 + int(score[elf])) % len(score)

    return score[n_recipes : n_recipes + 10]


def part2(recipe_str: str) -> int:
    score = "37"
    elves = [0, 1]

    while recipe_str not in score[-7:]:
        # Determine the new recipe(s) score and add them
        score += str(sum(int(score[elf]) for elf in elves))

        # Move the elves forward through the recipes
        for idx, elf in enumerate(elves):
            elves[idx] = (elf + 1 + int(score[elf])) % len(score)

    return score.index(recipe_str)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    part1(20)
