"""
Exercise: 
Desc    : 将一颗色子掷60000次，统计每种点数出现的次数
Author  : wysn
Date    : 2025.2.5
"""
import random

counters = [0] * 6
times = 60000

for _ in range(times):
    face = random.randrange(1,7)
    counters[face - 1] += 1

for face in range(1,7):
    print(f'{face}点出现了{counters[face-1]}次,概率为{counters[face-1]/times * 100:.2f}%')