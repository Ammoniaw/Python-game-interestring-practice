# 2-4.4 特殊函数-1 显示多个静止小球
import pgzrun
def draw():
    screen.fill('white')
    # 绘制窗口默认（800*600）绘制三个横坐标不同小球
    screen.draw.filled_circle((150, 300),100,'red')
    screen.draw.filled_circle((400, 300), 100, 'yellow')
    screen.draw.filled_circle((650, 300), 100, 'green')
pgzrun.go()  # 游戏开始运行
