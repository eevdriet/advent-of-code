from typing import *
import re
import sys


def trick_shot(x_min: int, x_max: int, y_min: int, y_max: int):
    def simulate(velo_x: int, velo_y: int, x=0, y=0):
        if x > x_max or y < y_min:
            return 0
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return 1

        return simulate(max(velo_x - 1, 0), velo_y - 1 , x + velo_x, y + velo_y)

    x_range = range(1, x_max + 1)
    y_range = range(y_min, -y_min)
    hits = (simulate(velo_x, velo_y) for velo_x in x_range for velo_y in y_range)

    return sum(hits)

def main():
    x_min, x_max, y_min, y_max = map(int, re.findall(r'-?\d+', sys.stdin.read()))

    print(y_min * (y_min + 1) // 2)                 # part 1
    print(trick_shot(x_min, x_max, y_min, y_max))   # part 2

if __name__ == '__main__':
    main()