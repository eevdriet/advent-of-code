import re
import sys
from itertools import combinations

from _2019.intcode import IntCode, asciify
from aoc.util import timed

DIRECTION_STEPS = {1j: "north", -1j: "south", 1: "east", -1: "west"}
STEP_DIRECTIONS = {"north": 1j, "south": -1j, "east": 1, "west": -1}
KILL_ITEMS = {
    "infinite loop",
    "escape pod",
    "molten lava",
    "photons",
    "giant electromagnet",
}


class Starship:
    def __init__(self, memory: list[int]):
        self.program: IntCode = IntCode(memory)
        self.exit_dirs: list[complex] = []
        self.items: set[str] = set()

    def search_for_items(self):
        dirs = []
        inputs = []
        visited = set()

        while True:
            outputs = self.program.run(inputs)
            message = "".join(chr(o) for o in outputs)

            # Determine the room we're in
            match = re.search(r"== (.*) ==", message)
            room = match.group(1)
            print(f"== {room} ==")

            # Remember the steps to the exit room and backtrack automatically
            if room == "Pressure-Sensitive Floor":
                self.exit_dirs = dirs.copy()

                dirs.pop()
                dirs.pop()
                inputs = asciify("north")
                continue

            # Take any items that may be present
            if match := re.search(r"Items here:\n((?:- .+\n)+)", message, re.MULTILINE):
                items = re.findall(r"- (.+)", match.group(1))

                for item in items:
                    if item not in KILL_ITEMS:
                        self.program.run(asciify(f"take {item}"))
                        self.items.add(item)

                        print(f"\t- Picking up {item}")

            # Determine the steps we can take from the current room
            match = re.search(r"Doors here lead:\n((?:- .+\n)+)", message, re.MULTILINE)
            steps = re.findall(r"- (.+)", match.group(1))

            # Try to go to a new room
            for step in steps:
                dir = STEP_DIRECTIONS[step]
                room = tuple(dirs + [dir])

                # Don't backtrack
                if dirs and dirs[-1] == -dir:
                    continue

                # Step leads to a new room: go there
                if room not in visited:
                    visited.add(room)
                    dirs.append(dir)

                    inputs = asciify(step)
                    print(f"\t- Going {step}")
                    break
            else:
                # If we're back at the start with no room to be reached, stop searching
                if not dirs:
                    break

                # Otherwise backtrack to the previous room
                last_dir = dirs.pop()
                step = DIRECTION_STEPS[-last_dir]
                print(f"\t- Backtracking with {step}")
                inputs = asciify(step)

        print()

    def go_to_exit(self):
        print("(( Going to the exit ))")
        if not self.exit_dirs:
            raise RuntimeError("Haven't found the exit yet")

        for dir in self.exit_dirs:
            step = DIRECTION_STEPS[dir]
            print(f"\t- Going {step}")
            self.program.run(asciify(step))

    def escape(self) -> int:
        print("(( Trying to escape ))")
        items = list(self.items)
        exit_step = DIRECTION_STEPS[self.exit_dirs[-1]]

        # Drop all items to start with a clean slate
        for item in items:
            self.program.run(asciify(f"drop {item}"))

        # Try all subsets of items until we can escape
        for n in range(len(items) + 1):
            for subset in combinations(items, n):
                # Take all items in the subset
                for item in subset:
                    self.program.run(asciify(f"take {item}"))

                print(f"\t- Trying with {subset}")

                # Try to escape
                outputs = self.program.run(asciify(exit_step))
                message = "".join(chr(o) for o in outputs)

                # Escaped!
                if "Analysis complete" in message:
                    match = re.search(r"get in by typing (-?\d+)", message)
                    return int(match.group(1))

                # If we couldn't get through, drop all items again
                for item in subset:
                    self.program.run(asciify(f"drop {item}"))

        raise RuntimeError("Couldn't find exit!")


def part1_manual(memory: list[int]) -> None:
    program = IntCode(memory)
    inputs = []
    outputs = [1]

    while outputs:
        outputs = program.run(inputs)
        message = "".join(chr(o) for o in outputs)

        print(message)
        inputs = asciify(input(">: "))


def part1_auto(memory: list[int]) -> int:
    starship = Starship(memory)

    starship.search_for_items()
    starship.go_to_exit()

    return starship.escape()


def parse(text: str) -> list[int]:
    return [int(num) for num in text.split(",")]


def main():
    text = sys.stdin.read()
    parsed = parse(text)

    result1, elapsed = timed(part1_auto, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")


if __name__ == "__main__":
    main()
