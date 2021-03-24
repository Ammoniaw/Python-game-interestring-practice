# 练习 4-3
"""
1.使用[x,y]的形式存储小球的坐标
2.随机生成100个小球的坐标
3.使用screen.draw.filled_circle()函数绘制这100个小球
"""
# 游戏窗口默认为600*800
import pgzrun
import random 

# 根据balls来绘制小球
def draw():
    screen.fill('white')  # 白色背景
    balls = []

# 生成100个小球 存储到balls中
    for i in range(100):
        x = random.randint(0, 800)  # 小球随机的x坐标
        y = random.randint(0, 800)  # 小球随机的y坐标
        ball = [x,y]  # 存储到ball中
        balls.append(ball)  # 将ball添加到balls中
    for ball in balls:
        screen.draw.filled_circle((ball[0],ball[1]),10,'red')  # 绘制这100个小球

# 添加鼠标点击事件
def on_mouse_down():  # 每点击一次，就重新生成100个随机小球 并绘制
    draw()
# 游戏运行
pgzrun.go()
