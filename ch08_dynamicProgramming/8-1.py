# chapter8 - Dynamic Programming
# 예제 1
# 피보나치 수열

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
dp = [0] * 100

def fibo(x):
    if x == 1 or x == 2: # 종료 조건, 1 또는 2일 때 1 반환
        return 1
    if dp[x] != 0: # 이미 계산한 적 있는 문제라면 그대로 반환
        return dp[x]

    # 계산한 적 없는 문제라면 점화식에 따라 피보나치 결과 반환
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo(99))
        
