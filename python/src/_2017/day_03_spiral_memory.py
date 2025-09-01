import sys

from aoc.util import timed


def parse(input: str) -> int:
    return int(input.strip())


def part1(num: int) -> int:
    # Find the nearest odd square >= n
    ring = 1
    while ring * ring < num:
        ring += 2

    radius = (ring - 1) // 2  # steps out from center
    square = ring * ring  # bottom-right corner

    # centers of each side
    centers = [square - radius - k * (ring - 1) for k in range(4)]

    dist_to_axis = min(abs(num - c) for c in centers)
    return radius + dist_to_axis


def part2(num: int) -> int:
    size = 1024
    grid = [[0] * size for _ in range(size)]

    width = 1
    row, col = size // 2, size // 2
    grid[row][col] = 1

    def val(row: int, col: int) -> int:
        return sum(grid[row + r][col + c] for r in (-1, 0, 1) for c in (-1, 0, 1))

    while grid[row][col] <= num:
        # Go right
        for _ in range(width):
            col += 1
            if (cell := val(row, col)) > num:
                return cell

            grid[row][col] = cell

        # Go up
        for _ in range(width):
            row -= 1
            if (cell := val(row, col)) > num:
                return cell

            grid[row][col] = cell

        width += 1

        # Go left
        for _ in range(width):
            col -= 1
            if (cell := val(row, col)) > num:
                return cell

            grid[row][col] = cell

        # Go down
        for _ in range(width):
            row += 1
            if (cell := val(row, col)) > num:
                return cell

            grid[row][col] = cell

        width += 1

    return -1


if __name__ == "__main__":
    # input = sys.stdin.read()
    # square = parse(input)
    #
    # result1, elapsed = timed(part1, square)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, square)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    part1(10)
