from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys


gauth = GoogleAuth()
gauth.LocalWebserverAuth()


drive = GoogleDrive(gauth)

print(gauth)

# file = drive.CreateFile()
# file.SetContentFile("imafile.txt")
# file.Upload()

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))
# sys.exit()
