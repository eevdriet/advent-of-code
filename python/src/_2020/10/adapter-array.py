from typing import *
from collections import Counter
import sys


def adapter_array(jolts: List[int]) -> int:
    counter = Counter(curr - prev for prev, curr in zip(jolts, jolts[1:]))
    
    return counter[1] * counter[3]

def adapter_array_2(jolts: List[int]) -> int:
    counter = {jolts[-1]: 1}
    
    for idx in reversed(range(len(jolts) - 1)):
        jolt = jolts[idx]
        counter[jolt] = sum(counter.get(jolt + n, 0) for n in range(1, 4))

    return counter[0]

def main():
    jolts = sorted(int(jolt) for jolt in sys.stdin)
    jolts = [0] + jolts + [3 + jolts[-1]]

    print(adapter_array(jolts))
    print(adapter_array_2(jolts))

if __name__ == '__main__':
    main()