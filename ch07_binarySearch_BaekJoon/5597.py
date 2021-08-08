# chapter4 - implementation
# 5597번 - 과제 안 내신 분..?

student = []

for i in range(28):
    n = int(input())
    student.append(n)

for i in range(1, 31):
    if i not in student:
        print(i)
