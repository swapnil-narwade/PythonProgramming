import threading            #this is for importing the threading
import time                 #this is for importing the time


def start(t, name):         #this is the function created to run by thread
    print(name + " started running")
    time.sleep(5)
    print(name + " is start after " + str(t) + " seconds time")


t1 = threading.Thread(target=start, name="thread1", args=(5, "thread1"))#here we assign the thread to t1
                                                                        #target is assigned by function name
                                                                        #name is the name of the thread created
                                                                        #Args are the arguments for the function assigned to thread
t1.start()                                                              #Thread t1 started i.e function startprint will start working
                                                                        #this print will work parallelly independent of thread t1
print("we will do something till 5 seconds are up")
t1.join()               #t1.join() will stop main function running and let the thread complete
time.sleep(2)
print("we will do something when 5 seconds are up")#after the thread t1 is complete this statement will run
