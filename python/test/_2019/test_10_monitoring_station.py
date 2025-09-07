import pytest

from _2019.day_10_monitoring_station import (parse, part1, part2,
                                             place_station, vaporize_asteroids)
from aoc.io import open_file


def data(name: str):
    with open_file(2019, 10, name=name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "n, coord, n_asteroids",
    [
        (1, (3, 4), 8),
        (2, (5, 8), 33),
        (3, (1, 2), 35),
        (4, (6, 3), 41),
        (5, (11, 13), 210),
    ],
)
def test_examples(n: int, coord: tuple[int, int], n_asteroids: int):
    example = data(f"example{n}")

    assert place_station(example) == (coord, n_asteroids)


def test_input1():
    input = data("input")
    assert part1(input) == 326


def test_example2():
    example = data("example5")
    station, _ = place_station(example)
    vaporized = vaporize_asteroids(station, example)

    assert vaporized[199] == (8, 2)
    assert part2(example) == 802


def test_input2():
    input = data("input")
    assert part2(input) == 1623
