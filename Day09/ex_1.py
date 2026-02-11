"""
双色球随即选号

Author  : wysn
Date    : 2025.2.5
"""
import random

from rich.console import Console
from rich.table import Table

console = Console()

n = int(input('选择几注号码:'))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]

table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    select_balls = random.sample(red_balls,6)
    select_balls.sort()
    blue_ball = random.choice(blue_balls)
    table.add_row(
        str(i+1),
        f'[red]{" ".join({f"{ball:0>2d}" for ball in select_balls})}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )
console.print(table)