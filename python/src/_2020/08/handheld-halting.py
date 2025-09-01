from typing import *
import re
import sys


def handheld_halting(program: List[Tuple[str, int]], part1=True):
    executed = set()
    counter = 0
    accumulator = 0
    
    while True:
        if counter in executed:
            return accumulator if part1 else None
        if counter >= len(program):
            return None if part1 else accumulator

        executed.add(counter)

        match program[counter]:
            case ("jmp", val):
                counter += val
                continue
            case ("acc", val):
                accumulator += val

        counter += 1

def handheld_halting_2(program: List[Tuple[str, int]]):
    for idx, (op, arg) in enumerate(program):
        if op not in {'jmp', 'nop'}:
            continue
        
        new_op = 'jmp' if op == 'nop' else 'nop'
        new_program = program[:idx] + [(new_op, arg)] + program[idx + 1:]
        
        if (accumulator := handheld_halting(new_program, part1=False)) is not None:
            return accumulator
        
    return None

def main():
    lines = [line.strip() for line in sys.stdin]
    
    program = []
    for line in lines:
        op, arg = re.match(r'(nop|acc|jmp) ([+-]\d+)', line).groups()
        program.append((op, int(arg)))
        
    print(handheld_halting_2(program))

if __name__ == '__main__':
    main()
