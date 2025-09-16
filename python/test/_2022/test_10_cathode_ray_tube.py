import pytest

from _2022.day_10_cathode_ray_tube import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2022, 10, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 0), (2, 13140)])
def test_examples1(n: int, expected: int):
    example = data(f"example{n if n else ''}")
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 13060


EXAMPLE_IMAGES = [
    "",
    "",
    """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""",
]


@pytest.mark.parametrize("n", [2])
def test_examples2(n: int):
    example = data(f"example{n if n else ''}")
    image = EXAMPLE_IMAGES[n]

    assert part2(example).strip() == image.strip()


INPUT_IMAGE = """
####...##.#..#.###..#..#.#....###..####.
#.......#.#..#.#..#.#..#.#....#..#....#.
###.....#.#..#.###..#..#.#....#..#...#..
#.......#.#..#.#..#.#..#.#....###...#...
#....#..#.#..#.#..#.#..#.#....#.#..#....
#.....##...##..###...##..####.#..#.####.
"""


def test_input2():
    input = data("input")
    assert part2(input).strip() == INPUT_IMAGE.strip()
