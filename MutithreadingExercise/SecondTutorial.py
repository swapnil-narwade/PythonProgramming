import threading
import time


def start_thread_function(t, name):
    print(name + " started running")
    time.sleep(5)
    print(name + " is start after " + str(t) + " seconds time")


thread_list = []                        #created a thread list to store all the thread created

for i in range(4):                      #put range how many threads you want to creat
    t = threading.Thread(target=start_thread_function, name="thread{}".format(i+1), args=(5,"thread{}".format(i+1) ))
    t.start()
    thread_list.append(t)               #appent all the thread in the thread list so that we can use those later
t.join()
for i in thread_list:                   #get all the thread from the thread list
    print(i.name)
