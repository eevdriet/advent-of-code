from typing import *
import sys
from pprint import pprint
from collections import defaultdict

Seats = Dict[complex, bool]
AdjSeats = Dict[complex, List[complex]]

directions = {
    direction
    for row in (-1, 0, 1)
    for col in (-1, 0, 1)
    if (direction := row + col * 1j)
}


def find_direct_neighbors(seats: Seats) -> AdjSeats:
    return {
        seat: [
            neighbor
            for direction in directions
            if (neighbor := seat + direction) in seats
        ]
        for seat in seats
    }

def find_adjacent_neighbors(seats: Seats, rows: int, cols: int) -> AdjSeats:
    neighbors = defaultdict(list)

    for seat in seats:
        for direction in directions:
            neighbor = seat + direction
            
            while 0 <= neighbor.real < rows and 0 <= neighbor.imag < cols:
                if neighbor in seats:
                    neighbors[seat].append(neighbor)
                    break
                
                neighbor += direction
                
    return neighbors



def find_occupied(seats: Seats, neighbors: AdjSeats, limit: int) -> int:
    while True:
        new_seats = {} 

        for position, is_occupied in seats.items():
            count = (seats[neighbor] for neighbor in neighbors[position])
            
            if is_occupied:
                new_seats[position] = sum(count) < limit
            else:
                new_seats[position] = not any(count)
                
        if seats == new_seats:
            return sum(seats.values())
        
        seats = new_seats
    

def main():
    lines = sys.stdin.read().splitlines()
    
    seats = {
        row + col * 1j: False
        for row, line in enumerate(lines)
        for col, seat in enumerate(line)
        if seat == 'L'
    }

    part1 = find_direct_neighbors(seats)
    part2 = find_adjacent_neighbors(seats, len(lines), len(lines[0]))

    print(find_occupied(seats, part1, 4))
    print(find_occupied(seats, part2, 5))

if __name__ == '__main__':
    main()