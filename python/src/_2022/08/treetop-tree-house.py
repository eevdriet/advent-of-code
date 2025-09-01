from typing import *
import sys

def treetop_tree_house(grid: List[List[int]]):
    rows, cols = len(grid), len(grid[0])
    n_visible = 0

    for row in range(rows):
        for col in range(cols):
            height = grid[row][col]

            visible = False
            visible |= all(grid[row][c] < height for c in range(col))
            visible |= all(grid[row][c] < height for c in range(col + 1, cols))
            visible |= all(grid[r][col] < height for r in range(row))
            visible |= all(grid[r][col] < height for r in range(row + 1, rows))
            
            n_visible += visible
                
    return n_visible

def treetop_tree_house2(grid: List[List[int]]):
    rows, cols = len(grid), len(grid[0])
    max_score = 0
    
    def count_trees(positions: List[Tuple[int, int]], height: int) -> int:
        n_trees = 0
        
        for row, col in positions:
            n_trees += 1
            if grid[row][col] >= height:
                break
        
        return n_trees
    
    for row in range(rows):
        for col in range(cols):
            height = grid[row][col]

            score = 1
            score *= count_trees([(row, c) for c in reversed(range(col))], height)
            score *= count_trees([(row, c) for c in range(col + 1, cols)], height)
            score *= count_trees([(r, col) for r in reversed(range(row))], height)
            score *= count_trees([(r, col) for r in range(row + 1, rows)], height)
            
            max_score = max(max_score, score)
                
    return max_score

def main():
    grid = [[int(cell) for cell in line.strip()] for line in sys.stdin]

    print(treetop_tree_house(grid))
    print(treetop_tree_house2(grid))

if __name__ == '__main__':
    main()