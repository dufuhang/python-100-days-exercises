"""
Exercise: CRAPS游戏
Desc    : CRAPS
Author  : wysn
Date    : 2025.2.5
"""
import random

money = 1000
while money > 0:
    print(f'You money is {money}$')
    while True:
        debt = int(input('Your debt: '))
        if 0 < debt <= money:
            break
        else:
            print(f'Debt must smaller or equal than your money!')
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'Point is {first_point}')
    if first_point == 7 or first_point == 11:
        print(f'Player win!\n')
        money += debt;
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print(f'Banker win!\n')
        money -= debt
    else:
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'Point is {current_point}')
            if current_point == 7:
                print(f'Banker win!\n')
                money -= debt
                break
            elif current_point == first_point:
                print(f'Player win!\n')
                money += debt
                break
print(f'You broken! Game over!')