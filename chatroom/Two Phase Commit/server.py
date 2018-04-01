#name Swapnil Narwade
#UTA ID-- smn6025
#Assignment-2
#referances:-- 1)	https://docs.python.org/2/library/httplib.html
# 2)	https://docs.python.org/2/library/datetime.html
# 3)	https://www.learnpython.org/en/Modules_and_Packages
# 4)	https://github.com/buckyroberts/Turtle/tree/master/Multiple_Clients
# 5)	https://www.youtube.com/watch?v=Po5JHXIoDr0&t=5s

import os
from tkinter import *
import tkinter.messagebox
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
addresses = []

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
        '''wanted to close all the connection before start new connection list but no need as we are already defining which port we want to connect'''
        # for c in self.connections:                  #loop for all the available connections
        #     c.close()                               #close all the connections
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
            '''created a thread to accept the new connection and start start_chat function that will start the communication
            between client and server '''
            acceptConnectionThread= threading.Thread(target=self.start_chat, args=(conn,address))
            acceptConnectionThread.start()
        '''here I want to create a thread just for connection between coordinator and server so that communicate
        to each other this can be done using accepting first connection in connection[]'''


        '''here i want to create a function in that we will send data from coordinator to server
        and this function will be the target for the above thread'''
        '''this function saves the message in server log file'''


        '''here I want to create another thread which accept 2nd 3rd 4th connection from connection lsit
        and start communicate with server '''

        '''this function contains the program for broadcasting, the message is here inside the log of server
        this function also gets the votes from all the client 2,3,4 and send this to coordinator '''


    def start_chat(self,conn,address):
        while True:
            data = conn.recv(1024)              #receiving data from client
            '''here i will receive the data in http encoding and print it in the server GUI'''
            if not data.decode():               #validating for empty data
                break
            dataInChar= data.decode()
            dummy,dataOnlyMessage = dataInChar.split("[START]")
            print(dataInChar)                        #printing data
            #data = data1.upper()                #sending data in upper case so we know that it came from server
            #print("sending " + data)
            '''here we are only sending the message back to the client and not the entire http encoding'''
            conn.send(dataOnlyMessage.encode())            #sending the data from client




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
        thread.daemon = True            #freeing the threading if its working is done
        thread.start()                  #start thr thread


def start_thread(server):

    while True:
        x = queue.get()                 #getting the thread in queue for later use
        if x == 1:
            server.create_socket()      #screate socket
            server.bind_socket()        #connecting to client for communication
            server.accept_connections()
             #accepting data from client
        # if x == 2:
        #     server.start_chat()         #this thread is used to handel the chatting
        queue.task_done()               #queue is finish

def thread_work():
    for x in threads:                   #checking the number of thread
        queue.put(x)                    #storing the thread in queue
    queue.join()                        #joining the queue

def serverFunction():
        create_threads()                    #creat thread is called here
        thread_work()


def connectServer():                                    #connect server button defined here
    def buttonOne():
        serverLabel = Server()                                  #thread buttonOne defined here
        #serverLabel.config(text="server started")
        ipAddress.config(text=serverLabel.host)
        portNumber.config(text=serverLabel.port)
        #os.system('python clientGUI.py')
        serverFunction()
    def threadButtonOne():                              #thread is defined here
        threading.Thread(target=buttonOne).start()      #new thresd is created

    threadButtonOne()                                   #thread is called here



# def connectClient():
#     client_name = clientName.get()
#     clientLabel.config(text=client_name + " connected")
#     os.system('python clientGUI.py')


def loadChat():                             #https://stackoverflow.com/questions/43480156/how-to-display-a-files-text-in-python-tkinter-text-widget
    load_file = 'server.txt'                #assigning server.txt file
    with open(load_file, 'r') as f:         #opening server file
        serverBox.insert(INSERT, f.read())  #inserting the file in textbox


def saveAndQuit():                          #save and quit function is defined here
    save_file = serverBox.get("1.0", 'end-1c')
    with open("server.txt", "a") as f:      #opening server.txt file to insert the textbox data
        f.write(save_file)                  #text from textbox is saved in serrver.txt file
    main_window.destroy()                   #close the window


main_window = Tk()                          #creating new window for server

main_window.title("My Server")              #window title
main_window.geometry("400x400")             #window size

firstFrame = Frame(main_window, width=40, height=30)
ip = Label(firstFrame, text="ip address of Server:", fg="blue")
ip.grid(row=0, column=0)
ipAddress = Label(firstFrame, text="", fg="red")
ipAddress.grid(row=1, column=0)

port = Label(firstFrame, text="port number:", fg="blue")
port.grid(row=0, column=4)

portNumber = Label(firstFrame, text="", fg="red")
portNumber.grid(row=1, column=4)

startServer = Button(firstFrame, text="StartServer", bg="green", fg="blue", command=connectServer) #connect server button called here
startServer.grid(row=2, column=3)

serverLabel = Label(firstFrame, text="", fg="red")
serverLabel.grid(row=2, column=4)

firstFrame.pack()

secondFrame = Frame(main_window, width=40, height=30)

serverBox = Text(secondFrame, width=45, height=16)

#get data from client and show inside the server
serverBox.grid()

load = Button(secondFrame, text="Load Chat", bg="green", fg="blue", command=loadChat) #loadd button called here
load.grid(rowspan=1, columnspan=2)

saveQuit = Button(secondFrame, text="Save & Quit", bg="green", fg="blue", command=saveAndQuit)  #save and quit button called here
saveQuit.grid(rowspan=2)

secondFrame.pack()
main_window.mainloop()
