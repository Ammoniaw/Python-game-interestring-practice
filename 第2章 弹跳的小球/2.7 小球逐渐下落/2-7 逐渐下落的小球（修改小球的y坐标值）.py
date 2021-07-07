# 2-7 实现小球逐渐下落
"""
实现步骤：小球逐渐下落的过程，小球的纵坐标在不断地变大（游戏窗口左上角为原点）
"""
import pgzrun

y = 100  # 设置小球的初始纵坐标为100

def draw():
    screen.fill("white")
    screen.draw.filled_circle((400,y),50,'red')  # 绘制小球

# 设置实时更新函数 不断增大小球的纵坐标y的值
def update():
    global y  # 同样将y设置为全局变量
    y += 2  # 最终小球会消失在屏幕上

pgzrun.go()  # 游戏开始运行