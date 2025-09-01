from typing import List, Set


def toboggan_trajectory(tree_pattern: List[str], slopes=[(3,1)]):
    rows, cols = len(tree_pattern), len(tree_pattern[0].strip())
    trees = {(row, col) for row in range(rows) for col in range(cols) if tree_pattern[row][col] == '#'}

    total_count = 1
    
    for slope in slopes:
        count = 0
        dc, dr = slope
        row, col = 0, 0

        while row < rows:
            if (row, col) in trees:
                count += 1
                
            row += dr
            col = (col + dc) % cols
            
        total_count *= count
            
    return total_count


def main():
    data = open(0).readlines()
    
    print(toboggan_trajectory(data))
    print(toboggan_trajectory(data, slopes=[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))

if __name__ == '__main__':
    main()