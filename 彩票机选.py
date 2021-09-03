# 彩票机选
import random

temp = [i for i in range(35)]
random.shuffle(temp)
i = 0
list1 = []
while i <= 7:
    list1.append(temp[i])
    i = i + 1
# list1.sort()
print('\033[0:31::1m')
print(*list1[0:6],end=' ')
print('\033[0:34::1m',end='')
print(list1[-1])









