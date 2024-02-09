import shutil
import os
import subprocess

# Clears out temp files in specified folders and flushes dns resolver cache with 0 user interaction.

def cleartemp(temp):
    for folder in temp:
        try:
            contents = os.listdir(folder)
            for item in contents:
                path = os.path.join(folder, item)
                try:
                    if os.path.isfile(path):
                        os.unlink(path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                except Exception:
                    pass
        except Exception:
            pass

# specifies folders to clear, replace "PATH_TO_COD_FOLDER" and "<YourUserName>" with... your cod folder path and ur windows username.
temp = [
    r"C:\Users\<YourUserName>\AppData\Local\Temp",
    r"C:\Windows\Temp",
    r"C:\Windows\Prefetch",
    r"C:\PATH_TO_COD_FOLDER\_retail_\xpak_cache",
    r"C:\PATH_TO_COD_FOLDER\_retail_\telescopeCache",
#optional
    #r"C:\CoD\Call of Duty\_retail_\telescopeStorage" # makes you agree to terms of use again, idrk what this is or if its even helpful/necessary to clean...
    #r"C:\CoD\Call of Duty\_retail_\cod23\shadercache" # shaders.
        # I only recommend clearing shader cache if you either; 1. Updated GPU drivers and want a fresh install of shaders. 
        #2. Changed texture filtering options in a graphics control panel, and are experiencing sharpening issues or repeatedly getting "shaders installing" on consecutive game launches. or 
        #3. Are experiencing texture issues that can't be resolved through in-game or config file tweaks, and just want to try it.
    #TIP: no matter what, do not interrupt the fresh shader install when you launch the game after clearing cache or updating GPU driver.
]

cleartemp(temp) # clears folders

subprocess.run(["ipconfig", "/flushdns"]) # clears DNS cache
