# chapter4 - implementation
# 1913번 - 달팽이

n = int(input())
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i].append(n ** 2 - i)

print(arr)
