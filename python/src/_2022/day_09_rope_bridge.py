import sys

from aoc.types import LetterDirection
from aoc.util import timed

Instruction = tuple[LetterDirection, int]
DIRECTION_STEPS: dict[LetterDirection, complex] = {"L": +1, "R": -1, "D": +1j, "U": -1j}


def parse(input: str) -> list[Instruction]:
    instructions = []

    for line in input.splitlines():
        dir, n_steps = line.split()

        instruction = dir, int(n_steps)
        instructions.append(instruction)

    return instructions


def count_tail_positions(instructions: list[Instruction], *, rope_len: int) -> int:
    # Keep track of the rope and which positions are seen by the tail
    rope = [0j] * rope_len
    seen_tail = {rope[-1]}

    def sign(num: int | float) -> int:
        return int(num > 0) - int(num < 0)

    for dir, n_steps in instructions:
        for _ in range(n_steps):
            # First move the head of the rope
            rope[0] += DIRECTION_STEPS[dir]

            # The let the rest of the rope follow if it is far away enough
            for idx in range(1, rope_len):
                dist = rope[idx - 1] - rope[idx]
                if abs(dist) < 2:
                    continue

                # If so, let the rope follow by a single step and count the tail position
                step = complex(sign(dist.real), sign(dist.imag))
                rope[idx] += step

                if idx == rope_len - 1:
                    seen_tail.add(rope[idx])

    return len(seen_tail)


def part1(instructions: list[Instruction]) -> int:
    return count_tail_positions(instructions, rope_len=2)


def part2(instructions: list[Instruction]) -> int:
    return count_tail_positions(instructions, rope_len=10)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
