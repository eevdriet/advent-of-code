import sys

from aoc.util import timed

GRID = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]


def parse(input: str) -> dict[str, str]:
    replacements = {}

    for line in input.splitlines():
        src, dst = line.split(" => ")
        replacements[src] = dst

    def rotate(pattern: str) -> str:
        grid = [list(row) for row in pattern.split("/")]
        n = len(grid)

        rotated = [[grid[n - c - 1][r] for c in range(n)] for r in range(n)]
        return "/".join("".join(row) for row in rotated)

    def flip(pattern: str) -> str:
        first, *middle, last = pattern.split("/")

        return "/".join([last, *middle, first])

    # Add flips and rotations
    for src in list(replacements.keys()):
        dst = replacements[src]
        replacements[flip(src)] = dst

        curr = src
        for _ in range(3):
            curr = rotate(curr)
            replacements[curr] = dst
            replacements[flip(curr)] = dst

    return replacements


def simulate_grid(
    grid: list[list[str]], replacements: dict[str, str], n_iters: int
) -> int:
    for _ in range(n_iters):
        # Determine replacements
        size = len(grid)
        step = 2 if size % 2 == 0 else 3

        # Create new grid
        new_size = size + (size // step)
        new_grid = [["."] * new_size for _ in range(new_size)]

        # Go block by block to use replacement rules
        for row in range(0, len(grid), step):
            for col in range(0, len(grid[row]), step):
                src = "/".join(
                    "".join(grid[r][col : col + step]) for r in range(row, row + step)
                )

                if src not in replacements:
                    raise ValueError(f"No replacement for {src}")

                dst = replacements[src].split("/")

                # Fill in the replacement
                for r in range(step + 1):
                    for c in range(step + 1):
                        new_grid[row + r + row // step][col + c + col // step] = dst[r][
                            c
                        ]

        grid = new_grid

    return sum(
        1
        for row in range(len(grid))
        for col in range(len(grid[row]))
        if grid[row][col] == "#"
    )


def part1(replacements: dict[str, str]) -> int:
    return simulate_grid(GRID, replacements, 5)


def part2(replacements: dict[str, str]) -> int:
    return simulate_grid(GRID, replacements, 18)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    replacements = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""".strip()

    result = simulate_grid(GRID, parse(replacements), 2)
    pass
