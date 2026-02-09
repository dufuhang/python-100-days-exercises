"""
Exercise: 百分制成绩转换成等级
Author  : wysn
Date    : 2025.2.5
"""

score = float(input('score = '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'{grade = }')