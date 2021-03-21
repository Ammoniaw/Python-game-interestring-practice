# 2-8-1 实现小球重复下落 （if语句）
import pgzrun

# 定义变量
r = 30
y = 30

def draw():
    screen.fill('white')
    screen.draw.filled_circle((400,y),r,'red')

#  更新小球的纵坐标y 
def update():
    global y 
    y = y + 1
    # 如果小球的顶部消失在窗口界面 使得y为30（即重新出现在顶部）
    if y >= 630:
        y = 30

pgzrun.go()