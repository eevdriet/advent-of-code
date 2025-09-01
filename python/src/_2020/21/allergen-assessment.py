from typing import *
from collections import Counter
from itertools import chain
import sys
import re

Ingredients = List[str]
Allergens = List[str]
Food = Tuple[Ingredients, Allergens]
Foods = List[Food]

def find_allergen_count(foods: Foods):
    all_ingredients = set()
    ingredient_counter = Counter()
    possible = {}
    
    for ingredients, allergens in foods:
        all_ingredients.update(ingredients)
        ingredient_counter.update(ingredients)

        for allergen in allergens:
            if not allergen in possible: 
                possible[allergen] = set(ingredients)
            else:
                possible[allergen] &= set(ingredients)
            
    has_allergens = set(chain.from_iterable(possible.values()))
    no_allergens = all_ingredients - has_allergens

    return sum(ingredient_counter[ingredient] for ingredient in no_allergens)

def find_allergen_list(foods: Foods):
    possible = {}
    all_allergens = set()
    
    for ingredients, allergens in foods:
        all_allergens.update(allergens)

        for allergen in allergens:
            if not allergen in possible: 
                possible[allergen] = set(ingredients)
            else:
                possible[allergen] &= set(ingredients)
            
    assessed_ingredients = set() 
    assessment = []
    
    while len(assessment) < len(all_allergens):
        for allergen, ingredients in possible.items():
            options_left = ingredients - assessed_ingredients
            if len(options_left) == 1:
                ingredient = min(options_left)
                assessment.append((allergen, ingredient))
                assessed_ingredients.add(ingredient)
                break

    return ",".join(ingredient for allergen, ingredient in sorted(assessment))

def main():
    lines = [line.strip() for line in sys.stdin]
    
    foods = []
    for line in lines:
     if (match := re.match(r'(.*)\(contains (.*)\)', line)):
        ingredients = match.group(1).split()
        allergens = match.group(2).split(', ')
        foods.append((ingredients, allergens))
         
    print(find_allergen_count(foods))
    print(find_allergen_list(foods))


if __name__ == '__main__':
    main()