import socket
import sys
from threading import Thread
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",12345))
done = False

def chat():
    while not done:
        msg = client.recv(1024).decode('utf-8')
        writeMessage(msg)

def writeMessage(msg):
    f = open("chat.txt","a") 
    f.write(msg)
    f.write("\n")
    f.close() 

print("Inserisci il tuo nickname in chat: ")
nickname = input()
print("Digita quit per uscire dalla chat !!!")

f = open("chat.txt","w") 
f.close()

t1 = Thread(target = chat)
t1.start()

while not done:
    msg1 = input("Message: ")
    msg = nickname + ": " + msg1
    client.send(msg.encode('utf-8'))
    if msg1 == "quit":
        done = True

print("Exit")
exit()