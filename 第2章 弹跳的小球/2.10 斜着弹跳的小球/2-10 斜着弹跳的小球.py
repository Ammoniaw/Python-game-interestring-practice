# 2-10 斜着弹跳的小球
"""
实现步骤：斜着弹跳意味着小球的横坐标也需要发生变化
即小球碰触到左右边界时，产生反弹的效果
将所有数值使用变量代替
"""
import pgzrun

# 游戏窗口的默认大小
WIDTH = 800
HEIGHT = 600
# 小球圆心的初始坐标
x = WIDTH / 2
y = HEIGHT / 2
r = 50  # 小球的半径r
speed_x = 2  # 小球横向的移动速度
speed_y = 2  # 小球纵向的移动速度

def draw():
    screen.fill('white')
    screen.draw.filled_circle((x,y),r,'red')

# 小球位置的实时更新
def update():
    global x,speed_x,y,speed_y   # update函数需要对这些都要改变，所以将他们设置为全局变量
    x += speed_x
    y += speed_y
    # 设置判断条件
    if y > HEIGHT-r or y<r:  # 当小球触碰到上下边界时
        speed_y = -speed_y  # 使得速度反向
    if x > WIDTH-r or x<r:  # 当小球触碰到左右边界时
        speed_x = -speed_x  # 使得速度反向

pgzrun.go()  # 游戏开始运行
    