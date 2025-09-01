from typing import *
import itertools
import sys
import re


def dirac_dice(positions: List[int]):
    player = 0
    scores = [0] * len(positions)
    die = itertools.cycle(range(1, 101))
    n_rolls = 0
    
    while True:
        # Compute round score
        dice_sum = sum(next(die) for _ in range(3))
        n_rolls += 3

        positions[player] = 1 + (positions[player] + dice_sum - 1) % 10
        scores[player] += positions[player]

        if scores[player] >= 1000:
            break

        player = (player + 1) % len(positions)

    return min(scores) * n_rolls

def dirac_dice2(positions: List[int]):
    dp = {}

    def count_wins(pos1, pos2, score1, score2):
      if score1 >= 21:
        return (1, 0)
      if score2 >= 21:
        return (0, 1)
      if (key := (pos1, pos2, score1, score2)) in dp:
        return dp[key]

      wins = (0, 0)
      for dice in itertools.product((1, 2, 3), repeat=3):
        pos1_new = 1 + (pos1 + sum(dice) - 1) % 10
        score1_new = score1 + pos1_new

        wins2, wins1 = count_wins(pos2, pos1_new, score2, score1_new)
        wins = (wins[0] + wins1, wins[1] + wins2)

      dp[(pos1, pos2, score1, score2)] = wins
      return wins
  
    return max(count_wins(*positions, 0, 0))

def main():
    positions = [int(re.search(r'position: (\d+)', line).group(1)) for line in sys.stdin]
    assert len(positions) == 2

    print(dirac_dice(positions[:]))
    print(dirac_dice2(positions[:]))

if __name__ == '__main__':
    main()