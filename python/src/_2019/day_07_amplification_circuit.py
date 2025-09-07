import sys
from itertools import permutations

from _2019.intcode import IntCode, Status
from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]


def part1(memory: list[int]) -> int:
    max_signal = 0

    for phases in permutations(range(5)):
        signal = 0

        for phase in phases:
            program = IntCode(memory.copy())

            inputs = [phase, signal]
            outputs = program.run(inputs)

            signal = outputs[-1]

        max_signal = max(signal, max_signal)

    return max_signal


def part2(memory: list[int]) -> int:
    max_signal = 0

    for phases in permutations(range(5, 10)):
        # Create amplifiers and feed them their phase once
        amps = [IntCode(memory.copy()) for _ in range(5)]
        for amp, phase in zip(amps, phases):
            amp.run([phase])

        signal = 0

        while not all(amp.status == Status.HALTED for amp in amps):
            for phase, amp in zip(phases, amps):
                inputs = [signal]
                outputs = amp.run(inputs)

                if outputs:
                    signal = outputs[-1]

        max_signal = max(signal, max_signal)

    return max_signal


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
