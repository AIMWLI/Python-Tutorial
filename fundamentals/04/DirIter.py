# 目录的遍历
import os

# 获取目录信息
print("请输入目录信息")
dir = input()
if os.path.exists(dir) == False:
    print("目录不存在,请重新输入")
    dir = input()


# 对一个目录进行遍历
def ShowPathInfo(path):
    print("------")
    for folder, subFolders, files in os.walk(path):
        print("当前遍历目录: " + folder)
        for f in files:
            print("[文件]" + f)
        for d in subFolders:
            print("[文件夹]" + d)
            ShowPathInfo(d)


# 主程序
print("遍历开始")
ShowPathInfo(dir)
print("遍历结束")
