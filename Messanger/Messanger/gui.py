# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 163)
        MainWindow.setMinimumSize(QtCore.QSize(316, 163))
        MainWindow.setMaximumSize(QtCore.QSize(316, 163))
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entry = QtWidgets.QPushButton(self.centralwidget)
        self.entry.setGeometry(QtCore.QRect(20, 110, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.entry.setFont(font)
        self.entry.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.entry.setObjectName("entry")
        self.registration = QtWidgets.QPushButton(self.centralwidget)
        self.registration.setGeometry(QtCore.QRect(170, 110, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.registration.setFont(font)
        self.registration.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.registration.setObjectName("registration")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 251, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login.setInputMask("")
        self.login.setObjectName("login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.login)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.entry.setText(_translate("MainWindow", "Вход"))
        self.registration.setText(_translate("MainWindow", "Регистрация"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.checkBox.setText(_translate("MainWindow", "Запомнить"))

import resurs_rc
