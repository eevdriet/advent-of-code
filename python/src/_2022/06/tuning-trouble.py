from typing import *
from collections import Counter
import sys


def tuning_trouble(chars: str, *, stride: int) -> int:
    for idx in range(stride, len(chars)):
        seen = set(chars[idx - stride:idx])
        if len(seen) == stride:
            return idx
            
    return None

def main():
	chars = sys.stdin.readline()

	print(tuning_trouble(chars, stride=4))      # part 1
	print(tuning_trouble(chars, stride=14))     # part 2

if __name__ == '__main__':
    main()