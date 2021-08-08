# chapter4 - implementation
# 20546번 - 기적의 매매법

n = int(input())
up = 0
down = 0

jun = n
junN = 0

sung = n
sungN = 0

stock = list(map(int, input().split()))


for i in range(len(stock)):
    if stock[i] <= jun:
        junN += jun // stock[i]
        jun = jun % stock[i]
        continue

jun += stock[-1] * junN


for i in range(len(stock) - 1):
    if stock[i] > stock[i + 1]:
        if up > 0:
            up = 0
            down += 1
        else:
            down += 1
            if down >= 3 and sung // stock[i + 1] > 0:
                sungN += sung // stock[i + 1]
                sung = sung % stock[i + 1]
                
    elif stock[i] < stock[i + 1]:
        if down > 0:
            down = 0
            up = 1
        else:
            up += 1
            if up >= 3 and sungN > 0:
                sung += sungN * stock[i + 1]
                sungN = 0
                
    else:
        down = 0
        up = 0


sung += sungN * stock[-1]

    
if jun == sung :
    print("SAMESAME")
elif jun < sung:
    print("TIMING")
else:
    print("BNP")
