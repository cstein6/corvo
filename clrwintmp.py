import shutil
import os

def cleartemp(folders):
    for folder in folders:
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

# Replace <YourUserName> with your Windows User and add/replace this list with your list of temporary folder paths.
folders = [
    r"C:\Users\<YourUserName>\AppData\Local\Temp",
    r"C:\Windows\Temp",
    r"C:\Windows\Prefetch"
]

cleartemp(folders)
