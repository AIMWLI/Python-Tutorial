import os
# 获取当前目录
import shutil

dir = os.getcwd()
print(dir)
os.chdir("C:\Develop\python-workspace\day07")
currentWorkDirectory = os.getcwd()
print(currentWorkDirectory)
# os.makedirs("day0888")
# os.makedirs("C:\Develop\python-workspace\day09")
# chdir = os.chdir("C:\Develop\python-workspace\day09")
# getcwd = os.getcwd()
# print(getcwd)
# 复制到另一个文件夹
# shutil.copy("C:\\Develop\\python-workspace\\day08\\a\\a.txt","C:\\Develop\\python-workspace\\day08\\b")
# 复制到另一个文件夹并改名
# shutil.copy("C:\\Develop\\python-workspace\\day08\\a\\a.txt","C:\\Develop\\python-workspace\\day08\\b\\alisaName.txt")
# 复制整个目录(备份)
# shutil.copytree("C:\\Develop\\python-workspace\\day08\\b","C:\\Develop\\python-workspace\\day08\\b-bak")
# 删除文件
# os.unlink("C:\\Develop\\python-workspace\\day08\\b-bak\\a.txt")

# 删除空文件夹
try:
    os.rmdir("C:\\Develop\\python-workspace\\day08\\b-bak")
except Exception as ex:
    print("错误信息:" + str(ex))  # 提示:错误信息,目录不是空的

# 删除文件夹及内容
# shutil.rmtree("C:\\Develop\\python-workspace\\day08\\b-bak")

# 移动文件
shutil.move("C:\\a\\1.txt", "C:\\b")
# 移动文件夹
shutil.move("C:\\a\\c", "C:\\b")

# 重命名文件
shutil.move("C:\\a\\2.txt", "C:\\a\\new2.txt")
# 重命名文件夹
shutil.move("C:\\a\\d", "C:\\a\\new_d")
