import re
import sys

from attrs import define

from aoc.util import timed


@define
class Passport(dict):
    @classmethod
    def parse(cls, text: str) -> "Passport":
        fields = cls()

        for field_str in text.split():
            field, val = field_str.split(":")
            fields[field] = val

        return fields

    def is_valid1(self) -> bool:
        REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

        return all(field in self for field in REQUIRED_FIELDS)

    def is_valid2(self) -> bool:
        def validate_height(height_str: str) -> bool:
            if not (match := re.match(r"(\d{2,3})(cm|in)", height_str)):
                return False

            height, type = match.groups()
            validators = {
                "cm": lambda height: int(height) in range(150, 194),
                "in": lambda height: int(height) in range(59, 77),
            }

            return validators[type](height)

        VALID_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        FIELD_VALIDATORS = {
            "hgt": validate_height,
            "byr": lambda year: int(year) in range(1920, 2003),
            "iyr": lambda year: int(year) in range(2010, 2021),
            "eyr": lambda year: int(year) in range(2020, 2031),
            "hcl": lambda color: re.match(r"^#[0-9a-f]{6}$", color),
            "ecl": lambda color: color in VALID_COLORS,
            "pid": lambda year: re.match(r"^[0-9]{9}$", year),
        }

        return all(
            field in self and validator(self[field])
            for field, validator in FIELD_VALIDATORS.items()
        )


def parse(input: str) -> list[Passport]:
    return [Passport.parse(lines) for lines in input.split("\n\n")]


def part1(passports: list[Passport]) -> int:
    return sum(1 for passport in passports if passport.is_valid1())


def part2(passports: list[Passport]) -> int:
    return sum(1 for passport in passports if passport.is_valid2())


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
