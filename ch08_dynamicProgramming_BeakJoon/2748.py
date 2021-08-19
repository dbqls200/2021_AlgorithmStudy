# chapter8 - dynamic programming
# 2748번 - 피보나치 수 2

n = int(input())
result = [0] * (n + 1)

if n > 0:
    result[1] = 1
    
for i in range(2, n + 1):
    result[i] = result[i - 1] + result[i - 2]

print(result[-1])
