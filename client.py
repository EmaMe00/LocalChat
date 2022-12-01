import socket
import os
from threading import Thread
import threading
from tkinter import *

#window=Tk()
#window.title('Client')
#window.geometry("600x400+10+20")
#txtfld=Entry(window, text="This is Entry Widget", bd=5)
#txtfld.place(x=40, y=500)
#window.mainloop()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",1234))

#client.connect(("localhost",12345))
done = False
mymsg = ""

def chat():
    while not done:
        msg = client.recv(1024).decode('utf-8')
        writeMessage(msg)
        if(mymsg != msg):
            print(msg)

def writeMessage(msg):
    f = open("chat.txt","a") 
    f.write(msg)
    f.write("\n")
    f.close() 

print("Inserisci il tuo nickname in chat: ")
nickname = input()
print("\n DIGITARE QUIT PER USCIRE DALLA CHAT \n")

f = open("chat.txt","w") 
f.write("Inizio chat: \n\n")
f.close()

t1 = Thread(target = chat)
t1.start()

#os.system("open chat.txt")
tmp = nickname + ": è entrato in chat \n" 
client.send(tmp.encode('utf-8'))

while not done:
    msg1 = input("")
    mymsg = nickname + ": " + msg1
    if msg1 == "quit":
        done = True
        tmp = nickname + ": è uscito dalla chat \n" 
        client.send(tmp.encode('utf-8'))
        client.send(mymsg.encode('utf-8'))
    else:
        client.send(mymsg.encode('utf-8'))

print("Exit")
exit()