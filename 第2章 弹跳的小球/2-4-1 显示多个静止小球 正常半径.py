# 显示多个静止小球
import pgzrun
def draw():
    screen.fill('white')
    screen.draw.filled_circle((150,300),100,'red')
    screen.draw.filled_circle((400,300),100,'yellow')
    screen.draw.filled_circle((650,300),100,'green')
pgzrun.go()