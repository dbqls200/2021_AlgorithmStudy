# chapter3 - greedy
# 2217번 - 로프

n = int(input())
k = []

for i in range(n):
    k.append(int(input()))

k.sort(reverse=True)

power = 0

for i in range(n):
    power = max(power, k[i] * (i + 1))

print(power)
