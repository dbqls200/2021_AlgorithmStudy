# chapter7 - binary search
# 1789번 - 수들의 합

import sys

input = sys.stdin.readline

s = int(input())

n = 1

while n * (n + 1) / 2 <= s:
    n += 1

print(n - 1)
