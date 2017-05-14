#!/bin/bash
# first restore the alsa mixer to enable output, line capture, and 0 dB levels
alsactl --file ./asound.state restore

pkill sox
function vox() {
rm -rf /home/pi/temp.mp3
sox -d /home/pi/temp.mp3 silence 1 1 .1% 1 0:00:01 .1% trim 0 04:00:00
wait

for i in /home/pi/temp.mp3 ; do
   b=`stat -c %s "$i"`
if [ $b -ge 4000 ] ; then

NAME=`date +%Y-%m-%d_%H-%M-%S`
TIME=`date +%H:%M:%S`
FILENAME=/home/pi/recordings/recordings/$NAME.mp3
mv /home/pi/temp.mp3 $FILENAME
rm -rf /home/pi/temp.mp3

else
rm -rf /home/pi/temp.mp3
fi
done
vox 
}
vox 
