from typing import *
import sys


def rock_paper_scissors(lines: List[Tuple[str, str]]):
    their_choices = {'A': 1, 'B': 2, 'C': 3}    # rock, paper, scissors
    my_choices = {'X': 1, 'Y': 2, 'Z': 3}       # rock, paper, scissors
    diff_scores = {0: 3, 1: 6, 2: 0}            # draw, win, loss
    
    total = 0

    for their_choice, my_choice in lines:
        their_score, my_score = their_choices[their_choice], my_choices[my_choice]
        
        total += my_score
        total += diff_scores[(my_score - their_score) % 3]
        
    return total

def rock_paper_scissors2(lines: List[Tuple[str, str]]):
    their_choices = ['A', 'B', 'C']
    my_choices = {'X': (0, -1), 'Y': (3, 0), 'Z': (6, 1)}
    
    total = 0

    for their_choice, my_score in lines:
        outcome_score, offset = my_choices[my_score]
        my_score = 1 + (their_choices.index(their_choice) + offset) % 3
        
        total += outcome_score
        total += my_score
        
    return total

def main():
	lines = [line.strip().split() for line in sys.stdin]

	print(rock_paper_scissors(lines))
	print(rock_paper_scissors2(lines))

if __name__ == '__main__':
    main()