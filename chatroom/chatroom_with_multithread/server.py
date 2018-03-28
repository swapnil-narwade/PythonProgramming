#name Swapnil Narwade
#UTA ID-- smn6025
#Assignment-1
#referances:-- 1)	https://docs.python.org/2/library/httplib.html
# 2)	https://docs.python.org/2/library/datetime.html
# 3)	https://www.learnpython.org/en/Modules_and_Packages
# 4)	https://github.com/buckyroberts/Turtle/tree/master/Multiple_Clients
# 5)	https://www.youtube.com/watch?v=Po5JHXIoDr0&t=5s

import socket                                     #importing all the required libraries
import threading
import time
import datetime
import sys
from queue import Queue
import struct
import signal
import urllib

threads = [1, 2]                                    #number of threads using
queue = Queue()                                     #using queue to save the threads
connections = []                                    #all the connections is going to be saved in here
addresses = []                                      #all the sddress are going to be stored in here


# class Packet(object):
#     message={ 'message': " ",
#              'host':  " ",
#              'user_agent': 'Mozila/5.0',
#              'connection' : 'open',
#              'content_type' : 'text',
#              'content_length' : 'len(message)',
#              'date' : datetime.date(2009, 5, 12) }
#
    # def __init__(self):
    #     self.message=""
    #     self.host=""
    #     self.user_agent=""
    #     self.connection="open"
    #     self.content_type = "text"
    #     self.date=datetime.date(2009, 5, 12)
    #

    # def connection():
    #     headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    #     conn = httplib.HTTPConnection(port)
    #     conn.request("POST", "", headers)
    #     response = conn.getresponse()


class Server(object):                               #creating a server class

    def __init__(self):                             #initialization
        self.host = '127.0.0.1'                     #host of server machine
        self.port = 8000                            #port of server machine
        self.s = None                               #socket
        self.connections = []                       #all the connections is going to be saved in here
        self.addresses = []                         #all the sddress are going to be stored in here


    def create_socket(self):                        #creating a socket function
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #this is socket
            # h1 = urllib.HTTPConnection(host, port)
            # h2 = urllib.HTTPConnection(host, port)
            # h3 = urllib.HTTPConnection(host, port)
            # h4 = urllib.HTTPConnection(host, port)
        except:
            print("error while creating socket: ")
            sys.exit(1)

    def bind_socket(self):                          #creating a bind function to bind the socket
        try:
            self.s.bind((self.host, self.port))     #binding the socket by joining port and host
            self.s.listen(5)                        #in listening mode for incoming connection
        except:
            print("Socket binding error: ")
            time.sleep(5)                           #wait for 5 second
            self.bind_socket()                      #recursion of bind function


    def accept_connections(self):                   #accepting the connections
        for c in self.connections:                  #loop for all the available connections
            c.close()                               #close all the connections
        self.connections = []
        self.addresses = []
        while 1:
            try:
                conn, address = self.s.accept()     #assigning new connection data to conn and address
                conn.setblocking(1)
            except:
                print('Error accepting connections: ')
                # Loop indefinitely
                continue
            self.connections.append(conn)           #appending new connections to the connection list
            self.addresses.append(address)          #appending new adress of new connections
            print("connection has been established |" + "IP| " + address[0] + " |port| " + str(address[1]))


    def start_chat(self):
        while True:
            for conn in self.connections:           #looking for each connection in connection list
                data = conn.recv(1024)              #receiving data from client
                if not data.decode():               #validating for empty data
                    break
                data1= data.decode()
                print(data1)                        #printing data
                data = data1.upper()                #sending data in upper case so we know that it came from server
                print("sending " + data)
                conn.send(data.encode())            #sending the data from client
            continue



                # if conn is not None:                #if connection is not None
                #     try:
                #         received_message = conn.recv(2048)
                #         print(received_message.decode())
                #         conn.send(received_message.encode())
                #         # end = datetime.datetime.now().strftime('%M:%S')
                #         # total = end - start
                #         # conn.send(str(total.encode()))
                #     except:
                #         print("connecting again")
                #         continue




def create_threads():                   #creating threads
    server = Server()                   #assignig Server class to server
    for _ in range(2):                  #
        thread = threading.Thread(target=start_thread, args=(server,))  #creating a new thread
        thread.daemon = True            #freeing the threadnif its working is done
        thread.start()                  #start thr thread


def start_thread(server):

    while True:
        x = queue.get()                 #getting the thread in queue for later use
        if x == 1:
            server.create_socket()      #screate socket
            server.bind_socket()        #connecting to client for communication
            server.accept_connections() #accepting data from client
        if x == 2:
            server.start_chat()         #this thread is used to handel the chatting
        queue.task_done()               #queue is finish

def thread_work():
    for x in threads:                   #checking the number of thread
        queue.put(x)                    #storing the thread in queue
    queue.join()                        #joining the queue

def main():
    create_threads()                    #creat thread is called here
    thread_work()                       #thread work is called here


if __name__ == '__main__':
    main()                              #programm start running from here