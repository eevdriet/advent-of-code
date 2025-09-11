import pytest

from _2020.day_04_passport_processing import Passport, parse, part1, part2
from aoc.io import open_file


def data(name: str):
    with open_file(2020, 4, name) as file:
        return parse(file.read())


@pytest.mark.parametrize(
    "fields, expected",
    [
        (
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
            True,
        ),
        (
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
            False,
        ),
        (
            "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
            True,
        ),
        (
            "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
            False,
        ),
    ],
)
def test_examples1(fields: str, expected: int):
    passport = Passport.parse(fields)

    assert passport.is_valid1() == expected


def test_input1():
    input = data("input")
    assert part1(input) == 196


@pytest.mark.parametrize(
    "fields, expected",
    [
        (
            "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
            False,
        ),
        (
            "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
            False,
        ),
        (
            "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
            False,
        ),
        (
            "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007",
            False,
        ),
        (
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
            True,
        ),
        (
            "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            True,
        ),
        (
            "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
            True,
        ),
        (
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
            True,
        ),
    ],
)
def test_examples2(fields: str, expected: int):
    passport = Passport.parse(fields)

    assert passport.is_valid2() == expected


def test_input2():
    input = data("input")
    assert part2(input) == 114
