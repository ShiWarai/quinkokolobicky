# -*- coding: utf-8 -*-

import sys,yadisk,os  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore
import gui as design
import gui1 as design1
import gui2 as design2
from time import sleep
from zipfile import ZipFile

class Auth(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.entry.clicked.connect(self.start_log)
        self.registration.clicked.connect(self.registration_start)
        self.updater_2.triggered.connect(self.update_programm)
        self.token='AQAAAAANsQTpAAVe0pR3bzkONUQXiZSS3tfEzXI'
        self.yandex=yadisk.YaDisk(id='9dc7649896da48b484e3dedea39f6fe2',secret='527c2f8b25ed45e181c6f8c1d31b8914',token=self.token)
        try:
            self.yandex.check_token(self.token)
        except:
            error_=QtWidgets.QErrorMessage()
            error_.showMessage('Ошибка доступа!')
            sleep(1)
            self.close()
    def update_programm(self):
        self.yandex.download(r'app:/app/versions.txt','versions.txt')
        l=open('versions.txt','r')
        versions=l.read()
        l.close();del l;os.remove('versions.txt')
        num=versions.index('|')
        num=versions[0:num]
        del versions
        try:
            self.yandex.download(r'app:/app/versions/'+num+r'/app.zip','app.zip')
            app=ZipFile(file='app.zip',mode='r')
            way=os.path.abspath(sys.argv[0]).split('\\')
            way.pop(len(way)-1);way_=''
            for x in way:
                way_+=x+'\\'
            way=way_;del way_
            app.extractall(way)
            app.close();os.remove(way+r'/app.zip')
            name=os.path.basename(sys.argv[0])
            try:
                os.remove(way+r'/old.exe')
            except:
                pass
            os.rename(sys.argv[0],way+r'/old.exe')
            os.rename(way+r'/updated.exe',way+r'/'+name)
            QtWidgets.QMessageBox.about(self,'Обновление','Требуется перезагрузка')
            self.close()
        except:
            QtWidgets.QMessageBox.about(self,'Ошибка','Ошибка загрузки!')
    def start_log(self):
        if self.yandex.exists('app:/users/'+str(self.login.text())+'@quinkokolobicky.net') and self.yandex.exists('app:/users/'+str(self.login.text())+r'@quinkokolobicky.net/password_'+str(self.password.text())):
            print('Done!')
        else:
            QtWidgets.QMessageBox.about(self,'Ошибка','Неверный данные пользователя!')
    def registration_start(self):
        reg_=Registartion(self)
        reg_.show()

class Registartion(QtWidgets.QMainWindow, design1.Ui_MainWindow):
    def __init__(self,parent=None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.parent=parent
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.repeat_password.hide()
        self.login.hide()
        self.password.hide()
        self.cancel.clicked.connect(self.canceler)
        self.okay.clicked.connect(self.done)
        self.login_edit.textChanged.connect(self.clear1)
        self.password_edit.textChanged.connect(self.clear2)
        self.repeat_password_edit.textChanged.connect(self.clear3)
    def clear1(self):
        if self.login.isVisible()==True:
            self.login.hide()
    def clear2(self):
        if self.password.isVisible()==True:
            self.password.hide()
    def clear3(self):
        if self.repeat_password.isVisible()==True:
            self.repeat_password.hide()
    def checker(self,a,b):
        if self.parent.yandex.exists(r'app:/users/'+a+'@quinkokolobicky.net'):
            return 1
        elif b.find('|')>=0 or b.find('"')>=0 or b.find('?')>=0 or b.find('*')>=0 or b.find('>')>=0 or b.find('<')>=0 or b.find(':')>=0 or b.find('/')>=0 or b.find('\\')>=0 or b.find('@')>=0 or b=='':
            return 2
        elif b!=str(self.repeat_password_edit.text()):
            return 3
        return 0
    def canceler(self):
        self.close()
    def done(self):
        login_=str(self.login_edit.text())
        password_=str(self.password_edit.text())
        ch=self.checker(login_,password_)
        if ch==1:
            self.login.setText('Логин занят')
            self.login.show()
            self.login.setStyleSheet('color: rgb(170, 0, 0);')
        elif ch==2:
            self.password.setText('Некоректный пароль')
            self.password.show()
            self.password.setStyleSheet('color: rgb(170, 0, 0);')
        elif ch==3:
            self.repeat_password.setText('Пароль не совпадает')
            self.repeat_password.show()
            self.repeat_password.setStyleSheet('color: rgb(170, 0, 0);')
        else:
            self.parent.yandex.mkdir(r'app:/users/'+login_+r'@quinkokolobicky.net')
            self.parent.yandex.mkdir(r'app:/users/'+login_+r'@quinkokolobicky.net/password_'+password_)
            self.parent.yandex.mkdir(r'app:/users/'+login_+r'@quinkokolobicky.net/Входящие')
            self.parent.yandex.mkdir(r'app:/users/'+login_+r'@quinkokolobicky.net/Корзина')
            self.parent.yandex.mkdir(r'app:/users/'+login_+r'@quinkokolobicky.net/Отправленные')
            self.parent.yandex.mkdir(r'app:/users/'+login_+r'@quinkokolobicky.net/Спам')
            self.parent.login.setText(login_)
            self.parent.password.setText(password_)
            self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Auth()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
