from typing import *
from sympy.ntheory.modular import crt
import sys


def next_arrival(timestamp: int, bus: int) -> int:
    last_arrival = timestamp // bus * bus
    return last_arrival + bus if timestamp % bus else last_arrival

def shuttle_search(timestamp: int, busses: List[int]) -> int:
    waiting_times = {next_arrival(timestamp, bus) - timestamp: bus for bus in busses}
    min_time = min(time for time in waiting_times)
    min_bus = waiting_times[min_time]

    return min_time * min_bus

def shuttle_search_2(busses: List[int]) -> int:
    moduli, remainders = [], []

    for delay in range(len(busses)):
        if (bus := busses[delay]) == 'x':
            continue
        
        moduli.append(bus)
        remainders.append(-delay % moduli[-1])
        
    return crt(moduli, remainders)[0]

def main():
    lines = [line.strip() for line in sys.stdin]
    timestamp = int(lines[0])

    busses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    busses_2 = [int(bus) if bus != 'x' else bus for bus in lines[1].split(',')]
    
    print(shuttle_search(timestamp, busses))
    print(shuttle_search_2(busses_2))

if __name__ == '__main__':
    main()