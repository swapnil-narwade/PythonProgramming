
import datetime
import time
import threading
tLock = threading.Lock()
def timer(name, delay, repeat):
    #print(name + " is started with delay " + str(delay))
    while repeat > 0:

        print(name + " time is " + str(datetime.datetime.now().time()))
        time.sleep(delay)
        repeat -=1

    print(name + " has stopped")

def main():
    print("main started")
    start = 0
    while start < 60:
        time.sleep(1)
        start += 1
        t1 = threading.Thread(target=timer, args=("timer 1", 2, 5))
        t2 = threading.Thread(target=timer, args=("timer 2", 4, 10))
        t3 = threading.Thread(target=timer, args=("timer 3", 8, 5))
        if start == 1:
            t2.start()
            t3.start()
        elif start == 30:

            t1.start()

main()