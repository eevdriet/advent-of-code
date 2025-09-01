import sys

import parse as ps
from attrs import define

from aoc.util import timed


@define
class Room:
    name: str
    id: int
    checksum: str

    @classmethod
    def parse(cls, text: str) -> "Room":
        name, id, checksum = ps.parse("{}-{:d}[{}]", text)

        return cls(name, id, checksum)

    def is_real(self):
        # Count all letters of the room name
        letter_counts = [[idx, 0] for idx in range(26)]

        for letter in self.name:
            if not letter.isalpha():
                continue

            idx = ord(letter) - ord("a")
            letter_counts[idx][1] += 1

        # Sort the letters by most counted first, alphabetized second
        letter_counts.sort(key=lambda x: (-x[1], x[0]))

        # Verify with the checksum whether the 5 most common match
        for idx in range(len(self.checksum)):
            letter = ord(self.checksum[idx]) - ord("a")
            if letter != letter_counts[idx][0]:
                return False

        return True

    def decrypt(self):
        decrypted = ["."] * len(self.name)
        n_rotations = self.id % 26

        for idx, letter in enumerate(self.name):
            if letter.isalpha():
                new_letter = (ord(letter) - ord("a") + n_rotations) % 26
                decrypted[idx] = chr(ord("a") + new_letter)

            elif letter == "-":
                decrypted[idx] = " "

        return "".join(decrypted)


def parse(input: str) -> list[Room]:
    return [Room.parse(line) for line in input.splitlines()]


def part1(rooms: list[Room]) -> int:
    return sum(room.id for room in rooms if room.is_real())


def part2(rooms: list[Room]) -> int:
    return next(
        (room.id for room in rooms if room.decrypt() == "northpole object storage"),
        -1,
    )


if __name__ == "__main__":
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")
