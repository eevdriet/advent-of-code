import re


def find_num(line: str) -> int:
    return find_nums(line)[0]


def find_nums(line: str) -> list[int]:
    return list(map(int, re.findall(r"([-+]?\d+)", line)))
