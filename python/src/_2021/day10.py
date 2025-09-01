from typing import *
import sys

delimiters = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def syntax_scoring(lines: List[str]):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    total = 0
    
    for line in lines:
        stack = []
        
        for delim in line:
            if delim in delimiters:
                stack.append(delim)
                continue
            
            opening = stack.pop()
            closing = delimiters[opening]            
            
            if closing != delim:
                total += scores[delim]
                break
    
    return total

def syntax_scoring2(lines: List[str]):
    penalties = {closing: score for score, closing in enumerate((')', ']', '}', '>'), 1)}
    scores = []
    
    for line in lines:
        stack = []
        
        for delim in line:
            if delim in delimiters:
                stack.append(delim)
                continue
            
            opening = stack.pop()
            closing = delimiters[opening]            
            
            if closing != delim:
                break
        else:
            score = 0
            while stack:
                opening = stack.pop()
                closing = delimiters[opening]
                penalty = penalties[closing]
                
                score = 5 * score + penalty
                
            if score > 0:
                scores.append(score)
    
    scores.sort()
    return scores[len(scores) // 2]

def main():
    lines = [line.strip() for line in sys.stdin]
    
    print(syntax_scoring(lines))
    print(syntax_scoring2(lines))

if __name__ == '__main__':
    main()