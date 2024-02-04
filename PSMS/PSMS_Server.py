import socket



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created: ")
port = 12345
server.bind(('127.0.0.1', port))
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
    

    
        
        
    
