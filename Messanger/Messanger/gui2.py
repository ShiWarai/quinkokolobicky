# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(686, 343)
        MainWindow.setMinimumSize(QtCore.QSize(686, 343))
        MainWindow.setMaximumSize(QtCore.QSize(686, 343))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.main_image = QtWidgets.QLabel(self.centralwidget)
        self.main_image.setEnabled(True)
        self.main_image.setGeometry(QtCore.QRect(-40, 10, 731, 291))
        self.main_image.setText("")
        self.main_image.setPixmap(QtGui.QPixmap(":/data/main.png"))
        self.main_image.setObjectName("main_image")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 260, 621, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.send_ = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.send_.setMinimumSize(QtCore.QSize(0, 41))
        self.send_.setMaximumSize(QtCore.QSize(1000, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_.setFont(font)
        self.send_.setObjectName("send_")
        self.horizontalLayout.addWidget(self.send_)
        self.cancel_ = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_.sizePolicy().hasHeightForWidth())
        self.cancel_.setSizePolicy(sizePolicy)
        self.cancel_.setMinimumSize(QtCore.QSize(0, 41))
        self.cancel_.setMaximumSize(QtCore.QSize(1000, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancel_.setFont(font)
        self.cancel_.setObjectName("cancel_")
        self.horizontalLayout.addWidget(self.cancel_)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 641, 103))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.email1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email1.setFont(font)
        self.email1.setObjectName("email1")
        self.horizontalLayout_2.addWidget(self.email1)
        self.email_ = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email_.setCursorPosition(20)
        self.email_.setObjectName("email_")
        self.horizontalLayout_2.addWidget(self.email_)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.theme = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.theme.setFont(font)
        self.theme.setObjectName("theme")
        self.horizontalLayout_3.addWidget(self.theme)
        self.theme_ = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.theme_.setCursorPosition(8)
        self.theme_.setObjectName("theme_")
        self.horizontalLayout_3.addWidget(self.theme_)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.main_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(20, 100, 641, 161))
        self.main_text.setObjectName("main_text")
        self.main_table = QtWidgets.QTableWidget(self.centralwidget)
        self.main_table.setGeometry(QtCore.QRect(10, 10, 665, 301))
        self.main_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_table.setRowCount(0)
        self.main_table.setColumnCount(2)
        self.main_table.setObjectName("main_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.main_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.main_table.setHorizontalHeaderItem(1, item)
        self.main_table.horizontalHeader().setVisible(True)
        self.main_table.horizontalHeader().setCascadingSectionResizes(False)
        self.main_table.horizontalHeader().setDefaultSectionSize(200)
        self.main_table.horizontalHeader().setSortIndicatorShown(False)
        self.main_table.horizontalHeader().setStretchLastSection(True)
        self.main_table.verticalHeader().setCascadingSectionResizes(False)
        self.main_table.verticalHeader().setSortIndicatorShown(False)
        self.main_table.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menuBar)
        self.menu_6.setEnabled(False)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menuBar)
        self.menu_7.setEnabled(False)
        self.menu_7.setObjectName("menu_7")
        self.menu_8 = QtWidgets.QMenu(self.menuBar)
        self.menu_8.setObjectName("menu_8")
        MainWindow.setMenuBar(self.menuBar)
        self.write = QtWidgets.QAction(MainWindow)
        self.write.setObjectName("write")
        self.use_old = QtWidgets.QAction(MainWindow)
        self.use_old.setObjectName("use_old")
        self.copy_from_imput = QtWidgets.QAction(MainWindow)
        self.copy_from_imput.setObjectName("copy_from_imput")
        self.open_input = QtWidgets.QAction(MainWindow)
        self.open_input.setObjectName("open_input")
        self.clear_input = QtWidgets.QAction(MainWindow)
        self.clear_input.setObjectName("clear_input")
        self.check_all = QtWidgets.QAction(MainWindow)
        self.check_all.setObjectName("check_all")
        self.open_output = QtWidgets.QAction(MainWindow)
        self.open_output.setObjectName("open_output")
        self.clear_output = QtWidgets.QAction(MainWindow)
        self.clear_output.setObjectName("clear_output")
        self.resend = QtWidgets.QAction(MainWindow)
        self.resend.setObjectName("resend")
        self.open_bl = QtWidgets.QAction(MainWindow)
        self.open_bl.setObjectName("open_bl")
        self.add_to_bl = QtWidgets.QAction(MainWindow)
        self.add_to_bl.setObjectName("add_to_bl")
        self.delete_from_bl = QtWidgets.QAction(MainWindow)
        self.delete_from_bl.setObjectName("delete_from_bl")
        self.clear_bl = QtWidgets.QAction(MainWindow)
        self.clear_bl.setObjectName("clear_bl")
        self.open_trash = QtWidgets.QAction(MainWindow)
        self.open_trash.setObjectName("open_trash")
        self.clear_trash = QtWidgets.QAction(MainWindow)
        self.clear_trash.setObjectName("clear_trash")
        self.open_other = QtWidgets.QAction(MainWindow)
        self.open_other.setObjectName("open_other")
        self.add_other = QtWidgets.QAction(MainWindow)
        self.add_other.setObjectName("add_other")
        self.delete_other = QtWidgets.QAction(MainWindow)
        self.delete_other.setObjectName("delete_other")
        self.update_start = QtWidgets.QAction(MainWindow)
        self.update_start.setObjectName("update_start")
        self.updated_is = QtWidgets.QAction(MainWindow)
        self.updated_is.setObjectName("updated_is")
        self.menu.addAction(self.open_input)
        self.menu.addAction(self.clear_input)
        self.menu.addAction(self.check_all)
        self.menu_2.addAction(self.open_output)
        self.menu_2.addAction(self.resend)
        self.menu_2.addAction(self.clear_output)
        self.menu_3.addAction(self.write)
        self.menu_3.addAction(self.use_old)
        self.menu_3.addAction(self.copy_from_imput)
        self.menu_4.addAction(self.open_bl)
        self.menu_4.addAction(self.add_to_bl)
        self.menu_4.addAction(self.delete_from_bl)
        self.menu_4.addAction(self.clear_bl)
        self.menu_5.addAction(self.open_trash)
        self.menu_5.addAction(self.clear_trash)
        self.menu_6.addAction(self.open_other)
        self.menu_6.addAction(self.add_other)
        self.menu_6.addAction(self.delete_other)
        self.menu_8.addAction(self.update_start)
        self.menu_8.addAction(self.updated_is)
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())
        self.menuBar.addAction(self.menu_6.menuAction())
        self.menuBar.addAction(self.menu_7.menuAction())
        self.menuBar.addAction(self.menu_8.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quinkokolobicky - "))
        self.send_.setText(_translate("MainWindow", "Отправить"))
        self.cancel_.setText(_translate("MainWindow", "Отмена"))
        self.email1.setText(_translate("MainWindow", "E-mail"))
        self.email_.setText(_translate("MainWindow", "@quinkokolobicky.net"))
        self.theme.setText(_translate("MainWindow", "Тема"))
        self.theme_.setText(_translate("MainWindow", "Без темы"))
        self.main_text.setPlainText(_translate("MainWindow", "Без текста"))
        self.main_table.setSortingEnabled(False)
        item = self.main_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "От кого"))
        item = self.main_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тема"))
        self.menu.setTitle(_translate("MainWindow", "Входящие"))
        self.menu_2.setTitle(_translate("MainWindow", "Исходящие"))
        self.menu_3.setTitle(_translate("MainWindow", "Новое письмо"))
        self.menu_4.setTitle(_translate("MainWindow", "Спам"))
        self.menu_5.setTitle(_translate("MainWindow", "Корзина"))
        self.menu_6.setTitle(_translate("MainWindow", "Другие папки"))
        self.menu_7.setTitle(_translate("MainWindow", "Настройки аккаунта"))
        self.menu_8.setTitle(_translate("MainWindow", "Обновить"))
        self.write.setText(_translate("MainWindow", "Написать"))
        self.use_old.setText(_translate("MainWindow", "Использовать шаблон"))
        self.copy_from_imput.setText(_translate("MainWindow", "Скопировать из исходящих"))
        self.open_input.setText(_translate("MainWindow", "Открыть"))
        self.clear_input.setText(_translate("MainWindow", "Очистить"))
        self.check_all.setText(_translate("MainWindow", "Отметить как прочтенное"))
        self.open_output.setText(_translate("MainWindow", "Открыть"))
        self.clear_output.setText(_translate("MainWindow", "Очистить"))
        self.resend.setText(_translate("MainWindow", "Переслать"))
        self.open_bl.setText(_translate("MainWindow", "Открыть"))
        self.add_to_bl.setText(_translate("MainWindow", "Добавить в ЧС нового абонента"))
        self.delete_from_bl.setText(_translate("MainWindow", "Удалить из ЧС абонента"))
        self.clear_bl.setText(_translate("MainWindow", "Очистить"))
        self.open_trash.setText(_translate("MainWindow", "Открыть"))
        self.clear_trash.setText(_translate("MainWindow", "Очистить"))
        self.open_other.setText(_translate("MainWindow", "Открыть"))
        self.add_other.setText(_translate("MainWindow", "Добавить новую папку"))
        self.delete_other.setText(_translate("MainWindow", "Удалить папку"))
        self.update_start.setText(_translate("MainWindow", "Запуск обновления"))
        self.updated_is.setText(_translate("MainWindow", "Проверка на новую версию"))

import resurs_rc
