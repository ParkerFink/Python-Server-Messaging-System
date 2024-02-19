import platform
import os
import json


#checks what the current os is
system = platform.system()
print(system)




#actions based on current os
if system == "Windows":
     with open('config.json', 'r') as inFile:
        data = json.load(inFile)

        if data['setup'] == False:
            os.system('pip install customtkinter')
            os.system('pip install pynput')
            os.system('pip install plyer')

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
            os.system('pip3 install customtkinter')
            os.system('pip3 install pynput')
            os.system('pip3 install plyer')

            data["setup"] = True

            with open('config.json', 'w') as inFile:
                json.dump(data, inFile)

            inFile.close()
            os.system('python3 PSMS_Client.py')

        elif data["setup"] == True:
            os.system('python3 PSMS_Client.py')


