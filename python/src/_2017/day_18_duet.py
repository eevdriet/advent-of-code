import operator
import sys
import threading
from collections import deque
from typing import Optional, override

from aoc.io import open_file
from aoc.program import Operation, Program
from aoc.program.ops import Add, Assign, Jump, Mod, Mul
from aoc.util import timed


class DuetProgram(Program):
    def __init__(self, p_val: int = 0):
        super().__init__(str(p_val))
        self["p"] = p_val

        # Use queues to send sounds between this and the partner program
        self.partner: Optional["DuetProgram"] = None
        self.inbox = deque([])
        self.outbox = self.inbox

        # Use a lock to indicate whether any sounds can be received
        self.is_waiting = False
        self.n_sends = 0

    def wire(self, other: "DuetProgram"):
        self.partner = other
        self.outbox = other.inbox

    def _execute(self, operation: Operation):
        print(self, operation)
        super()._execute(operation)


class JumpGreaterZero(Jump):
    def __init__(self, val: str, jump: str) -> None:
        super().__init__(operator.gt, val, "0", jump)


class Send(Operation[DuetProgram]):
    def __init__(self, val: str):
        self.val = val

    def execute(self, program: DuetProgram):
        # Send the sound
        sound = program.get_val(self.val)
        program.outbox.append(sound)
        program.n_sends += 1


class Receive(Operation[DuetProgram]):
    def __init__(self, reg: str, part2: bool):
        self.reg = reg
        self.part2 = part2

    def execute(self, program: DuetProgram):
        if not self.part2:
            if program[self.reg] != 0:
                program.halt()

            return

        # Wait until we can receive a sound
        if not program.inbox:
            program.is_waiting = True
            return

        program.is_waiting = False

        val = program.inbox.popleft()
        program[self.reg] = val


def parse(input: str, part2: bool) -> list[Operation[DuetProgram]]:
    ops = []

    for line in input.splitlines():
        match line.split():
            case ("snd", val):
                op = Send(val)
            case ("set", reg, val):
                op = Assign(reg, val)
            case ("add", reg, val):
                op = Add(reg, val)
            case ("mul", reg, val):
                op = Mul(reg, val)
            case ("mod", reg, val):
                op = Mod(reg, val)
            case ("rcv", val):
                op = Receive(val, part2)
            case ("jgz", val, jump):
                op = JumpGreaterZero(val, jump)
            case _:
                raise ValueError(f"Operation {line.split()} not recognized")

        ops.append(op)

    return ops


def part1(ops: list[Operation]) -> int:
    program = DuetProgram()
    program.run(ops)

    return program.outbox[-1]


def part2(ops: list[Operation]) -> int:
    # Set up the programs to wire to each other
    programs = [DuetProgram(idx) for idx in range(2)]
    for program in programs:
        program.operations = ops

    programs[0].wire(programs[1])
    programs[1].wire(programs[0])

    while True:
        for program in programs:
            if not (0 <= program.ip < len(ops)):
                program.halt()
                continue

            curr = program.operations[program.ip]
            program._execute(curr)

        if all(program.is_waiting or program.is_halted() for program in programs):
            break

    return programs[1].n_sends


def main():
    input = sys.stdin.read()

    result1, elapsed = timed(part1, parse(input, part2=False))
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parse(input, part2=True))
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    # with open_file(2017, 18, name="example") as file:
    #     result = part1(parse(file.read()))
    #     pass

    with open_file(2017, 18) as file:
        result = part2(parse(file.read(), True))
        print(result)
