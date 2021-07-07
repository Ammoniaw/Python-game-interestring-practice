# 2-4-1 显示多个静止小球
import pgzrun

def draw():
    screen.fill('white')
    # 修改3个小球的纵坐标，使得小球产生向上移动的效果
    screen.draw.filled_circle((150, 100), 100, 'red')
    screen.draw.filled_circle((400, 100), 100, 'yellow')
    screen.draw.filled_circle((650, 100), 100, 'green')

pgzrun.go()  # 游戏开始运行
