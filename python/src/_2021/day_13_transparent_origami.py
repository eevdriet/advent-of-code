import re
import sys

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Instruction = tuple[str, int]


@define
class Paper:
    dots: set[complex]
    n_rows: int
    n_cols: int

    @classmethod
    def parse(cls, text: str) -> "Paper":
        dots = set()

        for line in text.splitlines():
            x, y = map(int, line.split(","))

            dot = complex(x, y)
            dots.add(dot)

        n_rows = 1 + int(max((dot.imag for dot in dots)))
        n_cols = 1 + int(max((dot.real for dot in dots)))

        return cls(dots, n_rows, n_cols)

    def fold_up(self, y: int):
        self.dots = {
            dot if dot.imag <= y else complex(dot.real, 2 * y - dot.imag)
            for dot in self.dots
        }

        self.n_rows = y

    def fold_left(self, x: int):
        self.dots = {
            dot if dot.real <= x else complex(2 * x - dot.real, dot.imag)
            for dot in self.dots
        }

        self.n_cols = x

    def create_image(self) -> str:
        image = ""

        for y in range(self.n_rows):
            for x in range(self.n_cols):
                coord = complex(x, y)
                image += "#" if coord in self.dots else "."

            image += "\n"

        return image.strip()


def parse(input: str) -> tuple[Paper, list[Instruction]]:
    paper_text, instructions_text = input.split("\n\n")
    paper = Paper.parse(paper_text)

    instructions = []
    for line in instructions_text.splitlines():
        match = re.match(r"fold along (x|y)=(\d+)", line)
        fold_axis, axis = match.groups()

        instruction = ("up" if fold_axis == "y" else "left", int(axis))
        instructions.append(instruction)

    return paper, instructions


def part1(paper: Paper, instructions: list[Instruction]) -> int:
    for fold_dir, axis in instructions[:1]:
        match fold_dir:
            case "up":
                paper.fold_up(axis)
            case "left":
                paper.fold_left(axis)
            case _:
                raise ValueError(f"Found invalid folding direction '{fold_dir}'")

    return len(paper.dots)


def part2(paper: Paper, instructions: list[Instruction]) -> str:
    for fold_dir, axis in instructions:
        match fold_dir:
            case "up":
                paper.fold_up(axis)
            case "left":
                paper.fold_left(axis)
            case _:
                raise ValueError(f"Found invalid folding direction '{fold_dir}'")

    return paper.create_image()


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, *parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, *parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2021, 13, "example")
    part1(*parse(input))
