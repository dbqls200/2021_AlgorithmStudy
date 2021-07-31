# chapter8 - Dynamic Programming
# 예제 5

'''
# 문제 : 효율적인 화폐 구성
N가지 종류의 화폐가 있다.
이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만
순서만 다른 것은 같은 경우로 간주한다.

# 풀이 :
다이나믹 프로그래밍 이용. 바텀업
'''

n, m = map(int, input().split())
coin = list()

for i in range(n):
    coin.append(int(input()))

dp = [10001] * (m+1)

dp[0] = 0

for i in range(n):
    for j in range(coin[i], m + 1):
        if dp[j - coin[i]] != 10001:    # (i - k)원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - coin[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

print(dp)
