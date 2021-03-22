# 3-2-3 绘制5个同心圆 for语句
import pgzrun

def draw():
    screen.fill('white')
    for i in range(1,6):
        screen.draw.circle((400,300),i*10,'red')

pgzrun.go()