import pytest

from _2021.day_16_packet_decoder import parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2021, 16, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "hex, expected",
    [
        ("D2FE28", 6),
        ("38006F45291200", 1 + 6 + 2),
        ("EE00D40C823060", 7 + 2 + 4 + 1),
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_examples1(hex: str, expected: int):
    example = parse(hex)
    assert part1(example) == expected


def test_input1():
    input = data("input")
    assert part1(input) == 895


@pytest.mark.parametrize(
    "hex, expected",
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_examples2(hex: str, expected: int):
    example = parse(hex)
    assert part2(example) == expected


def test_input2():
    input = data("input")
    assert part2(input) == 1148595959144
