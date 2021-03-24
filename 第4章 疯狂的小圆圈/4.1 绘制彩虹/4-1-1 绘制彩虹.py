# 4-1-1 绘制彩虹图案
import pgzrun

def draw():
    screen.fill("white")  # 白色背景
    screen.draw.filled_circle((400,600),  400, 'red')
    screen.draw.filled_circle((400, 600), 380, 'orange')
    screen.draw.filled_circle((400, 600), 360, 'yellow')
    screen.draw.filled_circle((400, 600), 340, 'green')
    screen.draw.filled_circle((400, 600), 320, 'blue')
    screen.draw.filled_circle((400, 600), 300, 'cyan')
    screen.draw.filled_circle((400, 600), 280, 'purple')
    # 留白
    screen.draw.filled_circle((400, 600), 260, 'white')

pgzrun.go()
