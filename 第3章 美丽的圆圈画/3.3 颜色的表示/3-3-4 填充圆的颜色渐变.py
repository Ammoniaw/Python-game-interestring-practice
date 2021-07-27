# 3-3-4.4 特殊函数 填充圆的颜色渐变
import pgzrun

def draw():
    screen.fill((255,255,255)) # 白色背景
    for r in range(250,1,-50):  # 填充圆会覆盖 所以从最外侧开始绘制
        screen.draw.filled_circle((400,300),r,(r,0,0))

pgzrun.go()