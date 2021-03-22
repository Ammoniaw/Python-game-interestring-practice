# 练习 3-9-2 填充圆 黑色渐变为绿色
import pgzrun

def draw():
    screen.fill('white')
    for r in range(250,1,-1):
        screen.draw.filled_circle((400,300),r,(0,255-r,0))

pgzrun.go()