# 3-6-3 美丽的圆圈画完整代码版
import pgzrun  # 导入游戏库
import random  # 导入随机库

WIDTH = 1200  # 调整游戏窗口宽度
HEIGHT = 800  # 调整游戏窗口高度
R = 100  # 所绘制填充圆的最大半径


def draw():
    screen.fill('white')  # 游戏窗口背景颜色
    for x in range(R, WIDTH, 2*R):  # 横向绘制
        for y in range(R, HEIGHT, 2*R):  # 纵向绘制
            for r in range(1, R, 10):  # 绘制填充圆  R-r表示从外向内绘制圆圈
                screen.draw.filled_circle((x, y), R-r,\
                                          (random.randint(0, 255),\
                                           random.randint(0, 255),\
                                           random.randint(0, 255)))

# 添加鼠标点击事件

def on_mouse_down():
    draw()  # 点击鼠标即重新调用一次draw()函数

pgzrun.go()  # 运行游戏
