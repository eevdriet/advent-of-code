import re
import sys
from math import prod

from attrs import define

from aoc.io import read_file
from aoc.util import timed

Ticket = list[int]


@define
class Notes:
    field_rules: dict[str, list[range]]
    ticket: Ticket
    nearby_tickets: list[Ticket]

    @classmethod
    def parse(cls, text: str) -> "Notes":
        rules_text, ticket_text, nearby_text = text.split("\n\n")

        rules = {}
        for line in rules_text.splitlines():
            field, rule_text = line.split(": ")

            ranges = []
            for start, end in re.findall(r"(\d+)-(\d+)", rule_text):
                ranges.append(range(int(start), int(end) + 1))

            rules[field] = ranges

        ticket = list(map(int, re.findall(r"(-?\d+)", ticket_text)))

        nearby_tickets = []
        for line in nearby_text.splitlines()[1:]:
            nearby_ticket = list(map(int, re.findall(r"(-?\d+)", line)))
            nearby_tickets.append(nearby_ticket)

        return cls(rules, ticket, nearby_tickets)

    def validate(self, ticket: Ticket) -> int:
        error_rate = 0

        for val in ticket:
            if not any(
                val in rng for rule in self.field_rules.values() for rng in rule
            ):
                error_rate += val

        return error_rate

    def order_fields(self) -> list[str]:
        # Filter out valid tickets for the nearby ones
        tickets = [
            ticket for ticket in self.nearby_tickets if self.validate(ticket) == 0
        ]
        n_fields = len(tickets[0])

        # Determine which fields are valid for every position on the tickets
        pos_fields = [set(self.field_rules.keys()) for _ in range(n_fields)]

        for pos in range(n_fields):
            fields = pos_fields[pos]

            for field, rules in self.field_rules.items():
                for ticket in tickets:
                    if not any(ticket[pos] in rule for rule in rules):
                        fields.remove(field)
                        break

        # Then keep assigning positions to fields that only have 1 possibility left
        order = [""] * len(tickets[0])
        changed = True

        while changed:
            changed = False

            single_field_pos = {
                pos: next(iter(fields))
                for pos, fields in enumerate(pos_fields)
                if len(fields) == 1 and order[pos] == ""
            }

            pass

            for pos, field in single_field_pos.items():
                order[pos] = field

                for other_pos, fields in enumerate(pos_fields):
                    if pos != other_pos and field in fields:
                        fields.remove(field)
                        changed = True

        return order


def parse(input: str) -> Notes:
    return Notes.parse(input.strip())


def part1(notes: Notes) -> int:
    error_rate = 0

    for ticket in notes.nearby_tickets:
        error_rate += notes.validate(ticket)

    return error_rate


def part2(notes: Notes) -> int:
    fields = notes.order_fields()

    return prod(
        val for field, val in zip(fields, notes.ticket) if field.startswith("departure")
    )


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = read_file(2020, 16, "example2")
    part2(parse(input))
