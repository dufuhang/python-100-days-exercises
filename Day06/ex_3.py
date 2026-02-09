"""
Exercise: 猜数字游戏
Author  : wysn
Date    : 2025.2.5
"""

import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('Please input: '))
    if num < answer:
        print('大一点')
    elif num > answer:
        print('小一点')
    else:
        print('猜对了')
        break
print(f'一共猜了{counter}次')