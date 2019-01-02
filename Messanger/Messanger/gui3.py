# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(411, 264)
        About.setMinimumSize(QtCore.QSize(411, 264))
        About.setMaximumSize(QtCore.QSize(411, 264))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(About)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 391, 241))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setItalic(False)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Об авторе"))
        self.plainTextEdit.setPlainText(_translate("About", "Код и дизайн делал: Shi Warai\n"
"VK: https://vk.com/shi_warai\n"
"Github: https://github.com/ShiWarai\n"
"Twitter: https://twitter.com/Shi_Warai\n"
"Facebook: https://www.facebook.com/profile.php?id=100015145179964"))

import resurs_rc
