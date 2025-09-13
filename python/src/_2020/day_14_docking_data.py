import re
import sys

from attrs import define, field

from aoc.io import read_file
from aoc.util import timed

Instruction = tuple[str, ...]


@define
class System:
    mask: str = field(factory=lambda: "")
    mem: dict[int, int] = field(factory=lambda: {})

    def _execute(self, instruction: Instruction, part: int):
        match instruction:
            case ("mask", new_mask):
                self.mask = new_mask

            case ("mem", reg, val):
                reg, val = map(int, (reg, val))

                if part == 1:
                    result = self.mask_value(val)
                    self.mem[reg] = result

                elif part == 2:
                    for reg in self.find_registers(reg):
                        self.mem[reg] = val

            case _:
                raise ValueError(f"Invalid instruction '{instruction}'")

    def initialize(self, instructions: list[Instruction], *, part: int) -> int:
        for instruction in instructions:
            self._execute(instruction, part)

        return sum(val for val in self.mem.values())

    def mask_value(self, val: int) -> int:
        bit = 1

        for digit in reversed(self.mask):
            match digit:
                case "0":
                    val &= ~bit
                case "1":
                    val |= bit
                case "X":
                    pass
                case _:
                    raise ValueError(
                        f"Invalid digit '{digit}' found in mask {self.mask}"
                    )

            bit <<= 1

        return val

    def mask_address(self, address: int) -> tuple[int, list[int]]:
        bit = 1
        floating_bits = []

        for digit in reversed(self.mask):
            match digit:
                case "0":
                    pass
                case "1":
                    address |= bit
                case "X":
                    floating_bits.append(bit)
                case _:
                    raise ValueError(
                        f"Invalid digit '{digit}' found in mask {self.mask}"
                    )

            bit <<= 1

        return address, floating_bits

    def find_registers(self, reg: int) -> list[int]:
        address, floating_bits = self.mask_address(reg)
        regs = []

        def backtrack(pos: int, reg: int):
            if pos >= len(floating_bits):
                regs.append(reg)
                return

            backtrack(pos + 1, reg)
            backtrack(pos + 1, reg ^ floating_bits[pos])

        backtrack(0, address)
        return regs


def parse(input: str) -> list[Instruction]:
    instructions = []

    for line in input.splitlines():
        if match := re.match(r"mask = ([01X]+)", line):
            instructions.append(("mask", match.group(1)))

        elif match := re.match(r"mem\[(\d+)\] = (\d+)", line):
            reg, val = match.groups()
            instructions.append(("mem", reg, val))

        else:
            raise ValueError(f"Couldn't parse instruction from '{line}'")

    return instructions


def part1(instructions: list[Instruction]) -> int:
    system = System()
    return system.initialize(instructions, part=1)


def part2(instructions: list[Instruction]) -> int:
    system = System()
    return system.initialize(instructions, part=2)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2020, 14, "example2")
    print(part2(parse(input)))
