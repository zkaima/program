# 随机生成验证码

import random


def show():
    res = ''
    for i in range(6):
        shuzi = str(random.randint(0, 9))
        zimu = chr(random.randint(65, 90))
        res += random.choice([shuzi, zimu])
    return res


print(show(), end='')
