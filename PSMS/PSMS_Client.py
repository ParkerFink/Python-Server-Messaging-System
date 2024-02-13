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



messageList = []


#config 

socket = socket.socket()
port = data["port"]
ip = data["ip"]
socket.connect((ip, port))
print(socket.recv(1024).decode())










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
                tmp = Label(messages_scroll, text=message)
                tmp.pack()




recvThread = threading.Thread(target=recvMessage, name="recvThread")
recvThread.start()




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

    window = Tk()
    window.title("PSMS")
    window.geometry(width + "x" + height)

   

    def closeWindow():
        exit()


    #menu bar
    menubar = Menu(window)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="General", menu=file)

    file.add_command(label="Preferences", command= lambda: settingsWindow("800","500"))
    file.add_command(label="Exit", command= exit)


    #message box and send button
    messages_scroll = customtkinter.CTkScrollableFrame(window, width=600, height= 400, border_width=3, border_color='black')
    messages_scroll.pack()

    entry = customtkinter.CTkEntry(window, width=600,placeholder_text="Message", corner_radius=80)
    entry.pack()

    submit = customtkinter.CTkButton(window, text="Send", command=sendMsg, corner_radius=80)
    submit.pack()


    

    #send message hotkey
    listener = keyboard.Listener(on_press=whatKey)
    listener.start()


    #menu bar
    window.config(menu = menubar)
    window.mainloop()







#SETTINGS WINDOW
def settingsWindow(width, height):

    
    def closeWindow():
        settings.destroy()

  
            


    global settings
    settings = Tk()
    settings.title("Preferences")
    settings.geometry(width + "x" + height)



    backButton = Button(settings, text="Go Back", command=closeWindow)
    backButton.pack()


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

    lightMode = Button(settings, text="Toggle Lightmode- Work In Progress")
    lightMode.pack()




    settings.mainloop()






mainWindow("800", "500")





