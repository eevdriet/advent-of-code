from typing import *
import sys

Coord = Tuple[int, int]


def get_px_number(row: int, col: int, image: Set[Coord], is_on: bool) -> int:
    result = 0
    bit = 8
    
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
           if ((row + dr, col + dc) in image) == is_on:
               result += 2 ** bit
        bit -= 1
            
    assert 0 <= result < 512
    return result

def trench_map(image: Set[Coord], algorithm: List[chr], *, n_iterations: int) -> int:
    for step in range(n_iterations):
        is_on = (step % 2 == 0)
        new_image = set()

        min_row = min(row for row, _ in image)
        max_row = max(row for row, _ in image)
        min_col = min(col for _, col in image)
        max_col = max(col for _, col in image)

        for row in range(min_row - 5, max_row + 10):
            for col in range(min_col - 5, max_col + 10):
                new_px_number = get_px_number(row, col, image, is_on)
                if (algorithm[new_px_number] == '#') != is_on:
                    new_image.add((row, col))
                    
        image = new_image

    return len(image)

def main():
    algorithm, _, *image_lines = sys.stdin.read().splitlines()
    
    image = set()
    for row, line in enumerate(image_lines):
        for col, cell in enumerate(line):
            if cell == '#':
                image.add((row, col))

    print(trench_map(image.copy(), algorithm, n_iterations=2))
    print(trench_map(image.copy(), algorithm, n_iterations=50))

if __name__ == '__main__':
    main()