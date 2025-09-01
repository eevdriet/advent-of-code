from typing import *
from ...util import adjacent
from collections import defaultdict
import sys

Cell = Tuple[int, ...]


def conway_cubes(active_cells: Set[Cell], *, n_cycles: int) -> int:
    for _ in range(n_cycles):
        neighbor_counts = defaultdict(int)
        
        for cell in active_cells:
            for neighbor in adjacent(cell):
                neighbor_counts[neighbor] += 1
                
        stay_on = {cell for cell in active_cells if cell in neighbor_counts and neighbor_counts[cell] in (2, 3)}
        turn_on = {cell for cell, count in neighbor_counts.items() if cell not in active_cells and count == 3}
        active_cells = stay_on | turn_on

    return len(active_cells)
    
def read_cells(lines: List[str], *, dim: int) -> Set[Cell]:
    return set(
        (x, y) + (0,) * (dim - 2)
        for y, line in enumerate(lines)
        for x, cell in enumerate(line)
        if cell == '#'
    )

def main():
    lines = [line.strip() for line in sys.stdin]

    for dim in (3, 4):
        active_cells = read_cells(lines, dim=dim)
        conway_cubes(active_cells, n_cycles=6)

if __name__ == '__main__':
    main()