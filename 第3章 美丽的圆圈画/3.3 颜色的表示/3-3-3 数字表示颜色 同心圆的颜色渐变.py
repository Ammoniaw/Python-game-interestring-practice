# 同心圆的颜色 渐变
import pgzrun

def draw():
    screen.fill((255,255,255))  # 白色背景
    for r in  range(250,1,-50):  # 255 亮度最高
        screen.draw.circle((400,300),r,(r,0,0))

pgzrun.go()