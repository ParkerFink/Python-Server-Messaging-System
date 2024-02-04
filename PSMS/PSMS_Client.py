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



def recvMessage():
    msgPayload_in = socket.recv(1024).decode()
    messages.config(text=msgPayload_in)
    

recvThread = threading.Thread(target=recvMessage, name='recvThread')





#GUI
window = tkinter.Tk()
window.title("PSMS")
window.geometry('800x500')
recvThread.start()


def sendMsg():
    msgPayload = entry.get()
    print(msgPayload)
    socket.send(msgPayload.encode())
    entry.delete(0, 10000)







entry = tkinter.Entry()
entry.pack()

submit = tkinter.Button(text="Send", command=sendMsg)
submit.pack()


messages = tkinter.Label(text = messageList)
messages.pack()

sendHotkey = keyboard.add_hotkey('enter', lambda: sendMsg())


window.mainloop()







