#this is where we learn how to use lock
import threading
import time
lock = threading.Lock()
total = 0
def add_total():
    global total
    while total < 20000:
        lock.acquire()      #acquire lock where you want to make the program to use by other
                            #thread to use without the global changes
        total += 3          #here we want to make change in total but dont want to make change by other thread
                            #without releasing the lock so that other thread wont use it till its release

        print("this is thread 1 "+str(total)+" goodbye")
        lock.release()
        time.sleep(0.1)




def add_total_two():
    global total
    while total < 20:
        lock.acquire()
        total -= 2

        print("this is thread 2  "+str(total) +" welcome")
        lock.release()
        time.sleep(0.1)


def always_true():
    global total
    while total < 20:
        print("this is thread 3 "+ str(total) + " waiting")


thread_list = []
t1 = threading.Thread(target=add_total, name='thread1')
thread_list.append(t1)
t2 = threading.Thread(target= add_total_two, name='thread2')
thread_list.append(t2)
t3 = threading.Thread(target= always_true, name="thread3", daemon=True)#here we used daemon attribute which default set up as false
                                #by making the daemon attribute True it will also terminate when main function done compelting its task
thread_list.append(t3)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
#t3.join()   dont use thread.join()for infinite loop thread otherwise it will run for always
for i in thread_list:
    print(i.getName())      #.getName will get the name of thread
