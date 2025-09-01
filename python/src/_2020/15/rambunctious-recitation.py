from typing import *
import sys


def rambunctious_recitation(numbers: List[int], *, n_rounds: int):
    spoken = {num: round + 1 for round, num in enumerate(numbers)}
    last_num = numbers[-1]

    for round in range(len(numbers), n_rounds):
        spoken[last_num], last_num = round, round - spoken.get(last_num, round)
        
    return last_num

def main():
    numbers = list(int(num) for num in sys.stdin.read().split(','))
    
    print(rambunctious_recitation(numbers, n_rounds=2020))
    print(rambunctious_recitation(numbers, n_rounds=30000000))

if __name__ == '__main__':
    main()