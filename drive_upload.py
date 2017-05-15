from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob
import os
import time

RECORDING_DIR = './recordings'
UPLOADED_FILE = './uploaded.csv'
FID = '0B9DYSBa2wgiAaVBGZm5TenhBYlk' 
CRED_FILE = 'mycreds.txt'

gauth = GoogleAuth()
# try to load credentials
gauth.LoadCredentialsFile(CRED_FILE)
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
# save creds to file
gauth.SaveCredentialsFile(CRED_FILE)

DRIVE = GoogleDrive(gauth)

def upload():
    '''search for and upload files to drive '''

    # search for new files
    found = set(glob.glob(os.path.join(RECORDING_DIR,'*.mp3')))
    uploaded = set()
    if os.path.exists(UPLOADED_FILE):
        with open(UPLOADED_FILE) as up_file:
            uploaded = set(up_file.read().split(','))

    new_files = found - uploaded
    for new_f in new_files:
        f = DRIVE.CreateFile({"parents": [{"kind": "drive#fileLink", "id": FID}]})
        # Read file and set it as a content of this instance.
        f.SetContentFile(new_f)
        f.Upload() 

	print('uploaded title: %s, mimeType: %s' % (f['title'], f['mimeType']))


    # save the new uploaded files
    with open(UPLOADED_FILE, 'w') as up_file:
        up_file.write(','.join(found.union(uploaded)))

while True:
    upload()
    time.sleep(10)
