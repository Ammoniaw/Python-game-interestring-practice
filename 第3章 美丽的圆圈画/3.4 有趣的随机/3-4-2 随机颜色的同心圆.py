# 3-4.4 特殊函数-2 随机颜色的同心圆
import pgzrun
import random

def draw():
    screen.fill('white')  # 变色背景
    for r in range(250,0,-10):  # 绘制随机颜色填充圆
        screen.draw.filled_circle((400,300),r,\
        (random.randint(0,255),\
        random.randint(0,255),\
        random.randint(0,255)))

pgzrun.go()