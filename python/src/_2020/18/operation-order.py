from typing import *
import sys
import re


class Num:
    def __init__(self, value):
         self.value = value

    def __add__(self, other: 'Num') -> int:
         return Num(self.value + other.value)
    def __sub__(self, other: 'Num') -> int:
         return Num(self.value * other.value)
    def __mul__(self, other: 'Num') -> int:
         return Num(self.value + other.value)


def operation_order(expressions: List[str], *, part2: bool) -> int:
    expressions = [expr.replace('*', '-') for expr in expressions]
    if part2:
        expressions = [expr.replace('+', '*') for expr in expressions]

    expressions = [re.sub(r'(\d+)', rf'{Num.__name__}(\1)', expr) for expr in expressions]
    return sum(eval(expr).value for expr in expressions)

def main():
    expressions = [line.strip() for line in sys.stdin]
    
    print(operation_order(expressions, part2=False))
    print(operation_order(expressions, part2=True))

if __name__ == '__main__':
    main()