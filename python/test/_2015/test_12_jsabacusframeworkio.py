import pytest

from _2015.day_12_jsabacusframeworkio import parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2015, 12, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "doc_str, expected",
    [
        ("[1,2,3]", 6),
        ('{"a":2,"b":4}', 6),
        ("[[[3]]]", 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ("[]", 0),
        ("{}", 0),
    ],
)
def test_examples(doc_str, expected):
    doc = parse(doc_str)
    assert part1(doc) == expected


def test_input1(input):
    assert part1(input) == 111754


def test_input2(input):
    assert part2(input) == 65402
