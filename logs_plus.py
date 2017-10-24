import os                   # Load the Library Module
from time import strftime   # Load just the strftime Module from Time

logsdir = "/tmp/dir1"      # Set the Variable logsdir
zip_program = "zip"       # Set the Variable zip_program - 1.1

# recursion compress file endswith ".sh"
for (path, dirs, files) in os.walk(logsdir):
    for file in files:
        if file.endswith(".sh"):
            new_file_name = file + "." + strftime("%y-%m-%d") + ".zip"
            cmd = zip_program + " " + new_file_name + " " + file
            os.chdir(path)
            os.system(cmd)

