# _*_ coding:utf-8 _*_
import time
from multiprocessing import Process, Queue


# 向队列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息" + str(i)
            q.put(message)
            print("写入：%s" % message)


# 从队列中读取数据
def read_task(q):
    while not q.empty():
        time.sleep(2)  # 休眠2秒
        print("读取：%s" % q.get(True, 2))  # 等待2秒中，如果没有读取到任何信息，则抛出异常


if __name__ == "__main__":
    print("--------父进程开始---------")
    q = Queue()  # 父进程创建Queue，并传给各个子进程
    pw = Process(target=write_task, args=(q,))  # 实例化写入队列的子进程，并传递给队列
    pr = Process(target=read_task, args=(q,))  # 实例化读取队列的子进程，并传递给队列
    pw.start()  # 启动子进程pw，写入
    pr.start()  # 启动子进程pr，读取
    pw.join()  # 等待pw结束
    pr.join()  # 等待pr结束
    print("-------父进程结束-----------")
