# 使用包
# 第一种
# import service.size
# print(service.size.width)
# print(service.size.height)
# 第二种
# from service import size
# print(size.width, size.height)
# 第三种
from service.size import width,height
print(width, height)