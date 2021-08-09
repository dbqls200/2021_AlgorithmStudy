# chapter4 - implementation
# 20053번 - 최소, 최대 2

import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    print(min(num), end=' ')
    print(max(num))


