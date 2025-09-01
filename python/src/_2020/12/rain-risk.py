from typing import *
import sys
import re

def rain_risk(instructions: List[Tuple[str, int]]):
    position = 0 + 0j
    direction = 1 + 0j
    
    for action, value in instructions:
        match action:
            case 'N':
                position += value * 1j
            case 'E':
                position += value * 1
            case 'S':
                position -= value * 1j
            case 'W':
                position -= value * 1
            case 'F':
                position += value * direction
                
            case 'L':
                direction *= (1j ** (value // 90))
            case 'R':
                direction /= (1j ** (value // 90))
        
    return abs(position.real) + abs(position.imag)

def rain_risk_2(instructions: List[Tuple[str, int]]):
    pos = 0 + 0j
    waypoint = 10 + 1j
    
    for action, value in instructions:
        match action:
            case 'N':
                waypoint += value * 1j
            case 'E':
                waypoint += value * 1
            case 'S':
                waypoint -= value * 1j
            case 'W':
                waypoint -= value * 1
            case 'F':
                pos += value * waypoint
                
            case 'L':
                waypoint *= (1j ** (value // 90))
            case 'R':
                waypoint /= (1j ** (value // 90))
        
    return abs(pos.real) + abs(pos.imag)

def main():
    instructions = []
    
    for line in sys.stdin.readlines():
        action, value = re.match(r'([FNESWLR])(\d+)', line).groups()
        instructions.append((action, int(value)))
    
    print(rain_risk(instructions))
    print(rain_risk_2(instructions))

if __name__ == '__main__':
    main()