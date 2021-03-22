# 3-6-2 将所有的数值都使用变量来表示；添加鼠标点击事件
import pgzrun
import random

WIDTH = 1200
HEIGHT = 800
R = 100

def draw():
    screen.fill('white')
    for x in range(R, WIDTH, 2*R):
        for y in range(R, HEIGHT, 2*R):
            for r in range(1, R, 10):  # 绘制填充圆  R-r表示从外向内绘制圆圈
                screen.draw.filled_circle((x,y),R-r,\
                    (random.randint(0,255),\
                    random.randint(0, 255), \
                    random.randint(0, 255)))
            
# 添加鼠标点击事件
def on_mouse_down():
    draw()  # 点击鼠标即重新调用一次draw()函数

pgzrun.go()
