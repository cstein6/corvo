import shutil
import os

def cleartemp(temp_folders):
    for folder in temp_folders:
        try:
            folder_contents = os.listdir(folder)
            for item in folder_contents:
                item_path = os.path.join(folder, item)
                try:
                    if os.path.isfile(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                except Exception:
                    pass
        except Exception:
            pass

# Replace with your list of temporary folder paths
temp_folders = [
    r"C:\Users\Administrator\AppData\Local\Temp",
    r"C:\Windows\Temp",
    r"C:\Windows\Prefetch"
]

cleartemp(temp_folders)
