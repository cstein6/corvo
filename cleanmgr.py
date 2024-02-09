# For first time users, open cmd prompt and run "cleanmgr /sageset:99". A disk cleanup settings dialogue will open and you can select every category to routinely clean.
# After clicking OK, the dialogue will close, and you can run this script to use those options. To change them, or to use on a new PC/install, repeat the process.
import subprocess

subprocess.run(["cleanmgr", "/sagerun:99"])
