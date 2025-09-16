import pytest

from _2022.day_06_tuning_trouble import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2022, 6, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "chars, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_examples1(chars: str, expected: int):
    assert part1(chars) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 1766


@pytest.mark.parametrize(
    "chars, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_examples2(chars: str, expected: int):
    assert part2(chars) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 2383
