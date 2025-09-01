from typing import *
import itertools
import sys


def sea_cucumber(cucumbers: List[List[chr]]):
    rows, cols = len(cucumbers), len(cucumbers[0])
    step = 1

    for step in itertools.count(1):
        moved = False

        cucumbers2 = [[cucumbers[row][col] for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if cucumbers[row][col] != '>':
                    continue
                
                if cucumbers[row][(col + 1) % cols] == '.':
                    moved = True
                    cucumbers2[row][col] = '.'
                    cucumbers2[row][(col + 1) % cols] = '>'

        cucumbers3 = [[cucumbers2[row][col] for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if cucumbers2[row][col] != 'v':
                    continue
                
                if cucumbers2[(row + 1) % rows][col] == '.':
                    moved = True
                    cucumbers3[row][col] = '.'
                    cucumbers3[(row + 1) % rows][col] = 'v'
    
        if not moved:
            break

        cucumbers = cucumbers3
        
    return step

def main():
    lines = [line.strip() for line in sys.stdin]
    cucumbers = [[cell for cell in line] for line in lines]

    print(sea_cucumber(cucumbers))

if __name__ == '__main__':
    main()