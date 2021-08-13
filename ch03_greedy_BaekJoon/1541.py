# chapter3 - greedy
# 1541번 - 잃어버린 괄호


array = input().split('-')
result = 0

for i in array[0].split('+'):
    result += int(i)


for i in array[1:]:
    for j in i.split('+'):
        result -= int(j)
    
print(result)
