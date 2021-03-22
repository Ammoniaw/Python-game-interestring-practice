# 练习 3-9-3 填充圆 灰色渐变为黑色
import pgzrun

def  draw():
    screen.fill('white')
    for r in range(250,1,-1):
        screen.draw.filled_circle((400,300),r,(r,r,r))

pgzrun.go()