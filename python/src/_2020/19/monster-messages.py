from typing import *
import sys

Terminal = str
Seq = Tuple[str, ...]
NonTerminal = List[Seq]
Rule = Terminal | NonTerminal
Rules = Dict[str, Rule]


def parse_rules(lines: List[str], *, part2: bool):
    rules: Rules = {}

    for line in lines:
        key, rule = line.split(': ')
        
        if rule.startswith('"'):
            rule = rule[1:-1]
        else:
            rule = [tuple(key for key in keys.split()) for keys in rule.split(' | ')]
            
        rules[key] = rule
        
    if part2:
        other_rules = {"8": [("42",), ("42", "8")], "11": [("42", "31"), ("42", "11", "31")]}
        rules = {**rules, **other_rules}
        
    return rules

def expand_sequence(rules: Rules, sequence: Seq, message: str) -> Iterator[str]:
    if len(sequence) == 0:
        yield message
    else:
        first_key, *rest = sequence
        for message in expand_rule(rules, rules[first_key], message):
            yield from expand_sequence(rules, rest, message)


def expand_rule(rules: Rules, rule: Rule, message: str) -> Iterator[str]:
    if isinstance(rule, Terminal):
        if (n := len(message)) >= rule and message[:n] == rule:
            yield message[n:]

    elif isinstance(rule, list):
        for sequence in rule:
            yield from expand_sequence(rules, sequence, message)

def monster_messages(rules: Rules, messages: List[str]) -> int:
    def match_rule(message: str, rule: Rule) -> bool:
        return any(len(result) == 0 for result in expand_rule(rules, rule, message))
    
    return sum(match_rule(string, rules["0"]) for string in messages)

def main():
    lines, messages = map(str.splitlines, sys.stdin.read().split('\n\n'))
    rules1 = parse_rules(lines, part2=False)
    rules2 = parse_rules(lines, part2=True)
    
    print(monster_messages(rules1, messages))
    print(monster_messages(rules2, messages))
    
    
if __name__ == '__main__':
    main()