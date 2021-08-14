# chapter3 - greedy
# 11047 - 동전0


n, k = map(int, input().split())
a = [0 for i in range(n)]
result = 0

for p in range(n):
    a[p] = int(input())
    
a.sort(reverse=True)

for coin in a:
    if coin > k:
        continue
    if k == 0:
        break
    
    result += k // coin
    k %= coin

print(result)
