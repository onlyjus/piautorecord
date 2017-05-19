# piautorecord

This repository provides a script, `autorecord.sh` that will automatically
record when sound is detected and stop when sound is no longer detected.
Recorded files are then uploaded to google drive. This project was create to
automatically record and upload recordings from a mixer. 

# Dependencies

## Hardware

- Raspberry Pi
- [AudioInjector](https://www.audioinjector.net)
- Phono preamp (depends on level of audio input)

## Software

- sox
```
sudo apt-get install sox
```
- Python
- PyDrive
```
pip install PyDrive
```

# Usage

To use these files, clone the repository:

```
git clone https://github.com/onlyjus/piautorecord.git

```

Once the repository has been download, change to the directory:

```
cd piautorecord
```

Make sure to follow the configuration steps outlined below. Start the script
with:

```
./autorecord.sh
```

Note: you may need to change the permissions on the script:

```
chmod +x autorecord.sh
```

# Configuration

## Alsamixer

The alsa mixer state is applied everytime the script is run. This state needs
to be correctly configured. Try the included state file with:

```
alsactl --file ./asound.state restore
```

You can use te alsamixer to make configuration changes:

```
alsamixer
```

If changes are made, save them with:

```
alsactl --file ./asound.state store
```

## PyDrive

Please follow the configuration instructions at
[PyDrive](https://googledrive.github.io/PyDrive/docs/build/html/quickstart.html#authentication)
to generate the `client_secrets.json` file and place it in this directory.

Edit the `settings.ymal` file to add your `client_id` and `client_secret`. The values are in
the `client_secrets.json` file.

# Crontab

Crontab can be used to automatically run the scripts. Edit crontab:

```
crontab -e
```

Add the following lines to the end of the file:
```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/pi
SHELL=/bin/bash
@reboot cd path/to/piautorecord && ./autorecord.sh
* * * * * cd path/to/piautorecord && ./drive_upload.py 
```
