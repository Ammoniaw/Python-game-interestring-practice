# 练习2-3 结合之前所学知识
import pgzrun


def draw():
    screen.fill('white') #绘制白色背景
    screen.draw.circle((400, 300), 250, 'black')  # 绘制头
    screen.draw.circle((305, 180), 90, 'black')  # 绘制左眼眶
    screen.draw.circle((495, 180), 90, 'black')  # 绘制右眼眶
    screen.draw.filled_circle((275, 180), 55, 'black')  # 绘制左眼
    screen.draw.filled_circle((465, 180), 55, 'black')  # 绘制右眼
    screen.draw.circle((400, 300), 20, 'black')  # 绘制鼻子
    screen.draw.circle((400, 420), 70, 'black')  # 绘制嘴巴


pgzrun.go()
