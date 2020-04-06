from PyQt5.QtCore import QThread, pyqtSignal, Qt, QTimer
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
import os
import sys
from picamera import PiCamera
import subprocess
import RPi.GPIO as GPIO
import datetime
from photo_to_cloud import PhotoToCloud
import ptc_database
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


class PhotoCloudThread(QThread):
    signal_rx = pyqtSignal('PyQt_PyObject')
    # signal_rx_call = pyqtSignal('PyQt_PyObject')
    signal_tx = pyqtSignal('PyQt_PyObject')

    def __init__(self, BASE_PATH, app_log, *args, **kwargs):
        QThread.__init__(self)
        self.signal_tx.connect(self.status_read)
        self.status = True
        self.start_time = datetime.now()
        self.app_log = app_log
        self.app_log.info("Initialising PhotoCloudThread ")
        self.BASE_PATH = BASE_PATH
        self.status = "status"

    def download_database(self):
        self.signal_rx.emit("Downloading settings...")
        flag = 0
        if(self.settings_database.download()):
            print("Downloading settings...")
            self.signal_rx.emit("Downloading settings...")
        else:
            flag = 1
            print("Downloading settings falied")
            self.signal_rx.emit("Downloading settings failed")

        if(self.sequences_database.download()):
            print("Downloading sequences...")
            self.signal_rx.emit("Downloading sequences...")
        else:
            flag = 1
            print("Downloading sequences failed ...")
            self.signal_rx.emit("Downloading sequences failed...")

        if(self.sequence_step_database.download()):
            print("Downloading sequence steps...")
            self.signal_rx.emit("Downloading sequence steps...")
        else:
            flag = 1
            print("Downloading sequence steps falied")
            self.signal_rx.emit("Downloading sequence steps failed")

        if(self.led_groups_database.download()):
            print("Downloading LED groups...")
            self.signal_rx.emit("Downloading LED groups...")
        else:
            flag = 1
            print("Downloading LED groups failed")
            self.signal_rx.emit("Downloading LED groups failed")

        if flag == 0:
            self.signal_rx.emit("Downloading completed")
        else:
            self.signal_rx.emit("Downloading failed")


    def check_internet(self):
        ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
            return True
        except subprocess.CalledProcessError:
            # grep did not match any lines
            return False

    def read_sequence_id(self):
        sequence_id = None
        try:
            f = open("{}".format(os.path.join(self.BASE_PATH, 'active_seq')), "r")
            sequence_id = int(f.read())
            f.close()
        except:
            pass
        return sequence_id

    def run(self, *args, **kwargs):
        # super(serialThread, self).run(*args, **kwargs)
        time_diff = 60
        time_diff_shudown = 10*60
        low_battery_pin = 26
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        count_down_poweroff = 5
        shutdown_status = False
        poweroff_status = False
        restart_status = False
        self.brightness= 0
        GPIO.setup(low_battery_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        prev_time = datetime.now()
        prev_time_shutdown = datetime.now()
        prev_updatetime = datetime.now()
        Prevtime_poweroff = datetime.now()
        prev_time_showtimer = datetime.now()
        self.phototocloud = PhotoToCloud(self.app_log)
        if (self.check_internet()):
            self.signal_rx.emit("connected")
        else:
            self.signal_rx.emit("disconnected")
        self.settings_database = ptc_database.SettingsDatabase(self.app_log)
        self.sequence_step_database = ptc_database.SequenceStepsDatabase(self.app_log)
        self.led_groups_database = ptc_database.LEDGroupsDatabase(self.app_log)
        self.sequences_database = ptc_database.SequencesDatabase(self.app_log)
        while (1):
            if self.status == "start":
                sequence_id = self.read_sequence_id()
                if sequence_id is not None:
                    print("file read sequnce", sequence_id)
                    print("Process started")
                    # steps = 10
                    steps = self.phototocloud.start_process(sequence_id)
                    print("total number of steself.brightnessps to process", steps)
                    for step in range(0, steps):
                        print(step, "started")
                        self.phototocloud.process_step(step,sequence_id,self.brightness)
                        self.signal_rx.emit(str(step))
                    self.phototocloud.stop_process()
                    self.signal_rx.emit("finished")
                    # self.phototocloud.short_beep()
                    # self.phototocloud.short_beep()
                    time.sleep(1)
                    self.signal_rx.emit("backtomaainpage")
                    self.status = "status"
            elif self.status == "exitfromapp":
                self.phototocloud.lights_all_off()
                self.status = "status"
                sys.exit(1)
            elif self.status == "turnofflight":
                self.phototocloud.lights_all_off()
                self.status = "status"

            elif self.status == "beepstart":
                self.phototocloud.beepstart()
                self.status = "status"

            elif self.status == "cancel":
                print("cancel signal got")
                poweroff_status = False
                restart_status = False
                count_down_poweroff = 5
                sent_data = "Action Cancelled by User"
                self.signal_rx.emit(sent_data)
                self.status = "status"
            elif self.status == "download":
                print("download")
                self.download_database()
                self.status = "status"
            elif self.status == "status":
                pass
            elif self.status == "poweroff":
                poweroff_status = True
                Prevtime_poweroff = datetime.now()
                count_down_poweroff = 5
                self.status = "status"
            elif self.status == "restart":
                restart_status = True
                Prevtime_poweroff = datetime.now()
                count_down_poweroff = 5
                self.status = "status"
            elif type(self.status) is str:
                if "brightness" in self.status:
                    s = self.status
                    self.brightness = int(s.split("=")[1])
                    print("birghtness value set",self.brightness)
                    self.status = "status"
            else:
                sequence_id = self.read_sequence_id()
                print("step for light source")
                self.phototocloud.led_step(int(self.status), sequence_id,self.brightness)                
                self.status = "status"

            if poweroff_status == True:
                poweroff_diff = datetime.now() - Prevtime_poweroff
                if poweroff_diff.total_seconds()>5:
                    self.phototocloud.lights_all_off()
                    print("sudo poweroff")
                    os.system("sudo poweroff")
                else:
                    hh = datetime.now() - prev_time_showtimer
                    if hh.total_seconds() > 1:
                        sent_data = "Shutting down in " + str(count_down_poweroff)
                        self.signal_rx.emit(sent_data)
                        prev_time_showtimer = datetime.now()
                        count_down_poweroff-=1

            if restart_status == True:
                poweroff_diff = datetime.now() - Prevtime_poweroff
                if poweroff_diff.total_seconds()>5:
                    self.phototocloud.lights_all_off()
                    print("sudo reboot")
                    os.system("sudo reboot")
                else:
                    hh = datetime.now() - prev_time_showtimer
                    if hh.total_seconds() > 1:
                        sent_data = "Restart in " + str(count_down_poweroff)
                        self.signal_rx.emit(sent_data)
                        prev_time_showtimer = datetime.now()
                        count_down_poweroff-=1



            current_time = datetime.now()
            diff_time = current_time - prev_time
            if (diff_time.total_seconds()) > time_diff:
                if (self.check_internet()):
                    self.signal_rx.emit("connected")
                else:
                    self.signal_rx.emit("disconnected")
                prev_time = current_time


            low_battery_pin_value = GPIO.input(low_battery_pin)
            if (low_battery_pin_value == GPIO.LOW):
                if shutdown_status == False:
                    shutdown_status = True
                    prev_time_shutdown = datetime.now()
                else:
                    ss = datetime.now() - prev_time_shutdown
                    if (ss.total_seconds()) > time_diff_shudown:
                        self.phototocloud.stop_process()
                        os.system("sudo poweroff")
                    dd = datetime.now() - prev_updatetime
                    if dd.total_seconds() >15:
                        timeremaining = time_diff_shudown - ss.total_seconds()
                        sent_data = "Low Battery " + str(int(timeremaining))
                        self.signal_rx.emit(sent_data)
                        prev_updatetime = datetime.now()
            else:
                # self.signal_rx.emit("full mode")
                prev_time_shutdown = datetime.now()
                shutdown_status = False
            self.msleep(100)



    def status_read(self, data):
        # print("got rx data ", data)
        self.status = data
        print("type of the data",type(self.status))







