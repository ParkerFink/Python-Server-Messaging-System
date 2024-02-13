import socket
import json
import threading
import customtkinter

from pynput import keyboard
from tkinter import *

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
                tmp = Label(messages_scroll, text=message)
                tmp.pack()




recvThread = threading.Thread(target=recvMessage, name="recvThread")
recvThread.start()




#GUI
#MAIN WINDOW FUNCTION
def mainWindow(width, height):

    

    def sendMsg(key):

        if key == keyboard.Key.enter:

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
        window.destroy()
        exit()


    #menu bar
    menubar = Menu(window)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="General", menu=file)

    file.add_command(label="Preferences", command= lambda: settingsWindow("800","500"))
    file.add_command(label="Exit", command= lambda: closeWindow())


    #message box and send button
    messages_scroll = customtkinter.CTkScrollableFrame(window, width=600, height= 400, border_width=3, border_color='black')
    messages_scroll.pack()

    entry = Entry(width=75)
    entry.pack()

    submit = Button(text="Send", command=sendMsg)
    submit.pack()


    

    #send message hotkey
    listener = keyboard.Listener(on_press=sendMsg)
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
    settings.title("Settings")
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
            configFile.close()

        l2.config(text=entryGet)
        entry.delete(0, 10000)



    with open('config.json', 'r') as configFile:
        data = json.load(configFile)
        configFile.close()


    l1 = Label(settings, text="User Name: ")
    l1.pack()

    l2 = Label(settings, text= data["username"])
    l2.pack()

    entry = Entry(settings)
    entry.pack()



    newName = Button(settings, text="Enter New Name!", command= getEntry)
    newName.pack()

    #keyboard.add_hotkey('enter', lambda: getEntry())




    settings.mainloop()






mainWindow("800", "500")





