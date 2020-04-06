import logging
import os
import socket
import subprocess
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSizePolicy
import settings
# from photo_to_cloud import PhotoToCloud
import ptc_database
from display_pin_status import pin_status
from mainUI import Ui_MainWindow
from photo_cloud_thread import PhotoCloudThread
# class MatchBoxLineEdit(QLineEdit):
#     def focusInEvent(self, e):
#         print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
#         try:
#             subprocess.Popen(["matchbox-keyboard"])
#         except FileNotFoundError:
#             pass
#
#     def focusOutEvent(self,e):
#         print("sadddddddddddddddddddddddddddddddddd")
#         subprocess.Popen(["killall","matchbox-keyboard"])
from upload_file_thread import UploadFileQThread

# os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


class MyMainWindow(QMainWindow):

    def __init__(self, args, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if len(args) > 1:
            # self.resize(480, 640)
            self.showFullScreen()
            # self.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint)
        # self.showFullScreen()

        self.BASE_PATH = BASE_PATH

        self.log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
        self.my_handler = RotatingFileHandler('{}'.format(os.path.join(self.BASE_PATH, 'logs/photo_to_cloud.log')), mode='a', maxBytes=5 * 1024 * 1024,
                                              backupCount=1, encoding=None, delay=0)
        self.my_handler.setFormatter(self.log_formatter)
        self.my_handler.setLevel(logging.INFO)
        self.app_log = logging.getLogger('root')
        self.app_log.setLevel(logging.INFO)
        self.app_log.addHandler(self.my_handler)


        # page set up
        self.main_page = 0
        self.menu_page = 1
        self.setting_page = 2
        self.Led_sequence = 3
        self.brightness = 4
        self.screen_brightness = 5
        self.Network_status = 6
        self.password_input = 7
        self.get_update = 8
        self.shutdown_page = 9
        self.camerastatus_page = 10
        self.shutdowntatus_page = 11
        self.step = 0

        self.process_started = False
        self.pinThread = pin_status(self.app_log)
        self.pinThread.signal_rx.connect(self.pinDataEvent)
        self.pinThread.start()

        self.photo_thread = PhotoCloudThread(self.BASE_PATH, self.app_log)
        self.photo_thread.signal_rx.connect(self.photo_event)
        self.photo_thread.start()

        self.wifilist = []
        self.wifiselected = ""
        self.sequence_list = []
        self.sequence_id = []

        self.sequence_selected = ""
        # self.phototocloud = PhotoToCloud()
        self.ui.menuButton.clicked.connect(self.menubuttonClicked)
        self.ui.menuNextbutton.clicked.connect(self.selectClicked)
        self.ui.settingsNextbutton.clicked.connect(self.settins_selectClicked)
        self.ui.nextWiFiButton.clicked.connect(self.wifi_selectClicked)
        self.ui.nextLedSeqButton.clicked.connect(self.sequence_selectClicked)
        self.ui.exitWifipassButton.clicked.connect(self.select_exitwifi_password)
        self.ui.menuExitButton.clicked.connect(self.backtomain)
        self.ui.exitImageBrightnessButton.clicked.connect(self.brightness_increase)
        self.ui.brightnessLessButton.clicked.connect(self.brightness_decrease)
        self.ui.selectImageBrightnessButton.clicked.connect(self.chage_image_brightness)
        self.ui.exitScreenBrightnessButton.clicked.connect(self.screen_brightness_increase)
        self.ui.lessScreenBrightnessButton.clicked.connect(self.screen_brightness_decrease)
        self.ui.selectScreenBrightnessButton.clicked.connect(self.chage_screen_brightness)
        # self.ui.getUpdateButton.clicked.connect(self.update_database)
        self.ui.lightSourcepushbutton.clicked.connect(self.light_source_update)
        self.ui.takePhotoButton.clicked.connect(self.process_light)
        self.ui.shutdownButton.clicked.connect(self.shutdownsystem)
        self.ui.restartButton.clicked.connect(self.restartsystem)
        # self.ui.lineEdit.clicked.connect(self.open_keyboard)
        # self.ui.lineEdit.installEventFilter(self)
        # self.ui.lineEdit.focusOutEvent()
        # self.ui.lineEdit.focusInEvent = MatchBoxLineEdit()
        # self.ui.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        # self.ui.lineEdit.setFocus(True)
        self.ui.menuSelectButton.clicked.connect(self.nextClicked)
        self.ui.settingsSelectbutton.clicked.connect(self.nextClicked_settings)
        self.ui.selectWiFiButton.clicked.connect(self.nextClicked_wifi)
        self.ui.selectLedSeqButton.clicked.connect(self.nextClicked_sequence)
        self.ui.pushButton_6.clicked.connect(self.rescanNetwork)
        self.ui.exitAppButton.clicked.connect(self.exitApp)

        self.ui.settingsExitbutton.clicked.connect(self.backtomenu)
        self.ui.exitLedSeqButton.clicked.connect(self.backtomenu)
        self.ui.exitWiFiButton.clicked.connect(self.backtomenu)
        self.ui.exitUpdateButton.clicked.connect(self.backtomenu)
        self.ui.exitShutdownButton.clicked.connect(self.backtomenu)

        self.ui.saveWifipassButton.clicked.connect(self.save_wifi)
        self.ui.exitWiFiButton.clicked.connect(self.backtomenu)
        self.ui.cancelShutdownButton.clicked.connect(self.cancelActionShutDownOrRestart)
        self.ui.stopshutdown.clicked.connect(self.cancelActionShutDownOrRestart)
        self.ui.showKeyboardButton.clicked.connect(self.showKeyboard)
        self.ui.menuList.clicked.connect(self.menulistclicked)
        self.ui.settingsList.clicked.connect(self.settingslistclicked)
        self.ui.sequenceList.clicked.connect(self.sequencelistclicked)
        self.ui.wifiavailableList.clicked.connect(self.wifilistclicked)
        self.ui.updateSequenceButton.clicked.connect(self.update_database)

        # Database access
        self.processing = False
        self.start_time = datetime.now()

        # initiate the database
        self.settings_database = ptc_database.SettingsDatabase(self.app_log)
        self.sequence_step_database = ptc_database.SequenceStepsDatabase(self.app_log)
        self.led_groups_database = ptc_database.LEDGroupsDatabase(self.app_log)
        self.sequences_database = ptc_database.SequencesDatabase(self.app_log)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.sequences = []
        # self.ui.wifiavailableList.itemSelectionChanged.connect(self.selectionChanged)
        self.ui.statusInfo.setText("Waiting")
        self.set_sequnce_main_page()
        self.status_light_source = True
        self.light_source_update()
        time.sleep(1)
        self.startUploadFileThread()

        # self.status_wifi = False
        # time.sleep(10)
        # self.app_log.info("main, updating the database")
        # self.update_database()
        # self.app_log.info("main, updated the database")

    def startUploadFileThread(self):
        print("starting the upload qthred")
        self.file_upload_thread = UploadFileQThread(self.BASE_PATH)
        self.file_upload_thread.start()

        
        # self.update_database()

        # self.update_database()

    # def selectionChanged(self):
    #     print("Selected items: ")
    #     x = self.ui.wifiavailableList.selectedIndexes()
    #     index = x[0].row()
    #     print(index)

    # def focusInEvent(self, e):
    #     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #
    # def focusOutEvent(self, e):
    #     print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

    # def eventFilter(self, obj, event):
    #     if event.type() == QEvent.FocusIn:
    #         if obj == self.ui.lineEdit:
    #             try:
    #                 subprocess.Popen(["matchbox-keyboard"])
    #             except FileNotFoundError:
    #                 pass
    #         if event.type() == QEvent.FocusOut:
    #             if obj == self.ui.lineEdit:
    #                 subprocess.Popen(["killall", "matchbox-keyboard"])
    #     return False

    def showKeyboard(self):
        self.app_log.info("main, showKeyboard clicked")
        self.setWifiPasswordFocus()
        password = self.ui.lineEdit.text()
        print("pass", password)
        print("len ", len(password))
        self.ui.lineEdit.setCursorPosition(len(password))
        try:
            # os.system("sh /home/pi/Desktop/code_1/keyboard_open.sh")
            os.system("sh {}".format(os.path.join(self.BASE_PATH, 'keyboard_open.sh')))
        except FileNotFoundError:
            pass

    def exitApp(self):
        self.photo_thread.signal_tx.emit("exitfromapp")
        # sys.exit(1)

    def cancelActionShutDownOrRestart(self):
        self.app_log.info("main, cancelActionShutDownOrRestart clicked")
        print("cancelActionShutDownOrRestart signal emiting")
        self.photo_thread.signal_tx.emit("cancel")
        print("cancelActionShutDownOrRestart signal emitted")

    def mouseDoubleClickEvent(self, e):
        current_page = self.ui.stackedWidget.currentIndex()
        if current_page == self.password_input:
            self.showKeyboard()

    def menulistclicked(self, item):
        self.app_log.info("main, menuList clicked")
        print("clicked menuuuuuuuuu list", item.row())
        selected = item.row()
        if selected >= 0:
            self.selection_logic(selected)

    def settingslistclicked(self, item):
        self.app_log.info("main, settingsList clicked")
        print("clicked menuuuuuuuuu list", item.row())
        selected = item.row()
        if selected >= 0:
            self.settings_list_selected(selected)

    def sequencelistclicked(self, item):
        self.app_log.info("main, sequenceList clicked")
        print("clicked menuuuuuuuuu list", item.row())
        selected = item.row()
        if selected >= 0:
            self.led_sequnce_selected(selected)

    def wifilistclicked(self, item):
        self.app_log.info("main, wifiavailableList clicked")
        print("clicked menuuuuuuuuu list", item.row())
        selected = item.row()
        if selected >= 0:
            self.wifi_next_clicked(selected)

    def backtomenu(self):
        self.app_log.info("main, back to menu")
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.label_32.setText(" ")
        print("Button click")

    def backtomain(self):
        self.app_log.info("main, back to main")
        # self.app_log.info("main, menuExitButton clicked")
        self.ui.stackedWidget.setCurrentIndex(0)
        self.pinThread.signal_tx.emit("start")
        self.step = 0
        self.set_sequnce_main_page()
        self.light_source_update()

        # self.ui.lightSourceInfo.setText("Light Source Info")
        # print("Button click")

    def rescanNetwork(self):
        self.scan_network()

    def set_sequnce_main_page(self):
        try:
            f = open("{}".format(os.path.join(self.BASE_PATH, 'active_seq')), "r")
            sequence_id = int(f.read())
            f.close()
            name_seq = self.sequences_database.get_active_sequence_name(sequence_id)
            if name_seq is not None:
                self.set_led_group_name(self.step, sequence_id)
                # self.ui.lightSourceInfo.setText(self.sequence_selected + " " + str(self.step))
                self.sequence_selected = name_seq
            else:
                self.ui.lightSourceInfo.setText("No sequence available")
                try:
                    os.remove("{}".format(os.path.join(self.BASE_PATH, 'active_seq')))
                except Exception as e:
                    print("Exception update_database ", e)
                    pass

        except Exception as e:
            self.app_log.info("main, updateSequenceButton clicked "+str(e))
            print("Exception set_sequnce_main_page", e)
            # select default sequence
            self.sequences = self.sequences_database.get_all_sequences()
            print("sequences: ", self.sequences)
            sequence_set = False
            for sequence in self.sequences:
                sequence_set = True
                sequence_step_count = self.sequence_step_database.get_sequence_step_count_seq(sequence['id'])
                print(sequence_step_count)
                if sequence_step_count - 1 < self.step:
                    self.step = 0
                self.sequence_selected = sequence['name']
                self.filesave_sequence(sequence['id'])
                sequence_id = sequence['id']
                self.set_led_group_name(self.step, sequence_id)
                # self.ui.lightSourceInfo.setText(self.sequence_selected + " " + str(self.step))
                break
            if not sequence_set:
                self.ui.lightSourceInfo.setText("No sequence available")
                try:
                    os.remove("{}".format(os.path.join(self.BASE_PATH, 'active_seq')))
                except Exception as e:
                    print("Exception update_database ", e)
                    pass

    def set_sequnce_main_page_first(self):
        try:
            self.app_log.info("main, set_sequence_main_page_first started")
            f = open("{}".format(os.path.join(self.BASE_PATH, 'active_seq')), "r")
            sequence_id = int(f.read())
            f.close()
            self.app_log.info("main, file read done")
            self.sequences = self.sequences_database.get_all_sequences()
            sequence_set = False
            for sequence in self.sequences:  
                print("xxxxxxxxxxx",sequence['id'])              
                if int(sequence['id']) == sequence_id:
                    sequence_set = True
                    break
            if sequence_set == True:
                self.app_log.info("main, sequence same before")
                print("set_sequnce_main_page_first",sequence_set)
                name_seq = self.sequences_database.get_active_sequence_name(sequence_id)
                self.set_led_group_name(self.step, sequence_id)
                # self.ui.lightSourceInfo.setText(self.sequence_selected + " " + str(self.step))
                self.sequence_selected = name_seq
            else:
                self.app_log.info("main, new sequence")
                print("set_sequence_main_page_first",sequence_set)
                self.sequences = self.sequences_database.get_all_sequences()
                print("sequences: ", self.sequences)
                sequence_set1 = False
                for sequence in self.sequences:
                    sequence_set1 = True
                    sequence_step_count = self.sequence_step_database.get_sequence_step_count_seq(sequence['id'])
                    print(sequence_step_count)
                    if sequence_step_count - 1 < self.step:
                        self.step = 0
                    self.sequence_selected = sequence['name']
                    self.filesave_sequence(sequence['id'])
                    sequence_id = sequence['id']
                    self.set_led_group_name(self.step, sequence_id)
                    # self.ui.lightSourceInfo.setText(self.sequence_selected + " " + str(self.step))
                    break
                if not sequence_set1:
                    self.app_log.info("main, No sequence available")
                    self.ui.lightSourceInfo.setText("No sequence available") 
                    try:
                        os.remove("{}".format(os.path.join(self.BASE_PATH, 'active_seq')))
                    except Exception as e:
                        print("Exception update_database ", e)
                        pass           
        except Exception as e:
            self.app_log.info("main, set_sequence_main_page_first "+str(e))
            print("Exception set_sequnce_main_page", e)
            # select default sequence
            self.sequences = self.sequences_database.get_all_sequences()
            print("sequences: ", self.sequences)
            sequence_set = False
            for sequence in self.sequences:
                sequence_set = True
                sequence_step_count = self.sequence_step_database.get_sequence_step_count_seq(sequence['id'])
                print(sequence_step_count)
                if sequence_step_count - 1 < self.step:
                    self.step = 0
                self.sequence_selected = sequence['name']
                self.filesave_sequence(sequence['id'])
                sequence_id = sequence['id']
                self.set_led_group_name(self.step, sequence_id)
                # self.ui.lightSourceInfo.setText(self.sequence_selected + " " + str(self.step))
                break
            if not sequence_set:
                self.app_log.info("main, No sequence available")
                self.ui.lightSourceInfo.setText("No sequence available")
                try:
                    os.remove("{}".format(os.path.join(self.BASE_PATH, 'active_seq')))
                except Exception as e:
                    print("Exception update_database ", e)
                    pass

    def menubuttonClicked(self):
        # print("stacked widget: ")
        self.app_log.info("main, menubuttonClicked")
        self.pinThread.signal_tx.emit("stop")
        print(self.ui.stackedWidget.currentIndex())
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.menuList.setCurrentRow(0)
        self.photo_thread.signal_tx.emit("turnofflight")
        self.ui.label_32.setText(" ")
        print("Button click")

    def open_keyboard(self, e):
        try:
            subprocess.Popen(["matchbox-keyboard"])
        except FileNotFoundError:
            pass

    def close_keyboard(self, e):
        subprocess.Popen(["killall", "matchbox-keyboard"])

    def brightness_increase(self):
        # print("stacked widget: ")
        cu = self.ui.imageBrightnessbox.value()
        self.ui.imageBrightnessbox.setValue(cu + 1)

    def shutdownsystem(self):
        self.app_log.info("main, shutdownButton clicked")
        self.ui.stackedWidget.setCurrentIndex(self.shutdowntatus_page)
        # os.system("sudo poweroff")
        # for i in range(10,0,-1):
        #     self.ui.shudownTimer.setText("Timer in " + str(10))
        self.photo_thread.signal_tx.emit("poweroff")

    def restartsystem(self):
        self.app_log.info("main, restartbutton clicked")
        self.ui.stackedWidget.setCurrentIndex(self.shutdowntatus_page)
        # os.system("sudo poweroff")
        # for i in range(10,0,-1):
        #     self.ui.shudownTimer.setText("Timer in " + str(10))
        self.photo_thread.signal_tx.emit("restart")

    def update_database(self):
        self.app_log.info("main, updateSequenceButton clicked")
        self.photo_thread.signal_tx.emit("download")
        # try:
        #     os.remove("active_seq")
        # except Exception as e:
        #     print("Exception update_database ", e)
        #     pass
        # self.download_database()
        # self.set_sequnce_main_page()

    def brightness_decrease(self):
        # print("stacked widget: ")
        cu = self.ui.imageBrightnessbox.value()
        if cu - 1 >= 0:
            self.ui.imageBrightnessbox.setValue(cu - 1)

    def read_sequence_id(self):
        sequence_id = None
        try:
            f = open("{}".format(os.path.join(self.BASE_PATH, 'active_seq')), "r")
            sequence_id = int(f.read())
            f.close()
            self.app_log.info("read_sequence_id from the file")
        except Exception as e:
            self.app_log.info("read_sequence_id"+str(e))
            pass
        return sequence_id

    def process_light(self):
        self.app_log.info("main, take photo clicked")
        self.sequence_id = self.read_sequence_id()
        if self.sequence_id is None:
            self.app_log.info("main, sequnce id is None")
            return
        if self.process_started:
            return
        self.process_started = True
        self.app_log.info("main, take photo started")
        self.ui.lightSourceInfo.setText("Processing started")
        self.pinThread.signal_tx.emit("stop")
        self.ui.stackedWidget.setCurrentIndex(self.camerastatus_page)
        self.ui.pushButton.setIcon(QtGui.QIcon("{}".format(os.path.join(self.BASE_PATH, 'image_resources/update_icon.png'))))
        self.ui.cameraCapturinginfo.setText("Image Capturing in Progress.....")
        self.app_log.info("main, take photo stopeed")
        # self.phototocloud.process_loop()


    def get_led_gruop_name(self,step,sequencd_id):
        try:
            led_id = self.sequence_step_database.get_led_group_id(step, sequencd_id)
            group_name = self.led_groups_database.get_led_group_name(led_id)
            return group_name
        except Exception as exception:
            print(exception)
            return None

    def chage_image_brightness(self):
        cu = self.ui.imageBrightnessbox.value()
        self.photo_thread.signal_tx.emit("brightness=" + str(cu))
        self.ui.stackedWidget.setCurrentIndex(1)

    def chage_screen_brightness(self):
        cu = self.ui.spinBox_2.value()
        # self.pinThread.signal_tx.emit("brightness=" + str(cu))
        self.ui.stackedWidget.setCurrentIndex(1)

    def read_ssid_ipconfig(self):
        ssid = ""
        ipaddress = ""
        try:
            testIP = "8.8.8.8"
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((testIP, 0))
            ipaddress = s.getsockname()[0]
            ssid = os.popen("iwconfig wlan0 \
                            | grep 'ESSID' \
                            | awk '{print $4}' \
                        | awk -F\\\" '{print $2}'").read()
        except:
            pass
        return [ssid, ipaddress]

    def screen_brightness_increase(self):
        # print("stacked widget: ")
        cu = self.ui.spinBox_2.value()
        self.ui.spinBox_2.setValue(cu + 1)

    def screen_brightness_decrease(self):
        # print("stacked widget: ")
        cu = self.ui.spinBox_2.value()
        if cu - 1 >= 0:
            self.ui.spinBox_2.setValue(cu - 1)

    def set_led_group_name(self,step,sequence_id):
        group_name = self.get_led_gruop_name(step,sequence_id)
        self.ui.lightSourceInfo.setText(self.sequence_selected + " " + group_name)


    def light_source_update(self):
        self.app_log.info("main, source clicked")
        self.app_log.info("main, light_source_update")
        sequence_id = None
        try:
            f = open("{}".format(os.path.join(self.BASE_PATH, 'active_seq')), "r")
            sequence_id = int(f.read())
            f.close()
            self.app_log.info("main, sequence id saved in the file ")
        except Exception as e:
            self.app_log.info("main, read file exception " + str(e))
            pass

        if sequence_id is not None and self.sequence_selected is not None:
            self.app_log.info("sequence_id and sequence_selected is not None")
            sequence_step_count = self.sequence_step_database.get_sequence_step_count_seq(sequence_id)
            print(sequence_step_count)
            if sequence_step_count - 1 < self.step:
                self.step = 0
            # self.ui.lightSourceInfo.setText(self.sequence_selected + " " + str(self.step))
            self.set_led_group_name(self.step, sequence_id)
            # self.phototocloud.process_step(self.step)
            self.app_log.info("main, step started")
            self.photo_thread.signal_tx.emit(self.step)
            self.app_log.info("main, step stopped")
            # self.ph
            self.step += 1
        self.app_log.info("main, source clicked sequence id None or sequence_selected is not None")

    def scan_network(self):
        self.ui.wifiavailableList.clear()
        self.wifilist = self.wifilistarray()
        # self.wifilist = ["Item 1","Item 2"]
        self.ui.wifiavailableList.setFont(QFont("Fixed", 20))
        self.ui.wifiavailableList.addItems(self.wifilist)
        self.ui.wifiavailableList.setCurrentRow(0)

    def select_exitwifi_password(self):
        try:
            # os.system("sh /home/pi/Desktop/code_1/keyboard_on_off.sh")
            os.system("sh {}".format(os.path.join(self.BASE_PATH, 'keyboard_on_off.sh')))
        except FileNotFoundError:
            pass
        self.showFullScreen()
        self.ui.stackedWidget.setCurrentIndex(self.Network_status)
        self.scan_network()

    def settins_selectClicked(self):
        self.app_log.info("main, settingsNextbutton clicked")
        x = self.ui.settingsList.selectedIndexes()
        print("row_selected", x)
        if len(x) > 0:
            index = x[0].row()
            print(index)
            if index != -1 and index <= 0:
                self.ui.settingsList.setCurrentRow(index + 1)
                # del self.ui.menuList[index]
            else:
                self.ui.settingsList.setCurrentRow(0)

    def wifi_selectClicked(self):
        self.app_log.info("main, nextWiFiButton clicked")
        x = self.ui.wifiavailableList.selectedIndexes()
        index = x[0].row()
        print(index)
        wif_connected = len(self.wifilist)
        if index != -1 and index <= wif_connected - 2:
            self.ui.wifiavailableList.setCurrentRow(index + 1)
            # del self.ui.menuList[index]
        else:
            self.ui.wifiavailableList.setCurrentRow(0)

    def sequence_selectClicked(self):
        self.app_log.info("main, nextLedSeqButton clicked")
        x = self.ui.sequenceList.selectedIndexes()
        index = x[0].row()
        print(index)
        seq_connected = len(self.sequence_list)
        if index != -1 and index <= seq_connected - 2:
            self.ui.sequenceList.setCurrentRow(index + 1)
            # del self.ui.menuList[index]
        else:
            self.ui.sequenceList.setCurrentRow(0)

    def selectClicked(self):
        self.app_log.info("main, menuNextbutton clicked")
        x = self.ui.menuList.selectedIndexes()
        index = x[0].row()
        print(index)
        if index != -1 and index <= 2:
            self.ui.menuList.setCurrentRow(index + 1)
            # del self.ui.menuList[index]
        else:
            self.ui.menuList.setCurrentRow(0)

    def preview_back(self):
        self.ui.lightSourceInfo.setText("Light Source Info")

    def filesave_sequence(self, seq_val):
        try:
            f = open("{}".format(os.path.join(self.BASE_PATH, 'active_seq')), "w")
            f.write(str(seq_val))
            # perform file operations
        finally:
            f.close()

    def populate_sequence(self):
        self.ui.sequenceList.clear()
        self.sequence_list = []
        self.sequence_id = []
        self.sequences = (self.sequences_database.get_all_sequences())
        # self.sequence_list = ["Item _seq_1", "Item seq_2"]
        for sequence in self.sequences:
            self.sequence_list.append(sequence['name'])
            self.sequence_id.append(sequence['id'])
        self.ui.sequenceList.setFont(QFont("Fixed", 20))
        self.ui.sequenceList.addItems(self.sequence_list)
        self.ui.sequenceList.setCurrentRow(0)

    def selection_logic(self, selected):
        self.sequence_list = []
        self.sequence_id = []
        # Page - Sequence selection page
        if (selected == 0):
            self.ui.stackedWidget.setCurrentIndex(self.Led_sequence)
            self.ui.updateStatusLabel.setText(" ")
            self.populate_sequence()

        # if (selected == 1):
        #     # print("stacked widget: ")
        #     # print(self.ui.stackedWidget.currentIndex())
        #     self.ui.stackedWidget.setCurrentIndex(self.brightness)
        # if (selected == 2):
        #     # print("stacked widget: ")
        #     # print(self.ui.stackedWidget.currentIndex())
        #     self.ui.stackedWidget.setCurrentIndex(self.screen_brightness)

        if (selected == 1):
            self.ui.stackedWidget.setCurrentIndex(self.setting_page)
            [ssid, ipconfig] = self.read_ssid_ipconfig()
            self.ui.label_30.setText(ipconfig)
            self.ui.label_31.setText(ssid)
            self.ui.settingsList.setCurrentRow(0)

        if (selected == 2):
            self.ui.stackedWidget.setCurrentIndex(self.shutdown_page)
            self.ui.shudownTimer.setText(" ")

        if (selected == 3):
            os.system(settings.runServerCommand)
            restartbutton = QMessageBox()
            self.ui.label_32.setText("Server started")




    def nextClicked(self):
        self.app_log.info("main, menuSelectButton clicked")
        # ss = self.ui.menuList.selectedItems()
        # print(ss)
        x = self.ui.menuList.selectedIndexes()
        selected = x[0].row()
        self.selection_logic(selected)

    def wifilistarray(self):
        wifi_list = []
        try:
            os.remove("/home/pi/wifilist")
        except:
            pass
        try:
            os.system("iwlist scan >> /home/pi/wifilist")
            time.sleep(1)
            with open('/home/pi/wifilist') as openfileobject:
                for line in openfileobject:
                    if "ESSID" in line:
                        ssid = line.split(":")[1].replace('"', '').replace("\n", "")
                        wifi_list.append(ssid)
            print(wifi_list)
            return wifi_list
        except:
            return wifi_list

    def download_database(self):
        print("Downloading settings...")
        self.ui.updateStatusLabel.setText("Downloading settings...")
        self.settings_database.download()
        print("Downloading sequences...")
        self.ui.updateStatusLabel.setText("Downloading sequences...")
        self.sequences_database.download()
        print("Downloading sequence steps...")
        self.ui.updateStatusLabel.setText("Downloading sequence steps...")
        self.sequence_step_database.download()
        print("Downloading LED groups...")
        self.ui.updateStatusLabel.setText("Downloading LED groups...")
        self.led_groups_database.download()
        print("Downloading completed, please check log for full details.")
        self.ui.updateStatusLabel.setText("Downloading completed")

    def settings_list_selected(self, selected):
        if (selected == 0):
            self.ui.stackedWidget.setCurrentIndex(self.Network_status)
            self.ui.wifiavailableList.clear()
            self.wifilist = self.wifilistarray()
            # self.wifilist = ["Item 1","Item 2"]
            self.ui.wifiavailableList.setFont(QFont("Fixed", 20))
            self.ui.wifiavailableList.addItems(self.wifilist)
            self.ui.wifiavailableList.setCurrentRow(0)

    def nextClicked_settings(self):
        # ss = self.ui.menuList.selectedItems()
        # print(ss)
        self.app_log.info("main, settingsSelectbutton clicked")
        x = self.ui.settingsList.selectedIndexes()
        selected = x[0].row()
        self.settings_list_selected(selected)

    def wifi_next_clicked(self, selected):
        self.wifiselected = self.wifilist[selected]
        self.ui.stackedWidget.setCurrentIndex(self.password_input)
        self.showNormal()
        self.resize(322, 480)
        self.setGeometry(0, 0, 322, 479)
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setCursorPosition(0)
        try:
            # os.system("sh /home/pi/Desktop/code_1/keyboard_on_off.sh")
            os.system("sh {}".format(format(os.path.join(self.BASE_PATH, 'keyboard_on_off.sh'))))
        except FileNotFoundError:
            # subprocess.Popen(["killall", "matchbox-keyboard"])
            pass
        self.setWifiPasswordFocus()

    def setWifiPasswordFocus(self):
        self.ui.lineEdit.setFocus()

    def nextClicked_wifi(self):
        self.app_log.info("main, selectWiFiButton clicked")
        # ss = self.ui.menuList.selectedItems()
        # print(ss)
        # self.setGeometry(0, 0, 300, 460)
        x = self.ui.wifiavailableList.selectedIndexes()
        selected = x[0].row()
        print(self.wifilist[selected])
        self.wifi_next_clicked(selected)

    def led_sequnce_selected(self, selected):
        self.sequence_selected = self.sequence_list[selected]
        print(self.sequence_selected)
        sequence_id_active = self.sequence_id[selected]
        self.filesave_sequence(sequence_id_active)
        self.backtomain()
        # self.ui.stackedWidget.setCurrentIndex(self.menu_page)
        # self.ui.lightSourceInfo.setText(self.sequence_selected)

    def nextClicked_sequence(self):
        self.app_log.info("main, selectLedSeqButton clicked")
        # ss = self.ui.menuList.selectedItems()
        # print(ss)
        x = self.ui.sequenceList.selectedIndexes()
        selected = x[0].row()
        self.led_sequnce_selected(selected)

    def save_wifi(self):
        self.app_log.info("main, saveWifipassButton clicked")
        password = self.ui.lineEdit.text()
        print(password)
        ssid = self.wifiselected
        try:
            os.system("sh {}".format(format(os.path.join(self.BASE_PATH, 'keyboard_on_off.sh'))))
        except FileNotFoundError:
            pass
        # os.system("sudo sh /home/pi/Desktop/code_1/add_wifilist.sh " + ssid + " " + password)
        os.system("sudo sh {} ".format(format(os.path.join(self.BASE_PATH, 'add_wifilist.sh'))) + ssid + " " + password)
        self.showFullScreen()
        self.restartsystem()

        # restartbutton = QMessageBox()
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # restartbutton.setSizePolicy(sizePolicy)
        # buttonReply = restartbutton.question(self, 'Session', "Reboot your system now?",
        #                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # if buttonReply == QMessageBox.Yes:
        #     print('Yes clicked.')
        #     print("sudo reboot")
        # else:
        #     print('No clicked.')
        #     self.showFullScreen()
        #     self.ui.stackedWidget.setCurrentIndex(self.menu_page)
        # os.system("sudo reboot")



    def pinDataEvent(self, Rxdata):
        print('event test')
        print(Rxdata)
        print("stacked widget: ")
        current_page = self.ui.stackedWidget.currentIndex()
        if current_page == self.main_page:
            if Rxdata == '1':
                self.menubuttonClicked()
            if Rxdata == '2':
                self.process_light()
            if Rxdata == '3':
                self.light_source_update()
        elif current_page == self.menu_page:
            if Rxdata == '1':
                self.backtomain()
            if Rxdata == '2':
                self.nextClicked()
            if Rxdata == '3':
                self.selectClicked()
        elif current_page == self.setting_page:
            if Rxdata == '1':
                self.backtomenu()
            if Rxdata == '2':
                self.nextClicked_settings()
            if Rxdata == '3':
                self.settins_selectClicked()
        elif current_page == self.Led_sequence:
            if Rxdata == '1':
                self.backtomenu()
            if Rxdata == '2':
                self.nextClicked_sequence()
            if Rxdata == '3':
                self.sequence_selectClicked()
        elif current_page == self.brightness:
            if Rxdata == '1':
                self.brightness_increase()
            if Rxdata == '2':
                self.chage_image_brightness()
            if Rxdata == '3':
                self.brightness_decrease()
        elif current_page == self.screen_brightness:
            if Rxdata == '1':
                self.screen_brightness_increase()
            if Rxdata == '2':
                self.chage_screen_brightness()
            if Rxdata == '3':
                self.screen_brightness_decrease()
        elif current_page == self.Network_status:
            if Rxdata == '1':
                self.backtomenu()
            if Rxdata == '2':
                self.nextClicked_wifi()
            if Rxdata == '3':
                self.wifi_selectClicked()
        elif current_page == self.password_input:
            if Rxdata == '1':
                self.select_exitwifi_password()
            if Rxdata == '3':
                self.save_wifi()
        elif current_page == self.get_update:
            if Rxdata == '1':
                self.backtomenu()
            if Rxdata == '3':
                pass
        elif current_page == self.shutdown_page:
            if Rxdata == '1':
                self.backtomenu()
            if Rxdata == '3':
                self.cancelActionShutDownOrRestart()

        # if Rxdata == '4':
        #     self.ui.statusInfo.setText("Connected")
        #     self.ui.wifiStatus.setIcon(QtGui.QIcon('image_resources/wifiON_icon.ico'))
        #     self.ui.wifiStatus.setIconSize(QtCore.QSize(44, 40))
        # elif Rxdata == '5':
        #     self.ui.statusInfo.setText("Not Connected")
        #     self.ui.wifiStatus.setIcon(QtGui.QIcon('image_resources/wifiOFF_icon.png'))
        #     self.ui.wifiStatus.setIconSize(QtCore.QSize(44, 40))

        if Rxdata == 'stopped' and self.process_started:
            print("camera stopped")
            # self.phototocloud.process()
            self.photo_thread.signal_tx.emit("start")

    def photo_event(self, Rxdata):
        if (Rxdata == "finished"):
            # self.ui.lightSourceInfo.setText("processing {} ".format(Rxdata))
            self.ui.lightSourceInfo.setText("Ready")
            self.ui.cameraCapturinginfo.setText("Success!")
            # self.ui.pushButton.setIcon(QtGui.QIcon('/home/pi/Desktop/code_1/image_resources/tick_icon.png'))
            self.ui.pushButton.setIcon(QtGui.QIcon('{}'.format(os.path.join(self.BASE_PATH, 'image_resources/tick_icon.png'))))

        elif (Rxdata == "backtomaainpage"):
            self.pinThread.signal_tx.emit("start")
            self.ui.stackedWidget.setCurrentIndex(self.main_page)
            self.process_started = False
            self.step = 0


        elif (Rxdata == "connected"):
            self.ui.statusInfo.setText("Ready")
            # self.ui.wifiStatus.setIcon(QtGui.QIcon('/home/pi/Desktop/code_1/image_resources/wifiON_icon.png'))
            self.ui.wifiStatus.setIcon(QtGui.QIcon('{}'.format(os.path.join(self.BASE_PATH, 'image_resources/wifiON_icon.png'))))
            self.ui.wifiStatus.setIconSize(QtCore.QSize(44, 40))

        elif (Rxdata == "disconnected"):
            self.ui.statusInfo.setText("No WiFi connection")
            # self.ui.wifiStatus.setIcon(QtGui.QIcon('/home/pi/Desktop/code_1/image_resources/wifiOFF_icon.png'))
            self.ui.wifiStatus.setIcon(QtGui.QIcon('{}'.format(os.path.join(self.BASE_PATH, 'image_resources/wifiOFF_icon.png'))))
            self.ui.wifiStatus.setIconSize(QtCore.QSize(44, 40))

        elif "Downloading completed" in Rxdata:
            self.populate_sequence()
            self.ui.updateStatusLabel.setText(Rxdata)

        elif "Downloading failed" in Rxdata:
            self.populate_sequence()
            self.ui.updateStatusLabel.setText(Rxdata)

        elif "Downloading" in Rxdata:
            self.ui.updateStatusLabel.setText(Rxdata)

        elif "Low Battery" in Rxdata:
            self.ui.statusInfo.setText(Rxdata)

        elif "full mode" in Rxdata:
            print("Ready")
            pass
            # self.ui.statusInfo.setText("Ready")

        elif "Shutting down in" in Rxdata:
            # self.ui.shudownTimer.setText(Rxdata)
            Rxdata = Rxdata + " seconds"
            self.ui.shutdownstatus.setText(Rxdata)

        elif "Restart in " in Rxdata:
            # self.ui.shudownTimer.setText(Rxdata)
            Rxdata = Rxdata + " seconds"
            self.ui.shutdownstatus.setText(Rxdata)
        elif "Action Cancelled" in Rxdata:
            # self.ui.shudownTimer.setText(Rxdata)
            self.ui.shutdownstatus.setText(Rxdata)
            self.ui.stackedWidget.setCurrentIndex(self.shutdown_page)

        else:
            print("RX dataAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",Rxdata)
            # self.ui.lightSourceInfo.setText(self.sequence_selected + " " + Rxdata)
            # self.ui.cameraCapturinginfo.setText("Capturing Image")
            # print("sequnce id_ process light ", self.sequence_id)
            # print("sequnce id_ process light ", type(self.sequence_id))
            # self.set_led_group_name(int(Rxdata), self.sequence_id)


def main():
    '''
    Main app is run here
    :return:None
    '''
    app = QApplication(sys.argv)
    argv2 = app.arguments()
    ex = MyMainWindow(argv2)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
