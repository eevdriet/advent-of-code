import sys

from aoc.util import timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",")]


def speak_numbers(start_nums: list[int], n_turns: int) -> int:
    # Keep track of the last spoken number and the turn every number was last spoken
    spoken = {num: turn for turn, num in enumerate(start_nums, start=1)}
    last_num = start_nums[-1]

    for turn in range(len(start_nums), n_turns):
        last = last_num

        last_num = turn - spoken.get(last_num, turn)
        spoken[last] = turn

    return last_num


def part1(nums: list[int]) -> int:
    return speak_numbers(nums, 2020)


def part2(nums: list[int]) -> int:
    return speak_numbers(nums, 30_000_000)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
