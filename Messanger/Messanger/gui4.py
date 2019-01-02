# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListOfEmails(object):
    def setupUi(self, ListOfEmails):
        ListOfEmails.setObjectName("ListOfEmails")
        ListOfEmails.resize(424, 219)
        ListOfEmails.setMinimumSize(QtCore.QSize(424, 219))
        ListOfEmails.setMaximumSize(QtCore.QSize(424, 219))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ListOfEmails.setWindowIcon(icon)
        self.adress = QtWidgets.QTableWidget(ListOfEmails)
        self.adress.setGeometry(QtCore.QRect(20, 10, 381, 151))
        self.adress.setColumnCount(1)
        self.adress.setObjectName("adress")
        self.adress.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.adress.setHorizontalHeaderItem(0, item)
        self.adress.horizontalHeader().setStretchLastSection(True)
        self.cancel = QtWidgets.QPushButton(ListOfEmails)
        self.cancel.setGeometry(QtCore.QRect(120, 180, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancel.setFont(font)
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cancel.setObjectName("cancel")

        self.retranslateUi(ListOfEmails)
        QtCore.QMetaObject.connectSlotsByName(ListOfEmails)

    def retranslateUi(self, ListOfEmails):
        _translate = QtCore.QCoreApplication.translate
        ListOfEmails.setWindowTitle(_translate("ListOfEmails", "Выбрать из списка адресатов"))
        item = self.adress.horizontalHeaderItem(0)
        item.setText(_translate("ListOfEmails", "Адреса"))
        self.cancel.setText(_translate("ListOfEmails", "Отмена"))

import resurs_rc
