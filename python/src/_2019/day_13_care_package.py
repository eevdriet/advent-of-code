import sys

from _2019.day_09_sensor_boost import IntCode
from aoc.io import read_file
from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",")]


def part1(nums: list[int]) -> int:
    program = IntCode(nums)
    outputs, _ = program.run([])

    return sum(1 for idx in range(2, len(outputs), 3) if outputs[idx] == 2)


def part2(nums: list[int]) -> int:
    nums[0] = 2
    program = IntCode(nums)
    input = 0

    score = 0
    x_paddle = None
    x_ball = None

    while True:
        # Run the program until it expects another input or halts
        outputs, has_halted = program.run([input])
        assert len(outputs) % 3 == 0

        # Go through the output to update the score / coordinates
        for idx in range(0, len(outputs), 3):
            x, y, tile = outputs[idx : idx + 3]

            match x, y, tile:
                case -1, 0, _:
                    score = tile
                case _, _, 3:
                    x_paddle = x
                case _, _, 4:
                    x_ball = x

        # Stop running the program after it's halted
        if has_halted:
            break

        # Determine next output based on the ball and paddle coordinates
        if x_ball is None or x_paddle is None:
            input = 0
        elif x_ball < x_paddle:
            input = -1
        elif x_ball > x_paddle:
            input = 1
        else:
            input = 0

    return score


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 13)
    part1(parse(input))
