# chapter5 - DFS/BFS
# 2606번 - 바이러스


from sys import stdin
input = stdin.readline

def dfs (start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
            
dic = {}

for i in range(int(input())):
    dic[i + 1] = set()
    
for j in range(int(input())):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

visited = []

dfs(1, dic)

print(len(visited)-1)
