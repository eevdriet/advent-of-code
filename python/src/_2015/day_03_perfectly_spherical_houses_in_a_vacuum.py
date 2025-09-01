import sys

from aoc.util import timed


def parse(input: str) -> str:
    return input


def n_houses_visited(moves: str, *, n_santas: int = 1) -> int:
    x = [0] * n_santas
    y = [0] * n_santas
    visited = {(0, 0)}

    for santa in range(n_santas):
        for idx in range(0, len(moves), n_santas):
            if santa + idx >= len(moves):
                break

            move = moves[idx + santa]
            match move:
                case ">":
                    x[santa] += 1
                case "<":
                    x[santa] -= 1
                case "^":
                    y[santa] += 1
                case "v":
                    y[santa] -= 1

            pos = (x[santa], y[santa])
            visited.add(pos)

    return len(visited)


def part1(moves: str) -> int:
    return n_houses_visited(moves, n_santas=1)


def part2(moves: str) -> int:
    return n_houses_visited(moves, n_santas=2)


def main():
    input = sys.stdin.read()
    moves = parse(input)

    result1, elapsed = timed(part1, moves)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, moves)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
