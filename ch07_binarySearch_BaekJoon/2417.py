# chapter7 - binary search
# 2417번 - 정수 제곱근

import sys

input = sys.stdin.readline

n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    
    if mid ** 2 < n :
        start = mid + 1
    else:
        end = mid - 1

print(start)
