# 导入日志模块
import logging
# 日志模块配置
logging.basicConfig(level=logging.ERROR,format="%(asctime)s-%(levelname)s: %(message)s")
# 输出日志
logging.debug("debug日志")
'''
四，日志级别
主要有五种，可以通过logging.basicConfig中的level参数修改级别。
DEBUG:小问题，一般在调试时才会使用
INFO：正常运行消息
WARNING：警告，可能有问题
ERROR：错误，导致程序部分处理失败
CRITICAL：致命的问题，程序都要完蛋
'''
# logging.disable(logging.ERROR) # 禁用error级别日志,只打印critical日志
#输出日志
logging.debug("debug日志")#不会输出
logging.error("error日志")#会输出
logging.critical("critical日志")#会输出
#日志模块配置(级别，格式为：时间-级别-消息)
# 将日志输出导文件
logging.basicConfig(filename="C:\\runlog.txt",level=logging.ERROR,format="%(asctime)s-%(levelname)s:%(message)s")
#输出日志
logging.error("debug日志")
print   #回车由隔断语法含义
(" hello world ")


def getArea(width,height):
    return width * height
def printName(name):
    print("hello ",name)

printName("songjin")

print("this area is ",getArea(4,5))