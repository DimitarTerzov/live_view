import logging
import os
from logging.handlers import RotatingFileHandler

import dropbox
from PyQt5.QtCore import QThread

import ptc_database


class UploadFileQThread(QThread):
    def __init__(self, BASE_PATH, QObject_parent=None):
        super().__init__(QObject_parent)

        self.SLEEP_TIME = 1

        self.BASE_PATH = BASE_PATH

        self.log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

        self.my_handler = RotatingFileHandler('{}'.format(os.path.join(self.BASE_PATH, 'logs/upload_files.log')), mode='a', maxBytes=5 * 1024 * 1024,
                                              backupCount=1, encoding=None, delay=0)
        self.my_handler.setFormatter(self.log_formatter)
        self.my_handler.setLevel(logging.INFO)

        self.app_log = logging.getLogger('root')
        self.app_log.setLevel(logging.INFO)

        self.app_log.addHandler(self.my_handler)

        self.settings_database = ptc_database.SettingsDatabase(self.app_log)
        #       self.settings_database.download()
        print("Dropbox token ", self.settings_database.get_setting('dropbox_access_token'))
        self.dropbox_destination_folder = self.settings_database.get_setting('dropbox_destination_folder')
        print("dropbox_destination_folder: ", self.settings_database.get_setting('dropbox_destination_folder'))

        self.dbx = dropbox.Dropbox(self.settings_database.get_setting('dropbox_access_token'))

    def upload_file(self, source_sub_directory, image_file_name):
        try:
            """Method responsible for processing the uploading of files"""
            # print("source_sub_directory: ", source_sub_directory)
            source_full_path = os.path.join(source_sub_directory, image_file_name)
            # print("source_full_path: ", source_full_path)
            # print("dropbox_destination_folder: ", self.settings_database.get_setting('dropbox_destination_folder'))
            destination_full_path = os.path.join(self.dropbox_destination_folder, image_file_name)
            # print("destination_full_path: ", destination_full_path)
            with open(source_full_path, 'rb') as source_file:
                self.dbx.files_upload(source_file.read(), destination_full_path)

            self.app_log.info("uploaded file from  " + source_full_path + " to " + destination_full_path)
            print("uploaded file from  " + source_full_path + " to " + destination_full_path)
            os.remove(source_full_path)
        except Exception as exception:
            print("upload file exception", exception)
            self.app_log.exception('Exception: %s', exception)

    def process(self):
        """Method responsible for looping through the files to upload"""
        #set the file extension of interest
        extensions = ('.ready')
        #Loop through the files  in the current working directory
        # print("os.getcwd() ", os.getcwd())
        BASE_PATH = os.path.dirname(os.path.realpath(__file__))
        for sub_dir, dirs, files in os.walk(os.path.join(BASE_PATH, 'images')):
            # print("for 1")
            # print(sub_dir, dirs, files)
            for ready_file_name in files:
                # print("for 2")
                # print(ready_file_name)
                ext = os.path.splitext(ready_file_name)[-1].lower()
                if ext in extensions:
                    try:
                        pre, ext = os.path.splitext(ready_file_name)
                        image_file_name = pre + ".jpg"
                        # print("try ", pre, ext)
                        self.upload_file(sub_dir, image_file_name)
                        os.remove(os.path.join(sub_dir,ready_file_name))
                    except Exception as exception:
                        print("process upload file exception", exception)
                        self.app_log.exception('Exception: %s', exception)

    def run(self):
        while True:
            try:
                self.app_log.info("Looking for files to upload")
                self.process()
            except Exception as exception:
                self.app_log.exception('Exception: %s', exception)
            finally:
                self.sleep(self.SLEEP_TIME)


