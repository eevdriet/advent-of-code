import pytest

from _2018.day_20_a_regular_map import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 20, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize(
    "regex, expected",
    [
        ("^WNE$", 3),
        ("^ENWWW(NEEE|SSE(EE|N))$", 10),
        ("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$", 18),
        ("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$", 23),
        ("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$", 31),
    ],
)
def test_examples1(regex, expected):
    assert part1(parse(regex)) == expected


def test_input1(data):
    input = data("input")
    assert part1(input) == 3560


def test_input2(data):
    input = data("input")
    assert part2(input) == 8688
