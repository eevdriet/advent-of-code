from typing import List, Tuple

Card = Tuple[List[int], List[int]]


def parse(txt: str) -> List[Card]:
    cards = []

    for line in txt.splitlines():
        line = line.split(":")[1].strip()
        winning_numbers, numbers = [
            list(map(int, side.split())) for side in line.split(" | ")
        ]
        cards.append((winning_numbers, numbers))

    return cards


def part1(cards: List[Card]) -> int:
    total = 0

    for winning_nums, my_nums in cards:
        n_winning = sum(num in winning_nums for num in my_nums)
        if n_winning > 0:
            total += 2 ** (n_winning - 1)

    return total


def part2(cards: List[Card]) -> int:
    copies = {}

    for id, (winning_nums, my_nums) in enumerate(cards):
        if id not in copies:
            copies[id] = 1

        n_winning = sum(num in winning_nums for num in my_nums)

        for next_id in range(id + 1, id + n_winning + 1):
            copies[next_id] = copies.get(next_id, 1) + copies[id]

    return sum(copies.values())


def main():
    cards = parse(open("data/4.input").read().strip())

    print(f"Part 1: {part1(cards)}")
    print(f"Part 2: {part2(cards)}")


if __name__ == "__main__":
    main()
