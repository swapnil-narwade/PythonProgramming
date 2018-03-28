#name Swapnil Narwade
#UTA ID-- smn6025
#Assignment-1
#referances:-- 1)	https://docs.python.org/2/library/httplib.html
# 2)	https://docs.python.org/2/library/datetime.html
# 3)	https://www.learnpython.org/en/Modules_and_Packages
# 4)	https://github.com/buckyroberts/Turtle/tree/master/Multiple_Clients
# 5)	https://www.youtube.com/watch?v=Po5JHXIoDr0&t=5s

import sys
import os
from tkinter import *
import tkinter.messagebox
import threading


def connectServer():                                    #connect server button defined here
    def buttonOne():                                    #thread buttonOne defined here
        #serverLabel.config(text="server started")
        ipAddress.config(text="127.0.0.1")
        portNumber.config(text="8000")
        #os.system('python clientGUI.py')
        os.system('python server.py')                   #importing server.py and running here
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
ip = Label(firstFrame, text="ip address of Server:", fg="Blue")
ip.grid(row=0, column=0)
ipAddress = Label(firstFrame, text="", fg="Blue")
ipAddress.grid(row=1, column=0)

port = Label(firstFrame, text="port number:", fg="blue")
port.grid(row=0, column=4)

portNumber = Label(firstFrame, text="", fg="blue")
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

