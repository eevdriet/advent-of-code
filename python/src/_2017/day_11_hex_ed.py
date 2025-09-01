import sys

from aoc.util import timed

HexCoord = tuple[int, int]


def parse(input: str) -> list[str]:
    return input.strip().split(",")


def traverse_hex_grid(directions: list[str], *, objective: str) -> int:
    start: HexCoord = 0, 0
    pos: HexCoord = start
    seen = set([start])

    def dist(hex1: HexCoord, hex2: HexCoord) -> int:
        # Determine the distance
        x1, y1 = hex1
        x2, y2 = hex2

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        return dx + max(0, (dy - dx) // 2)

    for direction in directions:
        x, y = pos

        match direction:
            case "n":
                pos = (x, y - 2)
            case "s":
                pos = (x, y + 2)
            case "se":
                pos = (x + 1, y + 1)
            case "nw":
                pos = (x - 1, y - 1)
            case "ne":
                pos = (x + 1, y - 1)
            case "sw":
                pos = (x - 1, y + 1)

        seen.add(pos)

    match objective:
        case "dist_from_start":
            return dist(start, pos)
        case "furthest_from_start":
            return max((dist(start, pos) for pos in seen))
        case _:
            raise ValueError(f"Unknown objective {objective}")


def part1(directions: list[str]) -> int:
    return traverse_hex_grid(directions, objective="dist_from_start")


def part2(directions: list[str]) -> int:
    return traverse_hex_grid(directions, objective="furthest_from_start")


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(traverse_hex_grid, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
