import pytest

from _2019.day_22_slam_shuffle import Instruction, parse, part1_affine, part2, shuffle
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 22, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "instructions, expected",
    [
        (
            [("deal", 7), ("deal", "stack"), ("deal", "stack")],
            [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],
        ),
        (
            [("cut", 6), ("deal", 7), ("deal", "stack")],
            [3, 0, 7, 4, 1, 8, 5, 2, 9, 6],
        ),
        (
            [
                ("deal", "stack"),
                ("cut", -2),
                ("deal", 7),
                ("cut", 8),
                ("cut", -4),
                ("deal", 7),
                ("cut", 3),
                ("deal", 9),
                ("deal", 3),
                ("cut", -1),
            ],
            [9, 2, 5, 8, 1, 4, 7, 0, 3, 6],
        ),
    ],
)
def test_examples1(instructions: list[Instruction], expected: int):
    cards = list(range(10))
    assert shuffle(cards, instructions) == expected


def test_input1():
    input = data("input")
    assert part1_affine(input) == 6526


def test_input2():
    input = data("input")
    assert part2(input) == 79855812422607
