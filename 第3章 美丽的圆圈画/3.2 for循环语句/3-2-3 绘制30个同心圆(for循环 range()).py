# 3-2-3 绘制30个同心圆(for循环 range())
import pgzrun
def draw():
    screen.fill('white')
    for r in range(1,31):
        screen.draw.circle((400,300),r*10,'red')

pgzrun.go()
        