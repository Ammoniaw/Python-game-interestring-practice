# 使用变量r记录小球的半径
import pgzrun

def draw():
    # 创建变量r 
    r = 50
    # 绘制小球
    screen.fill('white')
    screen.draw.filled_circle((150,300),r,'red')
    screen.draw.filled_circle((400, 300), r, 'red')
    screen.draw.filled_circle((650, 300), r, 'red')

pgzrun.go()