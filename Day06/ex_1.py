"""
Exercise: 判断素数
Author  : wysn
Date    : 2025.2.5
"""
num = int(input('input a num: '))
end = int(num ** 0.5)
is_prime = True

for i in range(2, end + 1):
    if num % i  == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')