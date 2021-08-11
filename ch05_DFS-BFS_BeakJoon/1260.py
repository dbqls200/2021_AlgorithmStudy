# chapter5 - DFS/BFS
# 1260번 - DFS와 BFS

from collections import deque
from sys import stdin
input = stdin.readline

def dfs(graph, start):
    
    visit = list()
    stack = list()
    
    stack.append(start)
    
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            s = list(graph[node])
            stack.extend(reversed(s))

    return visit

def bfs(graph, start):
    visit = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
            
    return visit


n, m, start = map(int, input().split())
graph = {}

for i in range(n):
    graph[i + 1] = set()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

dfs_visit = dfs(graph, start)
bfs_visit = bfs(graph, start)

print(*dfs_visit, sep=' ')
print(*bfs_visit, sep=' ')
