# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 512)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(240, 320))
        MainWindow.setStyleSheet("/* ---------------------------------------------------------------------------\n"
"\n"
"    Created by the qtsass compiler\n"
"\n"
"    WARNING! All changes made in this file will be lost!\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* QDarkStyleSheet -----------------------------------------------------------\n"
"\n"
"This is the main style sheet, the palette has eight colors.\n"
"\n"
"It is based on three selecting colors, three greyish (background) colors\n"
"plus three whitish (foreground) colors. Each set of widgets of the same\n"
"type have a header like this:\n"
"\n"
"    ------------------\n"
"    GroupName --------\n"
"    ------------------\n"
"\n"
"And each widget is separated with a header like this:\n"
"\n"
"    QWidgetName ------\n"
"\n"
"This makes more easy to find and change some css field. The basic\n"
"configuration is described bellow.\n"
"\n"
"    BACKGROUND -----------\n"
"\n"
"        Light  #4D545B #505F69 (unpressed)\n"
"        Normal #31363B #32414B (border, disabled, pressed, checked, toolbars, menus)\n"
"        Dark   #232629 #19232D (background)\n"
"\n"
"    FOREGROUND -----------\n"
"\n"
"        Light  #EFF0F1 #F0F0F0 (texts/labels)\n"
"        Normal         #AAAAAA (not used yet)\n"
"        Dark   #505F69 #787878 (disabled texts)\n"
"\n"
"    SELECTION ------------\n"
"\n"
"        Light  #179AE0 #148CD2 (selection/hover/active)\n"
"        Normal #3375A3 #1464A0 (selected)\n"
"        Dark   #18465D #14506E (selected disabled)\n"
"\n"
"If a stranger configuration is required because of a bugfix or anything\n"
"else, keep the comment on the line above so nobody changes it, including the\n"
"issue number.\n"
"\n"
"*/\n"
"/*\n"
"\n"
"See Qt documentation:\n"
"\n"
"  - https://doc.qt.io/qt-5/stylesheet.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-reference.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-examples.html\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* QWidget ----------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QWidget {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"  selection-background-color: #14506E;\n"
"  selection-color: #787878;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QWidget::item:hover {\n"
"  background-color: #148CD2;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QMainWindow ------------------------------------------------------------\n"
"\n"
"This adjusts the splitter in the dock widget, not qsplitter\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMainWindow::separator {\n"
"  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"  background-color: #505F69;\n"
"  border: 0px solid #148CD2;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"  width: 5px;\n"
"  margin-top: 2px;\n"
"  margin-bottom: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"  height: 5px;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"/* QToolTip ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtooltip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolTip {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"/* QStatusBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStatusBar {\n"
"  border: 1px solid #32414B;\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: #32414B;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: transparent;\n"
"}\n"
"\n"
"/* QCheckBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
"  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 4px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:focus, QCheckBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:focus, QCheckBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus, QCheckBox::indicator:indeterminate:hover, QCheckBox::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"/* QGroupBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGroupBox {\n"
"  font-weight: bold;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 4px;\n"
"  margin-top: 16px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 3px;\n"
"  padding-left: 3px;\n"
"  padding-right: 5px;\n"
"  padding-top: 8px;\n"
"  padding-bottom: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QRadioButton -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QRadioButton {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
"  padding: 0px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton QWidget {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  border: none;\n"
"  outline: none;\n"
"  margin-left: 4px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QRadioButton::indicator:unchecked:focus, QRadioButton::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QRadioButton::indicator:checked:focus, QRadioButton::indicator:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QMenuBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenuBar {\n"
"  background-color: #32414B;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #32414B;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #32414B;\n"
"  background-color: #148CD2;\n"
"  color: #F0F0F0;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu {\n"
"  border: 0px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  margin: 0px;\n"
"  padding-left: 4px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #32414B;\n"
"  padding: 4px 24px 4px 24px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  padding-left: 6px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"  margin: 5px;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractItemView {\n"
"  alternate-background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"  padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ----------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractScrollArea {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  /* fix #159 */\n"
"  min-height: 1.25em;\n"
"  /* fix #159 */\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollArea QWidget QWidget:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #19232D;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/qss_icons/rc/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWidget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #32414B;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #32414B;\n"
"  border-bottom: 1px solid #19232D;\n"
"  padding: 2px;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QToolBar QToolButton {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBar QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked {\n"
"  border: 1px solid #19232D;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
"  background: #32414B;\n"
"  border: 0px;\n"
"  color: #F0F0F0;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"/* QAbstractSpinBox -------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractSpinBox {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-radius: 4px;\n"
"  /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  border-left: 1px solid #32414B;\n"
"  margin: 1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: bottom right;\n"
"  border-left: 1px solid #32414B;\n"
"  margin: 1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS --------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLabel::disabled {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QTextBrowser -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextBrowser {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser::selected, QTextBrowser::pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QGraphicsView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGraphicsView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView::selected, QGraphicsView::pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCalendarWidget --------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCalendarWidget {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QLCDNumber -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLCDNumber {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLCDNumber:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QProgressBar -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #1464A0;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #14506E;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS ---------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QPushButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPushButton {\n"
"  background-color: #505F69;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QPushButton:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
"  bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolButton {\n"
"  background-color: transparent;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
"  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background-color: transparent;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QToolButton:checked:disabled {\n"
"  border: 1px solid #14506E;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  margin: 1px;\n"
"  background-color: transparent;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton:disabled:hover {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"  padding: 2px;\n"
"  /* Only for MenuButtonPopup */\n"
"  padding-right: 12px;\n"
"  /* Make way for the popup button */\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"  padding: 2px;\n"
"  /* Only for InstantPopup */\n"
"  padding-right: 12px;\n"
"  /* Make way for the popup button */\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"  padding: 2px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  border-top-right-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  /* 16px width + 4px for border = 20px allocated above */\n"
"  width: 16px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-button:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  top: -8px;\n"
"  /* Shift it a bit */\n"
"  left: -4px;\n"
"  /* Shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCommandLinkButton -----------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCommandLinkButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"  background-color: transparent;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QComboBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QComboBox {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  selection-background-color: #1464A0;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  selection-color: #148CD2;\n"
"  selection-background-color: #32414B;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  selection-background-color: #19232D;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"  background-color: transparent;\n"
"  selection-background-color: transparent;\n"
"  color: transparent;\n"
"  selection-color: transparent;\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox::indicator:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:checked {\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"  border: 0px solid transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 20px;\n"
"  border-left-width: 0px;\n"
"  border-left-color: #32414B;\n"
"  border-left-style: solid;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"/* QSlider ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSlider:disabled {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"  background: #1464A0;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical :disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: #1464A0;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: -8px 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: 0 -8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabWidget {\n"
"  padding: 2px;\n"
"  selection-background-color: #32414B;\n"
"  /* Add wanted borders - fix #141, #126, #123 */\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  border: 0px solid #32414B;\n"
"}\n"
"\n"
"QTabWidget QWidget QWidget\n"
"QTableView,\n"
"QTabWidget QTreeView,\n"
"QTabWidget QListView,\n"
"QTabWidget QGroupBox,\n"
"QTabWidget QLineEdit,\n"
"QTabWidget QComboBox,\n"
"QTabWidget QFontComboBox,\n"
"QTabWidget QTextEdit,\n"
"QTabWidget QSpinBox,\n"
"QTabWidget QDoubleSpinBox {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane wit pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QTabBar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"  border: 0;\n"
"  margin: 2px;\n"
"  padding: 2px;\n"
"  image: url(\":/qss_icons/rc/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"/* QTabBar::tab - selected ------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar::tab {\n"
"  /* !selected and disabled ----------------------------------------- */\n"
"  /* selected ------------------------------------------------------- */\n"
"}\n"
"\n"
"QTabBar::tab:top:selected:disabled {\n"
"  border-bottom: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled {\n"
"  border-top: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:disabled {\n"
"  border-right: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled {\n"
"  border-left: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:disabled {\n"
"  border-bottom: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled {\n"
"  border-top: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled {\n"
"  border-right: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled {\n"
"  border-left: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"  border-bottom: 2px solid #19232D;\n"
"  margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"  border-top: 2px solid #19232D;\n"
"  margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"  border-left: 2px solid #19232D;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"  border-right: 2px solid #19232D;\n"
"  margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  min-width: 5px;\n"
"  border-bottom: 3px solid #32414B;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"  border-bottom: 3px solid #1464A0;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-bottom: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom {\n"
"  color: #F0F0F0;\n"
"  border-top: 3px solid #32414B;\n"
"  background-color: #32414B;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-top: 3px solid #1464A0;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-top: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-left-radius: 3px;\n"
"  border-bottom-left-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-right: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-right: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-left: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-left: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color: #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #32414B;\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: url(\":/qss_icons/rc/window_close.png\");\n"
"  titlebar-normal-icon: url(\":/qss_icons/rc/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Better size for title bar */\n"
"  padding: 6px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_undock_pressed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView -----------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/qss_icons/rc/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_closed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
"QListView::indicator:checked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView,\n"
"QTableView,\n"
"QColumnView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  gridline-color: #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTreeView:disabled,\n"
"QListView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QListView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QTreeView::hover,\n"
"QListView::hover,\n"
"QTableView::hover,\n"
"QColumnView::hover {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QTreeView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QTreeView::item:selected:hover,\n"
"QListView::item:selected:hover,\n"
"QTableView::item:selected:hover,\n"
"QColumnView::item:selected:hover {\n"
"  background: #1464A0;\n"
"  color: #19232D;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:selected:active {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"  outline: 0;\n"
"  color: #148CD2;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #19232D;\n"
"  border: 1px transparent #32414B;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QHeaderView {\n"
"  background-color: #32414B;\n"
"  border: 0px transparent #32414B;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"QHeaderView:disabled {\n"
"  background-color: #32414B;\n"
"  border: 1px transparent #32414B;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  padding: 2px;\n"
"  border-radius: 0px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"  color: #F0F0F0;\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QHeaderView::section:checked:disabled {\n"
"  color: #787878;\n"
"  background-color: #14506E;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"  border-left: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {\n"
"  border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"  border-top: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {\n"
"  border-top: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"  /* Those settings (border/width/height/background-color) solve bug */\n"
"  /* transparent arrow background and size */\n"
"  background-color: #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  background-color: #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"/* QToolBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBox {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::selected {\n"
"  padding: 0px;\n"
"  border: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  background-color: #505F69;\n"
"  border-bottom: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #14506E;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"  border-color: #148CD2;\n"
"  border-bottom: 2px solid #148CD2;\n"
"}\n"
"\n"
"QToolBox QScrollArea QWidget QWidget {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QFrame -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
".QFrame {\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
".QFrame[frameShape=\"0\"] {\n"
"  border-radius: 4px;\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
".QFrame[height=\"3\"], .QFrame[width=\"3\"] {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QSplitter --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSplitter {\n"
"  background-color: #32414B;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::separator {\n"
"  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 1px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::separator:hover {\n"
"  background-color: #787878;\n"
"}\n"
"\n"
"QSplitter::separator:horizontal {\n"
"  width: 5px;\n"
"  image: url(\":/qss_icons/rc/line_vertical.png\");\n"
"}\n"
"\n"
"QSplitter::separator:vertical {\n"
"  height: 5px;\n"
"  image: url(\":/qss_icons/rc/line_horizontal.png\");\n"
"}\n"
"\n"
"/* QDateEdit --------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDateEdit {\n"
"  selection-background-color: #1464A0;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:on {\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 20px;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QAbstractView:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"PlotWidget {\n"
"  /* Fix cut labels in plots #134 */\n"
"  padding: 0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainPage)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.statusInfo = QtWidgets.QLabel(self.mainPage)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusInfo.setFont(font)
        self.statusInfo.setObjectName("statusInfo")
        self.horizontalLayout_2.addWidget(self.statusInfo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.wifiStatus = QtWidgets.QPushButton(self.mainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiStatus.sizePolicy().hasHeightForWidth())
        self.wifiStatus.setSizePolicy(sizePolicy)
        self.wifiStatus.setStyleSheet("background: transparent;")
        self.wifiStatus.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/wifiON_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wifiStatus.setIcon(icon)
        self.wifiStatus.setIconSize(QtCore.QSize(32, 32))
        self.wifiStatus.setFlat(True)
        self.wifiStatus.setObjectName("wifiStatus")
        self.horizontalLayout_2.addWidget(self.wifiStatus)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lightSourceInfo = QtWidgets.QLabel(self.mainPage)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lightSourceInfo.setFont(font)
        self.lightSourceInfo.setObjectName("lightSourceInfo")
        self.horizontalLayout_3.addWidget(self.lightSourceInfo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuWidget = QtWidgets.QWidget(self.mainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuWidget.sizePolicy().hasHeightForWidth())
        self.menuWidget.setSizePolicy(sizePolicy)
        self.menuWidget.setObjectName("menuWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuButton = QtWidgets.QPushButton(self.menuWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setMinimumSize(QtCore.QSize(0, 75))
        self.menuButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menuButton.setStyleSheet("background: transparent;")
        self.menuButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon1)
        self.menuButton.setIconSize(QtCore.QSize(48, 48))
        self.menuButton.setDefault(False)
        self.menuButton.setFlat(True)
        self.menuButton.setObjectName("menuButton")
        self.verticalLayout.addWidget(self.menuButton)
        self.label_3 = QtWidgets.QLabel(self.menuWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.menuWidget)
        self.takePhotoWidget = QtWidgets.QWidget(self.mainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takePhotoWidget.sizePolicy().hasHeightForWidth())
        self.takePhotoWidget.setSizePolicy(sizePolicy)
        self.takePhotoWidget.setObjectName("takePhotoWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.takePhotoWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.takePhotoButton = QtWidgets.QPushButton(self.takePhotoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takePhotoButton.sizePolicy().hasHeightForWidth())
        self.takePhotoButton.setSizePolicy(sizePolicy)
        self.takePhotoButton.setMinimumSize(QtCore.QSize(0, 75))
        self.takePhotoButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.takePhotoButton.setStyleSheet("background: transparent;")
        self.takePhotoButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/photoIcon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.takePhotoButton.setIcon(icon2)
        self.takePhotoButton.setIconSize(QtCore.QSize(48, 48))
        self.takePhotoButton.setFlat(True)
        self.takePhotoButton.setObjectName("takePhotoButton")
        self.verticalLayout_2.addWidget(self.takePhotoButton)
        self.label_4 = QtWidgets.QLabel(self.takePhotoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addWidget(self.takePhotoWidget)
        self.lightSourceButton = QtWidgets.QWidget(self.mainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightSourceButton.sizePolicy().hasHeightForWidth())
        self.lightSourceButton.setSizePolicy(sizePolicy)
        self.lightSourceButton.setObjectName("lightSourceButton")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lightSourceButton)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lightSourcepushbutton = QtWidgets.QPushButton(self.lightSourceButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightSourcepushbutton.sizePolicy().hasHeightForWidth())
        self.lightSourcepushbutton.setSizePolicy(sizePolicy)
        self.lightSourcepushbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.lightSourcepushbutton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lightSourcepushbutton.setStyleSheet("background: transparent;")
        self.lightSourcepushbutton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/double_arrow_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lightSourcepushbutton.setIcon(icon3)
        self.lightSourcepushbutton.setIconSize(QtCore.QSize(48, 48))
        self.lightSourcepushbutton.setFlat(True)
        self.lightSourcepushbutton.setObjectName("lightSourcepushbutton")
        self.verticalLayout_3.addWidget(self.lightSourcepushbutton)
        self.label_5 = QtWidgets.QLabel(self.lightSourceButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.lightSourceButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.mainPage)
        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setObjectName("menuPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.menuPage)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.menuPage)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.menuList = QtWidgets.QListWidget(self.menuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuList.sizePolicy().hasHeightForWidth())
        self.menuList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menuList.setFont(font)
        self.menuList.setLineWidth(1)
        self.menuList.setAutoScrollMargin(0)
        self.menuList.setObjectName("menuList")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.menuList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.menuList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.menuList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.menuList.addItem(item)
        self.verticalLayout_8.addWidget(self.menuList)
        self.label_32 = QtWidgets.QLabel(self.menuPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_8.addWidget(self.label_32)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.exitButton = QtWidgets.QWidget(self.menuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QtCore.QSize(70, 0))
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.exitButton)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.menuExitButton = QtWidgets.QPushButton(self.exitButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuExitButton.sizePolicy().hasHeightForWidth())
        self.menuExitButton.setSizePolicy(sizePolicy)
        self.menuExitButton.setMinimumSize(QtCore.QSize(0, 75))
        self.menuExitButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menuExitButton.setStyleSheet("background: transparent;")
        self.menuExitButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuExitButton.setIcon(icon4)
        self.menuExitButton.setIconSize(QtCore.QSize(48, 48))
        self.menuExitButton.setDefault(False)
        self.menuExitButton.setFlat(True)
        self.menuExitButton.setObjectName("menuExitButton")
        self.verticalLayout_5.addWidget(self.menuExitButton)
        self.label_6 = QtWidgets.QLabel(self.exitButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.exitButton)
        self.selectButton = QtWidgets.QWidget(self.menuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton.sizePolicy().hasHeightForWidth())
        self.selectButton.setSizePolicy(sizePolicy)
        self.selectButton.setMinimumSize(QtCore.QSize(70, 0))
        self.selectButton.setObjectName("selectButton")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.selectButton)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.menuSelectButton = QtWidgets.QPushButton(self.selectButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuSelectButton.sizePolicy().hasHeightForWidth())
        self.menuSelectButton.setSizePolicy(sizePolicy)
        self.menuSelectButton.setMinimumSize(QtCore.QSize(0, 75))
        self.menuSelectButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menuSelectButton.setStyleSheet("background: transparent;")
        self.menuSelectButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/select_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSelectButton.setIcon(icon5)
        self.menuSelectButton.setIconSize(QtCore.QSize(48, 48))
        self.menuSelectButton.setFlat(True)
        self.menuSelectButton.setObjectName("menuSelectButton")
        self.verticalLayout_6.addWidget(self.menuSelectButton)
        self.label_7 = QtWidgets.QLabel(self.selectButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_5.addWidget(self.selectButton)
        self.nextWidget = QtWidgets.QWidget(self.menuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextWidget.sizePolicy().hasHeightForWidth())
        self.nextWidget.setSizePolicy(sizePolicy)
        self.nextWidget.setMinimumSize(QtCore.QSize(70, 0))
        self.nextWidget.setObjectName("nextWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.nextWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.menuNextbutton = QtWidgets.QPushButton(self.nextWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuNextbutton.sizePolicy().hasHeightForWidth())
        self.menuNextbutton.setSizePolicy(sizePolicy)
        self.menuNextbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.menuNextbutton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menuNextbutton.setStyleSheet("background: transparent;")
        self.menuNextbutton.setText("")
        self.menuNextbutton.setIcon(icon3)
        self.menuNextbutton.setIconSize(QtCore.QSize(48, 48))
        self.menuNextbutton.setFlat(True)
        self.menuNextbutton.setObjectName("menuNextbutton")
        self.verticalLayout_7.addWidget(self.menuNextbutton)
        self.nextLabel = QtWidgets.QLabel(self.nextWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel.sizePolicy().hasHeightForWidth())
        self.nextLabel.setSizePolicy(sizePolicy)
        self.nextLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nextLabel.setFont(font)
        self.nextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel.setWordWrap(True)
        self.nextLabel.setObjectName("nextLabel")
        self.verticalLayout_7.addWidget(self.nextLabel)
        self.horizontalLayout_5.addWidget(self.nextWidget)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.menuPage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.settingsPage)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_28 = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_39.addWidget(self.label_28)
        self.settingsList = QtWidgets.QListWidget(self.settingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsList.sizePolicy().hasHeightForWidth())
        self.settingsList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.settingsList.setFont(font)
        self.settingsList.setLineWidth(1)
        self.settingsList.setAutoScrollMargin(0)
        self.settingsList.setObjectName("settingsList")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(30)
        item.setFont(font)
        self.settingsList.addItem(item)
        self.verticalLayout_39.addWidget(self.settingsList)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_39.addItem(spacerItem4)
        self.label_30 = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_39.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.settingsPage)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_39.addWidget(self.label_31)
        spacerItem5 = QtWidgets.QSpacerItem(20, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_39.addItem(spacerItem5)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.exitButton_10 = QtWidgets.QWidget(self.settingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_10.sizePolicy().hasHeightForWidth())
        self.exitButton_10.setSizePolicy(sizePolicy)
        self.exitButton_10.setMinimumSize(QtCore.QSize(70, 0))
        self.exitButton_10.setObjectName("exitButton_10")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.exitButton_10)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.settingsExitbutton = QtWidgets.QPushButton(self.exitButton_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsExitbutton.sizePolicy().hasHeightForWidth())
        self.settingsExitbutton.setSizePolicy(sizePolicy)
        self.settingsExitbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.settingsExitbutton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settingsExitbutton.setStyleSheet("background: transparent;")
        self.settingsExitbutton.setText("")
        self.settingsExitbutton.setIcon(icon4)
        self.settingsExitbutton.setIconSize(QtCore.QSize(48, 48))
        self.settingsExitbutton.setDefault(False)
        self.settingsExitbutton.setFlat(True)
        self.settingsExitbutton.setObjectName("settingsExitbutton")
        self.verticalLayout_36.addWidget(self.settingsExitbutton)
        self.label_27 = QtWidgets.QLabel(self.exitButton_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_36.addWidget(self.label_27)
        self.horizontalLayout_16.addWidget(self.exitButton_10)
        self.selectButton_7 = QtWidgets.QWidget(self.settingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_7.sizePolicy().hasHeightForWidth())
        self.selectButton_7.setSizePolicy(sizePolicy)
        self.selectButton_7.setMinimumSize(QtCore.QSize(70, 0))
        self.selectButton_7.setObjectName("selectButton_7")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.selectButton_7)
        self.verticalLayout_38.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.settingsSelectbutton = QtWidgets.QPushButton(self.selectButton_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsSelectbutton.sizePolicy().hasHeightForWidth())
        self.settingsSelectbutton.setSizePolicy(sizePolicy)
        self.settingsSelectbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.settingsSelectbutton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settingsSelectbutton.setStyleSheet("background: transparent;")
        self.settingsSelectbutton.setText("")
        self.settingsSelectbutton.setIcon(icon5)
        self.settingsSelectbutton.setIconSize(QtCore.QSize(48, 48))
        self.settingsSelectbutton.setFlat(True)
        self.settingsSelectbutton.setObjectName("settingsSelectbutton")
        self.verticalLayout_38.addWidget(self.settingsSelectbutton)
        self.label_29 = QtWidgets.QLabel(self.selectButton_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_38.addWidget(self.label_29)
        self.horizontalLayout_16.addWidget(self.selectButton_7)
        self.nextWidget_4 = QtWidgets.QWidget(self.settingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextWidget_4.sizePolicy().hasHeightForWidth())
        self.nextWidget_4.setSizePolicy(sizePolicy)
        self.nextWidget_4.setMinimumSize(QtCore.QSize(70, 0))
        self.nextWidget_4.setObjectName("nextWidget_4")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.nextWidget_4)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.settingsNextbutton = QtWidgets.QPushButton(self.nextWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsNextbutton.sizePolicy().hasHeightForWidth())
        self.settingsNextbutton.setSizePolicy(sizePolicy)
        self.settingsNextbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.settingsNextbutton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.settingsNextbutton.setStyleSheet("background: transparent;")
        self.settingsNextbutton.setText("")
        self.settingsNextbutton.setIcon(icon3)
        self.settingsNextbutton.setIconSize(QtCore.QSize(48, 48))
        self.settingsNextbutton.setFlat(True)
        self.settingsNextbutton.setObjectName("settingsNextbutton")
        self.verticalLayout_37.addWidget(self.settingsNextbutton)
        self.nextLabel_7 = QtWidgets.QLabel(self.nextWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel_7.sizePolicy().hasHeightForWidth())
        self.nextLabel_7.setSizePolicy(sizePolicy)
        self.nextLabel_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nextLabel_7.setFont(font)
        self.nextLabel_7.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel_7.setWordWrap(True)
        self.nextLabel_7.setObjectName("nextLabel_7")
        self.verticalLayout_37.addWidget(self.nextLabel_7)
        self.horizontalLayout_16.addWidget(self.nextWidget_4)
        self.verticalLayout_39.addLayout(self.horizontalLayout_16)
        self.stackedWidget.addWidget(self.settingsPage)
        self.changeSequencePage = QtWidgets.QWidget()
        self.changeSequencePage.setObjectName("changeSequencePage")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.changeSequencePage)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_16 = QtWidgets.QLabel(self.changeSequencePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_35.addWidget(self.label_16)
        self.sequenceList = QtWidgets.QListWidget(self.changeSequencePage)
        self.sequenceList.setObjectName("sequenceList")
        item = QtWidgets.QListWidgetItem()
        self.sequenceList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.sequenceList.addItem(item)
        self.verticalLayout_35.addWidget(self.sequenceList)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_35.addItem(spacerItem6)
        self.updateSequenceButton = QtWidgets.QPushButton(self.changeSequencePage)
        self.updateSequenceButton.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.updateSequenceButton.setFont(font)
        self.updateSequenceButton.setObjectName("updateSequenceButton")
        self.verticalLayout_35.addWidget(self.updateSequenceButton)
        self.updateStatusLabel = QtWidgets.QLabel(self.changeSequencePage)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.updateStatusLabel.setFont(font)
        self.updateStatusLabel.setObjectName("updateStatusLabel")
        self.verticalLayout_35.addWidget(self.updateStatusLabel)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.exitButton_7 = QtWidgets.QWidget(self.changeSequencePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_7.sizePolicy().hasHeightForWidth())
        self.exitButton_7.setSizePolicy(sizePolicy)
        self.exitButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.exitButton_7.setObjectName("exitButton_7")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.exitButton_7)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.exitLedSeqButton = QtWidgets.QPushButton(self.exitButton_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitLedSeqButton.sizePolicy().hasHeightForWidth())
        self.exitLedSeqButton.setSizePolicy(sizePolicy)
        self.exitLedSeqButton.setMinimumSize(QtCore.QSize(0, 75))
        self.exitLedSeqButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitLedSeqButton.setStyleSheet("background: transparent;")
        self.exitLedSeqButton.setText("")
        self.exitLedSeqButton.setIcon(icon4)
        self.exitLedSeqButton.setIconSize(QtCore.QSize(48, 48))
        self.exitLedSeqButton.setDefault(False)
        self.exitLedSeqButton.setFlat(True)
        self.exitLedSeqButton.setObjectName("exitLedSeqButton")
        self.verticalLayout_26.addWidget(self.exitLedSeqButton)
        self.label_15 = QtWidgets.QLabel(self.exitButton_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_26.addWidget(self.label_15)
        self.horizontalLayout_13.addWidget(self.exitButton_7)
        self.selectButton_8 = QtWidgets.QWidget(self.changeSequencePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_8.sizePolicy().hasHeightForWidth())
        self.selectButton_8.setSizePolicy(sizePolicy)
        self.selectButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.selectButton_8.setObjectName("selectButton_8")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.selectButton_8)
        self.verticalLayout_28.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.selectLedSeqButton = QtWidgets.QPushButton(self.selectButton_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectLedSeqButton.sizePolicy().hasHeightForWidth())
        self.selectLedSeqButton.setSizePolicy(sizePolicy)
        self.selectLedSeqButton.setMinimumSize(QtCore.QSize(0, 75))
        self.selectLedSeqButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectLedSeqButton.setStyleSheet("background: transparent;")
        self.selectLedSeqButton.setText("")
        self.selectLedSeqButton.setIcon(icon5)
        self.selectLedSeqButton.setIconSize(QtCore.QSize(48, 48))
        self.selectLedSeqButton.setFlat(True)
        self.selectLedSeqButton.setObjectName("selectLedSeqButton")
        self.verticalLayout_28.addWidget(self.selectLedSeqButton)
        self.label_24 = QtWidgets.QLabel(self.selectButton_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_28.addWidget(self.label_24)
        self.horizontalLayout_13.addWidget(self.selectButton_8)
        self.nextWidget_3 = QtWidgets.QWidget(self.changeSequencePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextWidget_3.sizePolicy().hasHeightForWidth())
        self.nextWidget_3.setSizePolicy(sizePolicy)
        self.nextWidget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.nextWidget_3.setObjectName("nextWidget_3")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.nextWidget_3)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.nextLedSeqButton = QtWidgets.QPushButton(self.nextWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLedSeqButton.sizePolicy().hasHeightForWidth())
        self.nextLedSeqButton.setSizePolicy(sizePolicy)
        self.nextLedSeqButton.setMinimumSize(QtCore.QSize(0, 75))
        self.nextLedSeqButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextLedSeqButton.setStyleSheet("background: transparent;")
        self.nextLedSeqButton.setText("")
        self.nextLedSeqButton.setIcon(icon3)
        self.nextLedSeqButton.setIconSize(QtCore.QSize(48, 48))
        self.nextLedSeqButton.setFlat(True)
        self.nextLedSeqButton.setObjectName("nextLedSeqButton")
        self.verticalLayout_27.addWidget(self.nextLedSeqButton)
        self.nextLabel_6 = QtWidgets.QLabel(self.nextWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel_6.sizePolicy().hasHeightForWidth())
        self.nextLabel_6.setSizePolicy(sizePolicy)
        self.nextLabel_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nextLabel_6.setFont(font)
        self.nextLabel_6.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel_6.setWordWrap(True)
        self.nextLabel_6.setObjectName("nextLabel_6")
        self.verticalLayout_27.addWidget(self.nextLabel_6)
        self.horizontalLayout_13.addWidget(self.nextWidget_3)
        self.verticalLayout_35.addLayout(self.horizontalLayout_13)
        self.stackedWidget.addWidget(self.changeSequencePage)
        self.imageBrightnessPage = QtWidgets.QWidget()
        self.imageBrightnessPage.setObjectName("imageBrightnessPage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.imageBrightnessPage)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.imageBrightnessPage)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.imageBrightnessbox = QtWidgets.QSpinBox(self.imageBrightnessPage)
        font = QtGui.QFont()
        font.setPointSize(38)
        self.imageBrightnessbox.setFont(font)
        self.imageBrightnessbox.setMaximum(100)
        self.imageBrightnessbox.setProperty("value", 10)
        self.imageBrightnessbox.setObjectName("imageBrightnessbox")
        self.horizontalLayout_7.addWidget(self.imageBrightnessbox)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        spacerItem10 = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.exitButton_2 = QtWidgets.QWidget(self.imageBrightnessPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_2.sizePolicy().hasHeightForWidth())
        self.exitButton_2.setSizePolicy(sizePolicy)
        self.exitButton_2.setMinimumSize(QtCore.QSize(70, 0))
        self.exitButton_2.setObjectName("exitButton_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.exitButton_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.exitImageBrightnessButton = QtWidgets.QPushButton(self.exitButton_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitImageBrightnessButton.sizePolicy().hasHeightForWidth())
        self.exitImageBrightnessButton.setSizePolicy(sizePolicy)
        self.exitImageBrightnessButton.setMinimumSize(QtCore.QSize(0, 75))
        self.exitImageBrightnessButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitImageBrightnessButton.setStyleSheet("background: transparent;")
        self.exitImageBrightnessButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/add_circle_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitImageBrightnessButton.setIcon(icon6)
        self.exitImageBrightnessButton.setIconSize(QtCore.QSize(48, 48))
        self.exitImageBrightnessButton.setDefault(False)
        self.exitImageBrightnessButton.setFlat(True)
        self.exitImageBrightnessButton.setObjectName("exitImageBrightnessButton")
        self.verticalLayout_9.addWidget(self.exitImageBrightnessButton)
        self.label_8 = QtWidgets.QLabel(self.exitButton_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.horizontalLayout_6.addWidget(self.exitButton_2)
        self.selectButton_2 = QtWidgets.QWidget(self.imageBrightnessPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_2.sizePolicy().hasHeightForWidth())
        self.selectButton_2.setSizePolicy(sizePolicy)
        self.selectButton_2.setMinimumSize(QtCore.QSize(70, 0))
        self.selectButton_2.setObjectName("selectButton_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.selectButton_2)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.selectImageBrightnessButton = QtWidgets.QPushButton(self.selectButton_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectImageBrightnessButton.sizePolicy().hasHeightForWidth())
        self.selectImageBrightnessButton.setSizePolicy(sizePolicy)
        self.selectImageBrightnessButton.setMinimumSize(QtCore.QSize(0, 75))
        self.selectImageBrightnessButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectImageBrightnessButton.setStyleSheet("background: transparent;")
        self.selectImageBrightnessButton.setText("")
        self.selectImageBrightnessButton.setIcon(icon5)
        self.selectImageBrightnessButton.setIconSize(QtCore.QSize(48, 48))
        self.selectImageBrightnessButton.setFlat(True)
        self.selectImageBrightnessButton.setObjectName("selectImageBrightnessButton")
        self.verticalLayout_10.addWidget(self.selectImageBrightnessButton)
        self.nextLabel_2 = QtWidgets.QLabel(self.selectButton_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel_2.sizePolicy().hasHeightForWidth())
        self.nextLabel_2.setSizePolicy(sizePolicy)
        self.nextLabel_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel_2.setWordWrap(True)
        self.nextLabel_2.setObjectName("nextLabel_2")
        self.verticalLayout_10.addWidget(self.nextLabel_2)
        self.horizontalLayout_6.addWidget(self.selectButton_2)
        self.nextButton_2 = QtWidgets.QWidget(self.imageBrightnessPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton_2.sizePolicy().hasHeightForWidth())
        self.nextButton_2.setSizePolicy(sizePolicy)
        self.nextButton_2.setMinimumSize(QtCore.QSize(70, 0))
        self.nextButton_2.setObjectName("nextButton_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.nextButton_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.brightnessLessButton = QtWidgets.QPushButton(self.nextButton_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightnessLessButton.sizePolicy().hasHeightForWidth())
        self.brightnessLessButton.setSizePolicy(sizePolicy)
        self.brightnessLessButton.setMinimumSize(QtCore.QSize(0, 75))
        self.brightnessLessButton.setStyleSheet("background: transparent;")
        self.brightnessLessButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/minus-circle_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brightnessLessButton.setIcon(icon7)
        self.brightnessLessButton.setIconSize(QtCore.QSize(48, 48))
        self.brightnessLessButton.setObjectName("brightnessLessButton")
        self.verticalLayout_11.addWidget(self.brightnessLessButton)
        self.label_18 = QtWidgets.QLabel(self.nextButton_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_11.addWidget(self.label_18)
        self.horizontalLayout_6.addWidget(self.nextButton_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.imageBrightnessPage)
        self.screenBrightnessPage = QtWidgets.QWidget()
        self.screenBrightnessPage.setObjectName("screenBrightnessPage")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.screenBrightnessPage)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_2 = QtWidgets.QLabel(self.screenBrightnessPage)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_16.addWidget(self.label_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.spinBox_2 = QtWidgets.QSpinBox(self.screenBrightnessPage)
        font = QtGui.QFont()
        font.setPointSize(38)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setProperty("value", 10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_8.addWidget(self.spinBox_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.verticalLayout_16.addLayout(self.horizontalLayout_8)
        spacerItem14 = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.exitButton_3 = QtWidgets.QWidget(self.screenBrightnessPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_3.sizePolicy().hasHeightForWidth())
        self.exitButton_3.setSizePolicy(sizePolicy)
        self.exitButton_3.setMinimumSize(QtCore.QSize(70, 0))
        self.exitButton_3.setObjectName("exitButton_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.exitButton_3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.exitScreenBrightnessButton = QtWidgets.QPushButton(self.exitButton_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitScreenBrightnessButton.sizePolicy().hasHeightForWidth())
        self.exitScreenBrightnessButton.setSizePolicy(sizePolicy)
        self.exitScreenBrightnessButton.setMinimumSize(QtCore.QSize(0, 75))
        self.exitScreenBrightnessButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitScreenBrightnessButton.setStyleSheet("background: transparent;")
        self.exitScreenBrightnessButton.setText("")
        self.exitScreenBrightnessButton.setIcon(icon6)
        self.exitScreenBrightnessButton.setIconSize(QtCore.QSize(48, 48))
        self.exitScreenBrightnessButton.setDefault(False)
        self.exitScreenBrightnessButton.setFlat(True)
        self.exitScreenBrightnessButton.setObjectName("exitScreenBrightnessButton")
        self.verticalLayout_13.addWidget(self.exitScreenBrightnessButton)
        self.label_9 = QtWidgets.QLabel(self.exitButton_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.horizontalLayout_9.addWidget(self.exitButton_3)
        self.selectButton_3 = QtWidgets.QWidget(self.screenBrightnessPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_3.sizePolicy().hasHeightForWidth())
        self.selectButton_3.setSizePolicy(sizePolicy)
        self.selectButton_3.setMinimumSize(QtCore.QSize(70, 0))
        self.selectButton_3.setObjectName("selectButton_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.selectButton_3)
        self.verticalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.selectScreenBrightnessButton = QtWidgets.QPushButton(self.selectButton_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectScreenBrightnessButton.sizePolicy().hasHeightForWidth())
        self.selectScreenBrightnessButton.setSizePolicy(sizePolicy)
        self.selectScreenBrightnessButton.setMinimumSize(QtCore.QSize(0, 75))
        self.selectScreenBrightnessButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectScreenBrightnessButton.setStyleSheet("background: transparent;")
        self.selectScreenBrightnessButton.setText("")
        self.selectScreenBrightnessButton.setIcon(icon5)
        self.selectScreenBrightnessButton.setIconSize(QtCore.QSize(48, 48))
        self.selectScreenBrightnessButton.setFlat(True)
        self.selectScreenBrightnessButton.setObjectName("selectScreenBrightnessButton")
        self.verticalLayout_14.addWidget(self.selectScreenBrightnessButton)
        self.label_19 = QtWidgets.QLabel(self.selectButton_3)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_14.addWidget(self.label_19)
        self.horizontalLayout_9.addWidget(self.selectButton_3)
        self.nextButton_3 = QtWidgets.QWidget(self.screenBrightnessPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton_3.sizePolicy().hasHeightForWidth())
        self.nextButton_3.setSizePolicy(sizePolicy)
        self.nextButton_3.setMinimumSize(QtCore.QSize(70, 0))
        self.nextButton_3.setObjectName("nextButton_3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.nextButton_3)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lessScreenBrightnessButton = QtWidgets.QPushButton(self.nextButton_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lessScreenBrightnessButton.sizePolicy().hasHeightForWidth())
        self.lessScreenBrightnessButton.setSizePolicy(sizePolicy)
        self.lessScreenBrightnessButton.setMinimumSize(QtCore.QSize(0, 75))
        self.lessScreenBrightnessButton.setStyleSheet("background: transparent;")
        self.lessScreenBrightnessButton.setText("")
        self.lessScreenBrightnessButton.setIcon(icon7)
        self.lessScreenBrightnessButton.setIconSize(QtCore.QSize(48, 48))
        self.lessScreenBrightnessButton.setObjectName("lessScreenBrightnessButton")
        self.verticalLayout_15.addWidget(self.lessScreenBrightnessButton)
        self.nextLabel_3 = QtWidgets.QLabel(self.nextButton_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel_3.sizePolicy().hasHeightForWidth())
        self.nextLabel_3.setSizePolicy(sizePolicy)
        self.nextLabel_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel_3.setWordWrap(True)
        self.nextLabel_3.setObjectName("nextLabel_3")
        self.verticalLayout_15.addWidget(self.nextLabel_3)
        self.horizontalLayout_9.addWidget(self.nextButton_3)
        self.verticalLayout_16.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.screenBrightnessPage)
        self.wifiSetupPage = QtWidgets.QWidget()
        self.wifiSetupPage.setObjectName("wifiSetupPage")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.wifiSetupPage)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.wifiSetupPage)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.pushButton_6 = QtWidgets.QPushButton(self.wifiSetupPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background: transparent;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/rescan_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        self.verticalLayout_29.addLayout(self.horizontalLayout_10)
        self.wifiavailableList = QtWidgets.QListWidget(self.wifiSetupPage)
        self.wifiavailableList.setObjectName("wifiavailableList")
        item = QtWidgets.QListWidgetItem()
        self.wifiavailableList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wifiavailableList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wifiavailableList.addItem(item)
        self.verticalLayout_29.addWidget(self.wifiavailableList)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.exitButton_4 = QtWidgets.QWidget(self.wifiSetupPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_4.sizePolicy().hasHeightForWidth())
        self.exitButton_4.setSizePolicy(sizePolicy)
        self.exitButton_4.setMinimumSize(QtCore.QSize(70, 0))
        self.exitButton_4.setObjectName("exitButton_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.exitButton_4)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.exitWiFiButton = QtWidgets.QPushButton(self.exitButton_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitWiFiButton.sizePolicy().hasHeightForWidth())
        self.exitWiFiButton.setSizePolicy(sizePolicy)
        self.exitWiFiButton.setMinimumSize(QtCore.QSize(0, 75))
        self.exitWiFiButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitWiFiButton.setStyleSheet("background: transparent;")
        self.exitWiFiButton.setText("")
        self.exitWiFiButton.setIcon(icon4)
        self.exitWiFiButton.setIconSize(QtCore.QSize(48, 48))
        self.exitWiFiButton.setDefault(False)
        self.exitWiFiButton.setFlat(True)
        self.exitWiFiButton.setObjectName("exitWiFiButton")
        self.verticalLayout_17.addWidget(self.exitWiFiButton)
        self.label_10 = QtWidgets.QLabel(self.exitButton_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_17.addWidget(self.label_10)
        self.horizontalLayout_14.addWidget(self.exitButton_4)
        self.selectButton_4 = QtWidgets.QWidget(self.wifiSetupPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_4.sizePolicy().hasHeightForWidth())
        self.selectButton_4.setSizePolicy(sizePolicy)
        self.selectButton_4.setMinimumSize(QtCore.QSize(70, 0))
        self.selectButton_4.setObjectName("selectButton_4")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.selectButton_4)
        self.verticalLayout_19.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.selectWiFiButton = QtWidgets.QPushButton(self.selectButton_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectWiFiButton.sizePolicy().hasHeightForWidth())
        self.selectWiFiButton.setSizePolicy(sizePolicy)
        self.selectWiFiButton.setMinimumSize(QtCore.QSize(0, 75))
        self.selectWiFiButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectWiFiButton.setStyleSheet("background: transparent;")
        self.selectWiFiButton.setText("")
        self.selectWiFiButton.setIcon(icon5)
        self.selectWiFiButton.setIconSize(QtCore.QSize(48, 48))
        self.selectWiFiButton.setFlat(True)
        self.selectWiFiButton.setObjectName("selectWiFiButton")
        self.verticalLayout_19.addWidget(self.selectWiFiButton)
        self.label_20 = QtWidgets.QLabel(self.selectButton_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_19.addWidget(self.label_20)
        self.horizontalLayout_14.addWidget(self.selectButton_4)
        self.nextWidget_2 = QtWidgets.QWidget(self.wifiSetupPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextWidget_2.sizePolicy().hasHeightForWidth())
        self.nextWidget_2.setSizePolicy(sizePolicy)
        self.nextWidget_2.setMinimumSize(QtCore.QSize(70, 0))
        self.nextWidget_2.setObjectName("nextWidget_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.nextWidget_2)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.nextWiFiButton = QtWidgets.QPushButton(self.nextWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextWiFiButton.sizePolicy().hasHeightForWidth())
        self.nextWiFiButton.setSizePolicy(sizePolicy)
        self.nextWiFiButton.setMinimumSize(QtCore.QSize(0, 75))
        self.nextWiFiButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextWiFiButton.setStyleSheet("background: transparent;")
        self.nextWiFiButton.setText("")
        self.nextWiFiButton.setIcon(icon3)
        self.nextWiFiButton.setIconSize(QtCore.QSize(48, 48))
        self.nextWiFiButton.setFlat(True)
        self.nextWiFiButton.setObjectName("nextWiFiButton")
        self.verticalLayout_18.addWidget(self.nextWiFiButton)
        self.nextLabel_4 = QtWidgets.QLabel(self.nextWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel_4.sizePolicy().hasHeightForWidth())
        self.nextLabel_4.setSizePolicy(sizePolicy)
        self.nextLabel_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel_4.setWordWrap(True)
        self.nextLabel_4.setObjectName("nextLabel_4")
        self.verticalLayout_18.addWidget(self.nextLabel_4)
        self.horizontalLayout_14.addWidget(self.nextWidget_2)
        self.verticalLayout_29.addLayout(self.horizontalLayout_14)
        self.stackedWidget.addWidget(self.wifiSetupPage)
        self.wifiPasswordPage = QtWidgets.QWidget()
        self.wifiPasswordPage.setObjectName("wifiPasswordPage")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.wifiPasswordPage)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_25 = QtWidgets.QLabel(self.wifiPasswordPage)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_34.addWidget(self.label_25)
        self.showKeyboardButton = QtWidgets.QPushButton(self.wifiPasswordPage)
        self.showKeyboardButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.showKeyboardButton.setFont(font)
        self.showKeyboardButton.setObjectName("showKeyboardButton")
        self.verticalLayout_34.addWidget(self.showKeyboardButton)
        spacerItem15 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_34.addItem(spacerItem15)
        self.lineEdit = QtWidgets.QLineEdit(self.wifiPasswordPage)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_34.addWidget(self.lineEdit)
        self.label_23 = QtWidgets.QLabel(self.wifiPasswordPage)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_34.addWidget(self.label_23)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.exitButton_8 = QtWidgets.QWidget(self.wifiPasswordPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_8.sizePolicy().hasHeightForWidth())
        self.exitButton_8.setSizePolicy(sizePolicy)
        self.exitButton_8.setMinimumSize(QtCore.QSize(70, 0))
        self.exitButton_8.setObjectName("exitButton_8")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.exitButton_8)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.exitButton_9 = QtWidgets.QWidget(self.exitButton_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_9.sizePolicy().hasHeightForWidth())
        self.exitButton_9.setSizePolicy(sizePolicy)
        self.exitButton_9.setMinimumSize(QtCore.QSize(80, 0))
        self.exitButton_9.setObjectName("exitButton_9")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.exitButton_9)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.exitWifipassButton = QtWidgets.QPushButton(self.exitButton_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitWifipassButton.sizePolicy().hasHeightForWidth())
        self.exitWifipassButton.setSizePolicy(sizePolicy)
        self.exitWifipassButton.setMinimumSize(QtCore.QSize(0, 75))
        self.exitWifipassButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitWifipassButton.setStyleSheet("background: transparent;")
        self.exitWifipassButton.setText("")
        self.exitWifipassButton.setIcon(icon4)
        self.exitWifipassButton.setIconSize(QtCore.QSize(32, 32))
        self.exitWifipassButton.setDefault(False)
        self.exitWifipassButton.setFlat(True)
        self.exitWifipassButton.setObjectName("exitWifipassButton")
        self.verticalLayout_33.addWidget(self.exitWifipassButton)
        self.label_26 = QtWidgets.QLabel(self.exitButton_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_33.addWidget(self.label_26)
        self.verticalLayout_32.addWidget(self.exitButton_9)
        self.horizontalLayout_15.addWidget(self.exitButton_8)
        self.selectButton_6 = QtWidgets.QWidget(self.wifiPasswordPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_6.sizePolicy().hasHeightForWidth())
        self.selectButton_6.setSizePolicy(sizePolicy)
        self.selectButton_6.setMinimumSize(QtCore.QSize(70, 0))
        self.selectButton_6.setObjectName("selectButton_6")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.selectButton_6)
        self.verticalLayout_31.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_31.addItem(spacerItem16)
        self.horizontalLayout_15.addWidget(self.selectButton_6)
        self.nextButton_5 = QtWidgets.QWidget(self.wifiPasswordPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton_5.sizePolicy().hasHeightForWidth())
        self.nextButton_5.setSizePolicy(sizePolicy)
        self.nextButton_5.setMinimumSize(QtCore.QSize(70, 0))
        self.nextButton_5.setObjectName("nextButton_5")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.nextButton_5)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.saveWifipassButton = QtWidgets.QPushButton(self.nextButton_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveWifipassButton.sizePolicy().hasHeightForWidth())
        self.saveWifipassButton.setSizePolicy(sizePolicy)
        self.saveWifipassButton.setMinimumSize(QtCore.QSize(0, 75))
        self.saveWifipassButton.setStyleSheet("background: transparent;")
        self.saveWifipassButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveWifipassButton.setIcon(icon9)
        self.saveWifipassButton.setIconSize(QtCore.QSize(32, 32))
        self.saveWifipassButton.setObjectName("saveWifipassButton")
        self.verticalLayout_30.addWidget(self.saveWifipassButton)
        self.nextLabel_5 = QtWidgets.QLabel(self.nextButton_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel_5.sizePolicy().hasHeightForWidth())
        self.nextLabel_5.setSizePolicy(sizePolicy)
        self.nextLabel_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextLabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel_5.setWordWrap(True)
        self.nextLabel_5.setObjectName("nextLabel_5")
        self.verticalLayout_30.addWidget(self.nextLabel_5)
        self.horizontalLayout_15.addWidget(self.nextButton_5)
        self.verticalLayout_34.addLayout(self.horizontalLayout_15)
        self.stackedWidget.addWidget(self.wifiPasswordPage)
        self.updatePage = QtWidgets.QWidget()
        self.updatePage.setObjectName("updatePage")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.updatePage)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        spacerItem17 = QtWidgets.QSpacerItem(20, 111, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem17)
        self.getUpdateButton = QtWidgets.QPushButton(self.updatePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getUpdateButton.sizePolicy().hasHeightForWidth())
        self.getUpdateButton.setSizePolicy(sizePolicy)
        self.getUpdateButton.setMinimumSize(QtCore.QSize(0, 125))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.getUpdateButton.setFont(font)
        self.getUpdateButton.setIcon(icon5)
        self.getUpdateButton.setIconSize(QtCore.QSize(48, 48))
        self.getUpdateButton.setObjectName("getUpdateButton")
        self.verticalLayout_21.addWidget(self.getUpdateButton)
        self.label_21 = QtWidgets.QLabel(self.updatePage)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_21.addWidget(self.label_21)
        spacerItem18 = QtWidgets.QSpacerItem(20, 111, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem18)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.exitButton_5 = QtWidgets.QWidget(self.updatePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_5.sizePolicy().hasHeightForWidth())
        self.exitButton_5.setSizePolicy(sizePolicy)
        self.exitButton_5.setMinimumSize(QtCore.QSize(80, 0))
        self.exitButton_5.setObjectName("exitButton_5")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.exitButton_5)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.exitUpdateButton = QtWidgets.QPushButton(self.exitButton_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitUpdateButton.sizePolicy().hasHeightForWidth())
        self.exitUpdateButton.setSizePolicy(sizePolicy)
        self.exitUpdateButton.setMinimumSize(QtCore.QSize(0, 75))
        self.exitUpdateButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitUpdateButton.setStyleSheet("background: transparent;")
        self.exitUpdateButton.setText("")
        self.exitUpdateButton.setIcon(icon4)
        self.exitUpdateButton.setIconSize(QtCore.QSize(48, 48))
        self.exitUpdateButton.setDefault(False)
        self.exitUpdateButton.setFlat(True)
        self.exitUpdateButton.setObjectName("exitUpdateButton")
        self.verticalLayout_20.addWidget(self.exitUpdateButton)
        self.label_12 = QtWidgets.QLabel(self.exitButton_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_20.addWidget(self.label_12)
        self.horizontalLayout_11.addWidget(self.exitButton_5)
        self.selectButton_5 = QtWidgets.QWidget(self.updatePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton_5.sizePolicy().hasHeightForWidth())
        self.selectButton_5.setSizePolicy(sizePolicy)
        self.selectButton_5.setObjectName("selectButton_5")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.selectButton_5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem19)
        self.horizontalLayout_11.addWidget(self.selectButton_5)
        self.nextButton_8 = QtWidgets.QWidget(self.updatePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton_8.sizePolicy().hasHeightForWidth())
        self.nextButton_8.setSizePolicy(sizePolicy)
        self.nextButton_8.setMinimumSize(QtCore.QSize(70, 0))
        self.nextButton_8.setObjectName("nextButton_8")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.nextButton_8)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.saveUpdateButton = QtWidgets.QPushButton(self.nextButton_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveUpdateButton.sizePolicy().hasHeightForWidth())
        self.saveUpdateButton.setSizePolicy(sizePolicy)
        self.saveUpdateButton.setMinimumSize(QtCore.QSize(0, 75))
        self.saveUpdateButton.setStyleSheet("background: transparent;")
        self.saveUpdateButton.setText("")
        self.saveUpdateButton.setIcon(icon9)
        self.saveUpdateButton.setIconSize(QtCore.QSize(48, 48))
        self.saveUpdateButton.setObjectName("saveUpdateButton")
        self.verticalLayout_40.addWidget(self.saveUpdateButton)
        self.nextLabel_8 = QtWidgets.QLabel(self.nextButton_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextLabel_8.sizePolicy().hasHeightForWidth())
        self.nextLabel_8.setSizePolicy(sizePolicy)
        self.nextLabel_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextLabel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLabel_8.setWordWrap(True)
        self.nextLabel_8.setObjectName("nextLabel_8")
        self.verticalLayout_40.addWidget(self.nextLabel_8)
        self.horizontalLayout_11.addWidget(self.nextButton_8)
        self.verticalLayout_21.addLayout(self.horizontalLayout_11)
        self.stackedWidget.addWidget(self.updatePage)
        self.shutdownPage = QtWidgets.QWidget()
        self.shutdownPage.setObjectName("shutdownPage")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.shutdownPage)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.exitAppButton = QtWidgets.QPushButton(self.shutdownPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.exitAppButton.sizePolicy().hasHeightForWidth())
        self.exitAppButton.setSizePolicy(sizePolicy)
        self.exitAppButton.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.exitAppButton.setFont(font)
        self.exitAppButton.setObjectName("exitAppButton")
        self.verticalLayout_25.addWidget(self.exitAppButton)
        spacerItem20 = QtWidgets.QSpacerItem(20, 104, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem20)
        self.shutdownButton = QtWidgets.QPushButton(self.shutdownPage)
        self.shutdownButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.shutdownButton.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/images/poweroff_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shutdownButton.setIcon(icon10)
        self.shutdownButton.setIconSize(QtCore.QSize(32, 32))
        self.shutdownButton.setObjectName("shutdownButton")
        self.verticalLayout_25.addWidget(self.shutdownButton)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem21)
        self.restartButton = QtWidgets.QPushButton(self.shutdownPage)
        self.restartButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.restartButton.setFont(font)
        self.restartButton.setObjectName("restartButton")
        self.verticalLayout_25.addWidget(self.restartButton)
        self.shudownTimer = QtWidgets.QLabel(self.shutdownPage)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.shudownTimer.setFont(font)
        self.shudownTimer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shudownTimer.setObjectName("shudownTimer")
        self.verticalLayout_25.addWidget(self.shudownTimer)
        spacerItem22 = QtWidgets.QSpacerItem(20, 103, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem22)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.exitButton_6 = QtWidgets.QWidget(self.shutdownPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton_6.sizePolicy().hasHeightForWidth())
        self.exitButton_6.setSizePolicy(sizePolicy)
        self.exitButton_6.setMinimumSize(QtCore.QSize(80, 0))
        self.exitButton_6.setObjectName("exitButton_6")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.exitButton_6)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.exitShutdownButton = QtWidgets.QPushButton(self.exitButton_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitShutdownButton.sizePolicy().hasHeightForWidth())
        self.exitShutdownButton.setSizePolicy(sizePolicy)
        self.exitShutdownButton.setMinimumSize(QtCore.QSize(0, 75))
        self.exitShutdownButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitShutdownButton.setStyleSheet("background: transparent;")
        self.exitShutdownButton.setText("")
        self.exitShutdownButton.setIcon(icon4)
        self.exitShutdownButton.setIconSize(QtCore.QSize(48, 48))
        self.exitShutdownButton.setDefault(False)
        self.exitShutdownButton.setFlat(True)
        self.exitShutdownButton.setObjectName("exitShutdownButton")
        self.verticalLayout_23.addWidget(self.exitShutdownButton)
        self.label_13 = QtWidgets.QLabel(self.exitButton_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_23.addWidget(self.label_13)
        self.horizontalLayout_12.addWidget(self.exitButton_6)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem23)
        self.cancelWidget = QtWidgets.QWidget(self.shutdownPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelWidget.sizePolicy().hasHeightForWidth())
        self.cancelWidget.setSizePolicy(sizePolicy)
        self.cancelWidget.setMinimumSize(QtCore.QSize(80, 0))
        self.cancelWidget.setObjectName("cancelWidget")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.cancelWidget)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.cancelShutdownButton = QtWidgets.QPushButton(self.cancelWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelShutdownButton.sizePolicy().hasHeightForWidth())
        self.cancelShutdownButton.setSizePolicy(sizePolicy)
        self.cancelShutdownButton.setMinimumSize(QtCore.QSize(0, 75))
        self.cancelShutdownButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelShutdownButton.setStyleSheet("background: transparent;")
        self.cancelShutdownButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/cancel_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelShutdownButton.setIcon(icon11)
        self.cancelShutdownButton.setIconSize(QtCore.QSize(48, 48))
        self.cancelShutdownButton.setDefault(False)
        self.cancelShutdownButton.setFlat(True)
        self.cancelShutdownButton.setObjectName("cancelShutdownButton")
        self.verticalLayout_24.addWidget(self.cancelShutdownButton)
        self.label_22 = QtWidgets.QLabel(self.cancelWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_24.addWidget(self.label_22)
        self.horizontalLayout_12.addWidget(self.cancelWidget)
        self.verticalLayout_25.addLayout(self.horizontalLayout_12)
        self.stackedWidget.addWidget(self.shutdownPage)
        self.captureStatusPage = QtWidgets.QWidget()
        self.captureStatusPage.setObjectName("captureStatusPage")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.captureStatusPage)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        spacerItem24 = QtWidgets.QSpacerItem(20, 223, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem24)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem25)
        self.pushButton = QtWidgets.QPushButton(self.captureStatusPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 75))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.pushButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/image_resources/image_resources/update_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_19.addWidget(self.pushButton)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem26)
        self.verticalLayout_22.addLayout(self.horizontalLayout_19)
        self.cameraCapturinginfo = QtWidgets.QLabel(self.captureStatusPage)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cameraCapturinginfo.setFont(font)
        self.cameraCapturinginfo.setText("")
        self.cameraCapturinginfo.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraCapturinginfo.setWordWrap(True)
        self.cameraCapturinginfo.setObjectName("cameraCapturinginfo")
        self.verticalLayout_22.addWidget(self.cameraCapturinginfo)
        spacerItem27 = QtWidgets.QSpacerItem(20, 223, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem27)
        self.stackedWidget.addWidget(self.captureStatusPage)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        spacerItem28 = QtWidgets.QSpacerItem(20, 182, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_42.addItem(spacerItem28)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem29)
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 75))
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon12)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_20.addWidget(self.pushButton_2)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem30)
        self.verticalLayout_42.addLayout(self.horizontalLayout_20)
        self.shutdownstatus = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.shutdownstatus.setFont(font)
        self.shutdownstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.shutdownstatus.setWordWrap(True)
        self.shutdownstatus.setObjectName("shutdownstatus")
        self.verticalLayout_42.addWidget(self.shutdownstatus)
        spacerItem31 = QtWidgets.QSpacerItem(20, 181, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_42.addItem(spacerItem31)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem32)
        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.stopshutdown = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopshutdown.sizePolicy().hasHeightForWidth())
        self.stopshutdown.setSizePolicy(sizePolicy)
        self.stopshutdown.setMinimumSize(QtCore.QSize(0, 75))
        self.stopshutdown.setStyleSheet("background: transparent;")
        self.stopshutdown.setText("")
        self.stopshutdown.setIcon(icon11)
        self.stopshutdown.setIconSize(QtCore.QSize(48, 48))
        self.stopshutdown.setObjectName("stopshutdown")
        self.verticalLayout_41.addWidget(self.stopshutdown)
        self.label_14 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_41.addWidget(self.label_14)
        self.horizontalLayout_18.addLayout(self.verticalLayout_41)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem33)
        self.verticalLayout_42.addLayout(self.horizontalLayout_18)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.menuList.setCurrentRow(-1)
        self.settingsList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.showKeyboardButton)
        MainWindow.setTabOrder(self.showKeyboardButton, self.takePhotoButton)
        MainWindow.setTabOrder(self.takePhotoButton, self.lightSourcepushbutton)
        MainWindow.setTabOrder(self.lightSourcepushbutton, self.menuList)
        MainWindow.setTabOrder(self.menuList, self.menuExitButton)
        MainWindow.setTabOrder(self.menuExitButton, self.menuSelectButton)
        MainWindow.setTabOrder(self.menuSelectButton, self.menuNextbutton)
        MainWindow.setTabOrder(self.menuNextbutton, self.settingsList)
        MainWindow.setTabOrder(self.settingsList, self.settingsExitbutton)
        MainWindow.setTabOrder(self.settingsExitbutton, self.settingsSelectbutton)
        MainWindow.setTabOrder(self.settingsSelectbutton, self.settingsNextbutton)
        MainWindow.setTabOrder(self.settingsNextbutton, self.sequenceList)
        MainWindow.setTabOrder(self.sequenceList, self.exitLedSeqButton)
        MainWindow.setTabOrder(self.exitLedSeqButton, self.selectLedSeqButton)
        MainWindow.setTabOrder(self.selectLedSeqButton, self.nextLedSeqButton)
        MainWindow.setTabOrder(self.nextLedSeqButton, self.imageBrightnessbox)
        MainWindow.setTabOrder(self.imageBrightnessbox, self.exitImageBrightnessButton)
        MainWindow.setTabOrder(self.exitImageBrightnessButton, self.selectImageBrightnessButton)
        MainWindow.setTabOrder(self.selectImageBrightnessButton, self.brightnessLessButton)
        MainWindow.setTabOrder(self.brightnessLessButton, self.spinBox_2)
        MainWindow.setTabOrder(self.spinBox_2, self.exitScreenBrightnessButton)
        MainWindow.setTabOrder(self.exitScreenBrightnessButton, self.selectScreenBrightnessButton)
        MainWindow.setTabOrder(self.selectScreenBrightnessButton, self.lessScreenBrightnessButton)
        MainWindow.setTabOrder(self.lessScreenBrightnessButton, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.wifiavailableList)
        MainWindow.setTabOrder(self.wifiavailableList, self.exitWiFiButton)
        MainWindow.setTabOrder(self.exitWiFiButton, self.selectWiFiButton)
        MainWindow.setTabOrder(self.selectWiFiButton, self.nextWiFiButton)
        MainWindow.setTabOrder(self.nextWiFiButton, self.menuButton)
        MainWindow.setTabOrder(self.menuButton, self.wifiStatus)
        MainWindow.setTabOrder(self.wifiStatus, self.exitWifipassButton)
        MainWindow.setTabOrder(self.exitWifipassButton, self.saveWifipassButton)
        MainWindow.setTabOrder(self.saveWifipassButton, self.getUpdateButton)
        MainWindow.setTabOrder(self.getUpdateButton, self.exitUpdateButton)
        MainWindow.setTabOrder(self.exitUpdateButton, self.saveUpdateButton)
        MainWindow.setTabOrder(self.saveUpdateButton, self.shutdownButton)
        MainWindow.setTabOrder(self.shutdownButton, self.restartButton)
        MainWindow.setTabOrder(self.restartButton, self.exitShutdownButton)
        MainWindow.setTabOrder(self.exitShutdownButton, self.cancelShutdownButton)
        MainWindow.setTabOrder(self.cancelShutdownButton, self.updateSequenceButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.statusInfo.setText(_translate("MainWindow", "Status Info"))
        self.lightSourceInfo.setText(_translate("MainWindow", "Light Source Info"))
        self.label_3.setText(_translate("MainWindow", "MENU"))
        self.label_4.setText(_translate("MainWindow", "CAPTURE"))
        self.label_5.setText(_translate("MainWindow", "SOURCE"))
        self.label_17.setText(_translate("MainWindow", "MENU"))
        __sortingEnabled = self.menuList.isSortingEnabled()
        self.menuList.setSortingEnabled(False)
        item = self.menuList.item(0)
        item.setText(_translate("MainWindow", "SELECT SEQUENCE"))
        item = self.menuList.item(1)
        item.setText(_translate("MainWindow", "WIFI SETTINGS"))
        item = self.menuList.item(2)
        item.setText(_translate("MainWindow", "SHUTDOWN"))
        item = self.menuList.item(3)
        item.setText(_translate("MainWindow", "RUN SERVER"))
        self.menuList.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "BACK"))
        self.label_7.setText(_translate("MainWindow", "SELECT"))
        self.nextLabel.setText(_translate("MainWindow", "NEXT"))
        self.label_28.setText(_translate("MainWindow", "SETTINGS"))
        __sortingEnabled = self.settingsList.isSortingEnabled()
        self.settingsList.setSortingEnabled(False)
        item = self.settingsList.item(0)
        item.setText(_translate("MainWindow", "WIFI SETUP"))
        self.settingsList.setSortingEnabled(__sortingEnabled)
        self.label_30.setText(_translate("MainWindow", "IP Address: 192.168.1.2"))
        self.label_31.setText(_translate("MainWindow", "Connected To: ELEMENTZ"))
        self.label_27.setText(_translate("MainWindow", "BACK"))
        self.label_29.setText(_translate("MainWindow", "SELECT"))
        self.nextLabel_7.setText(_translate("MainWindow", "NEXT"))
        self.label_16.setText(_translate("MainWindow", "LED SEQUENCE"))
        __sortingEnabled = self.sequenceList.isSortingEnabled()
        self.sequenceList.setSortingEnabled(False)
        item = self.sequenceList.item(0)
        item.setText(_translate("MainWindow", "Sequence 1"))
        item = self.sequenceList.item(1)
        item.setText(_translate("MainWindow", "Sequence 2"))
        self.sequenceList.setSortingEnabled(__sortingEnabled)
        self.updateSequenceButton.setText(_translate("MainWindow", "UPDATE SEQUENCE"))
        self.updateStatusLabel.setText(_translate("MainWindow", "update status"))
        self.label_15.setText(_translate("MainWindow", "BACK"))
        self.label_24.setText(_translate("MainWindow", "SELECT"))
        self.nextLabel_6.setText(_translate("MainWindow", "NEXT"))
        self.label.setText(_translate("MainWindow", "IMAGE BRIGHTNESS"))
        self.label_8.setText(_translate("MainWindow", "MORE"))
        self.nextLabel_2.setText(_translate("MainWindow", "SELECT"))
        self.label_18.setText(_translate("MainWindow", "LESS"))
        self.label_2.setText(_translate("MainWindow", "SCREEN BRIGHTNESS"))
        self.label_9.setText(_translate("MainWindow", "MORE"))
        self.label_19.setText(_translate("MainWindow", "SELECT"))
        self.nextLabel_3.setText(_translate("MainWindow", "LESS"))
        self.label_11.setText(_translate("MainWindow", "AVAILABLE NETWORKS"))
        self.pushButton_6.setText(_translate("MainWindow", "RESCAN"))
        __sortingEnabled = self.wifiavailableList.isSortingEnabled()
        self.wifiavailableList.setSortingEnabled(False)
        item = self.wifiavailableList.item(0)
        item.setText(_translate("MainWindow", "Elementz BroadBand"))
        item = self.wifiavailableList.item(1)
        item.setText(_translate("MainWindow", "ELEMENTZ"))
        item = self.wifiavailableList.item(2)
        item.setText(_translate("MainWindow", "Elementz Asianet"))
        self.wifiavailableList.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("MainWindow", "  BACK  "))
        self.label_20.setText(_translate("MainWindow", "SELECT"))
        self.nextLabel_4.setText(_translate("MainWindow", "NEXT"))
        self.label_25.setText(_translate("MainWindow", "WiFi PASSWORD"))
        self.showKeyboardButton.setText(_translate("MainWindow", "SHOW KEYBOARD"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.label_23.setText(_translate("MainWindow", "Save status"))
        self.label_26.setText(_translate("MainWindow", "  BACK  "))
        self.nextLabel_5.setText(_translate("MainWindow", "SAVE"))
        self.getUpdateButton.setText(_translate("MainWindow", "GET UPDATES"))
        self.label_21.setText(_translate("MainWindow", "Update Info"))
        self.label_12.setText(_translate("MainWindow", "BACK"))
        self.nextLabel_8.setText(_translate("MainWindow", "SAVE"))
        self.exitAppButton.setText(_translate("MainWindow", "EXIT"))
        self.shutdownButton.setText(_translate("MainWindow", "SHUTDOWN"))
        self.restartButton.setText(_translate("MainWindow", "RESTART"))
        self.shudownTimer.setText(_translate("MainWindow", "Timer in (s)"))
        self.label_13.setText(_translate("MainWindow", "BACK"))
        self.label_22.setText(_translate("MainWindow", "CANCEL"))
        self.shutdownstatus.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "CANCEL"))

import resource_rc
