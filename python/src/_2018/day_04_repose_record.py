import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta

from attrs import define, field

from aoc.io import open_file
from aoc.util import timed


@define
class Guard:
    id: int
    sleep: dict[int, int] = field(factory=lambda: defaultdict(int))

    def __hash__(self) -> int:
        return hash(self.id)


@define
class Record:
    dt: datetime
    message: str

    @classmethod
    def parse(cls, line: str) -> "Record":
        if not (match := re.match(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.*)", line)):
            raise ValueError(f"Could parse Record from {line}")

        dt_str, message = match.groups()
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

        return cls(dt, message)


def parse(input: str) -> list[Record]:
    return [Record.parse(line) for line in input.splitlines()]


def find_guard(records: list[Record], *, part2: bool = False) -> int:
    # Chronologically sort the records
    records.sort(key=lambda record: record.dt)

    # Keep track of all guards and their sleep
    guards = {}
    guard = None
    start_sleep = datetime.now()

    # Go through the records
    for record in records:
        match record.message.split()[0]:
            # New guard begins shift
            case "Guard":
                id = int(re.match(r"Guard #(\d+) begins shift", record.message)[1])
                guard = guards[id] if id in guards else Guard(id)
                guards[id] = guard
            case "falls":
                start_sleep = record.dt
            case "wakes":
                end_sleep = record.dt

                # Loop over every minute and register sleep
                curr_time = start_sleep

                while curr_time < end_sleep:
                    guard.sleep[60 * curr_time.hour + curr_time.minute] += 1
                    curr_time += timedelta(minutes=1)

    # Find guard that slept the most and the minute they slept most often
    if not part2:
        guard = max(guards.values(), key=lambda guard: sum(guard.sleep.values()))

    # Find the guard that sleeps some minute the most days and that minute
    else:
        guard = max(
            guards.values(), key=lambda guard: max(guard.sleep.values(), default=0)
        )

    min = max(guard.sleep, key=lambda min: guard.sleep[min])

    return guard.id * min


def part1(records: list[Record]) -> int:
    return find_guard(records, part2=False)


def part2(records: list[Record]) -> int:
    return find_guard(records, part2=True)


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    with open_file(2018, 4, "example") as file:
        part1(parse(file.read()))
