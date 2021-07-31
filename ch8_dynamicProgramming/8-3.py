# chapter8 - Dynamic Programming
# 예제 3

'''
# 문제 : 개미 전사
식량창고는 일직선으로 이어져 있으며
각 식량창고에는 정해진 수의 식량을 저장하고 있다.
개미 전사는 식량창고를 선택적으로 약탈하는데,
서로 인접한 식량창고는 약탈하지 못한다.
개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때,
얻을 수 있는 식량의 최댓값을 구하라.

# 풀이 :
다이나믹 프로그래밍으로 작성.
'''

n = int(input())
k = list(map(int, input().split()))
dp = [0] * n

dp[0] = k[0]
dp[1] = max(k[0], k[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + k[i])

print(dp[n-1])
