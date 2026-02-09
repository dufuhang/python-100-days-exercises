"""
Exercise: 判断闰年
Author  : wysn
Date    : 2026.2.5
"""

year = int(input('Please input year: '))

is_leap = (year % 4 != 0 and year % 100 == 0) or (year % 400 == 0)
print(f'is_leap = %s' % is_leap)