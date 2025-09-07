import pytest

from _2019.day_03_crossed_wires import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2019, 3, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "wire1, wire2, expected",
    [
        (
            [("R", 8), ("U", 5), ("L", 5), ("D", 3)],
            [("U", 7), ("R", 6), ("D", 4), ("L", 4)],
            6,
        ),
        (
            [
                ("R", 75),
                ("D", 30),
                ("R", 83),
                ("U", 83),
                ("L", 12),
                ("D", 49),
                ("R", 71),
                ("U", 7),
                ("L", 72),
            ],
            [
                ("U", 62),
                ("R", 66),
                ("U", 55),
                ("R", 34),
                ("D", 71),
                ("R", 55),
                ("D", 58),
                ("R", 83),
            ],
            159,
        ),
        (
            [
                ("R", 98),
                ("U", 47),
                ("R", 26),
                ("D", 63),
                ("R", 33),
                ("U", 87),
                ("L", 62),
                ("D", 20),
                ("R", 33),
                ("U", 53),
                ("R", 51),
            ],
            [
                ("U", 98),
                ("R", 91),
                ("D", 20),
                ("R", 16),
                ("D", 67),
                ("R", 40),
                ("U", 7),
                ("R", 15),
                ("U", 6),
                ("R", 7),
            ],
            135,
        ),
    ],
)
def test_examples1(wire1, wire2, expected):
    assert part1(wire1, wire2) == expected


def test_input1(data):
    input = data("input")
    assert part1(*input) == 865


@pytest.mark.parametrize(
    "wire1, wire2, expected",
    [
        (
            [("R", 8), ("U", 5), ("L", 5), ("D", 3)],
            [("U", 7), ("R", 6), ("D", 4), ("L", 4)],
            30,
        ),
        (
            [
                ("R", 75),
                ("D", 30),
                ("R", 83),
                ("U", 83),
                ("L", 12),
                ("D", 49),
                ("R", 71),
                ("U", 7),
                ("L", 72),
            ],
            [
                ("U", 62),
                ("R", 66),
                ("U", 55),
                ("R", 34),
                ("D", 71),
                ("R", 55),
                ("D", 58),
                ("R", 83),
            ],
            610,
        ),
        (
            [
                ("R", 98),
                ("U", 47),
                ("R", 26),
                ("D", 63),
                ("R", 33),
                ("U", 87),
                ("L", 62),
                ("D", 20),
                ("R", 33),
                ("U", 53),
                ("R", 51),
            ],
            [
                ("U", 98),
                ("R", 91),
                ("D", 20),
                ("R", 16),
                ("D", 67),
                ("R", 40),
                ("U", 7),
                ("R", 15),
                ("U", 6),
                ("R", 7),
            ],
            410,
        ),
    ],
)
def test_examples2(wire1, wire2, expected):
    assert part2(wire1, wire2) == expected


def test_input2(data):
    input = data("input")
    assert part2(*input) == 35038
