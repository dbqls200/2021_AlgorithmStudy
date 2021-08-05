# chapter3 - greedy
# 20115번 - 에너지 드링크

import sys

input = sys.stdin.readline

n = int(input())
drink = list(map(int, input().split()))

drink.sort(reverse=True)

result = drink[0]

for i in range(1, n):
    result += drink[i] / 2

print(result)
