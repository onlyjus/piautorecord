#!/usr/bin/python
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob
import os
import time
import logging
import sys

# setup logger
LOGGER = logging.getLogger('drive_upload')
hdlr = logging.FileHandler('./drive_upload.log')
formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(formatter)
LOGGER.addHandler(hdlr)
LOGGER.setLevel(logging.ERROR)

def my_handler(type, value, tb):
    LOGGER.exception('Exception: {0}'.format(str(value)))

sys.excepthook = my_handler

RECORDING_DIR = './recordings'
UPLOADED_FILE = './uploaded.csv'

# folder id
FID = '0B9DYSBa2wgiAaVBGZm5TenhBYlk' 
CRED_FILE = 'credentials.json'

LOGGER.info('authenticating')
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
        LOGGER.info('Uploading new file {}'.format(new_f))
        f = DRIVE.CreateFile({"parents": [{"kind": "drive#fileLink", "id": FID}]})
        # Read file and set it as a content of this instance.
        f.SetContentFile(new_f)
        f.Upload() 

	LOGGER.info('Uploaded title: %s, mimeType: %s' % (f['title'], f['mimeType']))


    # save the new uploaded files
    with open(UPLOADED_FILE, 'w') as up_file:
        up_file.write(','.join(found.union(uploaded)))

def remove_files():
    found = set(glob.glob(os.path.join(RECORDING_DIR, '*.mp3')))

    cur_time = time.time()
    for f in found:
        created = os.path.getmtime(f)
        if cur_time - created > 30*24*60*60:
            os.remove(f)


if __name__ == '__main__':
    LOGGER.info('Searching for new files')
    upload()
    remove_files()
