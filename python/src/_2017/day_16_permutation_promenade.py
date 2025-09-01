import sys
from collections import deque

from aoc.util import timed

Move = tuple[str, ...]


def parse(input: str) -> list[Move]:
    moves = []

    for move in input.split(","):
        typ = move[0]
        args = move[1:].split("/")

        moves.append((typ, *args))

    return moves


def dance(programs: deque[str], moves: list[Move]) -> deque[str]:
    for move in moves:
        match move:
            case ("s", n_rotations):
                programs.rotate(int(n_rotations))
            case ("x", src, dst):
                idx1, idx2 = map(int, (src, dst))
                programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
            case ("p", src, dst):
                idx1, idx2 = map(int, (programs.index(src), programs.index(dst)))
                programs[idx1], programs[idx2] = programs[idx2], programs[idx1]

    return programs


def part1(moves: list[Move]) -> str:
    programs = deque([chr(ord("a") + offset) for offset in range(16)])

    return "".join(dance(programs, moves))


def part2(moves: list[Move], n_dances: int = 1_000_000) -> str:
    # Determine the effect of a single dance on the positions
    curr = deque([chr(ord("a") + offset) for offset in range(16)])

    # Keep going until we come back to a dance we've seen before
    def hash(queue: deque[str]) -> str:
        return "".join(queue)

    seen = {hash(curr): 0}
    cycle_len = n_dances
    curr_dance = 1

    while curr_dance < n_dances:
        curr = dance(curr, moves)
        key = hash(curr)

        if key in seen:
            cycle_len = curr_dance - seen[key]
            break

        seen[key] = curr_dance
        curr_dance += 1

    # Then perform the remaining dances
    n_remaining = (n_dances - curr_dance) % cycle_len

    for _ in range(n_remaining):
        curr = dance(curr, moves)

    return "".join(curr)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    programs = deque([chr(ord("a") + offset) for offset in range(5)])

    moves = "s1,x3/4,pe/b"
    part2(parse(moves))
    dance(programs, parse(moves))
