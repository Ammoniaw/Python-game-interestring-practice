# 2-8 利用if语句实现小球重复下落
import pgzrun

y = 50  # 设置小球的初始纵坐标为50

def draw():
    screen.fill('white')
    screen.draw.filled_circle((400,y),50,'green')

# 设置实时更新函数
def update():
    """因为小球半径为50，所以当小球的纵坐标为600-50=550时，小球就下落到边界"""
    global y
    y += 3
    if y >=550:  # 当小球运动到边界时，重新设置小球的纵坐标为50，即回到最开始的位置
        y = 50

pgzrun.go()  # 游戏开始运行