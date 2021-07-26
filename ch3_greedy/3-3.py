# chapter3 - Greedy
# 예제 3-3

'''
# 문제 : 숫자 카드 게임
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.

1. 숫자 카드는 N x M 형태(N은 행의 개수, M은 열의 개수)
2. 뽑고자 하는 카드가 포함된 행 선택
3. 선택된 행에 포함된 카드들 중 가장 낮은 숫자 카드 선택

# 풀이 :
각 행마다 가장 작은 수를 찾은 다음 그 수 중에서 가장 큰 수를 찾자.
'''




# n = 행의 개수, m = 열의 개수
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))    # 한 줄씩 입력 받기
    
    min_value = min(data)    # 현재 입력받은 수에서 가장 작은 수 찾기

    result = max(result, min_value)    # min_value에서 가장 큰 수 찾기

print(result)
    

    
