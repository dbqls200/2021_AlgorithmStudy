# chapter8 - Dynamic Programming
# 예제 2

'''
# 문제 : 1로 만들기
정수 x가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.
1. x가 5로 나누어 떨어지면, 5로 나눈다.
2. x가 3으로 나누어 떨어지면, 3으로 나눈다.
3. x가 2로 나누어 떨어지면, 2로 나눈다.
4. x에서 1을 뺀다.

# 풀이 :
다이나믹 프로그래밍으로 작성.
한 번 계산한 것은 저장해두고 필요할 때 가져다 쓰자.
'''
 
x = int(input())

dp = [0] * (x + 1)

for i in range(2, x + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2]  + 1)
        
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])

