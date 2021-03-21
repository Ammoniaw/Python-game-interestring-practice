# 3-1-1 绘制5个同心圆
import pgzrun

def draw():
    screen.fill('white')
    screen.draw.circle((400, 300), 10, 'red')
    screen.draw.circle((400, 300), 20, 'orange')
    screen.draw.circle((400, 300), 30, 'yellow')
    screen.draw.circle((400, 300), 40, 'purple')
    screen.draw.circle((400, 300), 50, 'green')

pgzrun.go()