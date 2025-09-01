import pytest

from _2016.day_09_explosives_in_cyberspace import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 9, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "format, expected",
    [
        ("ADVENT", 6),
        ("A(1x5)BC", 7),
        ("(3x3)XYZ", 9),
        ("A(2x2)BCD(2x2)EFG", 11),
        ("(6x1)(1x3)A", 6),
        ("X(8x2)(3x3)ABCY", 18),
    ],
)
def test_examples1(format, expected):
    assert part1(format) == expected


@pytest.mark.parametrize(
    "format, expected",
    [
        ("(3x3)XYZ", 9),
        ("X(8x2)(3x3)ABCY", 20),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ],
)
def test_examples2(format, expected):
    assert part2(format) == expected


def test_input1(input):
    assert part1(input) == 70186


def test_input2(input):
    assert part2(input) == 10915059201
