from typing import *
from collections import defaultdict
import sys

Graph = Dict[str, Set[str]]

def passage_pathing(graph: Graph) -> int:
    def dfs(cave: str, visited: Set[str] = set()) -> int:
        if cave == 'end':
            return 1
        if cave.islower() and cave in visited:
            return 0

        return sum(dfs(neighbor, visited | {cave}) for neighbor in graph[cave])        

    return dfs('start')

def passage_pathing2(graph: Graph):
    def dfs(cave: str, visited: dict = defaultdict(int)) -> int:
        if cave == 'end':
            return 1

        if cave.islower() and cave in visited:
            if cave == "start":
                return 0
            if any(cave.islower() and count >= 2 for cave, count in visited.items()):
                return 0

        new_visited = visited.copy()
        new_visited[cave] += 1
        
        return sum(dfs(neighbor, new_visited) for neighbor in graph[cave])

    return dfs('start')

def main():
    lines = [line.strip() for line in sys.stdin]
    
    graph: Graph = defaultdict(set)
    for line in lines:
        src, dst = line.split('-')

        graph[src].add(dst)
        graph[dst].add(src)

    print(passage_pathing(graph))
    print(passage_pathing2(graph))

if __name__ == '__main__':
    main()