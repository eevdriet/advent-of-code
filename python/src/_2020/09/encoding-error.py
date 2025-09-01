from typing import *
import sys
import itertools


def encoding_error(numbers: List[int], *, preamble: int):
    for idx in range(preamble, len(numbers)):
        target = numbers[idx]
        prev_numbers = numbers[idx - preamble:idx]
        
        for first, second in itertools.combinations(prev_numbers, 2):
            if first + second == target:
                break
        else:
            return target
        
    return None

def find_cont_sum(numbers: List[int], target: int):
    left, right = 0, 0
    cont_sum = numbers[left]

    while left <= right and right < len(numbers):
        if cont_sum < target:
            right += 1
            cont_sum += numbers[right]
        elif cont_sum > target:
            cont_sum -= numbers[left]
            left += 1
        else:
            cont_numbers = numbers[left:right+1]
            return min(cont_numbers) + max(cont_numbers)
        
    return None
    

def main():
    numbers = [int(line) for line in sys.stdin]
    first_number = encoding_error(numbers, preamble=25)
    print(find_cont_sum(numbers, first_number))

if __name__ == '__main__':
    main()