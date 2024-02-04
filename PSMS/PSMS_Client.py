import socket
import json
import tkinter
import keyboard



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





#GUI
window = tkinter.Tk()
window.title("PSMS")
window.geometry('800x500')

def sendMsg():
    msgPayload = entry.get()
    print(msgPayload)
    socket.send(msgPayload.encode())
    entry.delete(0, 10000)


entry = tkinter.Entry()
entry.pack()

submit = tkinter.Button(text="Send", command=sendMsg)
submit.pack()

sendHotkey = keyboard.add_hotkey('enter', lambda: sendMsg())

window.mainloop()







