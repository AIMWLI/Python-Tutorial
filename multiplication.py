# 九九乘法表
'''     Python3中不换行输出，end""     '''
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print(" ")

