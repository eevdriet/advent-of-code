from typing import *
from math import prod
import sys
import re


def get_all_values(info: Dict[int, Set]):
    values = set()
    for value in info.values():
        values.update(value)
        
    return values

def ticket_translation(info: Dict[str, Tuple[range, range]], nearby_tickets: List[Tuple[int]]):
    all_values = get_all_values(info)
    return sum(
        value
        for ticket in nearby_tickets
        for value in ticket
        if value not in all_values
    )
    
    
def ticket_translation_2(info: Dict[str, Tuple[range, range]], my_ticket: List[int], nearby_tickets: List[Tuple[int]]):
    all_values = get_all_values(info)
    def is_valid(ticket: Tuple[int]):
        return all(value in all_values for value in ticket)

    nearby_tickets = [ticket for ticket in nearby_tickets if is_valid(ticket)]
    
    fieldKeys = {field: set(info.keys()) for field in range(len(my_ticket))}
    for ticket in nearby_tickets:
        for field, value in enumerate(ticket):
            for key, values in info.items():
                if value not in values:
                    fieldKeys[field].remove(key)
                    
    keys = [None] * len(my_ticket)
    for field in sorted(fieldKeys, key=fieldKeys.get):
        key, = fieldKeys[field] - set(keys)     # set - set => set
        keys[field] = key
        
    return prod(
        value for key, value in zip(keys, my_ticket)
        if key.startswith("departure")
    )

def main():
    lines = sys.stdin.read()
    info_lines, my_lines, nearby_lines = lines.split('\n\n')
    
    info = {}
    for line in info_lines.splitlines():
        if not (match := re.match(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', line)):
            continue
        
        key = match.group(1)
        low1, high1, low2, high2 = map(int, match.groups()[1:])
        info[key] = set()
        info[key].update(range(low1, high1 + 1))
        info[key].update(range(low2, high2 + 1))
        
    my_ticket = [int(field) for field in my_lines.splitlines()[1].split(',')]
        
    nearby_tickets = []
    for line in nearby_lines.splitlines()[1:]:
        ticket_fields = map(int, line.split(','))
        nearby_tickets.append(tuple(ticket_fields))
        
    print(ticket_translation(info, nearby_tickets))
    print(ticket_translation_2(info, my_ticket, nearby_tickets))
    

if __name__ == '__main__':
    main()