# chapter7 - Binary Search
# 예제 3

'''
# 문제 : 떡볶이 떡 만들기
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라.

# 풀이 :
떡의 길이 중 가장 작은 길이로 먼저 h를 설정한 뒤,
잘린 떡의 길이 총합이 m이 될 때까지 계속해서 1씩 늘려가는 방법.

혼자서 작성해본 코드지만 이진 탐색을 사용하지 않음.
''' 


n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

h = array[0]
h_list = [0 for i in range(n)]

while True:
    for i in range(len(array)):
        if array[i] > h :
            h_list[i] = array[i] - h
        else:
            h_list[i] = 0
    if sum(h_list) == m:
        print(h)
        break
    else:
        h += 1
