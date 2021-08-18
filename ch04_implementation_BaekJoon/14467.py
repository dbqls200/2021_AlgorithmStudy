# chapter4 - implementation
# 14467번 - 소가 길을 건너간 이유 1

n = int(input())
arr = [-1] * 11
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())

    if arr[a] == -1:
        arr[a] = b
        
    elif arr[a] != b:
        cnt += 1
        arr[a] = b

print(cnt)

