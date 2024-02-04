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







def onNewClient(client_socket, addr):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print({addr} ,": ", data)
    client_socket.close()





while True:
    connection, address = server.accept()
    connection.send("Connection Created!".encode())
    recvThread = threading.Thread(target=onNewClient, args=(connection, address))
    recvThread.start()
recvThread.join()



    


    
    

    
        
        
    
