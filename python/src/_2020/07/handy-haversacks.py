from typing import *
import re
import collections
import sys

Container = DefaultDict[str, Dict[str, int]]
ContainIn = DefaultDict[str, Set[str]]


def handy_haversacks(bags: ContainIn):
    holds_gold = set()
    
    def dfs(color: str):
        for outer_bag in bags[color]:
            holds_gold.add(outer_bag)
            dfs(outer_bag)
            
    dfs('shiny gold')
    return len(holds_gold)



def handy_haversacks_2(bags: Container):
    def count_bags(color: str) -> int:
        total_count = 0
        
        for inner_bag, count in bags[color].items():
            total_count += count
            total_count += count * count_bags(inner_bag)
            
        return total_count
    
    return count_bags('shiny gold')

def main():
    contains = collections.defaultdict(dict)
    contained_in = collections.defaultdict(set)

    for rule in [line.strip() for line in sys.stdin]:
        outer_bag = re.match(r'(.+?) bags contain', rule)[1]
        
        for count, inner_bag in re.findall(r'(\d+) (.+?) bags?[,.]', rule):
            contains[outer_bag][inner_bag] = int(count)
            contained_in[inner_bag].add(outer_bag)
        
    print(handy_haversacks(contained_in))
    print(handy_haversacks_2(contains))
    

if __name__ == '__main__':
    main()