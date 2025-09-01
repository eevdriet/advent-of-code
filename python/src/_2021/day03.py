from typing import *
from collections import Counter
import sys


def binary_diagnostic(numbers: List[int]):
    gamma, epsilon = 0, 0
    bit = 1
    
    while True:
        n_bits_set = sum(bool(number & bit) for number in numbers)
        if n_bits_set == 0:
            break
        
        if n_bits_set > len(numbers) // 2:
            gamma |= bit
        else:
            epsilon |= bit
            
        bit <<= 1
        
    return gamma * epsilon

def binary_diagnostic2(numbers: List[str]):
    n_bits = max(len(number) for number in numbers)
    
    def diagnose(numbers: List[str], *, choose_common: bool) -> int:
        number_set = set(numbers)
        yes_chr = '0' if choose_common else '1'
        no_chr = str(1 - int(yes_chr))

        for idx in range(n_bits):
            bits_counter = Counter(number[idx] for number in number_set)
            
            if bits_counter['0'] > bits_counter['1']:
                number_set = {number for number in number_set if number[idx] == yes_chr}
            else:
                number_set = {number for number in number_set if number[idx] == no_chr}
                
            if len(number_set) == 1:
                break 
                
        return int(min(number_set), 2)

    oxygen = diagnose(numbers, choose_common=True)
    co2 = diagnose(numbers, choose_common=False)
    
    return oxygen * co2

def main():
    lines = [line.strip() for line in sys.stdin]
    numbers = [int(line.strip(), 2) for line in lines]
    
    print(binary_diagnostic(numbers))
    print(binary_diagnostic2(lines))

if __name__ == '__main__':
    main()