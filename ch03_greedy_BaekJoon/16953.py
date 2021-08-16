# chapter3 - greedy
# 16953번 - A -> B

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0
    
    
while (a < b):
    if b % 2 == 0:
        b //= 2
        cnt += 1

    elif str(b)[-1] == '1':
        b -= 1
        b //= 10
        cnt += 1
        
    else:
        break
        

if a == b:
    print(cnt + 1)
else:
    print(-1)



