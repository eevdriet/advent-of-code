import sys

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split()]


def redistribute(memory: list[int], part2: bool = False) -> int:
    seen = {}

    state = tuple(memory)
    n_cycles = 0

    while state not in seen:
        seen[state] = n_cycles
        n_cycles += 1

        # Determine memory bank with most memory
        max_idx = max(range(len(memory)), key=lambda i: (memory[i], -i))
        pos = max_idx

        for _ in range(memory[max_idx]):
            pos = (pos + 1) % len(memory)
            memory[pos] += 1
            memory[max_idx] -= 1

        state = tuple(memory)

    return n_cycles - seen[state] if part2 else n_cycles


def part1(memory: list[int]) -> int:
    return redistribute(memory)


def part2(memory: list[int]) -> int:
    return redistribute(memory, part2=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
