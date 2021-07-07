# 2-4-2 显示多个静止小球 缩小半径
import pgzrun

def draw():
    screen.fill('white')
    # 绘制窗口默认（800*600）绘制三个横坐标不同小球
    screen.draw.filled_circle((150, 300), 50, 'red')
    screen.draw.filled_circle((400, 300), 50, 'yellow')
    screen.draw.filled_circle((650, 300), 50, 'green')

pgzrun.go()  # 游戏开始运行
