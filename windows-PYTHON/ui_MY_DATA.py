# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MY_DATAYNhpGN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(827, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(240, 190, 571, 441)) #画图区域大小
        
        self.matplotFigure = QVBoxLayout(self.verticalLayoutWidget)
        self.matplotFigure.setObjectName(u"matplotFigure")
        self.matplotFigure.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")        
        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 471, 441))
        
        self.matplotFigure.addWidget(self.widget)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 40, 806, 153)) #按键大小
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 801, 21))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 200, 201, 400)) #提示区域大小
        
        self.combobox = QComboBox(self, minimumWidth=200)
        self.combobox.setEditable(True)
        
        layout = QtWidgets.QHBoxLayout(self)
        layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        layout.addWidget(self.combobox)

        self.rleg0Angle = QPushButton(self.gridLayoutWidget)
        self.rleg0Angle.setObjectName(u"rlegHip1Angle")
        self.gridLayout.addWidget(self.rleg0Angle, 0, 0, 1, 1)
        
        self.rleg1Angle = QPushButton(self.gridLayoutWidget)
        self.rleg1Angle.setObjectName(u"rlegHip2Angle")
        self.gridLayout.addWidget(self.rleg1Angle, 0, 1, 1, 1)
        
        self.rleg2Angle = QPushButton(self.gridLayoutWidget)
        self.rleg2Angle.setObjectName(u"rlegHip3Angle")
        self.gridLayout.addWidget(self.rleg2Angle, 0, 2, 1, 1)

        self.rleg3Angle = QPushButton(self.gridLayoutWidget)
        self.rleg3Angle.setObjectName(u"rlegKneeAngle")
        self.gridLayout.addWidget(self.rleg3Angle, 0, 3, 1, 1)
        
        self.rleg4Angle = QPushButton(self.gridLayoutWidget)
        self.rleg4Angle.setObjectName(u"rlegAnkle5Angle")
        self.gridLayout.addWidget(self.rleg4Angle, 0, 4, 1, 1)
        
        self.rleg5Angle = QPushButton(self.gridLayoutWidget)
        self.rleg5Angle.setObjectName(u"rlegAnkle6Angle")
        self.gridLayout.addWidget(self.rleg5Angle, 0, 5, 1, 1)
        
        self.lleg0Angle = QPushButton(self.gridLayoutWidget)
        self.lleg0Angle.setObjectName(u"llegHip1Angle")
        self.gridLayout.addWidget(self.lleg0Angle, 1, 0, 1, 1)
        
        self.lleg1Angle = QPushButton(self.gridLayoutWidget)
        self.lleg1Angle.setObjectName(u"llegHip2Angle")
        self.gridLayout.addWidget(self.lleg1Angle, 1, 1, 1, 1)

        self.lleg2Angle = QPushButton(self.gridLayoutWidget)
        self.lleg2Angle.setObjectName(u"llegHip3Angle")
        self.gridLayout.addWidget(self.lleg2Angle, 1, 2, 1, 1)
        
        self.lleg3Angle = QPushButton(self.gridLayoutWidget)
        self.lleg3Angle.setObjectName(u"llegKneeAngle")
        self.gridLayout.addWidget(self.lleg3Angle, 1, 3, 1, 1)
        
        self.lleg4Angle = QPushButton(self.gridLayoutWidget)
        self.lleg4Angle.setObjectName(u"llegAnkle5Angle")
        self.gridLayout.addWidget(self.lleg4Angle, 1, 4, 1, 1)
        
        self.lleg5Angle = QPushButton(self.gridLayoutWidget)
        self.lleg5Angle.setObjectName(u"llegAnkle6Angle")
        self.gridLayout.addWidget(self.lleg5Angle, 1, 5, 1, 1)
        
        self.rleg0Torque = QPushButton(self.gridLayoutWidget)
        self.rleg0Torque.setObjectName(u"rlegHip1Torque")
        self.gridLayout.addWidget(self.rleg0Torque, 2, 0, 1, 1)

        self.rleg1Torque = QPushButton(self.gridLayoutWidget)
        self.rleg1Torque.setObjectName(u"rlegHip2Torque")
        self.gridLayout.addWidget(self.rleg1Torque, 2, 1, 1, 1)

        self.rleg2Torque = QPushButton(self.gridLayoutWidget)
        self.rleg2Torque.setObjectName(u"rlegHip3Torque")
        self.gridLayout.addWidget(self.rleg2Torque, 2, 2, 1, 1)
        
        self.rleg3Torque = QPushButton(self.gridLayoutWidget)
        self.rleg3Torque.setObjectName(u"rlegKneeTorque")
        self.gridLayout.addWidget(self.rleg3Torque, 2, 3, 1, 1)   
        
        self.rleg4Torque = QPushButton(self.gridLayoutWidget)
        self.rleg4Torque.setObjectName(u"rlegAnkle5Torque")
        self.gridLayout.addWidget(self.rleg4Torque, 2, 4, 1, 1)        
        
        self.rleg5Torque = QPushButton(self.gridLayoutWidget)
        self.rleg5Torque.setObjectName(u"rlegAnkle6Torque")
        self.gridLayout.addWidget(self.rleg5Torque, 2, 5, 1, 1)      
        
        self.lleg0Torque = QPushButton(self.gridLayoutWidget)
        self.lleg0Torque.setObjectName(u"llegHip1Torque")
        self.gridLayout.addWidget(self.lleg0Torque, 3, 0, 1, 1)

        self.lleg1Torque = QPushButton(self.gridLayoutWidget)
        self.lleg1Torque.setObjectName(u"llegHip2Torque")
        self.gridLayout.addWidget(self.lleg1Torque, 3, 1, 1, 1)

        self.lleg2Torque = QPushButton(self.gridLayoutWidget)
        self.lleg2Torque.setObjectName(u"llegHip3Torque")
        self.gridLayout.addWidget(self.lleg2Torque, 3, 2, 1, 1)
        
        self.lleg3Torque = QPushButton(self.gridLayoutWidget)
        self.lleg3Torque.setObjectName(u"llegKneeTorque")
        self.gridLayout.addWidget(self.lleg3Torque, 3, 3, 1, 1)   
        
        self.lleg4Torque = QPushButton(self.gridLayoutWidget)
        self.lleg4Torque.setObjectName(u"llegAnkle5Torque")
        self.gridLayout.addWidget(self.lleg4Torque, 3, 4, 1, 1)        
        
        self.lleg5Torque = QPushButton(self.gridLayoutWidget)
        self.lleg5Torque.setObjectName(u"llegAnkle6Torque")
        self.gridLayout.addWidget(self.lleg5Torque, 3, 5, 1, 1)

        self.rarmAngle = QPushButton(self.gridLayoutWidget)
        self.rarmAngle.setObjectName(u"rarmAngle")
        self.gridLayout.addWidget(self.rarmAngle, 0, 6, 1, 1)

        self.rarmTorque = QPushButton(self.gridLayoutWidget)
        self.rarmTorque.setObjectName(u"rarmTorque")
        self.gridLayout.addWidget(self.rarmTorque, 1, 6, 1, 1)

        self.larmAngle = QPushButton(self.gridLayoutWidget)
        self.larmAngle.setObjectName(u"larmAngle")
        self.gridLayout.addWidget(self.larmAngle, 0, 7, 1, 1)

        self.larmTorque = QPushButton(self.gridLayoutWidget)
        self.larmTorque.setObjectName(u"larmTorque")
        self.gridLayout.addWidget(self.larmTorque, 1, 7, 1, 1)

        self.rlegForce = QPushButton(self.gridLayoutWidget)
        self.rlegForce.setObjectName(u"rlegForce")
        self.gridLayout.addWidget(self.rlegForce, 2, 6, 1, 1)
        
        self.llegForce = QPushButton(self.gridLayoutWidget)
        self.llegForce.setObjectName(u"llegForce")
        self.gridLayout.addWidget(self.llegForce, 2, 7, 1, 1)

        self.roll = QPushButton(self.gridLayoutWidget)
        self.roll.setObjectName(u"roll")
        self.gridLayout.addWidget(self.roll, 3, 6, 1, 1)

        self.pitch = QPushButton(self.gridLayoutWidget)
        self.pitch.setObjectName(u"pitch")
        self.gridLayout.addWidget(self.pitch, 3, 7, 1, 1)
        
        self.ComX = QPushButton(self.gridLayoutWidget)
        self.ComX.setObjectName(u"ComX")
        self.gridLayout.addWidget(self.ComX, 4, 6, 1, 1)
        
        self.ComZ = QPushButton(self.gridLayoutWidget)
        self.ComZ.setObjectName(u"ComZ")
        self.gridLayout.addWidget(self.ComZ, 4, 7, 1, 1)

        # self.pushButton_16 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_16.setObjectName(u"pushButton_16")
        # self.gridLayout.addWidget(self.pushButton_16, 2, 4, 1, 1)

        # self.pushButton_18 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_18.setObjectName(u"pushButton_18")
        # self.gridLayout.addWidget(self.pushButton_18, 2, 5, 1, 1)

        # self.pushButton_20 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_20.setObjectName(u"pushButton_20")
        # self.gridLayout.addWidget(self.pushButton_20, 2, 6, 1, 1)

        # self.pushButton_22 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_22.setObjectName(u"pushButton_22")
        # self.gridLayout.addWidget(self.pushButton_22, 2, 7, 1, 1)

        # self.pushButton_24 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_24.setObjectName(u"pushButton_24")
        # self.gridLayout.addWidget(self.pushButton_24, 2, 8, 1, 1)
        
        self.Clear = QPushButton(self.gridLayoutWidget)
        self.Clear.setObjectName(u"Clear")
        self.gridLayout.addWidget(self.Clear, 4, 0, 1, 1)
        # self.peroidTime = QPushButton(self.centralwidget)
        # self.peroidTime.setObjectName(u"peroidTime")
        # self.peroidTime.setGeometry(QRect(20, 210, 75, 23))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 827, 23))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jump Data Visualization", None))
        self.rleg0Angle.setText(QCoreApplication.translate("MainWindow", u"RlegHip1Angle", None))
        self.rleg1Angle.setText(QCoreApplication.translate("MainWindow", u"RlegHip2Angle", None))
        self.rleg2Angle.setText(QCoreApplication.translate("MainWindow", u"RlegHip3Angle", None))
        self.rleg3Angle.setText(QCoreApplication.translate("MainWindow", u"RlegKneeAngle", None))
        self.rleg4Angle.setText(QCoreApplication.translate("MainWindow", u"RlegAnkle5Angle", None))
        self.rleg5Angle.setText(QCoreApplication.translate("MainWindow", u"RlegAnkle6Angle", None))
        self.lleg0Angle.setText(QCoreApplication.translate("MainWindow", u"LlegHip1Angle", None))
        self.lleg1Angle.setText(QCoreApplication.translate("MainWindow", u"LlegHip2Angle", None))
        self.lleg2Angle.setText(QCoreApplication.translate("MainWindow", u"LlegHip3Angle", None))
        self.lleg3Angle.setText(QCoreApplication.translate("MainWindow", u"LlegKneeAngle", None))
        self.lleg4Angle.setText(QCoreApplication.translate("MainWindow", u"LlegAnkle5Angle", None))
        self.lleg5Angle.setText(QCoreApplication.translate("MainWindow", u"LlegAnkle6Angle", None))
        self.rleg0Torque.setText(QCoreApplication.translate("MainWindow", u"RlegHip1Torque", None))
        self.rleg1Torque.setText(QCoreApplication.translate("MainWindow", u"RlegHip2Torque", None))
        self.rleg2Torque.setText(QCoreApplication.translate("MainWindow", u"RlegHip3Torque", None))
        self.rleg3Torque.setText(QCoreApplication.translate("MainWindow", u"RlegKneeTorque", None))
        self.rleg4Torque.setText(QCoreApplication.translate("MainWindow", u"RlegAnkle5Torque", None))
        self.rleg5Torque.setText(QCoreApplication.translate("MainWindow", u"RlegAnkle6Torque", None))
        self.lleg0Torque.setText(QCoreApplication.translate("MainWindow", u"llegHip1Torque", None))
        self.lleg1Torque.setText(QCoreApplication.translate("MainWindow", u"llegHip2Torque", None))
        self.lleg2Torque.setText(QCoreApplication.translate("MainWindow", u"llegHip3Torque", None))
        self.lleg3Torque.setText(QCoreApplication.translate("MainWindow", u"llegKneeTorque", None))
        self.lleg4Torque.setText(QCoreApplication.translate("MainWindow", u"llegAnkle5Torque", None))
        self.lleg5Torque.setText(QCoreApplication.translate("MainWindow", u"llegAnkle6Torque", None))
        self.rarmAngle.setText(QCoreApplication.translate("MainWindow", u"RArmAngle", None))
        self.rarmTorque.setText(QCoreApplication.translate("MainWindow", u"RArmTorque", None))
        self.larmAngle.setText(QCoreApplication.translate("MainWindow", u"LArmAngle", None))
        self.larmTorque.setText(QCoreApplication.translate("MainWindow", u"LArmTorque", None))
        self.rlegForce.setText(QCoreApplication.translate("MainWindow", u"RlegForce", None))
        self.llegForce.setText(QCoreApplication.translate("MainWindow", u"LlegForce", None))
        self.roll.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pitch.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.ComX.setText(QCoreApplication.translate("MainWindow", u"ComX", None))
        self.ComZ.setText(QCoreApplication.translate("MainWindow", u"ComZ", None))
        # self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"-", None))
        # self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"-", None))
        # self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"-", None))
        # self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"-", None))
        # self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The index of data", None))
        self.Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        # self.peroidTime.setText(QCoreApplication.translate("MainWindow", u"PeriodTime", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

