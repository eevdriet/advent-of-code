import pytest

from _2020.day_16_ticket_translation import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 16, name) as file:
        return parse(file.read())


@pytest.mark.parametrize("n, expected", [(1, 71)])
def test_examples1(n: int, expected: int):
    notes = data(f"example{n if n else ''}")
    assert part1(notes) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 27911


@pytest.mark.parametrize("n, expected", [(1, ["row", "class", "seat"])])
def test_examples2(n: int, expected: int):
    notes = data(f"example{n if n else ''}")
    assert notes.order_fields() == expected


def test_input2():
    input = data("input")
    assert part2(input) == 737176602479
