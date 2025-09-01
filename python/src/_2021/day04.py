from typing import *
import sys

Cell = Tuple[int, int]
Grid = List[List[int]]
GridMap = Dict[str, Cell] # number -> (row, col, checked_off) 
BingoCard = Tuple[Grid, GridMap]

MARKED = -1

def has_won(grid: Grid) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    diag1, diag2 = True, True
    
    for r in range(rows):
        row, col = True, True

        for c in range(cols):
            row &= grid[r][c] == MARKED
            col &= grid[c][r] == MARKED

            if r == c:
                diag1 &= grid[r][c] == MARKED
            if r + c == rows - 1:
                diag2 &= grid[r][c] == MARKED
                
        if row or col:
            return True
        
    return diag1 or diag2


def giant_squid(numbers: List[int], cards: List[BingoCard]) -> int:
    for number in numbers:
        for grid, grid_map in cards:
            if number not in grid_map:
                continue

            row, col = grid_map[number]
            grid[row][col] = MARKED
            
            if has_won(grid):
                non_marked = sum(cell for cell, (row, col) in grid_map.items() if grid[row][col] != MARKED)
                return number * non_marked
        
    return None

def giant_squid2(numbers: List[int], cards: List[BingoCard]) -> int:
    winners = [False] * len(cards)

    for number in numbers:
        for idx, (grid, grid_map) in enumerate(cards):
            if winners[idx]:
                continue
            if number not in grid_map:
                continue

            row, col = grid_map[number]
            grid[row][col] = MARKED
            
            if has_won(grid):
                winners[idx] = True
                
                if all(winners):
                    non_marked = sum(cell for cell, (row, col) in grid_map.items() if grid[row][col] != MARKED)
                    return number * non_marked
        
    return None

def main():
    number_line, *cards_lines = sys.stdin.read().split('\n\n')
    numbers = [int(number) for number in number_line.strip().split(',')]
    
    cards: List[BingoCard] = []
    for card_lines in cards_lines:
        grid = []
        grid_map = {}
        
        for r, row in enumerate(card_lines.strip().split('\n')):
            grid.append([])
            for c, cell in enumerate(row.strip().split()):
                grid_map[int(cell)] = (int(r), int(c))
                grid[r].append(int(cell))
                
        cards.append((grid, grid_map))
        
    print(giant_squid(numbers, cards))
    print(giant_squid2(numbers, cards))

if __name__ == '__main__':
    main()