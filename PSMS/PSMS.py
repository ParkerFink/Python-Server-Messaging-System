import platform
import os
import json


#checks what the current os is
system = platform.system()
print(system)

modules = ['customtkinter', 'pynput', 'plyer']


#actions based on current os
if system == "Windows":
     with open('config.json', 'r') as inFile:
        data = json.load(inFile)

        if data['setup'] == False:
            for module in modules:
                os.system('pip install ' + module)
            data["setup"] = True
            
            with open('config.json', 'w') as inFile:
                json.dump(data, inFile)

            inFile.close()
            os.system('python PSMS_Client.py')
    
        elif data["setup"] == True:
            os.system('python PSMS_Client.py')
    



elif system == "Linux":
    with open('config.json', 'r') as inFile:
        data = json.load(inFile)

        if data['setup'] == False:

            for module in modules:
                os.system('pip3 install ' + module)
            data["setup"] = True

            with open('config.json', 'w') as inFile:
                json.dump(data, inFile)

            inFile.close()
            os.system('python3 PSMS_Client.py')

        elif data["setup"] == True:
            os.system('python3 PSMS_Client.py')


