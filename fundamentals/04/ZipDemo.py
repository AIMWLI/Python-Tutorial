import zipfile

file = zipfile.ZipFile("C:\\Develop\\python-workspace\\day08\\zipTest.zip", "w")
# 把两个文件压缩到zip包中
file.write("C:\\Develop\\python-workspace\\day08\\test.txt")
file.write("C:\\Develop\\python-workspace\\day08\\test2.txt")
file.write(".\\test3.txt")
file.close()

# 查看压缩文件内容 r表示读取
zip_file = zipfile.ZipFile("C:\\Develop\\python-workspace\\day08\\zipTest.zip")
print(zip_file.namelist())
# 解压
zip_file.extractall(".\\a")
zip_file.close()
