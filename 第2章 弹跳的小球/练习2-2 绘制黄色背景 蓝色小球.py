# 练习2-2 绘制黄色背景 蓝色小球效果
import pgzrun
def draw():
    # 黄色背景
    screen.fill('yellow')
    # 蓝色小球
    screen.draw.filled_circle((400,300),100,'blue')
pgzrun.go()