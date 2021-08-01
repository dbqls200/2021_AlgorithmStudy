# chapter7 - Binary Search
# 예제 2
# 방법 1. 집합 자료형 이용

'''
# 문제 : 부품 찾기
손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.

# 풀이 : 
손님이 문의한 부품 리스트를 돌면서
가게의 부품 리스트에 존재하면 yes, 그렇지 않으면 no
'''


n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print("yes", end=' ')
    else:
        print("no", end= ' ')
