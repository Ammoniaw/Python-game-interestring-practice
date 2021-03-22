# 练习3-8 for循环语句绘制黑白相间的圆圈画
import pgzrun

def draw():
    screen.fill('white')  # 游戏窗口白色背景
    for r in range(250,1,-50):  # 实心圆绘制会覆盖 所以从最外侧开始绘制
        screen.draw.filled_circle((400,300),r,'black')  # 黑色实心圆
        screen.draw.filled_circle((400,300),r-25,'white')  # 半径较小的白色实心圆

pgzrun.go()