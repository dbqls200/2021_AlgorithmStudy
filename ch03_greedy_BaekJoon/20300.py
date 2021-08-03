# chapter3 - greedy
# 20300번 - 서강근육맨

import sys

input = sys.stdin.readline

n = int(input())
loss = list(map(int, input().split()))
loss.sort(reverse=True)
result = loss[0]
        

if n % 2 == 0:
    for i in range(1, n):
        result = max(result, loss[i - 1] + loss[-i])
else:
    for i in range(1, n):
        result = max(result, loss[i] + loss[-i])

print(result)
