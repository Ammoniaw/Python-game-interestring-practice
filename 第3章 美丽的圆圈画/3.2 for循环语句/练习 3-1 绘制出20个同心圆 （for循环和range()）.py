# 练习3-1绘制20个同心圆 （for循环 range函数）
import pgzrun

def draw():
    screen.fill('white')
    for r in range(1,201,10):
        screen.draw.circle((400,300),r,'red')

pgzrun.go()