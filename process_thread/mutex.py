import threading
import time

n = 100


def task():
    global n
    mutex.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    print("buy success,  %d" % n)
    mutex.release()


if __name__ == '__main__':
    mutex = threading.Lock()
    t_1 = []
    for i in range(10):
        t = threading.Thread(target=task)
        t_1.append(t)
        t.start()
    for t in t_1:
        t.join()
