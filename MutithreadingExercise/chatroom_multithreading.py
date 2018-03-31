import threading
import time

total = 0
def add_total():
    global total
    for i in range(10):
        total += 1
        print(total)
        time.sleep(1)



def add_total_two():
    global total
    for i in range(5):
        total += 2
        print(total)
        time.sleep(2)




thread_list = []
t1 = threading.Thread(target=add_total, name='threads1')
thread_list.append(t1)
t2 = threading.Thread(target= add_total_two, name='threads2')
thread_list.append(t2)


t1.start()
t2.start()
t1.join()
for i in thread_list:
    print(i.getName())
