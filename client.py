import socket
from threading import Thread

#(thread) print the chat update
def chat():
    while not done:
        msg = client.recv(1024).decode('utf-8')
        writeMessageInFile(msg)
        if(mymsg != msg):
            print(msg)


#write chat in file
def writeMessageInFile(msg):
    f = open("chat.txt","a") 
    f.write(msg)
    f.write("\n")
    f.close() 


def writeMessage():
    done1 = False
    while not done1:
        msg1 = input()
        mymsg = nickname + ": " + msg1
        if msg1 == "quit":
            done1 = True
            tmp = nickname + ": è uscito dalla chat \n" 
            client.send(tmp.encode('utf-8'))
            client.send(mymsg.encode('utf-8'))
        else:
            client.send(mymsg.encode('utf-8'))
    print("Exit")
    

#setting client TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",49151))
#client.connect(("localhost",12345))

#condition exit for some while
done = False

#string tmp
mymsg = ""
msg = ""
str = ""
appoggio = 1

#insert nickname
print("Inserisci il tuo nickname in chat: ")
#nickname = e1.get()
nickname = input()

print("DIGITARE QUIT PER USCIRE DALLA CHAT \n")

f = open("chat.txt","w") 
f.write("Inizio chat: \n\n")
f.close()

t1 = Thread(target = chat)
t1.start()


tmp = nickname + ": è entrato in chat" 
client.send(tmp.encode('utf-8'))


while not done:
    msg1 = input()
    mymsg = nickname + ": " + msg1
    if msg1 == "quit":
        done = True
        tmp = nickname + ": è uscito dalla chat" 
        client.send(tmp.encode('utf-8'))
        client.send(mymsg.encode('utf-8'))
    else:
        client.send(mymsg.encode('utf-8'))

print("Stai uscendo dalla chat....")
print("Exit")





