from typing import *
from collections import defaultdict
from copy import deepcopy
import re
import sys

Crate = str
Instruction = Tuple[int, int, int]

def supply_stacks(stacks: Dict[int, List[Crate]], instructions: List[Instruction]):
    for amount, src, dst in instructions:
        crates = [stacks[src].pop() for _ in range(amount)]
        stacks[dst].extend(crates)
        
    return ''.join(stacks[idx][-1] for idx in sorted(stacks.keys()))

def supply_stacks2(stacks: Dict[int, List[Crate]], instructions: List[Instruction]):
    for amount, src, dst in instructions:
        crates = stacks[src][-amount:]
        stacks[src] = stacks[src][:-amount]
        stacks[dst].extend(crates)
        
    return ''.join(stacks[idx][-1] for idx in sorted(stacks.keys()))

def main():
    stack_lines, instruction_lines = sys.stdin.read().split('\n\n')
    
    stacks = defaultdict(list)
    for line in stack_lines.splitlines():
        for match in re.finditer(r'\[(\w)\]', line):
            idx = 1 + (match.start() // 4)
            crate = match.group(1)
            
            stacks[idx].append(crate)
            
    for idx in stacks:
        stacks[idx].reverse()
            
    instructions = []
    for line in instruction_lines.splitlines():
        amount, src, dst = map(int, re.findall(r'\d+', line))
        instructions.append((amount, src, dst))

    print(supply_stacks(deepcopy(stacks), instructions))
    print(supply_stacks2(deepcopy(stacks), instructions))

if __name__ == '__main__':
    main()