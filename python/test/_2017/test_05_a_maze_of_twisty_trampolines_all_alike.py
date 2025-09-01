import pytest
from _2017.day_05_a_maze_of_twisty_trampolines_all_alike import parse, part1, part2
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2017, 5, name=name) as file:
            return parse(file.read())

    return _load

@pytest.mark.parametrize("xyz, expected", [])
def test_examples(xyz, expected):
    assert part1(xyz) == expected

@pytest.mark.skip(reason="Skip until solution found through AOC")
def test_input1(data):
    input = data('input')
    assert part1(input) == ...


@pytest.mark.skip(reason="Skip until solution found through AOC")
def test_input2(data):
    input = data('input')
    assert part2(input) == ...

