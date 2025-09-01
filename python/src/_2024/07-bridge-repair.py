from math import floor, log10
from typing import TextIO

from aoc.io import FileType, open_file
from aoc.util import ends_with, n_digits
from attrs import define

YEAR = 2024
DAY = 7
Equation = tuple[int, tuple[int]]


def is_tractable(target: int, values: tuple[int], allow_concat: bool) -> bool:
    # Separate last value, if one remains it should be the target
    *values, last = values
    if not values:
        return target == last

    # Otherwise first try multiplication
    # Check if target divides the last value and what remains is also tractable
    quot, rem = divmod(target, last)
    if rem == 0 and is_tractable(quot, values, allow_concat):
        return True

    # Otherwise, try concatenation if allowed
    if (
        allow_concat
        and ends_with(target, last)
        and is_tractable(target // (10 ** n_digits(last)), values, allow_concat)
    ):
        return True

    # Finally, try addition
    return is_tractable(target - last, values, allow_concat)


def parse(file: TextIO) -> list[Equation]:
    equations = []

    for line in file.read().splitlines():
        target, values = line.split(": ")

        target = int(target)
        values = [int(value) for value in values.split()]

        equation = (target, values)
        equations.append(equation)

    return equations


def main():
    with open_file(YEAR, DAY, FileType.INPUT) as file:
        equations = parse(file)

    print(
        f"Part 1: {sum(target for target, values in equations if is_tractable(target, values, allow_concat=False))}"
    )
    print(
        f"Part 2: {sum(target for target, values in equations if is_tractable(target, values, allow_concat=True))}"
    )


if __name__ == "__main__":
    main()
