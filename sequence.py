"""Module responsible for the loading and setting of the light sequence"""

import ptc_database

class Sequence():
    """Class responsible for the loading and setting of the light sequence"""

    def __init__(self, application_log):
        self.app_log = application_log
        self.sequence_databases = ptc_database.SequenceDatabases(self.app_log)
        self.sequence_databases.download()

        self.green = 0
        self.red = 1
        self.blue = 2
        self.white = 3
        self.exposure_mode = 4
        self.awb_mode = 5
        self.image_effect = 6
        self.iso = 7
        self.shutter_speed = 8
        self.brightness = 9
        self.saturation = 10
        self.led_brightness = 11
        self.contrast = 12
        self.exposure_compensation = 13

    def get_selected_sequence(self):
        """Get which sequence to use"""
        return  self.sequences_db.get_active()

    def get_sequence_step_count(self):
        """Get how many steps are in the sequence"""
        return 

    def get_sequence_data(self):
        """Get the data for a specific step"""
        return self.sequence_dictionary[self.get_selected_sequence()]

    def get_sequence_step_data(self, step):
        """Get the data for a specific step"""
        return self.sequence_dictionary[self.get_selected_sequence()][step]
