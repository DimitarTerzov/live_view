"""Module responsible for interacting with the PI Camera fpr the Photo to cloud project"""
# pylint: disable=line-too-long,no-member,broad-except
from time import sleep
import datetime
from picamera import PiCamera
import os

class PTCCamera():
    """Class responsible for interacting with the PI Camera"""
    def __init__(self, application_log, sequence_step_database, settings_database):
        """Initialization of logging and the PiCamera"""
        self.app_log = application_log
        try:
            self.app_log.info("Initialising the camera")
            self.initialised = False

            #Initialize the Pi Camera.
            self.camera = PiCamera()

            self.start_timestamp = None
            self.sequence_step_database = sequence_step_database
            self.settings_database = settings_database

            self.apply_settings()
            #camera warm up!
            # self.camera.start_preview()
            # sleep(2)
            # self.camera.stop_preview()
            self.BASE_PATH = os.path.dirname(os.path.realpath(__file__))
            self.app_log.info("Initialising camera - complete")
            self.initialised = True
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)


    def apply_settings(self):
        """Apply settings to the camera"""
        try:
            #From the settings
            self.camera.resolution = (int(self.settings_database.get_setting('resolution_x')), int(self.settings_database.get_setting('resolution_y')))
            self.camera.zoom = (float(self.settings_database.get_setting('zoom_x')), float(self.settings_database.get_setting('zoom_y')), float(self.settings_database.get_setting('zoom_w')), float(self.settings_database.get_setting('zoom_h')))
            self.camera.drc_strength = self.settings_database.get_setting('drc_strength')
            self.camera.image_denoise = (self.settings_database.get_setting('image_denoise') == '1')
            self.camera.meter_mode = self.settings_database.get_setting('meter_mode')

            self.camera.exposure_compensation = int(self.settings_database.get_setting('exposure_compensation'))

            if self.settings_database.get_setting('color_effects') == '0':
                self.camera.color_effects = None
            else:
                self.camera.color_effects = (int(self.settings_database.get_setting('color_effects_u')), int(self.settings_database.get_setting('color_effects_v')))

            self.camera.image_effect = self.settings_database.get_setting('image_effect')
            # self.camera.image_effect = "none"
            if self.camera.image_effect != 'none':
                self.set_image_effect_params()

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def apply_sequence_step_data(self, step):
        """Apply the sequence step data to the camera."""
        try:
            sequence_step_data = self.sequence_step_database.get_sequence_step_data(step)
            self.camera.exposure_mode = sequence_step_data[self.sequence_step_database.exposure_mode]
            self.camera.awb_mode = sequence_step_data[self.sequence_step_database.awb_mode]
            self.camera.iso = int(sequence_step_data[self.sequence_step_database.iso])
            self.camera.shutter_speed = int(sequence_step_data[self.sequence_step_database.shutter_speed])
            self.camera.brightness = int(sequence_step_data[self.sequence_step_database.brightness])
            self.camera.saturation = int(sequence_step_data[self.sequence_step_database.saturation])
            self.camera.contrast = int(sequence_step_data[self.sequence_step_database.contrast])

            self.camera.exif_tags['IFD0.ImageDescription'] = "exposure_mode = " + self.camera.exposure_mode + ", " + "awb_mode = " + self.camera.awb_mode + ", iso = " + str(self.camera.iso)

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)


    def apply_sequence_step_data_seq(self, step, sequence_id):
        """Apply the sequence step data to the camera."""
        try:
            sequence_step_data = self.sequence_step_database.get_sequence_step_data_seq(step,sequence_id)
            print("sequence step data")
            print(sequence_step_data)

            self.camera.exposure_mode = sequence_step_data[self.sequence_step_database.exposure_mode]
            self.camera.awb_mode = sequence_step_data[self.sequence_step_database.awb_mode]
            self.camera.iso = int(sequence_step_data[self.sequence_step_database.iso])
            self.camera.shutter_speed = int(sequence_step_data[self.sequence_step_database.shutter_speed])
            self.camera.brightness = int(sequence_step_data[self.sequence_step_database.brightness])
            self.camera.saturation = int(sequence_step_data[self.sequence_step_database.saturation])
            self.camera.contrast = int(sequence_step_data[self.sequence_step_database.contrast])

            self.camera.exif_tags['IFD0.ImageDescription'] = "exposure_mode = " + self.camera.exposure_mode + ", " + "awb_mode = " + self.camera.awb_mode + ", iso = " + str(self.camera.iso)

        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def take_picture(self, step, sequence_id):
        """Taking the picture. Accepts the sequence step and meta data as paprameters."""
        try:
            #Apply the camera settings
            if step == 0:
                #create the timestamp for the filename for the pictures, this timestamp will be applied the all pictures in this sequence
                self.start_timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            print("applying the camera settings SEQ ID:", sequence_id)
            self.apply_sequence_step_data_seq(step,sequence_id)

            #Save the meta data
            self.camera.exif_tags['IFD0.Copyright'] = self.settings_database.get_setting('image_copyright')

            #capture and save the picture
            image_source_directory = os.path.join(self.BASE_PATH, 'images') + "/"
            image_file_name = self.settings_database.get_setting('image_name') + "-"  + self.start_timestamp + '-' + str(step) + '.jpg'
            ready_file_path = image_source_directory + self.settings_database.get_setting('image_name') + "-"  + self.start_timestamp + '-' + str(step) + '.ready'
            self.camera.rotation = int(self.settings_database.get_setting('rotation'))
            # print("camera rotation: ", self.camera.rotation)
            self.camera.capture(image_source_directory + image_file_name)

            #Some files were being moved to dropbox before being fully written, so this was added to prevent that.
            with open(ready_file_path, 'w') as ready_file:
                ready_file.write(' ')
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def set_image_effect_params(self):
        """Apply settings to the camera effects"""
        try:
            if self.camera.image_effect == 'solarize':
                self.camera.image_effect.yuv = int(self.settings_database.get_setting('image_effects_param_1'))
                self.camera.image_effect.x0 = int(self.settings_database.get_setting('image_effects_param_2'))
                self.camera.image_effect.y1 = int(self.settings_database.get_setting('image_effects_param_3'))
                self.camera.image_effect.y2 = int(self.settings_database.get_setting('image_effects_param_4'))
                self.camera.image_effect.y3 = int(self.settings_database.get_setting('image_effects_param_5'))
            elif self.camera.image_effect == 'colorpoint':
                self.camera.image_effect.quadrant = int(self.settings_database.get_setting('image_effects_param_1'))
            elif self.camera.image_effect == 'colorbalance':
                self.camera.image_effect.lens = int(self.settings_database.get_setting('image_effects_param_1'))
                self.camera.image_effect.r = int(self.settings_database.get_setting('image_effects_param_2'))
                self.camera.image_effect.g = int(self.settings_database.get_setting('image_effects_param_3'))
                self.camera.image_effect.b = int(self.settings_database.get_setting('image_effects_param_4'))
                self.camera.image_effect.uv = int(self.settings_database.get_setting('image_effects_param_5'))
            elif self.camera.image_effect == 'colorswap':
                self.camera.image_effect.dir = int(self.settings_database.get_setting('image_effects_param_1'))
            elif self.camera.image_effect == 'posterise':
                self.camera.image_effect.steps = int(self.settings_database.get_setting('image_effects_param_1'))
            elif self.camera.image_effect == 'blur':
                self.camera.image_effect.size = int(self.settings_database.get_setting('image_effects_param_1'))
            elif self.camera.image_effect == 'film':
                self.camera.image_effect.strength = int(self.settings_database.get_setting('image_effects_param_1'))
                self.camera.image_effect.u = int(self.settings_database.get_setting('image_effects_param_2'))
                self.camera.image_effect.v = int(self.settings_database.get_setting('image_effects_param_3'))
            elif self.camera.image_effect == 'watercolor':
                self.camera.image_effect.u = int(self.settings_database.get_setting('image_effects_param_1'))
                self.camera.image_effect.v = int(self.settings_database.get_setting('image_effects_param_2'))
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)

    def __del__(self):
        """The destructor cleans up the camera resources."""
        try:
            self.camera.close()
        except Exception as exception:
            self.app_log.exception('Exception: %s', exception)


if __name__ == '__main__':
    PTCCamera().apply_settings()
