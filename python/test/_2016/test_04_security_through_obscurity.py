import pytest

from _2016.day_04_security_through_obscurity import Room, parse, part1, part2
from aoc.io import FileType, open_file


@pytest.fixture
def input():
    with open_file(2016, 4, FileType.INPUT) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "text, expected",
    [
        ("aaaaa-bbb-z-y-x-123[abxyz]", True),
        ("a-b-c-d-e-f-g-h-987[abcde]", True),
        ("not-a-real-room-404[oarel]", True),
        ("totally-real-room-200[decoy]", False),
    ],
)
def test_examples1(text, expected):
    room = Room.parse(text)
    assert room.is_real() == expected


@pytest.mark.parametrize(
    "text, expected", [("qzmt-zixmtkozy-ivhz-343[.....]", "very encrypted name")]
)
def test_examples2(text, expected):
    room = Room.parse(text)
    assert room.decrypt() == expected


def test_input1(input):
    assert part1(input) == 185371


def test_input2(input):
    assert part2(input) == 984
