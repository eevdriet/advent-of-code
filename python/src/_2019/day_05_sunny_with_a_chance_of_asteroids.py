import sys
from collections import deque
from typing import Generator, Optional

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]


class IntCode:
    def __init__(self, memory: list[int]):
        self.mem = memory[:]  # make a local copy
        self.rel_base = 0
        self.ip = 0

    def _get(self, src: int, mode: int) -> int:
        match mode:
            case 0:
                return self.mem[src]
            case 1:
                return src
            case _:
                raise ValueError(f"Expected mode 0, 1 or 2, given {mode}")

    def run_until_output(self, inputs: list[int]) -> tuple[Optional[int], bool]:
        """
        Run the program until it produces an output (return (value, False)),
        or halts (return (None, True)), or needs input but none provided
        (return (None, False)).
        """
        inp: deque[int] = deque(inputs)

        while True:
            instr = self.mem[self.ip]
            op = instr % 100
            m1 = (instr // 100) % 10
            m2 = (instr // 1000) % 10
            # m3 = (instr // 10000) % 10  # not needed for address params in this puzzle

            match op:
                case 1:
                    a, b, dst = self.mem[self.ip + 1 : self.ip + 4]
                    self.mem[dst] = self._get(a, m1) + self._get(b, m2)
                    self.ip += 4

                case 2:
                    a, b, dst = self.mem[self.ip + 1 : self.ip + 4]
                    self.mem[dst] = self._get(a, m1) * self._get(b, m2)
                    self.ip += 4

                case 3:
                    dst = self.mem[self.ip + 1]
                    if not inp:
                        # need input but none available: pause and return (no output, not halted)
                        return None, False
                    self.mem[dst] = inp.popleft()
                    self.ip += 2

                case 4:
                    src = self.mem[self.ip + 1]
                    out = self._get(src, m1)
                    self.ip += 2
                    return out, False

                case 5:
                    a, b = self.mem[self.ip + 1 : self.ip + 3]
                    if self._get(a, m1) != 0:
                        self.ip = self._get(b, m2)
                    else:
                        self.ip += 3

                case 6:
                    a, b = self.mem[self.ip + 1 : self.ip + 3]
                    if self._get(a, m1) == 0:
                        self.ip = self._get(b, m2)
                    else:
                        self.ip += 3

                case 7:
                    a, b, dst = self.mem[self.ip + 1 : self.ip + 4]
                    self.mem[dst] = 1 if self._get(a, m1) < self._get(b, m2) else 0
                    self.ip += 4

                case 8:
                    a, b, dst = self.mem[self.ip + 1 : self.ip + 4]
                    self.mem[dst] = 1 if self._get(a, m1) == self._get(b, m2) else 0
                    self.ip += 4

                case 99:
                    return None, True
                case _:
                    raise RuntimeError(f"Unknown opcode {op} at ip={self.ip}")


def run(program: list[int], inputs: list[int]) -> Generator[int, None, None]:
    ip = 0
    inputs = inputs[:]

    def get_val(src: int, mode: int) -> int:
        return src if mode == 1 else program[src]

    while True:
        instruction = program[ip]

        op = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10
        mode3 = (instruction // 10000) % 10

        match op:
            # Add
            case 1:
                src1, src2, dst = program[ip + 1 : ip + 4]
                program[dst] = get_val(src1, mode1) + get_val(src2, mode2)
                ip += 4

            # Multiply
            case 2:
                src1, src2, dst = program[ip + 1 : ip + 4]
                program[dst] = get_val(src1, mode1) * get_val(src2, mode2)
                ip += 4

            # Input
            case 3:
                if not inputs:
                    # Wait for new input to be sent to the generator
                    new_input = yield None
                    inputs.append(new_input)

                dst = program[ip + 1]
                program[dst] = inputs.pop(0)
                ip += 2

            # Output
            case 4:
                out = get_val(program[ip + 1], mode1)
                ip += 2

                yield out

            # Jump if true
            case 5:
                if get_val(program[ip + 1], mode1) != 0:
                    ip = get_val(program[ip + 2], mode2)
                else:
                    ip += 3

            # Jump if false
            case 6:
                if get_val(program[ip + 1], mode1) == 0:
                    ip = get_val(program[ip + 2], mode2)
                else:
                    ip += 3

            # Less than
            case 7:
                first, second, third = program[ip + 1 : ip + 4]
                program[third] = (
                    1 if get_val(first, mode1) < get_val(second, mode2) else 0
                )
                ip += 4

            # Equals
            case 8:
                first, second, third = program[ip + 1 : ip + 4]
                program[third] = (
                    1 if get_val(first, mode1) == get_val(second, mode2) else 0
                )
                ip += 4

            # Halt
            case 99:
                return


def part1(nums: list[int]) -> int:
    inputs = [1]
    outputs = [val for val in run(nums, inputs)]

    return outputs[-1]


def part2(nums: list[int]) -> int:
    inputs = [5]
    outputs = [val for val in run(nums, inputs)]

    return outputs[-1]


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
