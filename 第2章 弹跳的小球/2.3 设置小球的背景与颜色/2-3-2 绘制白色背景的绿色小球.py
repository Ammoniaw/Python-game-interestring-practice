# 2-3-2 设置小球及背景的填充颜色
import pgzrun
def draw():
    screen.fill('white')  # 修改背景颜色为白色
    screen.draw.filled_circle((400,300),100,'green')
pgzrun.go()