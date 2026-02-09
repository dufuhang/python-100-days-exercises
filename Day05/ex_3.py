"""
Exercise: 计算三角形的周长和面积
Author  : wysn
Date    : 2025.2.5
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if (a + b > c) and (a + c > b) and (b + c > a):
    perimeter = a + b + c
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area =  (s * (s - a) * (s - b) * (s * c)) ** 0.5
    print(f'面积: {area:.1f}')
else:
    print(f'不能构成三角形')