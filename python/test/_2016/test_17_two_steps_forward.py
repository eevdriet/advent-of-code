import pytest

from _2016.day_17_two_steps_forward import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 17, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "passcode, expected",
    [
        ("ihgpwlah", "DDRRRD"),
        ("kglvqrro", "DDUDRLRRUDRD"),
        ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
    ],
)
def test_examples1(passcode, expected):
    assert part1(passcode) == expected


@pytest.mark.parametrize(
    "passcode, expected",
    [
        ("ihgpwlah", "370"),
        ("kglvqrro", "492"),
        ("ulqzkmiv", "830"),
    ],
)
def test_examples2(passcode, expected):
    assert part2(passcode) == expected


def test_input1(input):
    assert part1(input) == "RDURRDDLRD"


def test_input2(input):
    assert part2(input) == "526"
