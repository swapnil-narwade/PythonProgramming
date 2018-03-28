from threading import Thread
import time


class WriteFile(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out


    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        time.sleep(5)
        print("run is running ")

def Main():
    message = input("enter the data ")
    back = WriteFile(message, 'out.txt')
    back.start()
