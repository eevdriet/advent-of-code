import pytest

from _2018.day_11_chronal_charge import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 11, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("serial, expected", [(18, "33,45")])
def test_examples1(serial, expected):
    assert part1(serial) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == "19,41"


@pytest.mark.parametrize("serial, expected", [(18, "90,269,16"), (42, "232,251,12")])
def test_examples2(serial, expected):
    assert part2(serial) == expected


def test_input2(data):
    input = data("input")
    assert part2(input) == "237,284,11"
