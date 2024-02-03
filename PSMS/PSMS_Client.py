import socket

#config 
socket = socket.socket()
port = 12345
socket.connect(('127.0.0.1', port))
print(socket.recv(1024).decode())



#user input

def sendMsg():
    msg = str(input("Message: "))
    socket.send(msg.encode())
    sendMsg()
sendMsg()


socket.close()