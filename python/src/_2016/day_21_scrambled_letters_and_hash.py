import sys
from collections import deque

import parse as ps

from aoc.io import FileType, open_file
from aoc.util import timed

Instruction = tuple


def parse(input: str) -> list[Instruction]:
    instructions = []

    for line in input.splitlines():
        if match := ps.parse("swap position {:d} with position {:d}", line):
            instructions.append(("swap_pos", *match))
        elif match := ps.parse("swap letter {:w} with letter {:w}", line):
            instructions.append(("swap_letter", *match))

        elif match := ps.search("rotate {:w} {:d} step", line):
            instructions.append(("rotate_dir", *match))
        elif match := ps.parse("rotate based on position of letter {:w}", line):
            instructions.append(("rotate_letter", *match))

        elif match := ps.parse("reverse positions {:d} through {:d}", line):
            instructions.append(("reverse", *match))
        elif match := ps.parse("move position {:d} to position {:d}", line):
            instructions.append(("move", *match))

    return instructions


def perform(
    word: str, instructions: list[Instruction], *, in_reverse: bool = False
) -> str:
    result = list(word)
    if in_reverse:
        instructions.reverse()

    for instruction in instructions:
        match instruction:
            case ("swap_pos", left, right):
                result[left], result[right] = (
                    result[right],
                    result[left],
                )
            case ("swap_letter", first, second):
                idx1 = result.index(first)
                idx2 = result.index(second)

                result[idx1], result[idx2] = (
                    result[idx2],
                    result[idx1],
                )
            case ("reverse", left, right):
                while left < right:
                    result[left], result[right] = result[right], result[left]
                    left += 1
                    right -= 1
            case ("rotate_dir", dir, n_steps):
                if int(dir == "left") + int(in_reverse) == 1:
                    n_steps = len(result) - n_steps

                queue = deque(result)
                queue.rotate(n_steps)
                result = list(queue)
            case ("rotate_letter", letter):
                idx = result.index(letter)
                n_steps = (
                    idx + 1 + (idx >= 4)
                    if not in_reverse
                    else idx // 2 + (1 if (idx & 1 or idx == 0) else 5)
                )

                queue = deque(result)
                queue.rotate(n_steps)
                result = list(queue)
            case ("move", src, dst):
                if in_reverse:
                    src, dst = dst, src

                num = result[src]
                result.pop(src)
                result.insert(dst, num)

    return "".join(result)


def part1(instructions: list[Instruction]) -> str:
    return perform("abcdefgh", instructions)


def part2(instructions: list[Instruction]) -> str:
    return perform("fbgdceah", instructions, in_reverse=True)


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
