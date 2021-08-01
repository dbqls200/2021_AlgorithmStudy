# chapter7 - Binary Search
# 예제 2
# 방법 2. 이진 탐색


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return mid
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return None
    

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    result = binary_search(n_list, i, 0, n-1)
    
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')


'''
책 안보고 혼자 작성한 다음 책 봤는데 개똑같음.
근데 출력이 다르게 나옴 ㅅㅂ..
no yes yes가 안나오고
no yes no 나오고 쥐랄..
뭐가 다른거냐고 ~ .. ㅡㅅㅡ

응 발견함 ;;
none 들여쓰기 한 번 더 들어가있었음 ~ ㅅㅂ
'''
