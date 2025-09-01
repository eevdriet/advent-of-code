from typing import *
from math import prod
from operator import *
import sys


def packet_decoder(bits: str):
    versions = []

    def peek(data, n):
        ret = data[0][:n]
        data[0] = data[0][n:]
        return ret

    def parse(data):
        version = int(peek(data, 3), 2)
        versions.append(version)

        tid = int(peek(data, 3), 2)
        if tid == 4:
            t = []
            while True:
                cnt, *v = peek(data, 5)
                t += v
                if cnt == '0':
                    break
            return int("".join(t), 2)

        ltid = peek(data, 1)[0]
        spv = []
        if ltid == '0':
            len_subpackets = int(peek(data, 15), 2)
            subpackets = [peek(data, len_subpackets)]
            while subpackets[0]:
                spv.append(parse(subpackets))
        else:
            n_subpackets = int(peek(data, 11), 2)
            spv = [parse(data) for _ in range(n_subpackets)]
            
        match tid:
            case 0:
                return sum(spv)
            case 1:
                return prod(spv)
            case 2:
                return min(spv)
            case 3:
                return max(spv)
            case 5:
                return int(spv[0] > spv[1])
            case 6:
                return int(spv[0] < spv[1])
            case 7:
                return int(spv[0] == spv[1])

    part2 = parse([bits])
    return sum(versions), part2

def main():
    line = sys.stdin.read().strip()
    bits = ''.join(f'{int(hex, 16):04b}' for hex in line)
        
    part1, part2 = packet_decoder(bits)
    print(part1, part2)

if __name__ == '__main__':
    main()