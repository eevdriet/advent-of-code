import operator
import sys

from aoc.program import Operation, Program
from aoc.program.ops import Assign, Jump, Mul, Sub
from aoc.util import timed


class Coprocessor(Program):
    def __init__(self):
        super().__init__("Coprocessor")

        self.n_muls = 0


class DebugMul(Mul[Coprocessor]):
    def execute(self, program: Coprocessor):
        super().execute(program)
        program.n_muls += 1


class JumpNotZero(Jump):
    def __init__(self, val: str | int, jump: str | int):
        super().__init__(operator.ne, val, 0, jump)


def parse(input: str) -> list[Operation[Coprocessor]]:
    ops = []

    for line in input.splitlines():
        match line.split():
            case ("set", reg, val):
                op = Assign(reg, val)
            case ("sub", reg, val):
                op = Sub(reg, val)
            case ("mul", reg, val):
                op = DebugMul(reg, val)
            case ("jnz", val, jump):
                op = JumpNotZero(val, jump)
            case _:
                raise ValueError(f"Operation {line.split()} not recognized")

        ops.append(op)

    return ops


def part1(_operations: list[Operation]) -> int:
    # Compiled program
    n_muls = 0
    b = c = 57
    h = 0

    while True:
        f = 1

        for d in range(2, b):
            for e in range(2, b):
                g = d * e - b
                n_muls += 1

                if g == 0:
                    f = 0
        if f == 0:
            h += 1
        if b == c:
            break

        b += 17

    return n_muls


def part2(_operations: list[Operation]) -> int:
    def is_prime(num: int) -> bool:
        if num < 3:
            return num == 2

        div = 2
        while div * div <= num:
            if num % div == 0:
                return False

            div += 1

        return True

    b = 105700
    c = 122700
    h = 0

    for num in range(b, c + 1, 17):
        if not is_prime(num):
            h += 1

    return h


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
