import socket
import json
import threading
import customtkinter


from pynput import keyboard
from tkinter import *
from plyer import notification

with open('config.json', 'r') as inFile:
    global data
    data = json.load(inFile)
    print(data)
    inFile.close()



messageList = []


#config 
def connect():
    with open('config.json', 'r') as inFile:
        data = json.load(inFile)

    inFile.close()
    global socket
    global connection

    socket = socket.socket()
    port = data["port"]
    ip = data["ip"]
    connection = socket.connect((ip, port))
    print(socket.recv(1024).decode())

    connection_status.config(text="Connected")

    connectMSG = str(data["username"]) + ": Has Connected! "

    socket.send(connectMSG.encode())

    recvThread = threading.Thread(target=recvMessage, name="recvThread")
    recvThread.start()










#reciving messages
def recvMessage():
    while True:
        msgPayload_in = socket.recv(1024).decode()
        notification.notify(title = "PSMS", message = msgPayload_in, timeout = 2)

        if msgPayload_in == False:
            pass

        else:
            for message in messageList:
                messageList.clear()
            messageList.append(msgPayload_in)
            print(messageList)
            
            for message in messageList:
                tmp = Label(messages_scroll, text=message, anchor='w')
                tmp.pack()







#GUI
#MAIN WINDOW FUNCTION
def mainWindow(width, height):
    
    def whatKey(key):
        if key == keyboard.Key.enter:
            sendMsg()
        
        
        

    def sendMsg():

        with open('config.json', 'r') as configFile:
            username = json.load(configFile)
            configFile.close()


        msgPayload = str(entry.get())

        if msgPayload == "":
            pass

        else:
            print("Sent: " + msgPayload)
            msg = username["username"] + ": " + msgPayload
            socket.send(msg.encode())
            entry.delete(0, 10000)

        with open('config.json', 'r') as configFile:
            data = json.load(configFile)
            configFile.close()





    #MAIN WINDOW LOOP
    global window
    global messages_scroll
    global connection_status

    window = Tk()
    window.title("PSMS")
    window.geometry(width + "x" + height)

    #menu bar
    menubar = Menu(window)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="General", menu=file)

    file.add_command(label="Preferences", command= lambda: settingsWindow("800","500"))
    file.add_command(label="Exit", command= exit)



    groupChatsLabel = Label(window, text="Group Chats", border=3, relief='solid', width=10, justify='center')
    groupChatsLabel.grid(column=1, row=1)

    connection_status = Label(text="Disconnected", pady=5, width=15)
    connection_status.grid(column=2, row=1)


    #message box and send button
    messages_scroll = customtkinter.CTkScrollableFrame(window, width=600, height= 400, border_width=3, border_color='black', corner_radius=15)
    messages_scroll.grid(column=3, row=2)


    entry = customtkinter.CTkEntry(window, width=600,placeholder_text="Message", corner_radius=80)
    entry.grid(column=3, row=3)


    dms_label = Label(text="DMs", border=3, relief='solid', width=15, justify='center', pady=5)
    dms_label.grid(column=4, row=1)


    connectButton = customtkinter.CTkButton(window, width=140, text="Connect", command=connect)
    connectButton.grid(column=4, row=3)

    #send message hotkey
    listener = keyboard.Listener(on_press=whatKey)
    listener.start()

 

    #menu bar
    window.config(menu = menubar)
    window.mainloop()



#CONNECTION INFO UPDATE BOX
def CIUP(width, height):
    ciub = Tk()
    ciub.geometry(width + "x" + height)
    ciub.title("Update Connection Info")
    
    def updateInfo():
        newIP = connection_ip.get()
        

        newPORT = connection_port.get()
        newPORT = int(newPORT)


        with open('config.json', 'r') as inFile:
            file = json.load(inFile)
            file["ip"] = newIP
            file["port"] = newPORT
            
            newInfo = str(file["ip"]) + ":" + str(file["port"])

            with open('config.json', 'w') as inFile:
                json.dump(file, inFile)

                connectInfo.config(text=newInfo)
                inFile.close()
                ciub.destroy()

            


    connection_ip = customtkinter.CTkEntry(ciub, placeholder_text="IP Address")
    connection_ip.pack()

    connection_port = customtkinter.CTkEntry(ciub, placeholder_text="Port")
    connection_port.pack()

    submit = customtkinter.CTkButton(ciub, text="Update", command= updateInfo)
    submit.pack()


    ciub.mainloop()



#SETTINGS WINDOW
def settingsWindow(width, height):
    global settings
    global connectInfo

    settings = Tk()
    settings.title("Preferences")
    settings.geometry(width + "x" + height)



    


    def getEntry():

        entryGet = entry.get()

        with open('config.json', 'r') as configFile:
            data = json.load(configFile)
            configFile.close()

        data["username"] = entryGet

        with open('config.json', 'w') as configFile:
            json.dump(data, configFile)
            l1.config(text="User Name: " + data["username"])
            configFile.close()
        
        entry.delete(0, 10000)


    with open('config.json', 'r') as configFile:
        data = json.load(configFile)
        configFile.close()


    l1 = Label(settings, text="User Name: " + data["username"])
    l1.pack()

    

    entry = Entry(settings)
    entry.pack()



    newName = Button(settings, text="Enter New Name!", command= getEntry)
    newName.pack()



    #lightMode = Button(settings, text="Toggle Lightmode- Work In Progress")
    #lightMode.pack()


    with open('config.json', 'r') as inFile:
        data = json.load(inFile)

    
    connectionData = str(data["ip"]) + ":" + str(data["port"])



    connectInfo = Button(settings, text= connectionData, padx=10, pady=10, command= lambda: CIUP("200","200"))
    connectInfo.pack()


    connectButton = Button(settings, text="Connect To Server", command=connect)
    connectButton.pack()

    settings.mainloop()






mainWindow("1000", "500")





