# chapter3 - greedy
# 1758번 - 알바생 강호

import sys


n = int(sys.stdin.readline())
money = []
result = 0

for _ in range(n):
    money.append(int(sys.stdin.readline()))

money.sort(reverse=True)

for i in range(n):
    tip = money[i] - ((i + 1) - 1)

    if tip > 0:
        result += tip
        
    
print(result)
