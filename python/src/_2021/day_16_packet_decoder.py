import sys
from math import prod
from typing import final

from aoc.io import read_file
from aoc.util import timed


@final
class Packet:
    def __init__(
        self, version: int, type_id: int, val: int, sub_packets: list["Packet"]
    ):
        self.version = version
        self.type_id = type_id

        self.val = val
        self.sub_packets = sub_packets

    @classmethod
    def from_bits(cls, bits: str, pos: int = 0) -> tuple["Packet", int]:
        # Extract the bits and find relevant packet statistics
        version = int(bits[pos : pos + 3], 2)
        type_id = int(bits[pos + 3 : pos + 6], 2)

        pos += 6

        # Extract the value and possible sub packets based on the type id
        match type_id:
            case 4:
                val, pos = cls._parse_val(bits, pos)
                return cls(version, type_id, val, []), pos
            case _:
                return cls._parse_op_packet(bits, pos, version, type_id)

    @staticmethod
    def _parse_val(bits: str, pos: int) -> tuple[int, int]:
        val_bits = []

        while pos < len(bits) and bits[pos] == "1":
            val_bits += bits[pos + 1 : pos + 5]
            pos += 5

        if pos < len(bits) and bits[pos] == "0":
            val_bits += bits[pos + 1 : pos + 5]
            pos += 5

        return int("".join(val_bits), 2), pos

    @classmethod
    def _parse_op_packet(
        cls, bits: str, pos: int, version: int, type_id: int
    ) -> tuple["Packet", int]:
        # Parse sub packets for the operator packet
        sub_packets = []

        len_type_id = int(bits[pos])
        pos += 1

        match len_type_id:
            case 0:
                n_bits = int(bits[pos : pos + 15], 2)
                pos += 15

                idx = pos
                while idx != pos + n_bits:
                    packet, idx = cls.from_bits(bits, idx)
                    sub_packets.append(packet)

                pos += n_bits

            case 1:
                n_packets = int(bits[pos : pos + 11], 2)
                pos += 11

                for _ in range(n_packets):
                    packet, pos = cls.from_bits(bits, pos)
                    sub_packets.append(packet)

            case _:
                raise ValueError(f"Found invalid length type ID {len_type_id}")

        # Determine value of the packet based on its type id
        match type_id:
            case 0:
                val = sum(packet.val for packet in sub_packets)
            case 1:
                val = prod(packet.val for packet in sub_packets)
            case 2:
                val = min(packet.val for packet in sub_packets)
            case 3:
                val = max(packet.val for packet in sub_packets)
            case 5:
                first, second, *_ = sub_packets
                val = int(first.val > second.val)
            case 6:
                first, second, *_ = sub_packets
                val = int(first.val < second.val)
            case 7:
                first, second, *_ = sub_packets
                val = int(first.val == second.val)
            case _:
                raise ValueError(
                    f"Found invalid type id '{type_id}' for operator packet"
                )

        return Packet(version, type_id, val, sub_packets), pos


def parse(input: str) -> Packet:
    # Retrieve the bits from the hexadecimal input
    bits = ""

    for hex_digit in input.strip():
        num = int(hex_digit, 16)
        num_bits = bin(num)[2:]

        bits += f"{num_bits.rjust(4, '0')}"

    packet, _ = Packet.from_bits(bits)
    return packet


def part1(root_packet: Packet) -> int:
    def dfs(packet: Packet) -> int:
        return packet.version + sum(
            dfs(sub_packet) for sub_packet in packet.sub_packets
        )

    return dfs(root_packet)


def part2(packet: Packet) -> int:
    return packet.val


def main():
    input = sys.stdin.read()
    parsed = parse(input)

    result1, elapsed = timed(part1, parsed)
    print(f"Part 1: {result1} ({elapsed} elapsed)")

    result2, elapsed = timed(part2, parsed)
    print(f"Part 2: {result2} ({elapsed} elapsed)")


if __name__ == "__main__":
    input = "620080001611562C8802118E34"
    input = read_file(2021, 16)
    result = part1(parse(input))
    pass
