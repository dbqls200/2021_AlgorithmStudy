# chapter4 - implementation
# 1913번 - 달팽이

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = n // 2
y = n // 2
num = 1
length = 0

board[x][y] = num

while True:
    for i in range(4):
        for _ in range(length):
            x += dx[i]
            y += dy[i]
            num += 1
            board[x][y] = num

            if num == m:
                ans = [x + 1, y + 1]

    if x == y == 0:
        break
    x -= 1
    y -= 1
    length += 2

for i in range(n):
    print(*board[i])

print(*ans)
