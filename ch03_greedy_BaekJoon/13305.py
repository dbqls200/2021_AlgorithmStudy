# chapter3 - degree
# 13305번 - 주유소

n = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
m = price[0]

for i in range(n - 1):
    if price[i] < m:
        m = price[i]
    result += m * distance[i]   


print(result)
