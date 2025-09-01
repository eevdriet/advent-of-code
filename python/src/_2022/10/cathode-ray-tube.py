from itertools import accumulate
from typing import List

from aoc.io import FileType, open_file


def cathode_ray_tube(instructions: List[int], *, part1: bool):
    strength = 0
    image = ""

    for cycle, val in enumerate(accumulate([1] + instructions), 1):
        strength += cycle * val if (cycle % 40 == 20) else 0
        image += "#" if (cycle - 1) % 40 - val in [-1, 0, 1] else " "

    if part1:
        return strength

    return "\n".join(image[idx : idx + 20] for idx in range(0, len(image), 20))


if __name__ == "__main__":
    splitter = lambda x: int(x) if x[-1].isdigit() else 0

    with open_file(2015, 4, FileType.INPUT) as file:
        instructions = list(map(splitter, file.readlines()))

    print(cathode_ray_tube(instructions, part1=True))
    print(cathode_ray_tube(instructions, part1=False))
