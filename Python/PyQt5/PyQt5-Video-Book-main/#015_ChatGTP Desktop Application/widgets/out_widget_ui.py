# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/pingl/Desktop/ChatGTP\widgets\out_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(841, 258)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_9 = QtWidgets.QFrame(Form)
        self.frame_9.setStyleSheet("background: #f7f7f8;\n"
"border: 0.5px solid #dededf;\n"
"")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_11.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_10.setStyleSheet("border:none;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_14.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/thumb_up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon)
        self.pushButton_14.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 0, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_15.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/thumb_down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_11.addWidget(self.frame_10, 0, 3, 2, 1)
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setStyleSheet("border:none;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/chatGTP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout_11.addWidget(self.frame_12, 0, 1, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem3, 0, 0, 2, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem4, 0, 4, 2, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setMinimumSize(QtCore.QSize(600, 0))
        self.label_4.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: none;")
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_9, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Quantum computing is a type of computing that uses the principles of quantum mechanics to process information. In classical computing, a bit can only be in one of two states: 0 or 1. But in quantum computing, a qubit can be in multiple states simultaneously, called a superposition.\n"
"\n"
"This means that a quantum computer can perform many calculations at the same time, which can lead to exponentially faster processing speeds than classical computers for certain types of problems. Another important concept in quantum computing is entanglement, which allows two qubits to be linked together in such a way that their states become correlated.\n"
"\n"
"Overall, quantum computing is a very powerful tool that has the potential to revolutionize many fields, from cryptography to drug discovery. However, it is still in its early stages of development and there are many challenges that need to be overcome before it becomes widely available."))
from static import resource_rc
