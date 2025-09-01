from typing import *
import pprint
import sys


def prev_cells(row: int, col: int, rows: int, cols: int):
    if row + 1 < rows:
        yield row + 1, col
    if col + 1 < cols:
        yield row, col + 1

def chiton(grid: List[List[int]], *, n_expansions: int) -> int:
    rows, cols = len(grid), len(grid[0])

    dp = [[None] * n_expansions * cols for _ in range(n_expansions * rows)]
    for row in range(len(dp)):
        for col in range(len(dp[0])):
            elem = grid[row % rows][col % cols]
            offset = (row // rows) + (col // cols)
            risk = (elem + offset - 1) % 9 + 1
            dp[row][col] = risk

    rows, cols = len(dp), len(dp[0])
    
    for row in reversed(range(rows)):
        for col in reversed(range(cols)):
            neighbors = [dp[r][c] for r, c in prev_cells(row, col, rows, cols)]
            dp[row][col] += min(neighbors) if neighbors else 0

    return dp[0][0] - grid[0][0]

def main():
    grid = [[int(cell) for cell in row.strip()] for row in sys.stdin]

    print(chiton(grid, n_expansions=1))    # part 1
    print(chiton(grid, n_expansions=5))    # part 2

if __name__ == '__main__':
    main()