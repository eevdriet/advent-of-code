from typing import List
from math import log2
import re
import sys


def find_value(mask: str, val: int) -> int:
    floating_bits = []
    bit = 1

    for bit_chr in reversed(mask):
        match bit_chr:
            case 'X':
                floating_bits.append(bit)
            case '1':
                val |= bit
            case '0':
                val &= ~bit
        
        bit <<= 1
        
    return val, floating_bits

def find_registers(mask: str, reg: int) -> List[int]:
    reg, floating_bits = find_value(mask, reg)
    registers = []
    
    def backtrack(pos: int, reg: int):
        if pos >= len(floating_bits):
            registers.append(reg)
            return
            
        backtrack(pos + 1, reg)
        reg ^= floating_bits[pos]
        backtrack(pos + 1, reg)
        reg ^= ~floating_bits[pos]

    backtrack(0, reg)
    return registers

def docking_data(data, *, part1: bool) -> int:
    mem = {}
    mask = ''
    
    for line in data:
        match line:
            case ('mask', new_mask):
                assert len(new_mask) == 36
                mask = new_mask
            case ('mem', reg, val):
                if part1:
                    new_val, _ = find_value(mask, val)
                    mem[reg] = new_val
                else:
                    registers = find_registers(mask, reg)
                    
                    for reg in registers:
                        mem[reg] = val

    return sum(val for val in mem.values())

def main():
    data = []

    for line in sys.stdin:
        line = line.strip()

        if (mask := re.match(r'mask = ([01X]+)', line)):
            data.append(('mask', mask.group(1)))
        elif (match := re.match(r'mem\[(\d+)\] = (\d+)', line)):
            reg, val = map(int, match.groups())

            data.append(('mem', reg, val))
        else:
            print(line)
            
    print(docking_data(data, part1=True))
    print(docking_data(data, part1=False))


if __name__ == '__main__':
    main()