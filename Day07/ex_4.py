"""
Exercise: 百钱百鸡问题
Desc    : 百钱百鸡
Author  : wysn
Date    : 2025.2.5
"""
for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if ( x + y + z == 100) and (x * 5 + y * 3 + z // 3 == 100):
                print(f'公鸡:{x}只, 母鸡:{y}只, 小鸡:{z}只.')