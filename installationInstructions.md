LiveView Project 22 January 2020 Release
# STEP1: RPI OS Details

Image tested - Latest version (Noobs - 3.2.1)  from https://www.raspberrypi.org/downloads/noobs/
$ uname -a
Linux raspberrypi 4.19.75+ #1270 Tue Sep 24 18:38:54 BST 2019 armv6l GNU/Linux

# STPE2: Screen installations

Make sure the Display page you refer is correct
Follow https://www.waveshare.com/wiki/3.2inch_RPi_LCD_(B)

The screen with botton requires orientation of 270 degrees 
From the above poge - 270 degree rotation

```
2.1 cd ~
2.2 git clone https://github.com/waveshare/LCD-show.git
2.3 cd LCD-show/
2.4 ./LCD32-show 270  ## for ILI9341, rotate 90 for vertical (pins on bottom)
2.5 sudo reboot
```
# For ILI9341 screen
```
3.1 create an xorg.conf.d folder
3.2 sudo mkdir /etc/X11/xorg.conf.d
3.3 copy file 40-libinput-conf to the folder which we created
3.4 sudo cp /usr/share/X11/xorg.conf.d/40-libinput.conf /etc/X11/xorg.conf.d/
3.5 Append a statement to touchscreen part of the file as below:
   	sudo nano /etc/X11/xorg.conf.d/40-libinput.conf	
3.6 Find Statement Identifier "libinput touchscreen catchall"
	Add under MatchIstouchscreen "on":
	Option "CalibrationMatrix" "-1 0 1 0 -1 1 0 0 1" ##this is for pins down
3.7 save, close, reboot (doesnt need to be calibrated from my experience)
```
# For ILI9341 60FPS #
```
3.8 cd /boot
3.9 sudo nano config.txt
3.10 Add on bottom: 
hdmi_force_hotplug=1 hdmi_cvt=320 240 60 1 0 0 0 hdmi_group=2 hdmi_mode=1 hdmi_mode=87 dtparam=spi=on dtoverlay=waveshare32b:rotate=90,speed=81000000,fps=60
3.11 Exit and save
```

# STEP3: Touch calibration (Optional, only need these in case of calibrarion)

Transformation matrix - 180 degree  -- reference - https://wavesharejfs.blogspot.com/2018/03/touch-rotating-for-waveshare-lcd-modify.html
[-1, 0, 1, 0, -1, 1, 0, 0, 1]: 180 degree

The following commands are required in addition to waveshare wiki instructions
```
3.1 sudo apt-get install xserver-xorg-input-evdev
3.2 sudo cp -rf /usr/share/X11/xorg.conf.d/10-evdev.conf /usr/share/X11/xorg.conf.d/45-evdev.conf
3.3 sudo reboot
```

Run calibration from Raspberry PI Start menu -> Accessories -> Calibration

4 Dots will be presented in the screen, touch these one by one. After the process, a data to be copied to a file(/usr/share/X11/xorg.conf.d/99-calibration.conf) will be printed. Copy these  

Edit the file /usr/share/X11/xorg.conf.d/99-calibration.conf and put out from the calibration tool.

```
4.4 sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf
```

See sample below

```
Section "InputClass"
	Identifier	"calibration"
	MatchProduct	"ADS7846 Touchscreen"
	Option  "Calibration" "258 3927 537 3813"
	Option	"MinX"	"61507"
	Option	"MaxX"	"1161"
	Option	"MinY"	"60301"
	Option	"MaxY"	"3322"
	Option	"SwapXY"	"0" # unless it was already set to 1
	Option	"InvertX"	"0"  # unless it was already set
	Option	"InvertY"	"0"  # unless it was already set
EndSection
```


# Step 4: Installation Notes

Image tested - Latest version (Noobs - 3.2.1)  from https://www.raspberrypi.org/downloads/noobs/
$ uname -a
Linux raspberrypi 4.19.75+ #1270 Tue Sep 24 18:38:54 BST 2019 armv6l GNU/Linux

Update the pi
```
4.1 sudo apt update
4.2 sudo apt full-upgrade
```

Install the libraries
```
4.3 sudo pip3 install adafruit-circuitpython-neopixel
4.4 sudo pip3 install dropbox
4.5 sudo apt-get install sqlite3
4.6 sudo apt-get install python3-pyqt5
4.7 sudo apt-get install qml-module-qtquick-controls
4.8 sudo apt-get install qml-module-qt-labs-folderlistmodel
```
# Step 5: Install keyboard
```

5.1 sudo apt-get install libfakekey-dev libpng-dev libxft-dev autoconf libtool -y
5.2 git clone https://github.com/mwilliams03/matchbox-keyboard.git
5.3 cd matchbox-keyboard
5.4 ./autogen.sh
5.5 make
5.6 sudo make install
5.7 sudo apt-get install libmatchbox1 -y

```

# Step 6: Disable Mouse
```
6.1 sudo apt-get install unclutter 
6.2 /usr/bin/unclutter -idle 1 -root 
6.3 sudo reboot 
```

# Step 7: Running the code 

```
7.1. git clone https://github.com/SensioSkin/LiveView
7.2. cd LiveView/web/Laburnum_Systems
7.3. pip3 install -r requirements.txt
```

```
7.5. Set your user id in the settings.py file 
```
"""The Photo To Cloud System Configuration file."""
nano settings.py
Edit the below line to match the UserID

USER_ID = '1'

Note: USER_ID of a particular user can be got from the header of web application after login. 
In the top right corner of the web application the user id is shown after hyphen symbol. For example, 
if dhanish - 1 is shown, means the UserID of user - 'dhanish' is '1'. So 1 should be put in settings.py 

If the code_1 directory is in /home/pi/, then use the following command (change path if code_1 is in different folder)

7.6 Change the url in the file settings.py file.
change URL to match the server URL (original)
```
URL = "https://www.laburnumsystems.com/phototocloud/download_json.php?table="
```
(new one assuming running in local network)
```
URL = "http://192.168.43.155:8000/download_json?table="
```
Note: In the above line replace 192.168.43.155:8000 with the server IP address and port. 

(If run if the webserver is runing in rpi itself, the internal IP 127.0.0.1 can be used.)
```
URL = "http://127.0.0.1:8000/download_json?table="
```

Important: The program should be running from the Raspberry pi desktop and not from the ssh terminal as this contains GUI application

```
7.4 cd LiveView/Code_1
7.5 python3 test_main.py fullscreen
```
# Step 8: Autostart (Do not use this, uncomment or remove entries from ~/.profile and proceed to Step 9)

Full path to the code is required for the below steps. This can be noted by the following command
8.1 cd Liveview/Code_1 
8.2 pwd

Open the ```~/.profile``` file  using the following command

8.3 geany ~/.profile


8.4 Add the following to the bottom of the file for autostart program and server

```
cd /home/pi/LiveView/Code_1   
sudo python3 test_main.py fullscreen &
/usr/bin/python3 /home/pi/LiveView/web/Laburnum_Systems/manage.py runserver 0.0.0.0:8000 &
```
Note: make sure the correct path of Code1 folder is used as argument of the "cd" command above


# step 9: Autostart using the lxsession

Full path to the code is required for the below steps. This can be noted by the following command
9.1 cd Liveview/Code_1 
9.2 pwd

Open the ```/etc/xdg/lxsession/LXDE-pi/autostart``` file  using the following command

9.3 sudo geany /etc/xdg/lxsession/LXDE-pi/autostart

9.4 Add the following to the bottom of the file 

```
@/usr/bin/python3 <full path to>/LiveView/web/Laburnum_Systems/manage.py runserver 0.0.0.0:8000
@sudo /usr/bin/python3 <full path to>/LiveView/Code_1/test_main.py fullscreen
```

IMPORTANT: for auto start use either the step8 or step9. Dont use both simultaneously.
NOTE: "&"" not required at the end

# Development instructions in host system  (optional for developers only)
For making UI changes
```
#1. sudo apt-get install python3-pyqt5  
#2. sudo apt-get install pyqt5-dev-tools
#3. sudo apt-get install qttools5-dev-tools
```
Edit the main.ui file in QT5 Designer aplication and save. 

Run the following commands with the updated UI file 
```
#4. pyrcc5 resource.qrc -o resource_rc.py
#5. pyuic5 mainUI.ui -o mainUI.py
```
Comment out GPIOs for high-speed screen
```
#1 sudo nano ~/LiveView/Code_1/light.py //line 170 near bottom
#2 change result=board.D12 to result=board.D18
#3 save/exit
#4 sudo nano ~/LiveView/Code_1/photo_to_cloud.py
#5 edit self.buzzer=5 to self.buzzer=25
#6 save/exit


```
