import platform
import os
import json


#checks what the current os is
system = platform.system()

print(os)


#actions based on current os
if system == "Windows":
    os.system('pip install keyboard')
    os.system('python PSMS_Client.py')

elif system == "Linux":
    os.system('pip3 install keyboard')
    os.system('sudo python3 PSMS_Client.py')



