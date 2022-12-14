# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setStyleSheet("background-color: #263238;")
        self.spo_title = QtWidgets.QLabel(Form)
        self.spo_title.setGeometry(QtCore.QRect(590, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spo_title.setFont(font)
        self.spo_title.setStyleSheet("color: rgb(200, 200, 200);\n"
"")
        self.spo_title.setObjectName("spo_title")
        self.pulse_title = QtWidgets.QLabel(Form)
        self.pulse_title.setGeometry(QtCore.QRect(840, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pulse_title.setFont(font)
        self.pulse_title.setStyleSheet("color: rgb(200, 200, 200);")
        self.pulse_title.setObjectName("pulse_title")
        self.graphwidget = PlotWidget(Form)
        self.graphwidget.setGeometry(QtCore.QRect(10, 270, 1004, 300))
        self.graphwidget.setStyleSheet("")
        self.graphwidget.setObjectName("graphwidget")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(780, 70, 40, 170))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.spo_value = QtWidgets.QLabel(Form)
        self.spo_value.setGeometry(QtCore.QRect(590, 70, 170, 170))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.spo_value.setFont(font)
        self.spo_value.setStyleSheet("color: #0039cb;\n"
"border: 3px solid rgb(150, 150, 150);\n"
"background-color: #000a12;")
        self.spo_value.setFrameShape(QtWidgets.QFrame.Box)
        self.spo_value.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spo_value.setAlignment(QtCore.Qt.AlignCenter)
        self.spo_value.setObjectName("spo_value")
        self.pulse_value = QtWidgets.QLabel(Form)
        self.pulse_value.setGeometry(QtCore.QRect(840, 70, 170, 170))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.pulse_value.setFont(font)
        self.pulse_value.setStyleSheet("color: #009624;\n"
"border: 2px solid rgb(150, 150, 150);\n"
"\n"
"background-color: #000a12;")
        self.pulse_value.setFrameShape(QtWidgets.QFrame.Box)
        self.pulse_value.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pulse_value.setAlignment(QtCore.Qt.AlignCenter)
        self.pulse_value.setObjectName("pulse_value")
        self.status_label = QtWidgets.QLabel(Form)
        self.status_label.setGeometry(QtCore.QRect(330, 210, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.status_label.setFrameShape(QtWidgets.QFrame.Box)
        self.status_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 260, 1004, 1))
        self.line.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.history_value = QtWidgets.QTextBrowser(Form)
        self.history_value.setGeometry(QtCore.QRect(330, 70, 241, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.history_value.setFont(font)
        self.history_value.setStyleSheet("background-color: #000a12;\n"
"color: #f05545;\n"
"")
        self.history_value.setObjectName("history_value")
        self.control_button = QtWidgets.QPushButton(Form)
        self.control_button.setGeometry(QtCore.QRect(20, 30, 75, 31))
        self.control_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.control_button.setMouseTracking(False)
        self.control_button.setStyleSheet("background-color: rgb(41, 255, 148);")
        self.control_button.setCheckable(False)
        self.control_button.setObjectName("control_button")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 291, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: white;")
        self.groupBox.setObjectName("groupBox")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setGeometry(QtCore.QRect(20, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: white;")
        self.name_label.setObjectName("name_label")
        self.id_label = QtWidgets.QLabel(self.groupBox)
        self.id_label.setGeometry(QtCore.QRect(20, 64, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color: white;")
        self.id_label.setObjectName("id_label")
        self.sex_label = QtWidgets.QLabel(self.groupBox)
        self.sex_label.setGeometry(QtCore.QRect(20, 98, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sex_label.setFont(font)
        self.sex_label.setStyleSheet("color: white;")
        self.sex_label.setObjectName("sex_label")
        self.age_label = QtWidgets.QLabel(self.groupBox)
        self.age_label.setGeometry(QtCore.QRect(20, 132, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.age_label.setFont(font)
        self.age_label.setStyleSheet("color: white;")
        self.age_label.setObjectName("age_label")
        self.name_value = QtWidgets.QLineEdit(self.groupBox)
        self.name_value.setGeometry(QtCore.QRect(90, 30, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_value.setFont(font)
        self.name_value.setStyleSheet("background-color: white;\n"
"color: black;")
        self.name_value.setObjectName("name_value")
        self.id_value = QtWidgets.QLineEdit(self.groupBox)
        self.id_value.setGeometry(QtCore.QRect(90, 64, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_value.setFont(font)
        self.id_value.setStyleSheet("background-color: white;\n"
"color: black;")
        self.id_value.setObjectName("id_value")
        self.age_value = QtWidgets.QLineEdit(self.groupBox)
        self.age_value.setGeometry(QtCore.QRect(90, 132, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.age_value.setFont(font)
        self.age_value.setStyleSheet("background-color: white;\n"
"color: black;")
        self.age_value.setObjectName("age_value")
        self.sex_value = QtWidgets.QComboBox(self.groupBox)
        self.sex_value.setGeometry(QtCore.QRect(90, 98, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sex_value.setFont(font)
        self.sex_value.setStyleSheet("background-color: white;\n"
"color: black;")
        self.sex_value.setObjectName("sex_value")
        self.sex_value.addItem("")
        self.sex_value.addItem("")
        self.sex_value.addItem("")
        self.control_io_button = QtWidgets.QPushButton(Form)
        self.control_io_button.setGeometry(QtCore.QRect(200, 30, 75, 31))
        self.control_io_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.control_io_button.setMouseTracking(False)
        self.control_io_button.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.control_io_button.setCheckable(False)
        self.control_io_button.setChecked(False)
        self.control_io_button.setObjectName("control_io_button")
        self.control_reset_button = QtWidgets.QPushButton(Form)
        self.control_reset_button.setGeometry(QtCore.QRect(110, 30, 75, 31))
        self.control_reset_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.control_reset_button.setMouseTracking(False)
        self.control_reset_button.setStyleSheet("background-color: rgb(239, 255, 62);")
        self.control_reset_button.setCheckable(False)
        self.control_reset_button.setChecked(False)
        self.control_reset_button.setObjectName("control_reset_button")
        self.control_exit_button = QtWidgets.QPushButton(Form)
        self.control_exit_button.setGeometry(QtCore.QRect(290, 30, 75, 31))
        self.control_exit_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.control_exit_button.setMouseTracking(False)
        self.control_exit_button.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.control_exit_button.setCheckable(False)
        self.control_exit_button.setChecked(False)
        self.control_exit_button.setObjectName("control_exit_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.spo_title.setText(_translate("Form", "SpO2 (%)"))
        self.pulse_title.setText(_translate("Form", "Pulse (bpm)"))
        self.spo_value.setText(_translate("Form", "--"))
        self.pulse_value.setText(_translate("Form", "--"))
        self.status_label.setText(_translate("Form", "--"))
        self.control_button.setText(_translate("Form", "Start"))
        self.groupBox.setTitle(_translate("Form", "Identity"))
        self.name_label.setText(_translate("Form", "Name"))
        self.id_label.setText(_translate("Form", "ID"))
        self.sex_label.setText(_translate("Form", "Gender"))
        self.age_label.setText(_translate("Form", "Age"))
        self.sex_value.setItemText(0, _translate("Form", "Choose item"))
        self.sex_value.setItemText(1, _translate("Form", "Male"))
        self.sex_value.setItemText(2, _translate("Form", "Female"))
        self.control_io_button.setText(_translate("Form", "Save"))
        self.control_reset_button.setText(_translate("Form", "Reset"))
        self.control_exit_button.setText(_translate("Form", "Exit"))
from pyqtgraph import PlotWidget
import imageqrc_rc
