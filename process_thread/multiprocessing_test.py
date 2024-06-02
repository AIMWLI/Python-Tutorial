import os
import time
# -*- coding:utf-8 -*-
from multiprocessing import Process


def test(interval):
    print("zi jin cheng")


'''
zhu jin cheng ---start
zhu jin cheng ---end
zi jin cheng'''


def main():
    print("zhu jin cheng ---start")
    process = Process(target=test, args=(1,))
    process.start()
    print("zhu jin cheng ---end")


# 两个子进程将会调用的两个方法
def child_1(interval):
    print("子进程（%s）开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
    # 计时开始
    t_start = time.time()
    # 程序将会被挂起interval秒
    time.sleep(interval)
    # 计时结束
    t_end = time.time()
    print("子进程（%s）执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))


def child_2(interval):
    print("子进程（%s）开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
    # 计时开始
    t_start = time.time()
    # 程序将会被挂起interval秒
    time.sleep(interval)
    # 计时结束
    t_end = time.time()
    print("子进程（%s）执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))


def test_child():
    print("------父进程开始执行-------")
    # 输出当前程序的ID
    print("父进程PID：%s" % os.getpid())
    # 实例化进程p1
    p1 = Process(target=child_1, args=(1,))
    # 实例化进程p2
    p2 = Process(target=child_2, name="mrsoft", args=(2,))
    # 启动进程p1
    p1.start()
    # 启动进程p2
    p2.start()
    # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    # 输出p1和p2进程的别名和PID
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("------等待子进程-------")
    # 等待p1进程结束
    p1.join()
    # 等待p2进程结束
    p2.join()
    print("------父进程执行结束-------")


# 继承Process类
class SubProcess(Process):
    # 由于Process类本身也有__init__初识化方法，这个子类相当于重写了父类的这个方法
    def __init__(self, interval, name=''):
        # 调用Process父类的初始化方法
        Process.__init__(self)
        # 接收参数interval
        self.interval = interval
        # 判断传递的参数name是否存在
        if name:
            # 如果传递参数name,则为子进程创建name属性，否则使用默认属性
            self.name = name
            # 重写了Process类的run()方法

    def run(self):
        print("子进程(%s) 开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("子进程(%s)执行结束，耗时%0.2f秒" % (os.getpid(), t_stop - t_start))


def test_subprocess():
    """
    定义了一个SubProcess子类，继承multiprocess.Process父类。SubProcess子类中定义了两个方法：__init__()初始化方法和run()方法，
    在__init__()初始化方法中，调用父类multiprocess.Process的__init__()初始化方法，否则父类的__init__()方法会被覆盖，无法开启进程。
    此外，在SubProcess子类中没有定义start()方法，但在主程序中却调用了start()方法，此时就会自动执行SubProcess类的run()方法。

    """
    print("------父进程开始执行-------")
    # 输出当前程序的ID
    print("父进程PID：%s" % os.getpid())
    p1 = SubProcess(interval=1, name='mrsoft')
    p2 = SubProcess(interval=2)
    # 对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法，
    # 所以这里会执行p1.run()
    # 启动进程p1
    p1.start()
    # 启动进程p2
    p2.start()
    # 输出p1和p2进程的执行状态，如果真正进行，返回True,否则返回False
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    # 输出p1和p2进程的别名和PID
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("------等待子进程-------")
    # 等待p1进程结束
    p1.join()
    # 等待p2进程结束
    p2.join()
    print("------父进程执行结束-------")

# -*- coding=utf-8 -*-
from multiprocessing import Pool
import os, time

def task(name):
    print('子进程（%s）执行task %s ...' % ( os.getpid() ,name))
    # 休眠1秒
    time.sleep(3)

def test_pool():
    print('父进程（%s）.' % os.getpid())
    # 定义一个进程池，最大进程数3
    p = Pool(3)
    # 从0开始循环10次
    for i in range(10):
        # 使用非阻塞方式调用task()函数
        p.apply_async(task, args=(i,))
        # 阻塞方式调用task
        # p.apply(task, args=(i,))
    print('等待所有子进程结束...')
    # 关闭进程池，关闭后p不再接收新的请求
    p.close()
    # 等待子进程结束
    p.join()
    print('所有子进程结束.')


if __name__ == '__main__':
    # main()
    # test_child()
    # test_subprocess()
    test_pool()