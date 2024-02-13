import platform
import os



#checks what the current os is
system = platform.system()

print(system)


#actions based on current os
if system == "Windows":
    os.system('pip install keyboard')
    os.system('python PSMS_Client.py')
    

elif system == "Linux":
    os.system('pip3 install pynput')
    os.system('python3 PSMS_Client.py')
    

