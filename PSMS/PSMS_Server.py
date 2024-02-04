import socket
import json


with open('config.json', 'r') as inFile:
    global data
    data = json.load(inFile)
    print(data)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created: ")

port = data["port"]
ip = data["ip"]
server.bind((ip, port))
server.listen(10)




connectionList = [] 
messages = []


    

while True:
    connection, address = server.accept()
    connection.send("Connection Created!".encode())
    connectionList.append(address)
    print(connectionList)

    #messages.append(connection.recv(1024).decode())
    #print(messages)
    

    
        
        
    
