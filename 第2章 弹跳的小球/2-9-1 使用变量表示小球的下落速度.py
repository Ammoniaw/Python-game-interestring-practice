# 2-9-1 上下反弹的小球

import pgzrun

y = 100  # 小球的初始纵坐标
speed_y = 3 # 小球下落的速度
r = 30  # 所绘制的小球半径
# 绘制函数
def draw():
    screen.fill('white')  # 游戏窗口背景颜色
    screen.draw.filled_circle((400,y),r,'red')
# 小球位置更新函数
def update():
    global y 
    y = y + speed_y  # 每运行一次，就增加小球的纵坐标
    if y > 630:
        y = 30

pgzrun.go()
