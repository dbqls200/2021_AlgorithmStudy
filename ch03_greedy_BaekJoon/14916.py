# chapter3 - degree
# 14916번 - 거스름돈

n = int(input())
result = 0

if n == 1 or n == 3 :
    result = -1
    
else:
    if n % 5 == 0:
        result = n // 5

    elif n % 5 == 1 or n % 5 == 3:
        result = (n // 5) - 1
        n = (n % 5) + 5
        result += n // 2


    elif n % 5 == 2 or n % 5 == 4:
        result = n // 5
        n %= 5
        result += n // 2
        

print(result)
