# 修改代码 使用变量替代所有的数字（方便修改参数）
import pgzrun

HEIGHT = 600  # 游戏窗口的高度
WIDTH = 800  # 游戏窗口的宽度
r = 30  # 绘制小球的半径
color = 'red'  # 绘制小球的颜色
y = 100  # 小球初始的圆心纵坐标
speed_y = 3  # 小球纵方向的移动速度

# 绘制函数
def draw():
    screen.fill("white")  # 白色背景
    screen.draw.filled_circle((WIDTH/2,y),r,color)

# 小球位置更新函数 update()
def update():
    global y, speed_y
    y = y + speed_y
    if y > HEIGHT - r or y < r:
        speed_y = - speed_y

pgzrun.go()