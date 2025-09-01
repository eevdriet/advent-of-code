from typing import *
import sys

Patterns = List[str]
Outputs = List[str]
Entry = Tuple[Patterns, Outputs]


def seven_segment_search(entries: List[Entry]):
    uniq_digits = {'1': 2, '7': 3, '4': 4, '8': 7}

    total = 0
    for _, outputs in entries:
        total += sum(len(output) in uniq_digits.values() for output in outputs)
        
    return total

def seven_segment_search2(entries: List[Entry]):
    total = 0

    for patterns, outputs in entries:
        segments = {len(pattern): set(pattern) for pattern in patterns}
        four = segments[4]
        one = segments[2]
        number = ''

        for output in outputs:
            digits = set(output)
            
            match len(digits), len(digits & four), len(digits & one):
                case 2, _, _: number += '1'
                case 3, _, _: number += '7'
                case 4, _, _: number += '4'
                case 7, _, _: number += '8'
                case 5, 2, _: number += '2'
                case 5, 3, 1: number += '5'
                case 5, 3, 2: number += '3'
                case 6, 4, _: number += '9'
                case 6, 3, 1: number += '6'
                case 6, 3, 2: number += '0'
                
        total += int(number)
        
    return total

def main():
    lines = [line.strip() for line in sys.stdin]
    
    entries = []
    for line in lines:
        pattern, output = map(str.split, line.split(' | '))
        entries.append((pattern, output))
        
    print(seven_segment_search(entries))
    print(seven_segment_search2(entries))

if __name__ == '__main__':
    main()