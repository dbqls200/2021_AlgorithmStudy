# chapter10 - Graph
# 예제 10-2

'''
# 문제 : 팀 결성

# 풀이 :
서로소 집합 알고리즘 사용.
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same(a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return "YES"
    else:
        return "NO"

n, m = map(int, input().split())
parent = [0] * (n + 1)
result = list()

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union_parent(parent, a, b)
    else:
        result.append(same(a, b))

for i in result:
    print(i)
