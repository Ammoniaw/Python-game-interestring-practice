# 2-9 实现小球上下反弹效果
"""
实现步骤：下反弹时：小球的纵坐标为y=600-r(r为小球的半径)；
        上反弹时：小球的纵坐标为y=r;
"""
import pgzrun

y = 50  # 设置小球的初始纵坐标为50
speed_y = 3  # 小球在纵向的移动速度
r = 50  # 设置小球的半径为50
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400,y),r,'green')

# 设置实时更新函数，调整小球的纵坐标
def update():
    global y, speed_y  # update函数同样对speed_y的值进行了修改，因此需要设置为全局变量
    y += speed_y
    # 小球运动至下边界时,减小y的值;小球运动至上边界时，增大y的值
    if y >= 600-r or y <= r:
        speed_y = -speed_y  # 使得小球向上移动

pgzrun.go()  # 游戏开始运行