# chapter10 - Graph
# 예제 4

'''
# 문제 : 커리큘럼

# 풀이 :
위상정렬 이용
'''

from collections import deque
import copy

n = int(input())
parent = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        parent[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if parent[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            parent[i] -= 1
            if parent[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()

