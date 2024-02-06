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
            for message in messageList:
                messageList.clear()
            messageList.append(msgPayload_in)
            print(messageList)
            
            for message in messageList:
                tmp = tkinter.Label(window, text=message).pack()




recvThread = threading.Thread(target=recvMessage, name="recvThread")
recvThread.start()




#GUI
def mainWindow(width, height):
    with open('config.json', 'r') as configFile:
        data = json.load(configFile)

    global window
    window = tkinter.Tk()
    window.title("PSMS")
    window.geometry(width + "x" + height)

    settingsTab = tkinter.Button(text="Settings", command=lambda: settingsWindow("800","500"))
    settingsTab.pack()



    def sendMsg():
        msgPayload = str(entry.get())
        print("Sent: " + msgPayload)
        msg = data["username"] + ": " + msgPayload
        socket.send(msg.encode())
        entry.delete(0, 10000)



    entry = tkinter.Entry(width=50)
    entry.pack()

    submit = tkinter.Button(text="Send", command=sendMsg)
    submit.pack()
    keyboard.add_hotkey('enter', lambda: sendMsg())

    window.mainloop()








def settingsWindow(width, height):
    global settings
    settings = tkinter.Tk()
    settings.title("Settings")
    settings.geometry(width + "x" + height)

    def getEntry():
        entryGet = entry.get()
        with open('config.json', 'r') as configFile:
            data = json.load(configFile)
        data["username"] = entryGet

        with open('config.json', 'w') as configFile:
            json.dump(data, configFile)
        
        l2.config(text=entryGet)
        entry.delete(0, 10000)



    with open('config.json', 'r') as configFile:
        data = json.load(configFile)
        


    l1 = tkinter.Label(settings, text="User Name: ")
    l1.pack()

    l2 = tkinter.Label(settings, text= data["username"])
    l2.pack()

    entry = tkinter.Entry(settings)
    entry.pack()

    keyboard.add_hotkey('enter', lambda: getEntry())


    settings.mainloop()






mainWindow("800", "500")





