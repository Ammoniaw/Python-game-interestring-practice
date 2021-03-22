# 添加鼠标点击事件 绘制随机颜色同心圆
import pgzrun
import random

def draw():
    screen.fill('white')
    for r in range(250,0,-10):  # 白色背景
        screen.draw.filled_circle((400,300),r,\
        (random.randint(0,255),\
         random.randint(0, 255),\
         random.randint(0, 255)))

def on_mouse_down():  #点击鼠标任意按键
    draw()  # 调用draw()函数

pgzrun.go()