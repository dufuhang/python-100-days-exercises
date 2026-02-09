"""
Exercise: 100以内的素数
Author  : wysn
Date    : 2025.2.5
"""

for num in range(2,101):
    if_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)