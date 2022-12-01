import socket
from threading import Thread
"""
hostname = socket.gethostname()   
print(hostname)
socket.gethostbyname(hostname)  
print(IPAddr)
"""

#setting socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",1234))

#list of client
listClient = []

#list of message
message = []

#(thread) listening and accept new client
def listening():
    while True:
        server.listen()
        client, addr = server.accept()
        listClient.append(client)
        #start a sigle thread for each client
        th = Thread(target = recive, args=(client,))
        th.start()

#(thread) read message by client
def recive(client):
    msg = "null"
    done = False
    while not done:
        #message for client
        msg = client.recv(1024).decode('utf-8') 
        #print(msg.find("quit"))
        #if message is quit or empty remove client
        if msg.find("quit") != -1 or  msg == "":
            done = True
        elif msg != "null":
            print(msg)
            message.append(msg)
    
    listClient.remove(client)
    client.close()

#sending message to all client
def sendM():
    currentMessage = "null"
    
    #send only the last message
    while True:
        if message[len(message)-1] != currentMessage:
            for client in listClient:
                client.send(message[len(message)-1].encode('utf8'))
                currentMessage = message[len(message)-1]


t1 = Thread(target = listening)
#t2 = Thread(target = recive)
#t3 = Thread(target = sendM)

#start server
t1.start()

#starting message
message.append("null")

sendM()




