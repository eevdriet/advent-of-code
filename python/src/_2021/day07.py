from typing import *
from numpy import median, mean
from math import floor, ceil
import sys


def treachery_of_whales(positions: List[int]):
    m = median(positions)
    return sum(abs(m - position) for position in positions)

def treachery_of_whales2(positions: List[int]):
    mu = mean(positions)
    fuel = lambda pos, m: (abs(m - pos) * (abs(m - pos) + 1)) // 2
    
    opt1 = sum(fuel(pos, floor(mu)) for pos in positions)
    opt2 = sum(fuel(pos, ceil(mu)) for pos in positions)
    return min(opt1, opt2)

def main():
    positions = [int(position) for position in sys.stdin.readline().split(',')]
    
    print(treachery_of_whales(positions))
    print(treachery_of_whales2(positions))

if __name__ == '__main__':
    main()