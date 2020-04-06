"""Database  module for the Photo To Cloud System."""
# pylint: disable=line-too-long,no-member,broad-except,invalid-name
import os
import sqlite3
import urllib.request
import json
import logging
from logging.handlers import RotatingFileHandler
import settings

class PTCDatabase():
    """Database class for the Photo To Cloud System."""
    def __init__(self, table_name, application_log):
        """Initialization of logging and the database"""

        self.BASE_PATH = os.path.dirname(os.path.realpath(__file__))

        self.app_log = application_log
        self.app_log.info("Initialising PTC database - " + table_name)
        self.table_name = table_name
        self.data_dictionary = None
        self.field_list = ""
        self.value_list = ""
        self.url = settings.URL + self.table_name + "&user_id=" + settings.USER_ID

        # self.url = "https://www.laburnumsystems.com/phototocloud/download_json.php?table=" + self.table_name + "&user_id=" + settings.USER_ID
        self.conn = None

        try:
            # self.conn = sqlite3.connect("/home/pi/Desktop/code_1/ptc.db")
            self.conn = sqlite3.connect("{}".format(os.path.join(self.BASE_PATH, 'ptc.db')))
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def set_field_list(self, field_list):
        """ set the field list """
        self.field_list = field_list

    def set_value_list(self, value_list):
        """ set the value list """
        self.value_list = value_list

    def select_all_rows(self):
        """ Query all rows in the settings table """
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM " + self.table_name)

            rows = cur.fetchall()

            for row in rows:
                self.app_log.info(row)

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def delete_all_rows(self):
        """ delete all the settings table """
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE from " + self.table_name)
            self.conn.commit()
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def insert_row(self, new_row):
        """ update the settings table """
        try:
            print("inserting rows")
            cur = self.conn.cursor()
            cur.execute("INSERT INTO " + self.table_name  + " (" + self.field_list + ") VALUES (" + self.value_list + ")", new_row)
            self.conn.commit()
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def get_data_from_www(self):
        """Get the data from the Web"""
        try:
            self.app_log.info("Getting data from WWW for " + self.table_name + " for user_id " + settings.USER_ID)
            with urllib.request.urlopen(self.url) as response:
                aa = (response.read())
                self.data_dictionary = json.loads(aa.decode('utf-8'))
                self.app_log.info("Done!")
                return True
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def __del__(self):
        """Destructor - close the connection to the database"""
        try:
            self.conn.close()
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

class SettingsDatabase(PTCDatabase):
    """Class for handling the settings database"""
    def __init__(self, application_log):
        """Initialise the settings database object"""
        super(SettingsDatabase, self).__init__("settings", application_log)
        self.set_field_list("`id`, `name`, `value`")
        self.set_value_list("?,?,?")

    def download(self):
        """Download the data and insert into the database"""
        try:
            download_result = self.get_data_from_www()
            data_len = len(self.data_dictionary[self.table_name])
            self.app_log.info("Data length is - " + str(data_len))

            if (download_result and data_len > 0):
                self.delete_all_rows()
                for counter in range(0, data_len):
                    new_row = (self.data_dictionary[self.table_name][counter]['id'], self.data_dictionary[self.table_name][counter]['name'], self.data_dictionary[self.table_name][counter]['value'])
                    self.insert_row(new_row)
                self.select_all_rows()
                return True
            else:
                self.app_log.info("Unable to get data from internet")
                return False
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
            return False

    def get_setting(self, field):
        """ get setting from the dictionary """
        try:
            cur = self.conn.cursor()
            sql = "SELECT value FROM " + self.table_name + " where name = '" + field + "'"
            cur.execute(sql)
            rows = cur.fetchone()
            return rows[0]
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

class LEDGroupsDatabase(PTCDatabase):
    """Class for handling the LED groups database table"""
    def __init__(self, application_log):
        """ Initialise the LED groups database """
        super(LEDGroupsDatabase, self).__init__("led_groups", application_log)
        self.set_field_list("led_group_id, name, active, led_0, led_1, led_2, led_3, led_4, led_5, led_6, led_7, led_8, led_9, led_10, led_11")
        self.set_value_list("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")

    def download(self):
        """ download the data and insert it into the database """
        try:
            self.get_data_from_www()
            data_len = len(self.data_dictionary[self.table_name])
            self.app_log.info("Data length is - " + str(data_len))

            self.delete_all_rows()
            for counter in range(0, data_len):
                new_row = (self.data_dictionary[self.table_name][counter]['led_group_id'], self.data_dictionary[self.table_name][counter]['name'], self.data_dictionary[self.table_name][counter]['active'],
                           self.data_dictionary[self.table_name][counter]['led_0'], self.data_dictionary[self.table_name][counter]['led_1'], self.data_dictionary[self.table_name][counter]['led_2'],
                           self.data_dictionary[self.table_name][counter]['led_3'], self.data_dictionary[self.table_name][counter]['led_4'], self.data_dictionary[self.table_name][counter]['led_5'],
                           self.data_dictionary[self.table_name][counter]['led_6'], self.data_dictionary[self.table_name][counter]['led_7'], self.data_dictionary[self.table_name][counter]['led_8'],
                           self.data_dictionary[self.table_name][counter]['led_9'], self.data_dictionary[self.table_name][counter]['led_10'], self.data_dictionary[self.table_name][counter]['led_11'])
                self.insert_row(new_row)

            self.select_all_rows()
            return True
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
            return False

    def get_light_addresses(self, led_group_id):
        """ get light addresses from the database """
        try:
            cur = self.conn.cursor()
            sql = "SELECT " + self.field_list + " FROM " + self.table_name + " where led_group_id = " + led_group_id
            cur.execute(sql)
            rows = cur.fetchall()
            leds = []
            for counter in range(3, 15):
                if rows[0][counter] == '1':
                    leds.append(counter-3)
            return leds

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def get_led_group_name(self,led_group_id):
        try:
            cur = self.conn.cursor()
            sql = "SELECT " + self.field_list + " FROM " + self.table_name + " where led_group_id = " + led_group_id
            cur.execute(sql)
            rows = cur.fetchall()
            return rows[0][1]
        except Exception as exception:
            print("excepitony", exception)
            self.app_log.exception('Exception: %s', exception)


class SequencesDatabase(PTCDatabase):
    """Class for handling the Sequences database table"""
    def __init__(self, application_log):
        super(SequencesDatabase, self).__init__("sequences", application_log)
        self.set_field_list("'sequence_id', 'name'")
        self.set_value_list("?,?")

    def download(self):
        """ download the data and insert it into the database """
        try:
            self.get_data_from_www()
            data_len = len(self.data_dictionary[self.table_name])
            self.app_log.info("Data length is - " + str(data_len))


            self.delete_all_rows()
            for counter in range(0, data_len):
                new_row = (self.data_dictionary[self.table_name][counter]['sequence_id'], self.data_dictionary[self.table_name][counter]['name'])
                self.insert_row(new_row)
                active_sequence_id = self.data_dictionary[self.table_name][0]['sequence_id']
            self.select_all_rows()
            # return active_sequence_id
            return True
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
            return False

    def get_active_sequence_id(self):
        """ get the active sequence id from the database """
        try:
            cur = self.conn.cursor()
            sql = "SELECT sequence_id FROM " + self.table_name
            cur.execute(sql)
            rows = cur.fetchone()
            return rows[0]

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def get_active_sequence_name(self,sequence_id):
        """get the name of the active sequence"""
        try:
            cur = self.conn.cursor()
            sql = "SELECT name FROM " + self.table_name + " where sequence_id =  " + str(sequence_id)
            cur.execute(sql)
            rows = cur.fetchone()
            return rows[0]
        except Exception as exception:
            print("Exception ", exception)
            self.app_log.exception('Exception: %s', exception)

    def get_all_sequences(self):
        sequences = []
        """get the name of the active sequence"""
        try:
            cur = self.conn.cursor()
            sql = "SELECT * FROM " + self.table_name
            cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                print(row)
                sequences.append({'id':row[0], 'name': row[1]})
            return sequences

        except Exception as exception:
            print("Exception ", exception)
            self.app_log.exception('Exception: %s', exception)
            return []

class SequenceStepsDatabase(PTCDatabase):
    """Class for handling the Sequence Steps database table"""
    id = 0
    sequence_id = 1
    step_id = 2
    color = 3
    white = 4
    led_group_id = 5
    exposure_mode = 6
    awb_mode = 7
    iso = 8
    shutter_speed = 9
    brightness = 10
    saturation = 11
    led_brightness = 12
    contrast = 13

    def __init__(self, application_log):
        """ Initialise the  Sequence steps database object"""
        super(SequenceStepsDatabase, self).__init__("sequence_steps", application_log)
        self.set_field_list("id, sequence_id, step_id, color, white, led_group_id, exposure_mode, awb_mode, iso, shutter_speed, brightness, saturation, led_brightness, contrast")
        self.set_value_list("?,?,?,?,?,?,?,?,?,?,?,?,?,?")
        self.sequences_database = SequencesDatabase(self.app_log)

    def download(self):
        """ download the data and insert it into the database """
        self.get_data_from_www()
        try:
            data_len = len(self.data_dictionary[self.table_name])
            self.app_log.info("Data length is - " + str(data_len))

            self.delete_all_rows()
            for counter in range(0, data_len):
                new_row = (self.data_dictionary[self.table_name][counter]['id'], self.data_dictionary[self.table_name][counter]['sequence_id'], self.data_dictionary[self.table_name][counter]['step_id'],
                           self.data_dictionary[self.table_name][counter]['color'], self.data_dictionary[self.table_name][counter]['white'], self.data_dictionary[self.table_name][counter]['led_group_id'],
                           self.data_dictionary[self.table_name][counter]['exposure_mode'], self.data_dictionary[self.table_name][counter]['awb_mode'], self.data_dictionary[self.table_name][counter]['iso'],
                           self.data_dictionary[self.table_name][counter]['shutter_speed'], self.data_dictionary[self.table_name][counter]['brightness'], self.data_dictionary[self.table_name][counter]['saturation'],
                           self.data_dictionary[self.table_name][counter]['led_brightness'], self.data_dictionary[self.table_name][counter]['contrast'])
                self.insert_row(new_row)
            self.select_all_rows()
            return True
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)
            return False

    def get_sequence_step_count(self):
        """ get sequence step count """
        try:
            cur = self.conn.cursor()
            sql = "SELECT count(*) FROM " + self.table_name
            cur.execute(sql)
            rows = cur.fetchone()
            return rows[0]
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def get_sequence_step_count_seq(self,sequence_id):
        """ get sequence step count """
        try:
            cur = self.conn.cursor()
            sql = "SELECT count(*) FROM " + self.table_name + " where sequence_id =  " + str(sequence_id)
            cur.execute(sql)
            rows = cur.fetchone()
            return rows[0]
        except Exception as exception:
            print(exception)
            self.app_log.exception('Exception: %s', exception)



    def get_sequence_step_data(self, step):
        """ get sequence step data """
        try:
            cur = self.conn.cursor()
            sql = "SELECT " +  self.field_list + " FROM " + self.table_name
            cur.execute(sql)
            rows = cur.fetchall()
            return rows[step]
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def get_sequence_step_data_seq(self, step, sequence_id):
        """ get sequence step data """
        try:
            cur = self.conn.cursor()
            sql = "SELECT " +  self.field_list + " FROM " + self.table_name + " where sequence_id =  " + str(sequence_id)
            cur.execute(sql)
            rows = cur.fetchall()
            return rows[step]
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def get_sequence_step_lighting(self, step):
        """ get sequence step lighting """

        try:
            cur = self.conn.cursor()
            sql = "SELECT * FROM " + self.table_name
            cur.execute(sql)
            rows = cur.fetchall()

            led_group_id = rows[step][5]

            colors = rows[step][3].lstrip('#')
            red = int(colors[0:2], 16)
            green = int(colors[2:4], 16)
            blue = int(colors[4:6], 16)
            white = int(rows[step][4])

            led_brightness = int(rows[step][12])

            self.app_log.info("RGBW = (%d, %d, %d, %d)", red, green, blue, white)
            self.app_log.info("led_brightness = %d", led_brightness)

            red = red * led_brightness
            red = int(round(red/100))

            green = green * led_brightness
            green = int(round(green/100))

            blue = blue * led_brightness
            blue = int(round(blue/100))

#           white = white * led_brightness
#           white = int(round(white/100))

            self.app_log.info("Adjusted RGBW = (%d, %d, %d, %d)", red, green, blue, white)

            return red, green, blue, white, led_group_id

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def get_sequence_step_lighting_seq(self, step, sequence_id):
        """ get sequence step lighting """

        try:
            cur = self.conn.cursor()
            sql = "SELECT * FROM " + self.table_name + " where sequence_id =  " + str(sequence_id)
            cur.execute(sql)
            rows = cur.fetchall()


            led_group_id = rows[step][5]

            colors = rows[step][3].lstrip('#')
            red = int(colors[0:2], 16)
            green = int(colors[2:4], 16)
            blue = int(colors[4:6], 16)
            white = int(rows[step][4])

            led_brightness = int(rows[step][12])

            self.app_log.info("RGBW = (%d, %d, %d, %d)", red, green, blue, white)
            # print("RGBW = (%d, %d, %d, %d)", red, green, blue, white)
            self.app_log.info("led_brightness = %d", led_brightness)
            # print("led_brightness = %d", led_brightness)

            red = red * led_brightness
            red = int(round(red/100))

            green = green * led_brightness
            green = int(round(green/100))

            blue = blue * led_brightness
            blue = int(round(blue/100))

 #          white = white * led_brightness
 #          white = int(round(white/100))

            self.app_log.info("Adjusted RGBW = (%d, %d, %d, %d)", red, green, blue, white)

            return red, green, blue, white, led_group_id

        except Exception as exception:
            print(exception)
            self.app_log.exception('Exception: %s', exception)

    def get_led_group_id(self, step, sequence_id):
        try:
            cur = self.conn.cursor()
            sql = "SELECT * FROM " + self.table_name + " where sequence_id =  " + str(sequence_id)
            cur.execute(sql)
            rows = cur.fetchall()
            led_group_id = rows[step][5]
            return led_group_id
        except Exception as exception:
            print(exception)
            self.app_log.exception('Exception: %s', exception)




if __name__ == '__main__':
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
    my_handler = RotatingFileHandler('/home/pi/Desktop/code_1/logs/photo_to_cloud.log', mode='a', maxBytes=5*1024*1024, backupCount=1, encoding=None, delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)
    app_log = logging.getLogger('root')
    app_log.setLevel(logging.INFO)
    app_log.addHandler(my_handler)

    # sequences_database = SequencesDatabase(app_log)
    # print(sequences_database.get_all_sequences())

    # #initiate the database
    # print("Downloading settings...")
    # settings_database = SettingsDatabase(app_log)
    # settings_database.download()
    #
    # print("Downloading sequences...")
    # sequences_database = SequencesDatabase(app_log)
    # sequences_database.download()
    #
    # print("Downloading sequence steps...")
    # sequence_step_database = SequenceStepsDatabase(app_log)
    # # get_sequence_step_count_seq
    # sequence_step_database.get_sequence_step_lighting_seq(135,1)
    # print(sequence_step_database.get_sequence_step_data_seq(2,135))
    # s = (sequence_step_database.get_sequence_step_count_seq(135))
    # for i in range(0,s):
    #     print(i)
    #
    # print("Downloading LED groups...")
    # led_groups_database = LEDGroupsDatabase(app_log)
    # led_groups_database.download()
    #
    # print("Downloading completed, please check log for full details.")

    # initiate the database
    # print("Downloading settings...")
    # settings_database = SettingsDatabase(app_log)
    # settings_database.download()
    # # ss = (settings_database.get_setting("color_effects"))
    # # print(ss)
    #
    # print("Downloading sequences...")
    # sequences_database = SequencesDatabase(app_log)
    # sequences_database.download()
    #
    # print("Downloading sequence steps...")
    sequence_step_database = SequenceStepsDatabase(app_log)
    led_id = (sequence_step_database.get_led_group_id(2,6))
    # sequence_step_database.download()
    #
    # print("Downloading LED groups...")
    led_groups_database = LEDGroupsDatabase(app_log)
    print(led_groups_database.get_led_group_name(led_id))
    # red, green, blue, white, led_group_id = sequence_step_database.get_sequence_step_lighting_seq(step,sequence_id)

    # led_groups_database.download()
    # led_groups_database.get_light_addresses(led_group_id)


    print("Downloading completed, please check log for full details.")
