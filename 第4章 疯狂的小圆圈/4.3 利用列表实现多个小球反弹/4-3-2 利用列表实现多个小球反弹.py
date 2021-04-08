# 4-3-2 生成100个小球 存储在列表中

import pgzrun  # 导入游戏库
import random  # 导入随机库

WIDTH = 800  # 游戏窗口宽度
HEIGHT = 600  # 游戏窗口高度
balls = []  # 用来存储生成的100个小球信息

# 1.生成100个小球 并将信息存储到balls列表中

for i in range(100):
    x = random.randint(100,WIDTH - 100)  # 小球的x坐标
    y = random.randint(100,HEIGHT - 100)  # 小球的y坐标
    speed_x = random.randint(1,5)  # 小球x方向上的移动速度
    speed_y = random.randint(1,5)  # 小球y方向上的移动速度
    r = random.randint(5,50)  # 小球的半径
    # 用数字表示所绘制小球的颜色
    color_R = random.randint(10,255)
    color_G = random.randint(10,255)
    color_B = random.randint(10,255)

    # 将上述所有信息存储在ball列表中
    ball = [x,y,speed_x,speed_y,r,color_R,color_G,color_B]
    # 将存储小球所有信息的ball列表添加到balls列表中
    balls.append(ball)

# 根据上述信息绘制 小球
def draw():
    screen.fill('white')  # 设置游戏窗口背景颜色
    for ball in balls:  # 对balls列表中的所有ball进行绘制
        screen.draw.filled_circle((ball[0],ball[1]),ball[4],(ball[5],ball[6],ball[7]))

# update函数 对小球位置进行更新
def update():
    for ball in balls:  # 对balls列表中的所有ball进行绘制
        ball[0] += ball[2]  # 利用x方向上的移动速度更新x坐标
        ball[1] += ball[3]  # 利用y方向上的移动速度更新y坐标
        if ball[0] < ball[4] or ball[0] > WIDTH - ball[4]:  # 当小球触碰到左右边界时：
            ball[2] = -ball[2]  # 移动速度反向，实现反弹的效果

        if ball[1] < ball[4] or ball[1] > HEIGHT - ball[4]:  # 当小球触碰到上下边界时：
            ball[3] = -ball[3]  # 移动速度反向，实现反弹的效果

# 游戏开始运行
pgzrun.go()
