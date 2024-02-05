import socket
import json
import tkinter
import keyboard
import threading


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



messageList = []



#reciving messages
def recvMessage():
    while True:
        msgPayload_in = socket.recv(1024).decode()
        if msgPayload_in == False:
            pass

        else:
            
            window.winfo_exists()

            messageList.append(msgPayload_in)
            print(messageList)
            for message in messageList:
                tkinter.Label(text= message).pack()




recvThread = threading.Thread(target=recvMessage, name="recvThread")
recvThread.start()




#GUI
window = tkinter.Tk()
window.title("PSMS")
window.geometry('800x500')


def sendMsg():
    msgPayload = str(entry.get())
    print("Sent: " + msgPayload)
    socket.send(msgPayload.encode())
    entry.delete(0, 10000)



entry = tkinter.Entry()
entry.pack()

submit = tkinter.Button(text="Send", command=sendMsg)
submit.pack()




sendHotkey = keyboard.add_hotkey('enter', lambda: sendMsg())


window.mainloop()







