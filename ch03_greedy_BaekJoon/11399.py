# chapter3 - greedy
# 11399번 - ATM

import sys

input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
result = 0

time.sort()

for i in range(n):
    result += time[i] * (n - i)

print(result)
