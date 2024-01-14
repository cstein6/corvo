import shutil
import os
import subprocess
import time

def cleartemp(temp):
    for folder in temp:
        try:
            contents = os.listdir(folder)
            for item in contents:
                filepath = os.path.join(folder, item)
                try:
                    if os.path.isfile(filepath):
                        os.unlink(filepath)
                    elif os.path.isdir(filepath):
                        shutil.rmtree(filepath)
                except Exception:
                    pass
        except Exception:
            pass

# folders to clear
temp = [
    r"C:\Users\Administrator\AppData\Local\Temp",
    r"C:\Windows\Temp",
    r"C:\Windows\Prefetch",
    r"C:\Call of Duty\_retail_\xpak_cache",
    r"C:\Call of Duty\_retail_\telescopeCache",
#optional
    #r"C:\Call of Duty\_retail_\telescopeStorage"
    #r"C:\Call of Duty\_retail_\cod23\shadercache" #shaders(rarely necessary)
]

#Disk cleanup (for first time users, open cmd prompt as admin and run the following command;
#  cleanmgr.exe /sageset:99
#select everything you would like to routinely clean, run the command, options will persist.

cleartemp(temp)

def cleanup():
    subprocess.run(["cleanmgr.exe", "/sagerun:99"], shell=True)

cleanup()
