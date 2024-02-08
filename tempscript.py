import shutil
import os
import subprocess
import time

#clears out temp files in selected folders, runs an advanced options disk clean, and flushes dns resolver cache with 0 interaction.. except;


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
    r"C:\CoD\Call of Duty\_retail_\xpak_cache",
    r"C:\CoD\Call of Duty\_retail_\telescopeCache",
#optional
    #r"C:\CoD\Call of Duty\_retail_\telescopeStorage"
    #r"C:\CoD\Call of Duty\_retail_\cod23\shadercache" #shaders(rarely necessary)
]

cleartemp(temp)

subprocess.run(["ipconfig", "/flushdns"])
