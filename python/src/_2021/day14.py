from typing import *
from collections import Counter
import sys

Pair = str
Element = str

Pairs = Dict[Pair, int]
Elements = Dict[str, int]
Rules = Dict[Pair, Element]

def extended_polymerization(pairs: Pairs, elements: Elements, rules: Rules, *, n_steps: int) -> int:
    for _ in range(n_steps):
        for pair, count in pairs.copy().items():
            if pair not in rules:
                continue

            pairs[pair] -= count

            new_elem = rules[pair]
            elements[new_elem] += count

            first, second = pair
            pairs[first + new_elem] += count
            pairs[new_elem + second] += count
    
    return max(elements.values()) - min(elements.values())

def main():
    template, _, *rule_lines = sys.stdin.read().splitlines()
    
    elements = Counter(template)
    pairs = Counter(map(str.__add__, template, template[1:]))
    rules = dict(rule.split(" -> ") for rule in rule_lines)
    
    print(extended_polymerization(pairs.copy(), elements.copy(), rules, n_steps=10))      # part 1
    print(extended_polymerization(pairs.copy(), elements.copy(), rules, n_steps=40))      # part 2

if __name__ == '__main__':
    main()