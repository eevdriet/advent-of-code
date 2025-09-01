import pytest

from _2018.day_07_the_sum_of_its_parts import (complete_tasks, parse, part1,
                                               part2)
from aoc.io import open_file


@pytest.fixture
def data():
    def _load(name: str):
        with open_file(2018, 7, name=name) as file:
            return parse(file.read())

    return _load


def test_example1(data):
    example = data("example")
    assert part1(example) == "CABDFE"


def test_input1(data):
    input = data("input")
    assert part1(input) == "OCPUEFIXHRGWDZABTQJYMNKVSL"


def test_example2(data):
    example = data("example")
    assert complete_tasks(example, n_elves=2, base_duration=0, part2=True) == "15"


def test_input2(data):
    input = data("input")
    assert part2(input) == "991"
