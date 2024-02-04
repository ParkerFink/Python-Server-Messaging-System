import socket
import json


with open('config.json', 'r') as inFile:
    global data
    data = json.load(inFile)
    print(data)


#config 
socket = socket.socket()
port = data["port"]
ip = data["ip"]
socket.connect((ip, port))
print(socket.recv(1024).decode())



#user input

def sendMsg():
    msg = str(input("Message: "))
    socket.send(msg.encode())
    sendMsg()
sendMsg()


#socket.close()