import pytest

from _2019.day_16_flawed_frequency_transmission import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 16, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "n, expected",
    [
        ("80871224585914546619083218645595", "24176176"),
        ("19617804207202209144916044189917", "73745418"),
        ("69317163492948606335995924319873", "52432133"),
    ],
)
def test_examples1(n: str, expected: str):
    assert part1(n) == expected


def test_input1():
    input = data("input")
    assert part1(input) == "59522422"


def test_input2():
    input = data("input")
    assert part2(input) == "18650834"
