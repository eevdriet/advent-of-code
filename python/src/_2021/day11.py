from typing import *
import sys

Coord = Tuple[int, int]
Octopuses = Dict[Coord, int]


def adjacent(pos: Coord) -> Iterator[Coord]:
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0:
                continue
            
            x, y = pos
            yield (x + dx, y + dy)

def dumbo_octopus(octopuses: Octopuses, *, part1: bool) -> int:
    n_flashes = 0
    step = 1

    while True:
        flashed = []

        for position in octopuses.keys():
            octopuses[position] += 1
            if octopuses[position] > 9:
                flashed.append(position)
                
        while flashed:
            position = flashed.pop()
            if octopuses[position] == 0:
                continue
            
            octopuses[position] = 0
            n_flashes += 1
            
            for neighbor in adjacent(position):
                if (neighbor not in octopuses) or octopuses[neighbor] == 0:
                    continue
                
                octopuses[neighbor] += 1
                if octopuses[neighbor] > 9:
                    flashed.append(neighbor)
            
        if part1 and step == 100:
            break
        if not part1 and all(energy == 0 for energy in octopuses.values()):
            break
            
        step += 1
        
    return n_flashes if part1 else step

def main():
    octopuses: Octopuses = {}

    for r, line in enumerate(sys.stdin):
        for c, energy in enumerate(line.strip()):
            octopuses[r, c] = int(energy)
            
    print(dumbo_octopus(octopuses.copy(), part1=True))
    print(dumbo_octopus(octopuses.copy(), part1=False))

if __name__ == '__main__':
    main()