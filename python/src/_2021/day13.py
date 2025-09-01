from typing import *
import sys
import re

Dot = Tuple[int, int]
Fold = Tuple[str, int]

def transparent_origami(dots: Set[Dot], fold: Fold) -> Set[Dot]:
    axis, line = fold
    new_dots = set()
        
    for x, y in dots:
        match axis:
            case 'x':
                x = x if x < line else line - (x - line)
            case 'y':
                y = y if y < line else line - (y - line)
            
        new_dots.add((x, y))
        
    return new_dots

def part1(dots: Set[Dot], folds: List[Fold]) -> int:
    dots = transparent_origami(dots, folds[0])

    print(len(dots))

def part2(dots: Set[Dot], folds: List[Fold]):
    for fold in folds:
        dots = transparent_origami(dots, fold)

    for y in range(6):
        print(*[' #'[(x,y) in dots] for x in range(40)])

def main():
    dots_lines, instruction_lines = sys.stdin.read().split('\n\n')
    
    dots: Set[Dot] = set()
    for line in dots_lines.splitlines():
        x, y = map(int, line.split(','))
        dots.add((x, y))
        
    instructions: List[Fold] = []
    for line in instruction_lines.splitlines():
        if (match := re.match(r'fold along ([xy])=(\d+)', line)):
            instructions.append((match.group(1), int(match.group(2))))

    part1(dots, instructions)
    part2(dots, instructions)
    
if __name__ == '__main__':
    main()