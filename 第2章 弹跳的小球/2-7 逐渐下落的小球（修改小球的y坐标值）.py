# 2-7 逐渐下落的小球（修改小球的y坐标值）
import pgzrun
# 定义变量
r = 30
y = 1

def draw():
    screen.fill('white')
    screen.draw.filled_circle((400,y),r,'red')

# 更新函数 update()
def update():
    global y
    y = y + 1

pgzrun.go()