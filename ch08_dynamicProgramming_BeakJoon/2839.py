# chapter8 - dynamic programming 1
# 2839번 - 설탕 배달

n = int(input())
dp = [5002] * (n + 1)

for i in range(3, n + 1):
    res = min(dp[i - 3] + 1, dp[i - 5] + 1)
    
    if i % 5 == 0:
        res = min(res, i // 5)

    elif i % 3 == 0:
        res = min(res, i // 3)

        
    dp[i] = res


if dp[n] >= 5002:
    print(-1)
else:
    print(dp[n])
