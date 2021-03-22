# 3-2-5 range()函数添加步长 绘制同心圆
import pgzrun

def draw():
    screen.fill('white')
    for r in range(1,101,10):
        screen.draw.circle((400,300),r,'red')

pgzrun.go()