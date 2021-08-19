# chapter8 - dynamic programming
# 9655번 - 돌 게임

import sys
input = sys.stdin.readline

n = int(input())
res = n
dp = [0]

if n >= 3:
    for i in range(1, n):
        if res == 0:
            break
    
        if res < 3:
            dp.append(dp[i - 1] + 1)
            res -= 1
        else:
            dp.append(dp[i - 1] + 3)
            res -= 3


    
if len(dp) % 2 == 0 or n == 1:
    print("SK")
elif len(dp) % 2 != 0 or n == 2:
    print("CY")
