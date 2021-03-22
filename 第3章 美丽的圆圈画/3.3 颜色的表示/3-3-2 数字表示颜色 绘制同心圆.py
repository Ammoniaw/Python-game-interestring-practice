# 3-3-2 利用数字表示颜色方法 绘制5个红色的同心圆
import pgzrun

color = (255,0,0)

def draw():
    screen.fill((255,255,255))  # 白色背景
    for r in range(100,1,-20):
        screen.draw.circle((400,300),r,color)

pgzrun.go()