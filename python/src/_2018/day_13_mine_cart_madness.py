import sys
from typing import Optional

from attrs import define, field

from aoc.io import open_file
from aoc.util import timed

TURNS = [-1j, 1, 1j]
DIRECTIONS: dict[str, complex] = {">": 1, "v": 1j, "<": -1, "^": -1j}
DIRECTIONS_REV: dict[complex, str] = {1: ">", 1j: "v", -1: "<", -1j: "^"}
CURVES = {
    "/": {
        1: -1j,  # right → up
        -1: 1j,  # left → down
        1j: -1,  # down → left
        -1j: 1,  # up → right
    },
    "\\": {
        1: 1j,  # right → down
        -1: -1j,  # left → up
        1j: 1,  # down → right
        -1j: -1,  # up → left
    },
}


@define(hash=True)
class Cart:
    id: str
    pos: complex = field(eq=False, hash=False)
    dir: complex = field(eq=False, hash=False)
    dir_idx: int = field(default=0, eq=False, hash=False)

    def move(self):
        self.pos += self.dir

    def turn(self, dir: Optional[complex] = None):
        if dir is not None:
            self.dir = dir
        else:
            self.dir *= TURNS[self.dir_idx]
            self.dir_idx = (self.dir_idx + 1) % len(TURNS)


Grid = dict[complex, str]


def parse(input: str) -> tuple[Grid, list[Cart]]:
    grid = {}
    carts = []

    for y, row in enumerate(input.splitlines()):
        for x, cell in enumerate(row):
            pos = complex(x, y)
            match cell:
                case "/" | "\\" | "-" | "|" | "+":
                    grid[pos] = cell
                case ">" | "v" | "<" | "^":
                    grid[pos] = "-" if cell in [">", "<"] else "|"
                    dir = DIRECTIONS[cell]

                    id = f"{len(carts)}"
                    cart = Cart(id, pos, dir)
                    carts.append(cart)

    return grid, carts


def print_grid(grid: Grid, carts: set[Cart]):
    max_x = int(max(grid.keys(), key=lambda pos: pos.real).real)
    max_y = int(max(grid.keys(), key=lambda pos: pos.imag).imag)

    image = [["."] * (max_x + 1) for _ in range(max_y + 1)]

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            pos = complex(x, y)

            cart = next((cart for cart in carts if cart.pos == pos), None)
            image[y][x] = (
                DIRECTIONS_REV[cart.dir] if cart is not None else grid.get(pos, ".")
            )

    print("\n".join("".join(row) for row in image))
    print()


def push_carts(grid: Grid, carts: list[Cart], *, part2: bool = False) -> str:
    remaining = set(carts)

    def pos_str(pos: complex):
        return f"{int(pos.real)},{int(pos.imag)}"

    while len(remaining) > 1:
        # Move carts from top-left to bottom-right
        curr_carts = sorted(remaining, key=lambda c: (c.pos.imag, c.pos.real))
        positions = {cart.pos: cart for cart in remaining}

        for cart in curr_carts:
            if cart not in remaining:
                continue

            # Remove old position
            positions.pop(cart.pos)
            cart.move()

            # Turn if needed
            match grid.get(cart.pos):
                case "+":
                    cart.turn()
                case "\\" | "/":
                    dir = CURVES[grid[cart.pos]][cart.dir]
                    cart.turn(dir)

            # Move

            if cart.pos in positions:
                if not part2:
                    return pos_str(cart.pos)

                # Remove both crashed carts
                other = positions.pop(cart.pos)
                remaining.discard(cart)
                remaining.discard(other)
                continue

            positions[cart.pos] = cart

    assert len(remaining) == 1
    return pos_str(next(iter(remaining)).pos)


def part1(grid: Grid, carts: list[Cart]) -> str:
    return push_carts(grid, carts, part2=False)


def part2(grid: Grid, carts: list[Cart]) -> str:
    return push_carts(grid, carts, part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(push_carts, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2018, 13, "input") as file:
        part2(*parse(file.read()))
