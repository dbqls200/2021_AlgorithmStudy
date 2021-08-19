# chapter8 - dynamic programming
# 1010번 - 다리 놓기
# dp 사용

import sys
input = sys.stdin.readline

t = int(input())


for i in range(t):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for j in range(m + 1):
        dp[1][j] = j

    for j in range(2, n + 1):
        for k in range(j, m + 1):
            for l in range(k, j - 1, -1):
                dp[j][k] += dp[j-1][l-1]


    print(dp[n][m])
