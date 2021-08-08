# chapter3 - greedy
# 20365번 - 블로그2


n = int(input())
color = input()
start = color[0]
count = [1] * 3
changeB = 'B'
changeR = 'R'


for i in color:
    if start != i:
        count[0] += 1
        start = i
    if i == 'R':
        if changeB == 'B':
            count[1] += 1
            changeB = 'R'
        changeR = 'R'
    else:
        if changeR == 'R':
            count[2] += 1
            changeR = 'B'
        changeB = 'B'

print(min(count))
