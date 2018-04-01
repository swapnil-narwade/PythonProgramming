#name Swapnil Narwade
#UTA ID-- smn6025
#Assignment-2
#referances:-- 1)	https://docs.python.org/2/library/httplib.html
# 2)	https://docs.python.org/2/library/datetime.html
# 3)	https://www.learnpython.org/en/Modules_and_Packages
# 4)	https://github.com/buckyroberts/Turtle/tree/master/Multiple_Clients
# 5)	https://www.youtube.com/watch?v=Po5JHXIoDr0&t=5s

from tkinter import *
from tkinter import messagebox
import sys
import threading
import os                                                 #importing standerd libraries
import socket
import urllib
import datetime
import time


class Coordinator(object):                                       #created a Client class

    def __init__(self):                                     #initialized attributes
        self.host = '127.0.0.1'                             #this is the host of our server
        self.port = 8000                                    #this is the port of server where connection bind
        self.s = None                                       #this is a socket


    def create_socket(self):                                #creating a socket
        self.s = socket.socket()

    def connect_socket(self):                               #connect to a server socket
        try:
            self.s.connect((self.host, self.port))          # connect host and port
        except:
            print("Socket connection error: ")
            time.sleep(5)                                   #wait for 5 second and connect again


    def sendFromMessageTextBox(self,message):
        self.s.send(message.encode())                          #send message to client in string
        data = self.s.recv(1024)
        print(data.decode())#data received from server and decoded

    def commands(self):
        while True:                                         #run in loop to get and send request
            try:
            # message = input("-->")                      #message is getting from terminal
            # while message != 'q':                       #checking if message is not q
                # self.s.send(message.encode())
                          #sending the message in byte format by encoding
                name = input("")
                self.sendFromTerminal(name)
                #message = input("-->")                  #message is getting from terminal
                #self.s.close()                              #socket is closed

                # msg = self.s.recv(2048)                     #to receive string
                # print("-->" + msg.decode())                 #print message
                # sent_message = input("-->")                 #accept input from terminal
                # message1 = datetime.datetime.now().strftime('%M:%S')        #message with time
                # message2 = sent_message + str(" (") + str(message1) + str(")")
                # self.s.send(message2.encode())
                # continue                                    #continue to commands functions
            except:
                time.sleep(5)                               #wait for 5 minute to receive text
                print("type something")
                continue


coordinator = Coordinator()

def coordinatorFunction():
#    coordinator = Coordinator()                                       #assign Client class to client
    coordinator.create_socket()                                  #create socket for client
    while True:                                             #run in loop
        try:
            coordinator.connect_socket()                         #connect socket
        except:
            print("Error on socket connections:")
            time.sleep(5)                                   #wait for 5 second to reconnect

        try:
            coordinator.commands()                               #run command function

        except:
            print("Error")
        coordinator.s.close()



def connectCoordinator():                                    #creating start client button function
    def buttonTwo():                                    #this is thread so the after clicking the start client button the gui wont froze
    #    cordinator = Coordinator()
        '''This is a part for getting the clients name as the coordinator is only one so dont need to change its name'''
        # client_name = clientName.get()                  #this is getting the value form name entry
        # if client_name.isalpha():                       #checking for the client name validation
        #     main_window.title(client_name)              #window named changed to clients name
        coordinatorLabel.config(text="connected")        #getting port and host and displaying on chatbox
        ipAddressCoordinator.config(text=coordinator.host)
        portNumberCoordinator.config(text=coordinator.port)
        coordinatorFunction()
        '''This is for the validation of client name but as there is only one coordinator we dont need to specify seperately'''
        # else:
        #     messagebox.showerror("warning", "Enter the valid name")#error validation for message
        # clientName.set("")

    def threadButtonTwo():
        threading.Thread(target=buttonTwo).start()      #starting thread here

    threadButtonTwo()                                   #calling thread here


def sendMessage():                                      #send message function defined here

    message_send = message.get()                        #message from chatbox is getting here
    if message_send != "":                              #checking if message id not empty
        coordinatorBoxText.insert(END,                       #inserting the message to the textbox
                             str(main_window.title() + " :- " + message_send + " (" + datetime.datetime.now().strftime('%M:%S')
                                 + ")\n"))
        # message_terminal = serveBoxText.get("1.0", END)    #sending messages to the terminal
        # print("coordinator:- " + message_send)
        date = datetime.datetime.now()
        httpEncodedMessage = "POST HTTP/1.1\nHost: "+coordinator.host+":"+str(coordinator.port)+"\nUser-Agent: Independant/1.0\nDate: "+str(date)+"\nContent-Type: text/plain\nContent-Length: "+str(len(message_send))+"\n\n[START]coordinator: "+message_send+"\n"

        coordinator.sendFromMessageTextBox(httpEncodedMessage)
        message.set("")
    else:
        messagebox.showerror("warning", "empty message")    #validation for message


def sendGlobalCommit():
    '''here coordinator gets the vote of all the clients and send message to the server with its decision'''

    pass


def sendGlobalAbort():
    '''here coordinator gets the vote of all the clients and send message to the server with its decision'''
    pass


main_window = Tk()                                      #creating GUI window using tkInter library

main_window.title("Coordinator")                        #window title
main_window.geometry("400x450")                         #window size

frame1 = Frame(main_window, height=40, width=30)        #frame1 created

ipCoordinator = Label(frame1, text="ip address of Coordinator", fg="Blue")    #ipClient label
ipCoordinator.grid(row=0, column=0, sticky=W)

ipAddressCoordinator = Label(frame1, text="", fg="Red")                 #ipaAdrress Label
ipAddressCoordinator.grid(row=1, column=0, sticky=W)

portCoordinator = Label(frame1, text="port number of client", fg="Blue") #portClient label
portCoordinator.grid(row=0, column=2)

portNumberCoordinator = Label(frame1, text="", fg="Red")        #portnumber label
portNumberCoordinator.grid(row=1, column=2)
frame1.pack()

firstFrame = Frame(main_window, width=40, height=30)

coordinatorLabel = Label(firstFrame, text="", fg="red")          #cllient Label
coordinatorLabel.grid(row=0, column=0, sticky=W)
'''this part is for naming the client window, this is a Coordinator so sont need to change the name of it'''
# nameLabel = Label(firstFrame, text="Enter client name:-", fg="blue")
# nameLabel.grid(row=1, column=0, sticky=E)
# clientName = StringVar()
#
# nameEntry = Entry(firstFrame, textvariable=clientName, width=30)        #name Entry for client name
# nameEntry.grid(row=1, column=3, sticky=W)

startCoordinator = Button(firstFrame, text="StartCoordinator", bg="green", fg="blue", command=connectCoordinator) #Start client button
startCoordinator.grid(row=2, column=3)

firstFrame.pack()

clientFrame = Frame(main_window)
'''this is show the user what to type in the textbox'''
# messageLabel = Label(clientFrame, text="enter the message")     #message lanel
# messageLabel.grid(row=1, column=0, sticky=E)
message = StringVar()
messageEntry = Entry(clientFrame, textvariable=message, width=30)       #message textbox created
messageEntry.grid(row=1, column=1, sticky=W)
sendButton = Button(clientFrame, text="Send", command=sendMessage)      #send button
sendButton.grid(row=1, column=4, sticky=E)

clientFrame.pack()

clientBox = Frame(main_window)
# here we should get name this client and his message with time duration of client sending the message
# valueMessage = StringVar()                #here we should get value = message from client and show it to label
coordinatorBoxText = Text(clientBox, width=45, height=15)                    #textbox for chatting created
coordinatorBoxText.grid()
clientBox.pack()
globalCommitFrame = Frame(main_window)
fakeLabel = Label(globalCommitFrame, text="")          #cllient Label
fakeLabel.grid(row=0, column=0, sticky=W)
globalCommitButton = Button(globalCommitFrame, text="Gloabal Commit", bg="green", fg="white", command=sendGlobalCommit)      #send button
globalCommitButton.grid(row=1, column=2, sticky=E)
globalAbortButton = Button(globalCommitFrame, text="Gloabal Abort", bg="red", fg="white", command=sendGlobalAbort)      #send button
globalAbortButton.grid(row=1, column=4, sticky=E)
globalCommitFrame.pack()
main_window.mainloop()
