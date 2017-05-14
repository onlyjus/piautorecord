from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
fid = '0B9DYSBa2wgiAaVBGZm5TenhBYlk'
f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
# Read file and set it as a content of this instance.
f.SetContentFile('./recordings/2017-04-08_23-01-40.mp3')
f.Upload() 

print('title: %s, mimeType: %s' % (f['title'], f['mimeType']))

#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for file1 in file_list:
#  print('title: %s, id: %s' % (file1['title'], file1['id']))
