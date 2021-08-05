# chapter3 - greedy
# 1931번 - 회의실 배정

import sys

input = sys.stdin.readline

n = int(input())
time = []

for i in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda a : a[0])
time.sort(key=lambda a : a[1])

last = 0
cnt = 0

for i, j in time:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
