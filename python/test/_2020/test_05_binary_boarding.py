import pytest

from _2020.day_05_binary_boarding import BoardingPass, parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 5, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "text, row, col",
    [("BFFFBBFRRR", 70, 7), ("FFFBBBFRRR", 14, 7), ("BBFFBBFRLL", 102, 4)],
)
def test_examples(text: str, row: int, col: int):
    boarding_pass = BoardingPass.parse(text)

    assert boarding_pass.row == row
    assert boarding_pass.col == col


def test_input1():
    input = data("input")
    assert part1(input) == 883


def test_input2():
    input = data("input")
    assert part2(input) == 532
