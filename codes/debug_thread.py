import threading
import time


def get_thread_name():
    t = threading.current_thread()
    return t.name


def print_time(delay):
    """Define a function for the thread."""
    thread_name=get_thread_name()
    count = 0
    while count < 8:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (thread_name, time.ctime(time.time())))


t1 = threading.Thread(target=print_time, args=(1,))
t2 = threading.Thread(target=print_time, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()

# ————————————————
# 版权声明：本文为CSDN博主「醒了的追梦人」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_33472146/article/details/90606359

