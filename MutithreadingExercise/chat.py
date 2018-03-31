message_HTTP = "POST HTTP/1.1\nHost: "+HOST+":"+str(PORT)+"\nUser-Agent: CHAT/1.0\nDate: "+now+"\nContent-Type: text/plain\nContent-Length: "+str(encoded_msg_size)+"\n\n"+encoded_msg+"\n"
