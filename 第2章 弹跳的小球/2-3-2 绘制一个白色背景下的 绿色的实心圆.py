# 2-3-2 绘制一个白色背景下的绿色小球
import pgzrun
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400,300),100,'green')
pgzrun.go()