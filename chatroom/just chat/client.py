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

class Client(object):                                       #created a Client class

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

    def commands(self):
        name = input("")
        self.s.send(name.encode())                          #send message to client in string
        while True:                                         #run in loop to get and send request
            try:
                # message = input("-->")                      #message is getting from terminal
                # while message != 'q':                       #checking if message is not q
                    # self.s.send(message.encode())
                              #sending the message in byte format by encoding

                data = self.s.recv(1024)
                print("data received from server " + data.decode())#data received from server and decoded
                message = input("-->")                  #message is getting from terminal
                self.s.close()                              #socket is closed

                # msg = self.s.recv(2048)                     #to receive string
                # print("-->" + msg.decode())                 #print message
                # sent_message = input("-->")                 #accept input from terminal
                # message1 = datetime.datetime.now().strftime('%M:%S')        #message with time
                # message2 = sent_message + str(" (") + str(message1) + str(")")
                # self.s.send(message2.encode())
                #continue                                    #continue to commands functions
            except:
                time.sleep(5)                               #wait for 5 minute to receive text
                print("type something")
                continue

def client():
    client = Client()                                       #assign Client class to client
    client.create_socket()                                  #create socket for client
    while True:                                             #run in loop
        try:
            client.connect_socket()                         #connect socket
        except:
            print("Error on socket connections:")
            time.sleep(5)                                   #wait for 5 second to reconnect

        try:
            client.commands()                               #run command function

        except:
            print("Error")
        client.s.close()


def connectClient():                                    #creating start client button function
    def buttonTwo():                                    #this is thread so the after clicking the start client button the gui wont froze

        client_name = clientName.get()                  #this is getting the value form name entry
        if client_name.isalpha():                       #checking for the client name validation
            main_window.title(client_name)              #window named changed to clients name
            clientLabel.config(text="connected")        #getting port and host and displaying on chatbox
            ipAddressClient.config(text="192.128.0.1")
            portNumberClient.config(text="8000")
            client()
        else:
            messagebox.showerror("warning", "Enter the valid name")#error validation for message
        clientName.set("")

    def threadButtonTwo():
        threading.Thread(target=buttonTwo).start()      #starting thread here

    threadButtonTwo()                                   #calling thread here


def sendMessage():                                      #send message function defined here

    message_send = message.get()                        #message from chatbox is getting here
    if message_send != "":                              #checking if message id not empty
        serverBoxText.insert(END,                       #inserting the message to the textbox
                             str(main_window.title() + " :- " + message_send + " (" + datetime.datetime.now().strftime('%M:%S')
                                 + ")\n"))
        message_terminal = serverBoxText.get("1.0", END)    #sending messages to the terminal
        print(message_terminal)
        message.set("")
    else:
        messagebox.showerror("warning", "empty message")    #validation for message


main_window = Tk()                                      #creating GUI window using tkInter library

main_window.title("Client Name")                        #window title
main_window.geometry("400x400")                         #window size

frame1 = Frame(main_window, height=40, width=30)        #frame1 created

ipClient = Label(frame1, text="ip address of Client", fg="Blue")    #ipClient label
ipClient.grid(row=0, column=0, sticky=W)

ipAddressClient = Label(frame1, text="", fg="Blue")                 #ipaAdrress Label
ipAddressClient.grid(row=1, column=0, sticky=W)

portClient = Label(frame1, text="port number of client", fg="Blue") #portClient label
portClient.grid(row=0, column=2)

portNumberClient = Label(frame1, text="", fg="Blue")        #portnumber label
portNumberClient.grid(row=1, column=2)
frame1.pack()

firstFrame = Frame(main_window, width=40, height=30)

clientLabel = Label(firstFrame, text="", fg="red")          #cllient Label
clientLabel.grid(row=0, column=0, sticky=W)

nameLabel = Label(firstFrame, text="Enter client name:-", fg="blue")
nameLabel.grid(row=1, column=0, sticky=E)
clientName = StringVar()

nameEntry = Entry(firstFrame, textvariable=clientName, width=30)        #name Entry for client name
nameEntry.grid(row=1, column=3, sticky=W)

startClient = Button(firstFrame, text="StartClient", bg="green", fg="blue", command=connectClient) #Start client button
startClient.grid(row=2, column=3)

firstFrame.pack()

clientFrame = Frame(main_window)
messageLabel = Label(clientFrame, text="enter the message")     #message lanel
messageLabel.grid(row=1, column=0, sticky=E)
message = StringVar()
messageEntry = Entry(clientFrame, textvariable=message, width=30)       #message textbox created
messageEntry.grid(row=1, column=1, sticky=W)
sendButton = Button(clientFrame, text="Send", command=sendMessage)      #send button
sendButton.grid(row=1, column=4, sticky=E)

clientFrame.pack()

clientBox = Frame(main_window)
# here we should get name this client and his message with time duration of client sending the message
# valueMessage = StringVar()                #here we should get value = message from client and show it to label
serverBoxText = Text(clientBox, width=45, height=16)                    #textbox for chatting created
serverBoxText.grid()
clientBox.pack()

main_window.mainloop()                              #mainloop contiounsly running for displaying the GUI
