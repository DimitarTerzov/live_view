"""Top level application module for the Photo To Cloud System."""
# pylint: disable=line-too-long,no-member,broad-except,too-many-instance-attributes

import time
from time import sleep
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from subprocess import call
import RPi.GPIO as GPIO
import ptc_camera
import lights
import ptc_database

class PhotoToCloud():
    """Top level application class for the Photo To Cloud System."""

    def __init__(self, app_log):
        """Initializes the Photo To Cloud System."""
        try:
            self.processing = False
            self.start_time = datetime.now()

            self.app_log = app_log
            self.app_log.info("Initialising PhotoToCloud ")

            #initiate the database
            self.settings_database = ptc_database.SettingsDatabase(self.app_log)
            self.sequence_step_database = ptc_database.SequenceStepsDatabase(self.app_log)
            self.led_groups_database = ptc_database.LEDGroupsDatabase(self.app_log)

            #Setup the IO
            self.app_log.info("setting up IO")
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)

            #########
            # self.buzzer = int(self.settings_database.get_setting('buzzer_gpio'))
            # self.switch = int(self.settings_database.get_setting('switch_gpio'))
            # self.app_log.info("Shutter GPIO = %s", self.switch)
            # self.shut_down = int(self.settings_database.get_setting('shutdown_gpio'))
            # self.status_light = int(self.settings_database.get_setting('status_light_index'))
            #########
            self.buzzer = 25
            # self.switch = 6
            # self.shut_down =
            GPIO.setup(self.buzzer, GPIO.OUT)
            # GPIO.setup(self.switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            # GPIO.setup(self.shut_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            #########

            # self.camera = ptc_camera.PTCCamera(self.app_log, self.sequence_step_database, self.settings_database)
            self.lights = lights.Lights(self.app_log, self.sequence_step_database, self.settings_database, self.led_groups_database)

            self.app_log.info("Init time is %d ms", self.millis())

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
        finally:
            success = True
            if not self.lights.initialised:
                success = False

            # if not self.camera.initialised:
            #     success = False

            if success:
                self.lights.set_status(lights.GREEN)
            else:
                self.lights.set_status(lights.RED)

    def millis(self):
        """Calculate the milliseconds"""
        datetime_difference = datetime.now() - self.start_time
        return (datetime_difference.days * 24 * 60 * 60 + datetime_difference.seconds) * 1000 + datetime_difference.microseconds / 1000.0

    def start_process(self,sequence_id):
        print("starting process")
        self.short_beep()
        self.short_beep()
        self.short_beep()
        self.camera = ptc_camera.PTCCamera(self.app_log, self.sequence_step_database, self.settings_database)
        sequence_step_count = self.sequence_step_database.get_sequence_step_count_seq(sequence_id)
        self.lights.set_status(lights.OFF)
        # print("ddddddddddddddd",sequence_step_count)
        return sequence_step_count

    def stop_process(self):
        print("stopping process")
        self.lights.set_all_off()
        # self.lights.set_status(lights.GREEN)
        del self.camera
        self.short_beep()
        self.short_beep()

    def lights_all_off(self):
        print("stopping process")
        self.lights.set_all_off()
        # self.lights.set_status(lights.GREEN)
        # del self.camera
        # self.short_beep()
        # self.short_beep()

    def process_step(self,step,sequence_id,bright_value):
        """Iterates through each step in the sequence, setting up the lighting and taking the picture."""
        try:
            print("Sequence selected", sequence_id)
            print("process step function started",bright_value)
            if self.processing:
                return
            self.lights.set_status(lights.OFF)
            self.app_log.info("process_step: %d", step)
            self.lights.set_sequence_step(step,sequence_id,bright_value)
            self.camera.take_picture(step,sequence_id)

        except Exception as exception:
            self.app_log.exception('process_step Exception: %s', exception)

    def led_step(self,step,sequence_id, bright_value):
        """Iterates through each step in the sequence, setting up the lighting and taking the picture."""
        try:
            print("led step started",bright_value)
            # self.app_log.info("Checking processing status")

            # self.app_log.info("Not already processing, proceeding...")
            self.short_beep()

            self.lights.set_status(lights.OFF)
            self.app_log.info("step: %d", step)
            self.lights.set_sequence_step(step,sequence_id,bright_value)
            # self.short_beep()
            # self.short_beep()

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def beepstart(self):
        self.short_beep()
        self.short_beep()
        # self.short_beep()

    def process(self):
        """Iterates through each step in the sequence, setting up the lighting and taking the picture."""
        if self.processing:
            print("Already  process running")
            return

        print("Running process")
        try:
            self.app_log.info("Checking processing status")


            self.app_log.info("Not already processing, proceeding...")
            self.processing = True
            self.short_beep()

            self.camera = ptc_camera.PTCCamera(self.app_log, self.sequence_step_database, self.settings_database)

            sequence_step_count = self.sequence_step_database.get_sequence_step_count()

            self.app_log.info("Starting sequence - total step count is %d", sequence_step_count)

            # self.lights.set_status(lights.OFF)

            for step in range(sequence_step_count):
                print("running step ", step)
                self.app_log.info("step: %d", step)
                # self.lights.set_sequence_step(step)
                self.camera.take_picture(step)

            # self.lights.set_all_off()
            # self.lights.set_status(lights.GREEN)
            del self.camera

            self.short_beep()
            self.short_beep()

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
        finally:
            self.processing = False
        print("process finished")

    # def process_loop(self):
    #     """Top level Loop which checks for shutter switch press and triggers the processing."""
    #     try:
    #         print("process loop step started")
    #         start_time = None
    #         called = False
    #
    #         while True: # Run forever
    #             if GPIO.input(self.switch) == GPIO.LOW:
    #                 self.app_log.info("pressed")
    #                 self.process()
    #
    #             if not GPIO.input(self.shut_down) and start_time is None:
    #                 start_time = time.time()
    #
    #             if GPIO.input(self.shut_down):
    #                 start_time = None
    #
    #             if not GPIO.input(self.shut_down) and start_time is not None:
    #                 time_elapsed = time.time() - start_time
    #                 if time_elapsed >= 3 and not called:
    #                     called = True
    #                     self.lights.set_status(lights.OFF)
    #                     call("sudo nohup shutdown -h now", shell=True)
    #
    #             if not called:
    #                 if start_time is None:
    #                     self.lights.set_status(lights.GREEN)
    #                 else:
    #                     self.lights.set_status(lights.AMBER)
    #                     time.sleep(0.1)
    #                     self.lights.set_status(lights.OFF)
    #                     time.sleep(0.1)
    #
    #             sleep(0.1)
    #
    #     except Exception as exception:
    #         self.app_log.exception('Exception: %s', exception)
    #
    #     except KeyboardInterrupt:
    #         GPIO.cleanup() # resets all GPIO ports used by this program self.processing = False self.set_ready(True)

    def short_beep(self):
        """Provides a short beep from the buzzer."""
        GPIO.output(self.buzzer, 1)             # set BUZZER to 1/GPIO.HIGH/True
        sleep(0.2)                             # wait a split second
        GPIO.output(self.buzzer, 0)             # set BUZZER to 1/GPIO.HIGH/True
        sleep(0.2)

# if __name__ == '__main__':
#     PhotoToCloud().start_process()
