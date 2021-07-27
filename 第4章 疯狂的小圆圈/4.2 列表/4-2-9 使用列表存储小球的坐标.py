# 4.4 特殊函数-2-9 使用列表 存储小球的坐标[x,y]

# 列表存储小球坐标
ball_1 = [1,2]
ball_2 = [3,4]
ball_3 = [5,6]

balls = []  # 将上述列表存储到空列表 balls中

balls.append(ball_1)
balls.append(ball_2)
balls.append(ball_3)

# 输出balls列表中存储的小球元素的[x,y]坐标
for ball in balls:
    print("小球坐标为%d,%d"%(ball[0],ball[1]))