from typing import *
from collections import Counter, defaultdict
import sys


def lanternfish(fishes: List[int], *, n_days: int) -> int:
    fish_counter = Counter(fishes)
    
    for _ in range(n_days):
        new_counter = defaultdict(int)

        for fish, count in fish_counter.items():
            new_counter[(fish + 8) % 9] += count

            if fish == 0:
                new_counter[8] += count
            
        fish_counter = new_counter
        
    return sum(count for count in fish_counter.values())

def main():
    fishes = [int(fish) for fish in sys.stdin.readline().split(',')]
    
    print(lanternfish(fishes, n_days=80))   # part 1
    print(lanternfish(fishes, n_days=256))  # part 2

if __name__ == '__main__':
    main()