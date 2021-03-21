# 2-6-1 逐渐变大的小球
import pgzrun

r = 1

# 绘制函数draw()
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400,300),r,'red')

# 更新函数 update()
def update():
    # 将变量r定义为全局变量
    global r
    r = r + 1

pgzrun.go()