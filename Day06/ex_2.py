"""
Exercise: 最大公约数
Author  : wysn
Date    : 2025.2.5
"""

x = int(input('x = '))
y = int(input('y = '))

while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')