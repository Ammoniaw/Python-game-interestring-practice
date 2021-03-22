# 练习3-12 显示不同的效果
import pgzrun
import random

R = 50  # 圆的半径
WIDTH = 800  # 游戏窗口宽度
HEIGHT = 600  # 游戏窗口高度

# 绘制圆
def draw():
    screen.fill('white')
    for x in range(0,WIDTH+1,R):
        for y in range(0,HEIGHT+1,R):
            screen.draw.circle((x,y),R,\
                (random.randint(0,255),\
                random.randint(0, 255),\
                random.randint(0, 255)))

# 鼠标点击事件
def on_mouse_down():
    draw()  # 点击鼠标即重新调用一次draw()函数


pgzrun.go()
