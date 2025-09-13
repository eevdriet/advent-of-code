import pytest

from _2020.day_23_crab_cups import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 23, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "cups_str, n_rounds, expected",
    [("389125467", 10, "92658374"), ("389125467", 100, "67384529")],
)
def test_examples1(cups_str: str, n_rounds: int, expected: int):
    cups = parse(cups_str)
    assert part1(cups, n_rounds) == expected


def test_input1():
    input = data("input")
    assert part1(input) == "95648732"


@pytest.mark.parametrize(
    "cups_str, expected",
    [("389125467", 149245887792)],
)
def test_examples2(cups_str: str, expected: int):
    cups = parse(cups_str)
    assert part2(cups) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 192515314252
