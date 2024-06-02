import threading
import time


def process():
    """
    Returns:
        /opt/anaconda3/envs/myenv/bin/python /Users/songjin/PycharmProjects/Python-Tutorial/process_thread/multi_thread.py
    zhu xian cheng
    thread name is Thread-1 (process)
    thread name is Thread-3 (process)
    thread name is Thread-2 (process)
    thread name is Thread-1 (process)
    thread name is Thread-3 (process)
    thread name is Thread-2 (process)
    zhu xian cheng - end
    """
    for i in range(2):
        time.sleep(1)
        print("thread name is %s" % threading.current_thread().name)

class SubThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print("thread name is %s, i=%d" % (threading.current_thread().name, i))



if __name__ == '__main__':
    # print("zhu xian cheng")
    # threads = [threading.Thread(target=process) for i in range(3)]
    # for t in threads:
    #     t.start()  # 启动线程t，使其开始执行目标函数
    # for t in threads:
    #     t.join()  # 等待线程t执行完毕，然后再继续执行下面的代码
    # print("zhu xian cheng - end")

    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()


