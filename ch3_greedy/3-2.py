# chapter3 - Greedy
# 예제 3-2

'''
# 문제 : 큰 수의 법칙
다양한 수로 이루어진 배열에서 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
단, 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음.

# 풀이 :
가장 큰 수를 k번 더하고 두 번째로 큰 수를 한 번 더해줌.
이를 반복하면서 총 m번 더하자.
'''

# n = 배열 크기, m = 숫자가 더해지는 횟수, k = 최대 덧셈 가능 횟수
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()    # 입력받은 수 정렬하기
first = data[n-1]    # 가장 큰 수
second = data[n-2]    # 두 번째로 큰 수

result = 0    



# 방법 1

while(True):
    for i in range(k):
        if m == 0:
            break
        result += first    # 가장 큰 수 더하기
        m -= 1    # 총 덧셈 횟수 1회 차감
    if m == 0:
        break
    result += second    # 두 번째로 큰 수 더하기
    m -= 1    # 총 덧셈 횟수 1회 차감

print(result)



# 방법 2

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count =+ m % (k + 1)

result += count * first    # 가장 큰 수 더하기
result += (m-count) * second    # 두 번째로 큰 수 더하기

print(result)
