# chapter5 - DFS/BFS
# 1260번 - DFS와 BFS

from collections import deque
from sys import stdin
input = stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
n, m, start = map(int, input().split())
graph = [[0] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
visited = [False] * n

dfs(graph, start, visited)
bfs(graph, start, visited)
