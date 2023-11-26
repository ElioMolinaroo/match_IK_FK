# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'match_data.ui'
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
        MainWindow.resize(383, 662)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(272777, 272727))
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout_2 = QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.title_label = QLabel(self.main_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(0, 0))
        self.title_label.setMaximumSize(QSize(1155125, 1123243))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.separator01_line = QFrame(self.main_widget)
        self.separator01_line.setObjectName(u"separator01_line")
        self.separator01_line.setFrameShape(QFrame.HLine)
        self.separator01_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.separator01_line)

        self.blend_formLayout = QFormLayout()
        self.blend_formLayout.setObjectName(u"blend_formLayout")
        self.blend_formLayout.setLabelAlignment(Qt.AlignCenter)
        self.blend_formLayout.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.blendCtrl_label = QLabel(self.main_widget)
        self.blendCtrl_label.setObjectName(u"blendCtrl_label")

        self.blend_formLayout.setWidget(0, QFormLayout.LabelRole, self.blendCtrl_label)

        self.blendCtrl_lineEdit = QLineEdit(self.main_widget)
        self.blendCtrl_lineEdit.setObjectName(u"blendCtrl_lineEdit")
        self.blendCtrl_lineEdit.setMinimumSize(QSize(0, 25))

        self.blend_formLayout.setWidget(0, QFormLayout.FieldRole, self.blendCtrl_lineEdit)

        self.blendAttr_label = QLabel(self.main_widget)
        self.blendAttr_label.setObjectName(u"blendAttr_label")

        self.blend_formLayout.setWidget(1, QFormLayout.LabelRole, self.blendAttr_label)

        self.blendAttr_lineEdit = QLineEdit(self.main_widget)
        self.blendAttr_lineEdit.setObjectName(u"blendAttr_lineEdit")
        self.blendAttr_lineEdit.setMinimumSize(QSize(0, 25))

        self.blend_formLayout.setWidget(1, QFormLayout.FieldRole, self.blendAttr_lineEdit)

        self.info_label = QLabel(self.main_widget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setAlignment(Qt.AlignCenter)

        self.blend_formLayout.setWidget(2, QFormLayout.SpanningRole, self.info_label)


        self.verticalLayout.addLayout(self.blend_formLayout)

        self.separator02_line = QFrame(self.main_widget)
        self.separator02_line.setObjectName(u"separator02_line")
        self.separator02_line.setFrameShape(QFrame.HLine)
        self.separator02_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.separator02_line)

        self.IK_formLayout = QFormLayout()
        self.IK_formLayout.setObjectName(u"IK_formLayout")
        self.IK_formLayout.setLabelAlignment(Qt.AlignCenter)
        self.IK_formLayout.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.ik_joint01_label = QLabel(self.main_widget)
        self.ik_joint01_label.setObjectName(u"ik_joint01_label")

        self.IK_formLayout.setWidget(0, QFormLayout.LabelRole, self.ik_joint01_label)

        self.ik_joint01_lineEdit = QLineEdit(self.main_widget)
        self.ik_joint01_lineEdit.setObjectName(u"ik_joint01_lineEdit")
        self.ik_joint01_lineEdit.setMinimumSize(QSize(0, 25))

        self.IK_formLayout.setWidget(0, QFormLayout.FieldRole, self.ik_joint01_lineEdit)

        self.ik_joint02_label = QLabel(self.main_widget)
        self.ik_joint02_label.setObjectName(u"ik_joint02_label")

        self.IK_formLayout.setWidget(1, QFormLayout.LabelRole, self.ik_joint02_label)

        self.ik_joint02_lineEdit = QLineEdit(self.main_widget)
        self.ik_joint02_lineEdit.setObjectName(u"ik_joint02_lineEdit")
        self.ik_joint02_lineEdit.setMinimumSize(QSize(0, 25))

        self.IK_formLayout.setWidget(1, QFormLayout.FieldRole, self.ik_joint02_lineEdit)

        self.ik_joint03_label = QLabel(self.main_widget)
        self.ik_joint03_label.setObjectName(u"ik_joint03_label")

        self.IK_formLayout.setWidget(2, QFormLayout.LabelRole, self.ik_joint03_label)

        self.ik_joint03_lineEdit = QLineEdit(self.main_widget)
        self.ik_joint03_lineEdit.setObjectName(u"ik_joint03_lineEdit")
        self.ik_joint03_lineEdit.setMinimumSize(QSize(0, 25))

        self.IK_formLayout.setWidget(2, QFormLayout.FieldRole, self.ik_joint03_lineEdit)

        self.ik_ctrl01_label = QLabel(self.main_widget)
        self.ik_ctrl01_label.setObjectName(u"ik_ctrl01_label")

        self.IK_formLayout.setWidget(3, QFormLayout.LabelRole, self.ik_ctrl01_label)

        self.ik_ctrl01_lineEdit = QLineEdit(self.main_widget)
        self.ik_ctrl01_lineEdit.setObjectName(u"ik_ctrl01_lineEdit")
        self.ik_ctrl01_lineEdit.setMinimumSize(QSize(0, 25))

        self.IK_formLayout.setWidget(3, QFormLayout.FieldRole, self.ik_ctrl01_lineEdit)

        self.ik_ctrl02_label = QLabel(self.main_widget)
        self.ik_ctrl02_label.setObjectName(u"ik_ctrl02_label")

        self.IK_formLayout.setWidget(4, QFormLayout.LabelRole, self.ik_ctrl02_label)

        self.ik_ctrl02_lineEdit = QLineEdit(self.main_widget)
        self.ik_ctrl02_lineEdit.setObjectName(u"ik_ctrl02_lineEdit")
        self.ik_ctrl02_lineEdit.setMinimumSize(QSize(0, 25))

        self.IK_formLayout.setWidget(4, QFormLayout.FieldRole, self.ik_ctrl02_lineEdit)

        self.ik_ctrl03_label = QLabel(self.main_widget)
        self.ik_ctrl03_label.setObjectName(u"ik_ctrl03_label")

        self.IK_formLayout.setWidget(5, QFormLayout.LabelRole, self.ik_ctrl03_label)

        self.ik_ctrl03_lineEdit = QLineEdit(self.main_widget)
        self.ik_ctrl03_lineEdit.setObjectName(u"ik_ctrl03_lineEdit")
        self.ik_ctrl03_lineEdit.setMinimumSize(QSize(0, 25))

        self.IK_formLayout.setWidget(5, QFormLayout.FieldRole, self.ik_ctrl03_lineEdit)


        self.verticalLayout.addLayout(self.IK_formLayout)

        self.separator03_line = QFrame(self.main_widget)
        self.separator03_line.setObjectName(u"separator03_line")
        self.separator03_line.setFrameShape(QFrame.HLine)
        self.separator03_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.separator03_line)

        self.FK_formLayout = QFormLayout()
        self.FK_formLayout.setObjectName(u"FK_formLayout")
        self.FK_formLayout.setLabelAlignment(Qt.AlignCenter)
        self.FK_formLayout.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.fk_joint01_label = QLabel(self.main_widget)
        self.fk_joint01_label.setObjectName(u"fk_joint01_label")

        self.FK_formLayout.setWidget(0, QFormLayout.LabelRole, self.fk_joint01_label)

        self.fk_joint01_lineEdit = QLineEdit(self.main_widget)
        self.fk_joint01_lineEdit.setObjectName(u"fk_joint01_lineEdit")
        self.fk_joint01_lineEdit.setMinimumSize(QSize(0, 25))

        self.FK_formLayout.setWidget(0, QFormLayout.FieldRole, self.fk_joint01_lineEdit)

        self.fk_joint02_label = QLabel(self.main_widget)
        self.fk_joint02_label.setObjectName(u"fk_joint02_label")

        self.FK_formLayout.setWidget(1, QFormLayout.LabelRole, self.fk_joint02_label)

        self.fk_joint02_lineEdit = QLineEdit(self.main_widget)
        self.fk_joint02_lineEdit.setObjectName(u"fk_joint02_lineEdit")
        self.fk_joint02_lineEdit.setMinimumSize(QSize(0, 25))

        self.FK_formLayout.setWidget(1, QFormLayout.FieldRole, self.fk_joint02_lineEdit)

        self.fk_joint03_label = QLabel(self.main_widget)
        self.fk_joint03_label.setObjectName(u"fk_joint03_label")

        self.FK_formLayout.setWidget(2, QFormLayout.LabelRole, self.fk_joint03_label)

        self.fk_joint03_lineEdit = QLineEdit(self.main_widget)
        self.fk_joint03_lineEdit.setObjectName(u"fk_joint03_lineEdit")
        self.fk_joint03_lineEdit.setMinimumSize(QSize(0, 25))

        self.FK_formLayout.setWidget(2, QFormLayout.FieldRole, self.fk_joint03_lineEdit)

        self.fk_ctrl01_label = QLabel(self.main_widget)
        self.fk_ctrl01_label.setObjectName(u"fk_ctrl01_label")

        self.FK_formLayout.setWidget(3, QFormLayout.LabelRole, self.fk_ctrl01_label)

        self.fk_ctrl01_lineEdit = QLineEdit(self.main_widget)
        self.fk_ctrl01_lineEdit.setObjectName(u"fk_ctrl01_lineEdit")
        self.fk_ctrl01_lineEdit.setMinimumSize(QSize(0, 25))

        self.FK_formLayout.setWidget(3, QFormLayout.FieldRole, self.fk_ctrl01_lineEdit)

        self.fk_ctrl02_label = QLabel(self.main_widget)
        self.fk_ctrl02_label.setObjectName(u"fk_ctrl02_label")

        self.FK_formLayout.setWidget(4, QFormLayout.LabelRole, self.fk_ctrl02_label)

        self.fk_ctrl02_lineEdit = QLineEdit(self.main_widget)
        self.fk_ctrl02_lineEdit.setObjectName(u"fk_ctrl02_lineEdit")
        self.fk_ctrl02_lineEdit.setMinimumSize(QSize(0, 25))

        self.FK_formLayout.setWidget(4, QFormLayout.FieldRole, self.fk_ctrl02_lineEdit)

        self.fk_ctrl03_label = QLabel(self.main_widget)
        self.fk_ctrl03_label.setObjectName(u"fk_ctrl03_label")

        self.FK_formLayout.setWidget(5, QFormLayout.LabelRole, self.fk_ctrl03_label)

        self.fk_ctrl03_lineEdit = QLineEdit(self.main_widget)
        self.fk_ctrl03_lineEdit.setObjectName(u"fk_ctrl03_lineEdit")
        self.fk_ctrl03_lineEdit.setMinimumSize(QSize(0, 25))

        self.FK_formLayout.setWidget(5, QFormLayout.FieldRole, self.fk_ctrl03_lineEdit)


        self.verticalLayout.addLayout(self.FK_formLayout)

        self.sendToDatabase_button = QPushButton(self.main_widget)
        self.sendToDatabase_button.setObjectName(u"sendToDatabase_button")
        self.sendToDatabase_button.setMinimumSize(QSize(180, 40))
        self.sendToDatabase_button.setMaximumSize(QSize(180, 40))
        self.sendToDatabase_button.setAutoDefault(False)

        self.verticalLayout.addWidget(self.sendToDatabase_button, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(6, 2)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Match IK FK", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"IK FK Data", None))
        self.blendCtrl_label.setText(QCoreApplication.translate("MainWindow", u"Blend Control", None))
        self.blendAttr_label.setText(QCoreApplication.translate("MainWindow", u"Blend Attribute", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"^ Use the short name, nice name won't work... ^", None))
        self.ik_joint01_label.setText(QCoreApplication.translate("MainWindow", u"IK Joint 01", None))
        self.ik_joint01_lineEdit.setText("")
        self.ik_joint02_label.setText(QCoreApplication.translate("MainWindow", u"IK Joint 02", None))
        self.ik_joint02_lineEdit.setText("")
        self.ik_joint03_label.setText(QCoreApplication.translate("MainWindow", u"IK Joint 03", None))
        self.ik_joint03_lineEdit.setText("")
        self.ik_ctrl01_label.setText(QCoreApplication.translate("MainWindow", u"IK Control 01", None))
        self.ik_ctrl01_lineEdit.setText("")
        self.ik_ctrl02_label.setText(QCoreApplication.translate("MainWindow", u"IK Control 02", None))
        self.ik_ctrl02_lineEdit.setText("")
        self.ik_ctrl03_label.setText(QCoreApplication.translate("MainWindow", u"IK Control 03", None))
        self.ik_ctrl03_lineEdit.setText("")
        self.fk_joint01_label.setText(QCoreApplication.translate("MainWindow", u"FK Joint 01", None))
        self.fk_joint01_lineEdit.setText("")
        self.fk_joint02_label.setText(QCoreApplication.translate("MainWindow", u"FK Joint 02", None))
        self.fk_joint02_lineEdit.setText("")
        self.fk_joint03_label.setText(QCoreApplication.translate("MainWindow", u"FK Joint 03", None))
        self.fk_joint03_lineEdit.setText("")
        self.fk_ctrl01_label.setText(QCoreApplication.translate("MainWindow", u"FK Control 01", None))
        self.fk_ctrl01_lineEdit.setText("")
        self.fk_ctrl02_label.setText(QCoreApplication.translate("MainWindow", u"FK Control 02", None))
        self.fk_ctrl02_lineEdit.setText("")
        self.fk_ctrl03_label.setText(QCoreApplication.translate("MainWindow", u"FK Control 03", None))
        self.fk_ctrl03_lineEdit.setText("")
        self.sendToDatabase_button.setText(QCoreApplication.translate("MainWindow", u"SEND TO DATABASE", None))
    # retranslateUi

