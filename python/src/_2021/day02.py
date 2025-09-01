import re
import sys
from typing import *

Command = Tuple[str, int]


def dive(commands: List[Command]) -> int:
    width, depth = 0, 0

    for direction, steps in commands:
        match direction:
            case "forward":
                width += steps
            case "down":
                depth += steps
            case "up":
                depth -= steps

    return depth * width


def dive2(commands: List[Command]) -> int:
    width, depth, aim = 0, 0, 0

    for direction, steps in commands:
        match direction:
            case "forward":
                width += steps
                depth += aim * steps
            case "down":
                aim += steps
            case "up":
                aim -= steps

    return depth * width


def main():
    lines = [line.strip() for line in sys.stdin]

    commands = []
    for line in lines:
        if match := re.match(r"(forward|down|up) (\d+)", line):
            commands.append((match.group(1), int(match.group(2))))

    print(dive(commands))
    print(dive2(commands))


if __name__ == "__main__":
    main()

