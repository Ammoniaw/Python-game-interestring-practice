# 练习 2-4 实现小球更快的变大
"""
实现步骤：即让小球半径变化的更快
"""
import pgzrun
r = 50

def draw():
    screen.fill("white")  # 设置背景颜色为白色
    screen.draw.filled_circle((400, 300), r, 'red')

# 设置update()函数，来实时更新小球半径

def update():
    global r  # 设置半径r为全局变量
    r += 3  # 修改小球变大的速度为3，最终小球依旧会占据整个游戏窗口

pgzrun.go()  # 游戏开始运行
