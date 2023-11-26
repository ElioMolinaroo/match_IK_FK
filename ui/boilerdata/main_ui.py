# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(263, 148)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(15)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.limb_label = QLabel(self.centralwidget)
        self.limb_label.setObjectName(u"limb_label")
        font = QFont()
        font.setPointSize(10)
        self.limb_label.setFont(font)
        self.limb_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.main_layout.addWidget(self.limb_label, 0, 0, 1, 1)

        self.limb_comboBox = QComboBox(self.centralwidget)
        self.limb_comboBox.setObjectName(u"limb_comboBox")
        self.limb_comboBox.setMinimumSize(QSize(100, 35))

        self.main_layout.addWidget(self.limb_comboBox, 0, 1, 1, 2)

        self.match_button = QPushButton(self.centralwidget)
        self.match_button.setObjectName(u"match_button")
        self.match_button.setMinimumSize(QSize(100, 50))
        self.match_button.setMaximumSize(QSize(100, 50))

        self.main_layout.addWidget(self.match_button, 1, 0, 1, 2)

        self.getData_button = QPushButton(self.centralwidget)
        self.getData_button.setObjectName(u"getData_button")
        self.getData_button.setMinimumSize(QSize(100, 50))
        self.getData_button.setMaximumSize(QSize(100, 50))

        self.main_layout.addWidget(self.getData_button, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.limb_label.setText(QCoreApplication.translate("MainWindow", u"LIMB", None))
        self.match_button.setText(QCoreApplication.translate("MainWindow", u"MATCH", None))
        self.getData_button.setText(QCoreApplication.translate("MainWindow", u"GET DATA", None))
    # retranslateUi

