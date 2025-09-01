import sys
from math import prod
from typing import Optional

from aoc.util import partitions, timed

Ingredient = dict[str, int]
N_TEA_SPOONS = 100
N_CALORIES = 500


def parse(input: str) -> list[Ingredient]:
    ingredients = []

    for line in input.splitlines():
        ingredient = {}

        name, properties = line.split(": ")
        ingredient["name"] = name

        for property in properties.split(", "):
            typ, val = property.split(" ")
            ingredient[typ] = int(val)

        ingredients.append(ingredient)

    return ingredients


def find_best_recipe(
    ingredients: list[Ingredient],
    total_tea_spoons: int,
    total_calories: Optional[int] = None,
) -> int:
    props = set(ingredients[0].keys()) - {"name", "calories"}
    max_score = 0

    for recipe in partitions(total_tea_spoons, len(ingredients)):

        def total(prop: str):
            return sum(
                n_tea_spoons * ingredient[prop]
                for ingredient, n_tea_spoons in zip(ingredients, recipe)
            )

        if total_calories is not None and total("calories") != total_calories:
            continue

        score = prod(max(0, total(prop)) for prop in props)
        max_score = max(score, max_score)

    return max_score


def part1(ingredients: list[Ingredient]) -> int:
    return find_best_recipe(ingredients, N_TEA_SPOONS)


def part2(ingredients: list[Ingredient]) -> int:
    return find_best_recipe(ingredients, N_TEA_SPOONS, N_CALORIES)


if __name__ == "__main__":
    input = sys.stdin.read()
    ingredients = parse(input)

    result1, elapsed = timed(part1, ingredients)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, ingredients)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
