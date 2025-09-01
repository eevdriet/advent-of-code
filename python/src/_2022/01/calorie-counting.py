from typing import *
import sys


def calorie_counting(lines: List[str], *, n_max: int):
    calories = []
    
    curr_calories = 0
    for line in lines:
        if not line:
            calories.append(curr_calories)
            curr_calories = 0
            continue
            
        curr_calories += int(line)
        
    calories.sort()
    return sum(calories[:-n_max])

def main():
    lines = [line.strip() for line in sys.stdin]

    print(calorie_counting(lines, n_max=1))     # part 1
    print(calorie_counting(lines, n_max=3))     # part 2

if __name__ == '__main__':
    main()