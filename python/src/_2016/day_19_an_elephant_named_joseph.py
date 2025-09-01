import sys
from collections import deque
from math import log

from aoc.util import timed


def parse(input: str) -> int:
    return int(input)


def part1(n_elves: int) -> int:
    def neighbor(n: int) -> int:
        # You want to be in the first position for 2 elves (or 1)
        if n <= 2:
            return 1

        # Otherwise use the cases mentioned below
        if n & 1:
            return 2 * neighbor(n // 2) + 1
        else:
            return 2 * neighbor(n // 2) - 1

    return neighbor(n_elves)


def part3(n_elves: int) -> int:
    # Keep track of all elves in both halves
    # This makes it easy to steal from across the circle (leftmost takes rightmost)
    left = deque()
    right = deque()

    # Initialize elves
    for elf in range(1, n_elves + 1):
        if elf < (n_elves // 2) + 1:
            left.append(elf)
        else:
            right.appendleft(elf)

    # Keep stealing until a single elf remains
    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())

    return left[0] or right[0]


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
