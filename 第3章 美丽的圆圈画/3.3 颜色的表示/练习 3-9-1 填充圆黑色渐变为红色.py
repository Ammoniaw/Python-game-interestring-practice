# 练习3-9 填充圆 黑色渐变为红色 
import pgzrun

def draw():
    screen.fill('white')  # 白色背景
    for r in range(250,1,-1):  # 黑色数字表示(0,0,0)
        screen.draw.filled_circle((400,300),r,(255-r,0,0))

pgzrun.go()