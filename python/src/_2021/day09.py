from typing import *
from math import prod
import sys


def adjacent(position: complex, heights: Dict[complex, int]) -> Iterator[complex]:
    directions = [-1, 1, -1j, 1j]

    for direction in directions:
        if (neighbor := position + direction) in heights:
            yield neighbor

def smoke_basin(heights: Dict[complex, int]) -> int:
    total = 0
    
    for position, height in heights.items():
        if all(heights[neighbor] > height for neighbor in adjacent(position, heights)):
            total += height + 1
            
    return total

def smoke_basin2(heights: Dict[complex, int]) -> int:
    visited = set()

    def flood_fill(position: complex) -> int:
        if position in visited:
            return 0

        visited.add(position)

        if heights[position] == 9:
            return 0
        
        return 1 + sum(flood_fill(neighbor) for neighbor in adjacent(position, heights))
    
    sizes = [flood_fill(position) for position in heights.keys()]
    sizes.sort()

    return prod(sizes[-3:])

def main():
    heights = {}

    for r, line in enumerate(sys.stdin.readlines()):
        for c, height in enumerate(line.strip()):
            heights[complex(c, r)] = int(height)

    print(smoke_basin(heights))
    print(smoke_basin2(heights))

if __name__ == '__main__':
    main()