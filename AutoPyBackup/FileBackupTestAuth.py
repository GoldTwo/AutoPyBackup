from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

print(gauth)

file = drive.CreateFile()
file.SetContentFile('cat.png')
file.Upload()
print('title: %s, mimeType: %s' % (file['title'], file['mimeType']))

