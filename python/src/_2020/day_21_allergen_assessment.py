import re
import sys
from collections import Counter, defaultdict

from aoc.io import read_file
from aoc.util import timed

Food = tuple[set[str], set[str]]


def parse(input: str) -> list[Food]:
    foods = []
    for line in input.splitlines():
        match = re.match(r"(.*) \(contains (.*)\)", line)
        ingredients_text, allergens_text = match.groups()

        ingredients = set(ingredients_text.split())
        allergens = set(allergens_text.split(", "))

        food = ingredients, allergens
        foods.append(food)

    return foods


def part1(foods: list[Food]) -> int:
    # Keep track of all ingredients and how often they appear
    ingredients = set()
    ingredient_counts = Counter()

    # Keep track of which allergens are possible for each ingredient
    allergen_ingredients = {}

    for food_ingredients, allergens in foods:
        # Register new ingredients and add to their count
        ingredients |= food_ingredients
        ingredient_counts.update(food_ingredients)

        # Filter out ingredients that cannot be tied to specific allergens
        for allergen in allergens:
            if allergen not in allergen_ingredients:
                allergen_ingredients[allergen] = set(food_ingredients)
            else:
                allergen_ingredients[allergen] &= set(food_ingredients)

    # Partition the ingredients based on whether they can contain allergens
    has_allergens = {
        ingredient
        for ingredients in allergen_ingredients.values()
        for ingredient in ingredients
    }
    has_no_allergens = ingredients - has_allergens

    return sum(ingredient_counts[ingredient] for ingredient in has_no_allergens)


def part2(foods: list[Food]) -> str:
    # Keep track of all allergens and which are possible for each ingredient
    allergens = set()
    allergen_ingredients = defaultdict(set)

    for ingredients, food_allergens in foods:
        allergens |= food_allergens

        # Filter out ingredients that cannot be tied to specific allergens
        for allergen in food_allergens:
            if allergen not in allergen_ingredients:
                allergen_ingredients[allergen] = set(ingredients)
            else:
                allergen_ingredients[allergen] &= set(ingredients)

    # Perform pattern detection to o
    assessed_ingredients = set()
    result = {}

    while len(result) < len(allergens):
        for allergen, ingredients in allergen_ingredients.items():
            possible_ingredients = ingredients - assessed_ingredients

            if len(possible_ingredients) == 1:
                ingredient = next(iter(possible_ingredients))
                assessed_ingredients.add(ingredient)
                result[allergen] = ingredient
                break

    return ",".join(ingredient for _, ingredient in sorted(result.items()))


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2020, 21, "example")
    res = part2(parse(input))
    pass
