import os

# 如果目录不存在则创建
path = "C:\Develop\python-workspace\day08"
if os.path.exists((path)) == False:
    os.makedirs(path)
else:
    pass
os.chdir(path)
# 写入文件,如果文件不存在先创建文件
file = open("test.txt", "w")
file.write("this is my first demo of io\nnice python")
file.close()  # 读写完毕后一定要关闭文件对象
# 读取文件
file = open("test.txt", "r")
str = file.read()  # 读取内容
file.close()
print(str)

# 一行行的读取
file = open("test.txt")
readlines = file.readlines()
file.close()
print(readlines)
