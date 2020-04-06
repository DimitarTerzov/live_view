"""Module responsible for uploading files to the cloud"""
# pylint: disable=line-too-long,no-member,broad-except

import os
import time
import logging
from logging.handlers import RotatingFileHandler
import dropbox
import ptc_database

SLEEP_TIME = 1

class UploadFiles(object):
    """Class responsible for uploading files to the cloud"""
    def __init__(self):
        self.log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

        self.my_handler = RotatingFileHandler('/home/pi/Desktop/code_1/logs/upload_files.log', mode='a', maxBytes=5*1024*1024, backupCount=1, encoding=None, delay=0)
        self.my_handler.setFormatter(self.log_formatter)
        self.my_handler.setLevel(logging.INFO)

        self.app_log = logging.getLogger('root')
        self.app_log.setLevel(logging.INFO)

        self.app_log.addHandler(self.my_handler)

        self.settings_database = ptc_database.SettingsDatabase(self.app_log)
 #       self.settings_database.download()
        self.dbx = dropbox.Dropbox(self.settings_database.get_setting('dropbox_access_token'))
        self.app_log.info("Initialized dropbox")
        
        #initiate the database
        self.settings_database = ptc_database.SettingsDatabase(self.app_log)
        self.settings_database.download()

    def process(self):
        """Method responsible for looping through the files to upload"""
        #set the file extension of interest
        extensions = ('.ready')

        #Loop through the files  in the current working directory
        for sub_dir, dirs, files in os.walk(os.getcwd()):
            for ready_file_name in files:
                ext = os.path.splitext(ready_file_name)[-1].lower()
                if ext in extensions:
                    try:
                        pre, ext = os.path.splitext(ready_file_name)
                        image_file_name = pre + ".jpg"
                        self.upload_file(sub_dir, image_file_name)
                        os.remove(os.path.join(sub_dir,ready_file_name))
                    except Exception as exception:
                        self.app_log.exception('Exception: %s', exception)

    def upload_file(self, source_sub_directory, image_file_name):
        try:
            """Method responsible for processing the uploading of files"""
            source_full_path = os.path.join(source_sub_directory, image_file_name)
            destination_full_path = os.path.join(self.settings_database.get_setting('dropbox_destination_folder'), image_file_name)

            with open(source_full_path, 'rb') as source_file:
                self.dbx.files_upload(source_file.read(), destination_full_path)

            self.app_log.info("uploaded file from  " + source_full_path + " to " + destination_full_path)
 
            os.remove(source_full_path)
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def process_loop(self):
        """Method responsible for the control loop for looking for files to upload"""
        while True:
            try:
                self.app_log.info("Looking for files to upload")
                self.process()
            except Exception as exception:
                self.app_log.exception('Exception: %s', exception)
            finally:
                time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    ul_files = UploadFiles()
    ul_files.process_loop()
