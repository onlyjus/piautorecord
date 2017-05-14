# piautorecord

This repository provides a script, `autorecord.sh` that will automatically
record when sound is detected and stop when sound is no longer detected.
Recorded files are then uploaded to google drive. This project was create to
automatically record and upload recordings from a mixer of a worship service. 

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



# Configuration

## Alsamixer

The alsa mixer state is applied everytime the script is run. This state needs
to be correctly configured. Try the included state file with:

```
alsactl --file ./asound.state restore
```

You can use te alsamixer to make configuration chanages:

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
