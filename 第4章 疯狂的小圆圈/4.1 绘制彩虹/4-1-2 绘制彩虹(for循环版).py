# 4.4 特殊函数-1-2 绘制彩虹(for循环版)
import pgzrun  # 导入库

# 定义存储彩虹颜色的列表 colors
colors = ['red','orange','yellow','green',\
        'blue','cyan','purple','white']  # 白色为留白

# 绘制函数
def draw():
    screen.fill('white')  # 白色背景
    for i in range(8):  # 取0~8之间的整数(不包含8)
        screen.draw.filled_circle((400,600),400-20*i,colors[i])  # 从外向内绘制彩虹

# 游戏运行 
pgzrun.go()