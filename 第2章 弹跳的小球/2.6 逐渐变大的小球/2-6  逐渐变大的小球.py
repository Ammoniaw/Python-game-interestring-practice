# 2-6 逐渐变大的小球
import pgzrun
r = 50
def draw():
    screen.fill("white")  # 设置背景颜色为白色
    screen.draw.filled_circle((400,300),r,'red')

# 设置update()函数，来实时更新小球半径
def update():
    global r  # 设置半径r为全局变量
    r += 1  # 最后小球会占据整个屏幕

pgzrun.go()  # 游戏开始运行