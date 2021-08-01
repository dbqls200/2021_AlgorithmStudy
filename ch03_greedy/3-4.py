# chapter3 - Greedy
# 예제 3-4

'''
# 문제 : 1이 될 때까지
N이 1일 될 때까지,
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
위 과정 중 하나를 반복적으로 선택하여 수행.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택 가능
N이 1이 될 때 까지, 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하라.

# 풀이 :
N이 K로 나눠지면 2번 수행하고 안되면 1번 수행하자!
'''


# 방법 1 : 2번 안되면 1번 수행하자

n, k = map(int ,input().split())
count = 0

while True:
    if n == 1:    # n이 1이면 종료
        break
    if n % k == 0:    # n이 k로 나누어 떨어지는 경우
        n = n // k    # 2번 수행
        count += 1    # 동작 횟수 증가

    else:    # n이 k로 나누어 떨어지지 않는 경우
        n -= 1    # 1번 수행
        count += 1    # 동작 횟수 증가
    

print(count)



# 방법 2 : 최대한 2번 수행 후, 마지막으로 1번 수행

n, k = map(int, input().split())
count = 0

while n >= k:
    if n % k != 0:
        n -= k
        count +=1
    n //= k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)
