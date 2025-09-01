from typing import *
import sys


def combo_breaker(base: int, exp: int, *, n_iters: int, mod: int):
    for candidate in range(n_iters):
        if pow(7, candidate, 20201227) == exp:
            return pow(base, candidate, mod)
        
    return None

def main():
    lines = [line.strip() for line in sys.stdin]
    card, door, *_ = [int(line) for line in lines]
    
    print(combo_breaker(card, door, n_iters=100_000_000, mod=20201227))
    print(combo_breaker(door, card, n_iters=100_000_000, mod=20201227))

if __name__ == '__main__':
    main()