import threading
import time


def start(t, name):
    print(name + " started running")
    time.sleep(5)
    print(name + " is start after " + str(t) + " seconds time")


t1 = threading.Thread(target=start, name="thread1", args=(5, "thread1"))

t1.start()
print("we will do something till 5 seconds are up")
t1.join()
time.sleep(2)
print("we will do something when 5 seconds are up")
