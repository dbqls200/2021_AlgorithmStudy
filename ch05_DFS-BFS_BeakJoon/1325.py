# chapter5 - BFS/DFS
# 1325번 - 효율적인 해킹

from collections import deque 
from sys import stdin
input = stdin.readline

def bfs(start):
    queue = deque([start])
    v = [0 for _ in range(n + 1)]
    v[start] = 1
    cnt = 1
    
    while queue:
        node = queue.popleft()
        for x in graph[node]:
            if v[x] == 0:
                cnt += 1
                v[x] = 1
                queue.append(x)
            
    return cnt



n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n + 1):
    result[i] = bfs(i)

for i in range(1, n + 1):
    if result[i] == max(result):
        print(i, end=' ')
