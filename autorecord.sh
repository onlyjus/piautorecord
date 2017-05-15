#!/bin/bash
# first restore the alsa mixer
alsactl --file ./asound.state restore

# start drive upload
(python drive_upload.py &)

# stop sox
pkill sox

# The record function
function vox() {

# remove temp mp3
rm -rf /home/pi/temp.mp3

# record
sox -d /home/pi/temp.mp3 silence 1 1 .1% 1 0:00:01 .1% trim 0 04:00:00

wait

# check to see if the temp.mp3 is larger then 4000
for i in /home/pi/temp.mp3 ; do
   b=`stat -c %s "$i"`
if [ $b -ge 4000 ] ; then

NAME=`date +%Y-%m-%d_%H-%M-%S`
TIME=`date +%H:%M:%S`
FILENAME=./recordings/$NAME.mp3
mv /home/pi/temp.mp3 $FILENAME
rm -rf /home/pi/temp.mp3

else
rm -rf /home/pi/temp.mp3
fi
done
vox 
}
vox 
