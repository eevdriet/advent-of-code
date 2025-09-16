import sys

from aoc.util import timed


def parse(input: str) -> list[list[int]]:
    return [
        [int(num) for num in elf_block.strip().splitlines()]
        for elf_block in input.split("\n\n")
    ]


def part1(elves: list[list[int]]) -> int:
    return max(sum(elf) for elf in elves)


def part2(elves: list[list[int]]) -> int:
    elves.sort(key=lambda elf: sum(elf))

    return sum(sum(elf) for elf in elves[-3:])


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
