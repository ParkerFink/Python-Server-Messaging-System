import socket
import json
import threading




with open('config.json', 'r') as inFile:
    global data
    data = json.load(inFile)
    print(data)
    inFile.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created: ")

port = data["port"]
ip = data["ip"]
server.bind((ip, port))
server.listen(10)



connections = []


def onNewClient(client_socket, addr):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            client_socket.close()
            connections.remove(client_socket)
            break
        for user in connections:
            user.send(data.encode())
            #joinedMsg = addr + " has joined: "
            #user.send(joinedMsg.encode())
          

        print(data)
        





while True:
    connection, address = server.accept()
    connection.send("Connection Created!".encode())
    connections.append(connection)
    recvThread = threading.Thread(target=onNewClient, args=(connection, address))
    recvThread.start()
    




    


    
    

    
        
        
    
