from PyQt5.QtCore import QThread, pyqtSignal, Qt, QTimer
import time
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
import time
import os
from picamera import PiCamera
import subprocess
import datetime
import ptc_database
import logging

class pin_status(QThread):
    signal_rx = pyqtSignal('PyQt_PyObject')
    # signal_rx_call = pyqtSignal('PyQt_PyObject')
    signal_tx = pyqtSignal('PyQt_PyObject')
    def __init__(self, app_log,*args, **kwargs):
        QThread.__init__(self)
        self.app_log = app_log
        self.settings_database = ptc_database.SettingsDatabase(self.app_log)
        self.signal_tx.connect(self.pin_read)
        self.status = ""
        self.camera = PiCamera()
        self.camera.resolution = (320, 240)
        self.camera.rotation = int(self.settings_database.get_setting('rotation'))
        self.camera.start_preview()
        self.brightness = 50
        # GPIO.setwarnings(False)
        # GPIO.setmode(GPIO.BCM)
        # self.switch1 = 18
        # self.switch2 = 23
        # self.switch3 = 24
        # GPIO.setup(self.switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.switch2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.switch3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def run(self, *args, **kwargs):
        # super(serialThread, self).run(*args, **kwargs)
        self.settings_database1 = ptc_database.SettingsDatabase(self.app_log)
        lastswitch1 = 1
        lastswitch2 = 1
        lastswitch3 = 1
        while(1):
            # switch1_value = GPIO.input(self.switch1)
            # switch2_value = GPIO.input(self.switch2)
            # switch3_value = GPIO.input(self.switch3)
            # if (switch1_value == GPIO.LOW and lastswitch1 == 1):
            #     self.signal_rx.emit('1')            #
            # if (switch2_value == GPIO.LOW and lastswitch2 == 1):
            #     self.signal_rx.emit('2')
            # if (switch3_value == GPIO.LOW and lastswitch3 == 1):
            #     self.signal_rx.emit('3')

            # lastswitch1 = switch1_value
            # lastswitch2 = switch2_value
            # lastswitch3 = switch3_value

            if self.status == "start":
                print("started")
                try:
                    self.camera = PiCamera()
                    self.camera.resolution = (320, 240)
                    self.camera.rotation = int(self.settings_database1.get_setting('rotation'))
                    print("pin_status:", int(self.settings_database1.get_setting('rotation')))
                    # self.camera.brightness = self.brightness
                    self.camera.start_preview()
                except:
                    pass
                self.status = "ok"
            elif self.status == "stop":
                print("stopeed")
                try:
                    self.camera.close()
                    self.signal_rx.emit('stopped')
                    print("camera stopped and signal emitted")
                except Exception as e:
                    print("Exception at camera close : ", e)
                self.status = "ok"
            elif "brightness" in self.status:
                s = self.status
                self.brightness = int(s.split("=")[1])
                print("birghtness123 value set",self.brightness)
                self.status = "ok"

            self.msleep(200)
            # print("iiii")
            # self.signal_rx.emit(str(cnt))

    def pin_read(self, data):
        print(data)
        self.status = data