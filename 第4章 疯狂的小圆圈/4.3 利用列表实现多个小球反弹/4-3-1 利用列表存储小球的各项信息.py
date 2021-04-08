# 4-3-1 利用列表存储小球的各项信息
"""
列表存储小球的各项信息
绘制一个弹跳的小球
"""
import pgzrun  # 导入游戏库

# 设置绘制小球所需要的各种信息
WIDTH = 800  # 游戏窗口宽度
HEIGHT = 600  # 游戏窗口高度
x = WIDTH / 2  # 小球的初始x坐标
y = HEIGHT / 2  # 小球的初始y坐标
speed_x = 3  # 小球x方向的移动速度
speed_y = 5  # 小球y方向的移动速度
r = 30  # 小球的半径
# 小球的三个颜色分量
color_R = 255
color_G = 0
color_B = 0

# 将所有信息存储在列表ball中
ball = [x,y,speed_x,speed_y,r,color_R,color_G,color_B]

# 根据上述信息绘制小球
def draw():
    screen.fill('white')  # 设置游戏窗口背景为白色
    # 绘制小球
    screen.draw.filled_circle((ball[0],ball[1]),ball[4],(ball[5],ball[6],ball[7]))

# 设置更新函数 让小球运动起来
def update():  # 更新模块 每帧重复操作
    ball[0] += ball[2]  # 利用x方向的移动速度更新x坐标
    ball[1] += ball[3]  # 利用y方向的移动速度更新y坐标
    if ball[0] < ball[4] or ball[0] > WIDTH - ball[4]:  # 当小球运动到左右边界时
        ball[2] = -ball[2]  # x方向上的移动速度反向，达到反弹的效果
    if ball[1] < ball[4]  or ball[1] > HEIGHT - ball[4]:  # 当小球运动到上下边界时
        ball[3] = -ball[3]  # y方向上的移动速度反向，达到反弹的效果
# 游戏开始运行
pgzrun.go()
