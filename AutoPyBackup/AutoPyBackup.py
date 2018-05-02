from pydrive.auth import GoogleAuth
from tkinter import *
from tkinter.filedialog import askopenfilename
from pathlib import Path

# def upload(filename):
#     # gdrive upload filename


def openfile():
    window = Tk()
    print("Starting Tkinter Open Window")

    filetypes = [("", "*")]
    title = "Find file to backup"
    initialdir = "C:\\"

    window.fileName = askopenfilename(filetypes=filetypes, initialdir=initialdir, title=title)
    window.destroy()
    return window.fileName

# ======================================
#         Settings File Load
# ======================================

settingspath = Path("settings.cfg")

# Detects if the settings file is existent and if not it then creates a new fresh one
if not settingspath.exists():
    print("Creating new settings file")
    settingsfile = open("settings.cfg", "w")
    settingsfile.write("# Setup controls if the program goes into inital start mode, IE it will ask for OAuth from google and location of file")
    settingsfile.write("\n" + "# Default file controls the default file path, No need to mess with this just me storing data for later")
    settingsfile.write("\n" + "setup = false")
    settingsfile.write("\n" + "defaultfile = None")
    settingsfile.close()

settingsfile = open("settings.cfg", "r")
settingunparsed = str(settingsfile.read())
settinglineparse = settingunparsed.split("\n")

# Kills the lines with comments on them
# This took too long to figure out how to do do
for x in range(len(settinglineparse)):
    if settinglineparse[x - x][:2] == "# ":
        del settinglineparse[x - x]

# Assigns the final settings to variables
issetup = settinglineparse[0].split(" = ", 1)[1].lower()
defaultfile = settinglineparse[1].split(" = ", 1)[1]   

# ======================================
#             Main Base
# ======================================

# Check for Auth file then
gauth = GoogleAuth()
# gauth.LoadCredentialsFile("gauth.auth")
#
# if gauth.credentials is None:
#     gauth.LocalWebserverAuth()
# elif gauth.access_token_expired:
#     gauth.Refresh()
# else:
#     gauth.Authorize()
#
# gauth.SaveCredentialsFile("gauth.auth")
gauth.LocalWebserverAuth()

if bool(issetup) == True:
    print("setup = True")

# if file exists:
#     read file name
#     upload(filename)
# else:
#     openfile()

# print(openfile())



print(issetup)
print(defaultfile)

# On start upload file
# Every hour it checks if it has uploaded a file


