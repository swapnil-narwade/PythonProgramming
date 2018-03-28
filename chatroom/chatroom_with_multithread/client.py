#name Swapnil Narwade
#UTA ID-- smn6025
#Assignment-1
#referances:-- 1)	https://docs.python.org/2/library/httplib.html
# 2)	https://docs.python.org/2/library/datetime.html
# 3)	https://www.learnpython.org/en/Modules_and_Packages
# 4)	https://github.com/buckyroberts/Turtle/tree/master/Multiple_Clients
# 5)	https://www.youtube.com/watch?v=Po5JHXIoDr0&t=5s

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
        name = input("enter your name ")
        self.s.send(name.encode())                          #send message to client in string
        while True:                                         #run in loop to get and send request
            try:
                message = input("-->")                      #message is getting from terminal
                while message != 'q':                       #checking if message is not q
                    self.s.send(message.encode())           #sending the message in byte format by encoding
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
                continue                                    #continue to commands functions
            except:
                time.sleep(5)                               #wait for 5 minute to receive text
                print("type something")
                continue

def main():
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
        client.s.close()                                    #close client socket


if __name__ == '__main__':
    while True:
        main()
