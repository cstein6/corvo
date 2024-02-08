import subprocess

#For first time users, open cmd prompt and run "cleanmgr /sageset:99"
#a dialogue will open and you can select every category to routinely clean.
#after clicking OK, the dialogue will close, and you can run this script to use those options.
#to change the set options, or to use on a new PC/install, repeat this process.
subprocess.run(["cleanmgr", "/sagerun:99"])
