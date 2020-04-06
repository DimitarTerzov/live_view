"""Module responsible for the loading and setting of the light sequence"""
# pylint: disable=line-too-long,no-member,broad-except,too-many-instance-attributes
import neopixel
import board
import time

OFF = 0
RED = 1
AMBER = 2
GREEN = 3


class Lights():
    """Module responsible for the loading and setting of the light sequence"""
    def __init__(self, application_log, sequence_step_database, settings_database, led_groups_database):
        """Initialization of the light sequence class including loading the light sequence and initialising the Neopixels"""
        try:
            self.app_log = application_log

            self.initialised = False
            self.app_log.info("Initialising lights")

            self.last_status = None
            self.settings_database = settings_database
            self.led_groups_database = led_groups_database

            self.status_light_index = int(self.settings_database.get_setting('status_light_index'))

            status_light_brightness = int(self.settings_database.get_setting('status_light_brightness'))

            #green
            self.adjusted_255 = 255 * status_light_brightness
            self.adjusted_255 = int(round(self.adjusted_255/100))

            self.adjusted_40 = 40 * status_light_brightness
            self.adjusted_40 = int(round(self.adjusted_40/100))

            neopixel_gpio = self.get_neopixel_gpio()
            number_of_neopixels = int(self.settings_database.get_setting('number_of_neopixels'))
            self.neopixel_order = self.get_neopixel_order()
            # self.neopixel_order = neopixel.GRB

            print("neopixel_gpio: ", neopixel_gpio)
            print("neopixel_order: ", self.neopixel_order)

            self.pixels = neopixel.NeoPixel(neopixel_gpio, number_of_neopixels, auto_write=True, pixel_order=self.neopixel_order)
            # self.pixels[0] = (255, 0, 0, 0)
            # time.sleep(1)

            # self.pixels[1] = (0, 255, 0, 0)
            # time.sleep(1)

            # self.pixels[2] = (0, 0, 255, 0)
            # time.sleep(1)
            # print("neopixrel testing")

            self.sequence_step_database = sequence_step_database

            self.app_log.info("Lights initialised")
            self.initialised = True

        except Exception as exception:
            print("Exception : ", exception)
            self.app_log.info("Failed to initialise lights")
            self.app_log.exception('Exception: %s', exception)

    def set_status(self, status):
        """Set the NeoPixels status light"""
        if self.last_status == status:
            return True

        try:
            if status == OFF:
                self.pixels[self.status_light_index] = (0, 0, 0, 0)
                self.app_log.info("Set status light to off")
            else:
                if self.neopixel_order == neopixel.RGBW:
                    if status == GREEN:
                        self.pixels[self.status_light_index] = (self.adjusted_255, 0, 0, 0)
                        self.app_log.info("Set status light to green")
                    elif status == AMBER:
                        self.pixels[self.status_light_index] = (self.adjusted_40, self.adjusted_255, 0, 0)
                        self.app_log.info("Set status light to amber")
                    elif status == RED:
                        self.pixels[self.status_light_index] = (0, self.adjusted_255, 0, 0)
                        self.app_log.info("Set status light to red")
                else:
                    if status == GREEN:
                        self.pixels[self.status_light_index] = (0, self.adjusted_255, 0, 0)
                        self.app_log.info("Set status light to green")
                    elif status == AMBER:
                        self.pixels[self.status_light_index] = (self.adjusted_255, self.adjusted_40, 0, 0)
                        self.app_log.info("Set status light to amber")
                    elif status == RED:
                        self.pixels[self.status_light_index] = (self.adjusted_255, 0, 0, 0)
                        self.app_log.info("Set status light to red")
            self.last_status = status
            return True
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
            return False

    #Note: zero based light sequence
    def set_sequence_step(self, step,sequence_id,bright_value):
        """Set the NeoPixels to the step"""
        print("set_sequence_step ",bright_value)
        try:
            if step > self.sequence_step_database.get_sequence_step_count_seq(sequence_id):
                return
            print("collecting the rgb data for step {} and sequence {}".format(step, sequence_id))
            red, green, blue, white, led_group_id = self.sequence_step_database.get_sequence_step_lighting_seq(step,sequence_id)
            print("datas rgb are")
            print(red, green, blue, white, led_group_id)

            # white = int(white + white*bright_value/100)
            print("updated white ",white)
            #set the lights per the pattern step
            light_addresses = self.led_groups_database.get_light_addresses(led_group_id)
            self.neopixel_order = self.get_neopixel_order()
            print("light address",light_addresses)
            for address in range(0, 12):
                # print("address ", address)
                if address in light_addresses:
                    if self.neopixel_order == neopixel.RGBW:
                        print("self.neopixel_order == neopixel.RGBW:", red, green, blue, white)
                        self.pixels[address] = (green, red, blue, white)
                    elif self.neopixel_order == neopixel.GRBW:
                        print("self.neopixel_order == GRBW:", red, green, blue, white)
                        self.pixels[address] = (red, green, blue, white)
                    else:
                        print("self.neopixel_order == else", red, green, blue)
                        self.pixels[address] = (red, green, blue)
                else:
                    # print("self.neopixel_order == all zeros:")
                    if self.neopixel_order == neopixel.GRB:
                        self.pixels[address] = (0, 0, 0)
                    else: 
                        self.pixels[address] = (0, 0, 0, 0)
        except Exception as exception:
            print("Exception ", exception)
            self.app_log.exception('Exception: %s', exception)

    def get_neopixel_order(self):
        """Get the NeoPixels order from the database and translate to the constants"""
        result = None

        if self.settings_database.get_setting('neopixel_order') == "rgbw":
            self.app_log.info("neopixel_order:rgbw")
            result = neopixel.RGBW
        elif self.settings_database.get_setting('neopixel_order') == "grbw":
            self.app_log.info("neopixel_order:grbw")
            result = neopixel.GRBW

        return result

    def get_neopixel_gpio(self):
        """Get the NeoPixels GPIO from the database and translate to the constants"""
        #NeoPixels must be connected to GPIO10, GPIO12, GPIO18 or GPIO21 to work! GPIO18 is the standard pin.
        result = None

        # if self.settings_database.get_setting('neopixel_gpio') == "GPIO20":
        #     result = board.D20
        # elif self.settings_database.get_setting('neopixel_gpio') == "GPIO26":
        #     result = board.D26
        # elif self.settings_database.get_setting('neopixel_gpio') == "GPIO16":
        #     result = board.D16
        # elif self.settings_database.get_setting('neopixel_gpio') == "GPIO21":
        #     result = board.D21
        # else:
        result = board.D18

        return result

    def set_all_off(self):
        """set all assigned addresses off"""
        try:
            for address in range(12):
                self.pixels[address] = (0, 0, 0, 0)
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
