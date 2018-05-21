# JukeBox

## Parts used for v1

- raspberry Pi v1 B
- Adafruit PiTFT - 2.8" Touchscreen 320x240px ([tuto install][1])
- Philips SD HD card 16Gb

## Software adn configuration

### OS

I used the last image from adafruit downloadable [here][2].

### python3

Install python3 on the raspberry.

### pyQT5 and pyuic5

Install pyQT on the raspberry. 

### Mplayer

Install mplayer2 on the raspberry. 

### Modifiy alsa.conf


[ALSA.CONF][ALSA.CONF]

### Modify autostart
```
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
```

```
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
#@openbox
#@unclutter -idle 0
@/bin/bash /home/pi/Documents/python/JukeBox/listMusic.sh
@/usr/bin/python3 /home/pi/Documents/python/JukeBox/main.py > /media/JukeBox/juke.log
@point-rpi
```
### Auto-mount USB Key

Step 1 - Plug the usb key
Step 2 – Identify The Devices Unique ID
In order to find the unique reference (UUID) for your drive run the following command in the terminal :
```
ls -l /dev/disk/by-uuid/
```
The line will usually refer to “/sda” and in this example it is “sda1”. My ID is “12AB-3456”.
Step 3 – Create a Mount Point
```
sudo mkdir /media/JukeBox
sudo chown -R pi:pi /media/JukeBox
```
Step 4 – Auto Mount
```
sudo nano /etc/fstab
```
Then add the following line at the end :
```
UUID=12AB-3456 /media/JukeBox vfat auto,nofail,noatime,users,rw,uid=pi,gid=pi 0 0
```

### Qt Creator

I used Qt Creator on mac to create the interface.

Use the command pyuic5 to transform the .ui to .py
pyuic5 mainwindow.ui > mainwindow_auto.py

# Link

[PiTFT][1]

[OS Raspbian with PiTFT][2]

[Auto Mount][3]

[Mplayer][4]

[ALSA.CONF][ALSA.CONF]

[mplayer doc][mplayer doc]

[mplayer playlist][mplayer playlist]

[autostart][autostart]

[autostart without GUI][autostart without GUI]

[PyQT GUI][PyQT GUI]

[1]: https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/downloads?view=all
[2]: https://s3.amazonaws.com/adafruit-raspberry-pi/2016-10-18-pitft-28c.zip
[3]: http://www.raspberrypi-spy.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/
[4]: http://www.mplayerhq.hu/DOCS/HTML/fr/index.html

[mplayer doc]: http://stackoverflow.com/questions/28664813/play-m4a-in-python-script-with-mplayer
[mplayer playlist]: https://zuttobenkyou.wordpress.com/2009/01/17/how-to-quickly-make-a-playlist-for-mplayer/
[autostart]: http://blog.startingelectronics.com/auto-start-a-desktop-application-on-the-rapberry-pi/
[autostart without GUI]: http://alexba.in/blog/2013/01/07/use-your-raspberrypi-to-power-a-company-dashboard/
[PyQT GUI]: https://www.baldengineer.com/raspberry-pi-gui-tutorial.html
[ALSA.CONF]: http://raspberrypi.stackexchange.com/questions/39928/unable-to-set-default-input-and-output-audio-device-on-raspberry-jessie
