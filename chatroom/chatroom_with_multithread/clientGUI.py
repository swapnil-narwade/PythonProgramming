#name Swapnil Narwade
#UTA ID-- smn6025
#Assignment-1
#referances:-- 1)	https://docs.python.org/2/library/httplib.html
# 2)	https://docs.python.org/2/library/datetime.html
# 3)	https://www.learnpython.org/en/Modules_and_Packages
# 4)	https://github.com/buckyroberts/Turtle/tree/master/Multiple_Clients
# 5)	https://www.youtube.com/watch?v=Po5JHXIoDr0&t=5s


from tkinter import *
from tkinter import messagebox
import os
import sys
import datetime
import threading

def connectClient():                                    #creating start client button function
    def buttonTwo():                                    #this is thread so the after clicking the start client button the gui wont froze

        client_name = clientName.get()                  #this is getting the value form name entry
        if client_name.isalpha():                       #checking for the client name validation
            main_window.title(client_name)              #window named changed to clients name
            clientLabel.config(text="connected")        #getting port and host and displaying on chatbox
            ipAddressClient.config(text="192.128.0.1")
            portNumberClient.config(text="8000")
            os.system('python client.py')               #starting the client.py file
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
