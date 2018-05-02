from pydrive.auth import GoogleAuth
from tkinter import *
from tkinter.filedialog import askopenfilename
from pathlib import Path


def auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

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

settingspath = Path("settings.cfg")

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

for x in range(len(settinglineparse)):
    if settinglineparse[x - x][:2] == "# ":
        del settinglineparse[x - x]

issetup = settinglineparse[0].split(" = ", 1)[1].lower()
defaultfile = settinglineparse[1].split(" = ", 1)[1]   

if bool(issetup) == True:
    auth()
    


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


