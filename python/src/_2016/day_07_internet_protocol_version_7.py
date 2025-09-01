import re
import sys

from attrs import define

from aoc.util import timed


@define
class Address:
    insides: list[str]
    outsides: list[str]

    @classmethod
    def parse(cls, text: str) -> "Address":
        parts = re.split(r"[\[\]]", text)
        insides = [word for idx, word in enumerate(parts) if idx % 2 == 1]
        outsides = [word for idx, word in enumerate(parts) if idx % 2 == 0]

        return cls(insides, outsides)

    def supports_ip(self) -> bool:
        def contains_palindrome(text: str) -> bool:
            return any(
                text[idx] == text[idx + 3]
                and text[idx + 1] == text[idx + 2]
                and text[idx] != text[idx + 1]
                for idx in range(len(text) - 3)
            )

        return any(contains_palindrome(word) for word in self.outsides) and not any(
            contains_palindrome(word) for word in self.insides
        )

    def supports_ssl(self) -> bool:
        def is_palindrome(text: str, start: int) -> bool:
            return text[start] == text[start + 2] and text[start] != text[start + 1]

        # Generate all BABs for easy look up
        babs = {
            inside[start : start + 3]
            for inside in self.insides
            for start in range(len(inside) - 2)
            if is_palindrome(inside, start)
        }

        # Iterate through all ABAs and see if a corresponding BAB exists
        for outside in self.outsides:
            for start in range(len(outside) - 2):
                if is_palindrome(outside, start):
                    bab = f"{outside[start + 1]}{outside[start]}{outside[start + 1]}"
                    if bab in babs:
                        return True

        return False


def parse(input: str) -> list[Address]:
    return [Address.parse(line) for line in input.splitlines()]


def part1(addresses: list[Address]) -> int:
    return sum(1 for address in addresses if address.supports_ip())


def part2(addresses: list[Address]) -> int:
    return sum(1 for address in addresses if address.supports_ssl())


if __name__ == "__main__":
    # input = sys.stdin.read()
    # addresses = parse(input)
    #
    # result1, elapsed = timed(part1, addresses)
    # print(f"Part 1: {result1} ({elapsed} elapsed)")
    #
    # result2, elapsed = timed(part2, addresses)
    # print(f"Part 2: {result2} ({elapsed} elapsed)")

    address = Address.parse("aba[bab]xyz")
    address.supports_ssl()
