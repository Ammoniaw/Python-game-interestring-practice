import pgzrun

def draw():
    screen.fill('white')  # 设置背景颜色为白色
    screen.draw.circle((400, 300), 250, 'black')  # 绘制脸
    # 绘制眼眶
    screen.draw.circle((305, 180), 90, 'black')  
    screen.draw.circle((495, 180), 90, 'black')
    # 绘制眼球
    screen.draw.filled_circle((275, 180), 55, 'black')
    screen.draw.filled_circle((465, 180), 55, 'black')
    screen.draw.circle((400, 300), 20, 'black')  # 绘制鼻子
    screen.draw.circle((400, 420), 70, 'black')  # 绘制嘴巴

pgzrun.go()