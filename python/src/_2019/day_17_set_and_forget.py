import sys
from typing import override

from attrs import define

from _2019.intcode import IntCode, asciify
from aoc.io import read_file
from aoc.util import adjacent4, timed


def parse(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]


DIR_CHARS = {1j: "^", -1j: "v", -1: "<", 1: ">"}
DIRS = {"^": -1j, "v": 1j, "<": -1, ">": 1}
Routine = list[str]


@define
class Image(dict):
    dir: complex
    start: complex

    @override
    def __str__(self) -> str:
        x_max = int(max(coord.real for coord in self.keys()))
        y_max = int(max(coord.imag for coord in self.keys()))

        img = ""
        for y in range(y_max + 1):
            for x in range(x_max + 1):
                coord = complex(x, y)
                img += self.get(coord, " ")

        return img

    @classmethod
    def scan(cls, memory: list[int]) -> "Image":
        program = IntCode(memory)

        pos = 0 + 0j
        start = pos
        dir = 0j

        image = {}

        for cell in program.run():
            image[pos] = chr(cell)

            match chr(cell):
                case "\n":
                    pos = complex(0, pos.imag + 1)
                    continue
                case c if c in DIRS:
                    start = pos
                    dir = DIRS[c]
                case _:
                    pass

            pos = complex(pos.real + 1, pos.imag)

        img = cls(dir, start)
        img.update(image)

        return img

    def clean_path(self) -> list[str]:
        path = []
        coord = self.start
        dir = self.dir

        while True:
            # Include left/right turn if needed
            if self.get(coord + dir) != "#":
                if self.get(coord + (left := dir * -1j)) == "#":
                    path.append("L")
                    dir = left
                elif self.get(coord + (right := dir * 1j)) == "#":
                    path.append("R")
                    dir = right
                elif self.get(coord + dir) == ".":
                    break

                else:
                    raise ValueError(
                        f"Next position cannot be reached from {coord} by turning L/R"
                    )

            # Then step as many spots as possible to the scaffold
            n_steps = 0
            while self.get(coord + dir) == "#":
                coord += dir
                n_steps += 1

            path.append(str(n_steps))

        return path

    def find_repeat(
        self, path: list[str], routines: list[list[str]], main: list[int]
    ) -> tuple[bool, list[list[str]] | None, list[int] | None]:
        MAX_REGISTER_LENGTH = 20

        cleared = False
        while not cleared:
            cleared = True

            for i, prev in enumerate(routines):
                if len(prev) <= len(path) and path[: len(prev)] == prev:
                    path = path[len(prev) :]
                    main.append(i)
                    cleared = False
                    break

        # last run
        # either we have consumed all of our path
        # or this is a dead-end
        if len(routines) == 3:
            return (True, routines, main) if len(path) == 0 else (False, None, None)

        register_len = min(len(path), MAX_REGISTER_LENGTH // 2)

        # our string form of the path must fit within our register constraint
        # we start on a turn, so we do not want to end on a turn
        # repeats could then be (turn, turn, #), which is not an efficient sequence
        while len(",".join(path[:register_len])) > MAX_REGISTER_LENGTH or path[
            register_len - 1
        ] in {"R", "L"}:
            register_len -= 1

        while register_len > 0:
            res, matches, seq = self.find_repeat(
                path, routines + [path[:register_len]], main.copy()
            )
            if res:
                return res, matches, seq
            register_len -= 2

        return False, [], []


def part1(memory: list[int]) -> int:
    image = Image.scan(memory)
    intersections = {
        coord
        for coord, cell in image.items()
        if cell == "#"
        and all(image.get(neighbor) == "#" for neighbor in adjacent4(coord))
    }

    return int(
        sum(
            int(intersection.real) * int(intersection.imag)
            for intersection in intersections
        )
    )


def part2(memory: list[int]) -> int:
    # Retrieve the image and determine where the robot can start and go to
    image = Image.scan(memory.copy())

    # Then determine and compress the path the robot has to take to visit all scaffold
    path = image.clean_path()

    _, routines, sequence = image.find_repeat(path, [], [])
    if routines is None or sequence is None:
        raise RuntimeError

    # Finaly clean with the robot and determine the dust collected
    main = [chr(routine + ord("A")) for routine in sequence]
    input = (
        asciify(main)
        + asciify(routines[0])
        + asciify(routines[1])
        + asciify(routines[2])
        + asciify(["n", "\n"])
    )

    memory[0] = 2
    cleaning_program = IntCode(memory)

    dust = cleaning_program.run(input)
    return dust[-1]


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2019, 17)
    part2(parse(input))
