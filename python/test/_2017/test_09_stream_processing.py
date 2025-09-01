import pytest

from _2017.day_09_stream_processing import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 9, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "groups, expected",
    [
        ("{}", 1),
        ("{{{}}}", 6),
        ("{{},{}}", 5),
        ("{{{},{},{{}}}}", 16),
        ("{<{},{},{{}}>}", 1),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<a>},{<a>},{<a>},{<a>}}", 9),
        ("{{<!>},{<!>},{<!>},{<a>}}", 3),
    ],
)
def test_examples1(groups, expected):
    assert part1(groups) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 10820


@pytest.mark.parametrize(
    "groups, expected",
    [
        ("<>", 0),
        ("<random characters>", 17),
        ("<<<<>", 3),
        ("<{!>}>", 2),
        ("<!!>", 0),
        ("<!!!>>", 0),
        ('<{o"i!a,<{i<a>', 10),
    ],
)
def test_examples2(groups, expected):
    assert part2(groups) == expected


def test_input2(data):
    input = data("input")
    assert part2(input) == 5547
