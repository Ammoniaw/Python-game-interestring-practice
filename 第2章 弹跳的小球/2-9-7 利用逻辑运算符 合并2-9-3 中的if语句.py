# 利用逻辑运算符合并2-9-3中的if语句
import pgzrun

r = 30
y = 100
speed_y = 3  # 小球在纵方向的移动速度


def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, y), r, 'red')


def update():
    global y, speed_y  # 定义为全局变量
    y = y + speed_y
    if y >= 570 or y <= 30:  # 当小球触碰到游戏窗口底部时 或者 当小球运动到游戏窗口顶部时
        speed_y = -speed_y  # 使得小球不再下落，不断减少y坐标值 实现向上弹的效果 或者 不断增大小球的y坐标值 实现下落的效果

pgzrun.go()
