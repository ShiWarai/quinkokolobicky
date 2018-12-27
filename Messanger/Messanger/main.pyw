# -*- coding: utf-8 -*-

import sys,yadisk  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore
import gui as design
from time import sleep

class Programm(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.entry.clicked.connect(self.start_main)
        self.token='AQAAAAANsQTpAAVe0pR3bzkONUQXiZSS3tfEzXI'
        self.yandex=yadisk.YaDisk(id='9dc7649896da48b484e3dedea39f6fe2',secret='527c2f8b25ed45e181c6f8c1d31b8914',token=self.token)
        try:
            self.yandex.check_token(self.token)
        except:
            error_=QtWidgets.QErrorMessage()
            error_.showMessage('Ошибка доступа!')
            sleep(1)
            self.close()
    def start_main(self):
        pass
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Programm()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
