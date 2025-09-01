from typing import *
import re
import sys


def contains(left1: int, right1: int, left2: int, right2: int) -> bool:
    return (left2 <= left1 and right1 <= right2) or \
        (left1 <= left2 and right2 <= right1)
        
def overlaps(left1: int, right1: int, left2: int, right2: int) -> bool:
    return (left2 <= left1 <= right2 or left2 <= right1 <= right2) or \
        (left1 <= left2 <= right1 or left1 <= right2 <= right1)

def camp_cleanup(numbers: List[Tuple[int, int, int, int]], check_func):
    return sum(check_func(*number) for number in numbers)

def main():
    numbers = []
    
    for line in sys.stdin:
        numbers.append(tuple(map(int, re.findall(r'\d+', line.strip()))))

    print(camp_cleanup(numbers, contains))      # part 1
    print(camp_cleanup(numbers, overlaps))      # part 2

if __name__ == '__main__':
    main()