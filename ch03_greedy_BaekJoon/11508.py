# chapter3 - greedy
# 11508번 - 2+1 세일

import sys

input = sys.stdin.readline

n = int(input())
result = 0
dairy = list()

for i in range(n):
    dairy.append(int(input()))

dairy.sort(reverse=True)

ct = 1

for i in range(n):
    if ct % 3 == 0:
        ct = 1
        continue
    result += dairy[i]
    ct += 1
    
print(result)
