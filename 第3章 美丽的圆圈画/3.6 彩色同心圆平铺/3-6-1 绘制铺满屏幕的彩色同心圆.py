# 3-6-1 绘制铺满屏幕的彩色同心圆
import pgzrun
import random  # 随机库

R = 50

def draw():
    screen.fill('white')
    for x in range(R,800,2*R):
        for y in range(R,600,2*R):
            for r in range(R,0,-10):  # 绘制5层
                screen.draw.filled_circle((x,y),r,\
                (random.randint(0,255), \
                 random.randint(0, 255), \
                 random.randint(0, 255)))  # 随机颜色

pgzrun.go()
