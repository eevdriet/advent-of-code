from typing import *
from collections import deque  
import sys

Cards = Deque[int]

def calculate_score(cards: Cards):
    return sum((len(cards) - idx) * card for idx, card in enumerate(cards))

def crab_cards(player1: Cards, player2: Cards) -> int:
    while player1 and player2:
        card1, card2 = player1.popleft(), player2.popleft()
    
        if card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
            
    return calculate_score(player1 if len(player1) > 0 else player2)

def crab_cards_2(player1: Cards, player2: Cards) -> int:
    def play_game(cards1: Cards, cards2: Cards) -> bool:
        seen_cards = set()

        while cards1 and cards2:
            curr_cards = (tuple(cards1), tuple(cards2))
            if curr_cards in seen_cards:
                return True
            
            seen_cards.add(curr_cards)

            card1, card2 = cards1.popleft(), cards2.popleft()
            
            player1_wins: bool
            if len(cards1) >= card1 and len(cards2) >= card2:
                new_cards1 = deque(list(cards1)[:card1])
                new_cards2 = deque(list(cards2)[:card2])
                player1_wins = play_game(new_cards1, new_cards2)
            else:
                player1_wins = card1 > card2

            if player1_wins:
                cards1.extend([card1, card2])
            else:
                cards2.extend([card2, card1])
                
        return len(cards1) > 0
                
    play_game(player1, player2)
    return calculate_score(player1 if len(player1) > 0 else player2)

def main():
    players = sys.stdin.read().split('\n\n')

    cards: Cards = []
    for player in players:
        card_lines = player.splitlines()[1:]
        player_cards = [int(card) for card in card_lines]
        cards.append(deque(player_cards))

    #print(crab_cards(*cards))
    print(crab_cards_2(*cards))

if __name__ == '__main__':
    main()