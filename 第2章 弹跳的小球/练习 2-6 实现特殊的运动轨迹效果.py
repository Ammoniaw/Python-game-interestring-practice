# 练习2-6 弹跳小球实现特殊的运行效果
import pgzrun  # 导入游戏库

WIDTH = 800  # 游戏窗口的宽度
HEIGHT = 600  # 游戏窗口的高度
r = 3  # 所绘制小球的半径
color = 'red'  # 所绘制小球的颜色
x = WIDTH/2  # 小球圆心的初始横坐标
y = HEIGHT/2  # 小球圆心的初始纵坐标
speed_x = 3  # 小球横向的移动速度
speed_y = 5  # 小球纵向的移动速度

# 绘制函数


def draw():
    #screen.fill('white')  # 游戏窗口白色背景
    screen.draw.filled_circle((x, y), r, color)  # 绘制小球

# 小球位置更新函数


def update():
    global x, speed_x, y, speed_y  # 定义为全局变量
    x = x + speed_x   # 控制横向移动
    y = y + speed_y   # 控制纵向移动
    if y > HEIGHT - r or y < r:  # 当小球运动到游戏窗口底部时 或者 小球运动到游戏窗口顶部时
        speed_y = -speed_y  # 底部：不断减小y的值，实现“触底反弹”；顶部：不断增大y的值，实现“触顶反弹”
    if x > WIDTH - r or x < r:  # 当小球运动到游戏窗口右边界时 或者 小球运动到游戏窗口左边界时
        speed_x = -speed_x  # 右边界：不断减小x的值，实现“触右反弹”；左边界：不断增大x的值，实现“触左反弹”


pgzrun.go()
