import re
import sys

from aoc.io import FileType, open_file

Instruction = tuple[str, int]


def rope_bridge(instructions: list[Instruction], *, rope_len: int) -> int:
    rope = [0j] * rope_len
    seen = [set([x]) for x in rope]
    dirs = {"L": +1, "R": -1, "D": 1j, "U": -1j}
    sign = lambda x: complex((x.real > 0) - (x.real < 0), (x.imag > 0) - (x.imag < 0))

    for dir, n_steps in instructions:
        for _ in range(n_steps):
            rope[0] += dirs[dir]

            for idx in range(1, rope_len):
                dist = rope[idx - 1] - rope[idx]
                if abs(dist) < 2:
                    continue

                rope[idx] += sign(dist)
                seen[idx].add(rope[idx])

    return len(seen[rope_len - 1])


def main():
    with open_file(2022, 9, FileType.INPUT) as file:
        lines = [line.strip() for line in file.readlines()]

    instructions = []
    for line in lines:
        if match := re.match(r"(U|R|D|L) (\d+)", line):
            dir, n_steps = match.groups()
            instructions.append((dir, int(n_steps)))

    print(rope_bridge(instructions, rope_len=2))  # part 1
    print(rope_bridge(instructions, rope_len=10))  # part 2


if __name__ == "__main__":
    main()
