import pytest
from _{{year}}.day_{{padded_day}}_{{uslug}} import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file({{year}}, {{day}}, name=name) as file:
            return parse(file.read())

    return _load


@pytest.mark.parametrize("xyz, expected", [])
def test_examples(xyz, expected):
    assert part1(xyz) == expected


def test_input1(data):
    input = data('input')
    assert part1(input) == ...


@pytest.mark.skip(reason="Skip until solution to part 1 found through AOC")
def test_input2(data):
    input = data('input')
    assert part2(input) == ...

