# 练习3-7 用range()函数递减的方法 绘制同心圆
import pgzrun

def draw():
    screen.fill('white')  # 游戏窗口白色背景
    for r in range(100,1,-20):  # 步长递减
        screen.draw.circle((400,300),r,'black')

pgzrun.go()