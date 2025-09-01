from typing import *
from collections import Counter
import sys
import re

Coords = Tuple[int, int, int, int]



def hydrothermal_venture(coords: List[Coords], *, with_diags: bool):
    def get_vents(x1, y1, x2, y2) -> Iterator[complex]:
        if x1 == x2:
            yield from ((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        elif y1 == y2:
            yield from ((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
        elif with_diags:
            x_range = range(x1, x2 + 1) if x2 > x1 else reversed(range(x2, x1 + 1))
            y_range = range(y1, y2 + 1) if y2 > y1 else reversed(range(y2, y1 + 1))
            yield from ((x, y) for x, y in zip(x_range, y_range))

    coord_counter = Counter(
        vent 
        for coord in coords
        for vent in get_vents(*coord)
    ) 

    return sum(count >= 2 for count in coord_counter.values())

def main():
    lines = [line.strip() for line in sys.stdin]

    coords: List[Coords] = []
    for line in lines:
        if (match := re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)):
            coords.append(tuple(map(int, match.groups())))

    print(hydrothermal_venture(coords, with_diags=False))
    print(hydrothermal_venture(coords, with_diags=True))

if __name__ == '__main__':
    main()