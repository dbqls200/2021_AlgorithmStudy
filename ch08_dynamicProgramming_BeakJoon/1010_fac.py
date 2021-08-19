# chapter8 - dynamic programming
# 1010번 - 다리 놓기
# factorial 사용

import sys
import math
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))

    print(result)
