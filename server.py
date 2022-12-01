import socket
from threading import Thread
"""
hostname = socket.gethostname()   
print(hostname)
socket.gethostbyname(hostname)  
print(IPAddr)
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",12345))
listClient = []
message = []


def listening():
    while True:
        server.listen()
        client, addr = server.accept()
        listClient.append(client)
        th = Thread(target = recive, args=(client,))
        th.start()


def recive(client):
    msg = "null"
    done = False
    while not done:
        msg = client.recv(1024).decode('utf-8')
        print(msg.find("quit"))
        if msg.find("quit") != -1:
            done = True
        elif msg != "null":
            print(msg)
            message.append(msg)
    
    listClient.remove(client)
    client.close()

def sendM():
    currentMessage = "null"
    
    while True:
        if message[len(message)-1] != currentMessage:
            for client in listClient:
                client.send(message[len(message)-1].encode('utf8'))
                currentMessage = message[len(message)-1]

t1 = Thread(target = listening)
t2 = Thread(target = recive)
t3 = Thread(target = sendM)

t1.start()
message.append("null")
sendM()




