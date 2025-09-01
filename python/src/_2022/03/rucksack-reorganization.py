from typing import *
import sys


def find_priority(letter: str):
    if letter >= 'a':
        return 1 + (ord(letter) - ord('a'))

    return 27 + (ord(letter) - ord('A'))

def rucksack_reorganization(rucksacks: Iterable[List[str]]):
    total_priority = 0
    
    for rucksack in rucksacks:
        mid = len(rucksack) // 2

        common = set(item for item in rucksack[:mid])
        common &= set(item for item in rucksack[mid:])
        
        total_priority += sum(find_priority(item) for item in common)
    
    return total_priority

def rucksack_reorganization2(rucksacks: List[str]):
    total_priority = 0
    
    for idx in range(0, len(rucksacks), 3):
        common = set(item for item in rucksacks[idx])
        
        for rucksack in rucksacks[idx + 1:idx + 3]:
            common &= set(item for item in rucksack)

        total_priority += sum(find_priority(item) for item in common)
        
    return total_priority

def main():
	rucksacks = [line.strip() for line in sys.stdin]

	print(rucksack_reorganization(rucksacks))
	print(rucksack_reorganization2(rucksacks))

if __name__ == '__main__':
    main()