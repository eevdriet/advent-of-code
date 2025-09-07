import sys
from itertools import product

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]


def run(program: list[int]) -> int:
    ip = 0

    while ip + 3 < len(program):
        op, src1, src2, dst = program[ip : ip + 4]

        match op:
            case 1:
                program[dst] = program[src1] + program[src2]
            case 2:
                program[dst] = program[src1] * program[src2]
            case 99:
                break

        ip += 4

    return program[0]


def part1(nums: list[int]) -> int:
    nums[1] = 12
    nums[2] = 2

    return run(nums)


def part2(orig_nums: list[int]) -> int:
    RESULT = 19690720

    for noun, verb in product(range(100), repeat=2):
        nums = orig_nums.copy()
        nums[1] = noun
        nums[2] = verb

        if run(nums) == RESULT:
            return 100 * noun + verb

    raise RuntimeError(f"No valid noun, verb combination found to create {RESULT}")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(run, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
