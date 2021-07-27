# 4.4 特殊函数-2-5 通过索引的方式 修改列表中某一项元素的值

xlist = [1,2,3,4,5]
for i in range(5):
    xlist[i] = 2 * xlist[i]  # 使得列表中的数字乘以2倍

# 输出修改值后的列表
print(xlist)