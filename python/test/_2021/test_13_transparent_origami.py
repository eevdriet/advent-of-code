import pytest

from _2021.day_13_transparent_origami import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2021, 13, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(0, 17)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(*example) == expected


def test_input1():
    input = data("input")
    assert part1(*input) == 631


EXAMPLE_IMAGE = """
#####
#...#
#...#
#...#
#####
.....
.....
"""

INPUT_IMAGE = """
####.####.#....####...##..##..###..####.
#....#....#....#.......#.#..#.#..#.#....
###..###..#....###.....#.#....#..#.###..
#....#....#....#.......#.#.##.###..#....
#....#....#....#....#..#.#..#.#.#..#....
####.#....####.#.....##...###.#..#.#....
"""


@pytest.mark.parametrize("n, expected", [(0, EXAMPLE_IMAGE)])
def test_examples2(n: int, expected: str):
    example = data(f"example{n if n else ''}")
    assert part2(*example).strip() == expected.strip()


def test_input2():
    input = data("input")
    assert part2(*input).strip() == INPUT_IMAGE.strip()
