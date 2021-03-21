# 修改小球的y坐标值 使得3个小球向上移动 
import pgzrun

def draw():
    screen.fill('white')
    screen.draw.filled_circle((150, 200), 50, 'red')
    screen.draw.filled_circle((400, 200), 50, 'yellow')
    screen.draw.filled_circle((650, 200), 50, 'green')

pgzrun.go()
