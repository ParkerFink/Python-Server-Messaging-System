import socket



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created: ")

port = 12345

server.bind(('127.0.0.1', port))
server.listen()


while True:
    connection, address = server.accept()
    connection.send("Connection Created!".encode())
    connection.close()
    break
