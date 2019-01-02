# -*- coding: utf-8 -*-

import sys,yadisk,os,winsound  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore,QtGui
import gui as design
import gui1 as design1
import gui2 as design2
import gui3 as design3
import gui4 as design4
import threading
from time import sleep
from zipfile import ZipFile
import win32api

def resource_path(relative_path): 
    try: 
     base_path = sys._MEIPASS 
    except Exception: 
     base_path = os.path.abspath(".") 

    return os.path.join(base_path, relative_path) 

def getFileProperties(fname):
    """
    Read all properties of the given file return them as a dictionary.
    """
    propNames = ('Comments', 'InternalName', 'ProductName',
        'CompanyName', 'LegalCopyright', 'ProductVersion',
        'FileDescription', 'LegalTrademarks', 'PrivateBuild',
        'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

    try:
        # backslash as parm returns dictionary of numeric info corresponding to VS_FIXEDFILEINFO struc
        fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                fixedInfo['FileVersionLS'] % 65536)

        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the first pair.
        lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]

        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above

        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

        props['StringFileInfo'] = strInfo
    except:
        pass
    return props

class new_thr(threading.Thread):
    def __init__(self,yandex,out,inp,login,email,sensor):
        threading.Thread.__init__(self)
        self.yandex=yandex
        self.out=out
        self.inp=inp
        self.login_urself=login
        self.email_name=email
        self.sensor=sensor
    def run(self):
        self.sensor.mode.emit(1)
        oper=self.yandex.copy(self.inp,self.out,overwrite=True,force_async=True)
        while self.yandex.get_operation_status(operation_id=oper.href)=='in-progress':
            pass
        self.yandex.remove(self.out+r'/1_'+self.login_urself)
        self.yandex.mkdir(self.out+r'/1_'+self.email_name)
        self.sensor.mode.emit(2)


def reconnect(signal, newhandler=None, oldhandler=None):
    while True:
        try:
            if oldhandler is not None:
                signal.disconnect(oldhandler)
            else:
                signal.disconnect()
        except TypeError:
            break
    if newhandler is not None:
        signal.connect(newhandler)

class Auth(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.entry.clicked.connect(self.start_log)
        self.registration.clicked.connect(self.registration_start)
        self.updater_2.triggered.connect(self.update_program)
        self.token='AQAAAAANsQTpAAVe0pR3bzkONUQXiZSS3tfEzXI'
        self.about_=About()
        self.about_pr_2.triggered.connect(self.about_.show)
        self.about_2=About(True)
        self.about_at.triggered.connect(self.about_2.show)
        self.yandex=yadisk.YaDisk(id='9dc7649896da48b484e3dedea39f6fe2',secret='527c2f8b25ed45e181c6f8c1d31b8914',token=self.token)
        try:
            self.yandex.check_token(self.token)
        except:
            error_=QtWidgets.QErrorMessage()
            error_.showMessage('Ошибка доступа!')
            sleep(1)
            self.close()
        try:
            file_pass=open(r'last_pass.dat','r')
            file_pass_=file_pass.read()
            file_pass.close()
            self.login.setText(file_pass_.split('|')[0])
            self.password.setText(file_pass_.split('|')[1])
            self.checkBox.setChecked(True)
        except:
            pass
        self.setFocus()
    def update_program(self):
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
            main_=MainWindow(self,str(self.login.text())+'@quinkokolobicky.net',str(self.password.text()))
            if self.checkBox.isChecked():
                f1=open(r'last_pass.dat','w')
                f1.write(str(self.login.text())+'|'+str(self.password.text()))
                f1.close()
            else:
                try:
                    os.remove(r'last_pass.dat')
                except:
                    pass
            main_.show()
            self.hide()
        else:
            QtWidgets.QMessageBox.about(self,'Ошибка','Неверный данные пользователя!')
    def registration_start(self):
        reg_=Registartion(self)
        reg_.show()

class Commun(QtCore.QObject):
    mode=QtCore.pyqtSignal(int)
    soundMode=QtCore.pyqtSignal()

class List_Of_Emails(QtWidgets.QWidget, design4.Ui_ListOfEmails):
    def __init__(self,parents):
        super().__init__()
        self.parents=parents
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.cancel.clicked.connect(self.close)
    def showEvent(self,event):
        self.parents.setEnabled(False)
        self.list_=[]
        for x in list(self.parents.yandex.listdir('app:/users')):
            self.list_.append(x.name)
        self.adress.setRowCount(len(self.list_))
        for x in range(len(self.list_)):
            self.adress.setItem(0,x,QtWidgets.QTableWidgetItem(self.list_[x]))
        reconnect(self.adress.cellDoubleClicked,self.copy_email)
        event.accept()
    def closeEvent(self,event):
        self.hide();self.parents.setEnabled(True)
        event.ignore()
    def copy_email(self,row,column):
        self.parents.email_.setText(self.list_[row])
        self.close()
class MainWindow(QtWidgets.QMainWindow, design2.Ui_MainWindow):
    def __init__(self,parent,login,password):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.parent=parent
        self.yandex=parent.yandex
        super().__init__(parent)
        self.login_urself=login
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.null_state()
        self.email=r'app:/users/'+login
        self.setFocus();self.version_=''
        try:
            version_1=getFileProperties(os.path.basename(sys.argv[0]))['FileVersion'].split('.')
            for x in version_1:
                self.version_+=x
            self.version_=int(self.version_)
        except:
            self.version_=100
        self.login=login
        self.password=password
        self.setWindowTitle('Quinkokolobicky - '+self.login)
        self.update_start.triggered.connect(self.update_program)
        self.updated_is.triggered.connect(self.check_update)
        self.clear_input.triggered.connect(self.cleaning_input)
        self.clear_output.triggered.connect(self.cleaning_output)
        self.clear_trash.triggered.connect(self.cleaning_trash)
        self.write.triggered.connect(self.start_sending)
        self.open_input.triggered.connect(self.start_getting)
        self.open_output.triggered.connect(self.start_output)
        self.resend.triggered.connect(self.start_resend)
        self.stop_output=Commun()
        self.stop_output.mode.connect(self.moder)
        self.stop_output.soundMode.connect(self.soundMode)
        #self.about_=About()
        #self.about_2.triggered.connect(self.about_.show)
        #self.about_3=About(True)
        #self.about_1.triggered.connect(self.about_3.show)
        self.List_Emails=List_Of_Emails(self)
        self.new_messege=threading.Thread(target = self.new_messanger,args =(self,))
        self.new_messege.start()
        self.setFocus()
    
    def closeEvent(self,event):
        self.new_messege.do_run = False
        event.accept()

    def new_messanger(self,prog):
        av=threading.current_thread()
        sleep(1);list_last=[]
        for x in list(prog.yandex.listdir(prog.email+r'/Входящие')):
            list_last.append(x.name)
        while getattr(av,'do_run',True):
            try:
                list_=[]
                for x in list(prog.yandex.listdir(prog.email+r'/Входящие')):
                    list_.append(x.name)
                if list_!=list_last and len(list_)>=len(list_last):
                    if prog.isSound.isChecked()==True:
                        winsound.PlaySound(resource_path('sound.wav'), winsound.SND_FILENAME)

                    list_last=list_
                else:
                    list_last=list_
            except:
                pass
    @QtCore.pyqtSlot()
    def soundMode(self):
        if self.isSound.isChecked()==True:
            pass
        else:
            pass

    @QtCore.pyqtSlot(int)
    def moder(self,mode):
        if mode==1:
            self.menu_2.setEnabled(False)
        elif mode==2:
            self.menu_2.setEnabled(True)

    def null_state(self):
        self.main_image.show()
        self.cancel_.hide()
        self.send_.hide()
        self.theme.hide()
        self.email1.hide()
        self.email_.hide()
        self.theme_.hide()
        self.main_text.hide()
        reconnect(self.cancel_.clicked)
        reconnect(self.send_.clicked)
        self.main_table.hide()
        self.email_.setReadOnly(False)
        self.theme_.setReadOnly(False)
        self.main_text.setReadOnly(False)
        self.list_emails_button.hide()
    def start_sending(self):
        self.null_state()
        self.list_emails_button.show()
        self.main_image.hide()
        self.cancel_.setText('Отмена')
        self.send_.setText('Отправить')
        self.cancel_.show()
        self.send_.show()
        reconnect(self.cancel_.clicked,self.null_state)
        reconnect(self.send_.clicked,self.send)
        reconnect(self.list_emails_button.clicked,self.List_Emails.show)
        self.main_text.show()
        self.main_text.setPlainText('Нет текста')
        self.email1.show()
        self.theme.show()
        self.email_.show()
        self.theme_.show()
        self.theme_.setText(u'Нет темы')
        self.email_.setText('@quinkokolobicky.net')
    def start_getting(self):
        self.null_state()
        self.main_image.hide()
        self.main_table.show()
        item=self.main_table.horizontalHeaderItem(0);item.setText(QtCore.QCoreApplication.translate("MainWindow", "От кого"));del item
        self.main_table.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.main_table.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignCenter)
        list_mess=list(self.yandex.listdir(self.email+r'/Входящие'))
        count_mess=len(list_mess);self.name_mess=[]
        self.main_table.setRowCount(count_mess)
        for x in list_mess:
            self.name_mess.append(x.name)
        del list_mess
        self.emails=[]
        self.themes=[]
        for x in range(count_mess):
            a=list(self.yandex.listdir(self.email+r'/Входящие/'+self.name_mess[x]))
            self.emails.append(a[0].name[2:len(a[0].name)])
            self.themes.append(a[1].name[2:len(a[1].name)])
        self.emails.reverse()
        self.themes.reverse()
        self.name_mess.reverse()
        for x in range(count_mess):
            self.main_table.setItem(x,0,QtWidgets.QTableWidgetItem(self.emails[x]))
            self.main_table.setItem(x,1,QtWidgets.QTableWidgetItem(self.themes[x]))
        reconnect(self.main_table.cellDoubleClicked,self.open_message)
    def open_message(self,row,column):
        name=self.name_mess[row]
        self.null_state()
        self.main_image.hide()
        self.cancel_.setText('Отмена')
        self.cancel_.show()
        reconnect(self.cancel_.clicked,self.null_state)
        self.main_text.show()
        oper=self.yandex.download(self.email+r'/Входящие/'+name+r'/3_main/message.txt','message.txt')
        file_=open('message.txt','r')
        mess=file_.read()
        file_.close()
        try:
            os.remove('message.txt')
        except:
            pass
        self.main_text.setPlainText(mess)
        self.main_text.setReadOnly(True)
        self.email1.show()
        self.theme.show()
        self.email_.show()
        self.theme_.show()
        self.theme_.setText(self.themes[row])
        self.email_.setText(self.emails[row])
        self.email_.setReadOnly(True)
        self.theme_.setReadOnly(True)
    def start_resend(self):
        self.null_state()
        self.main_image.hide()
        self.main_table.show()
        item=self.main_table.horizontalHeaderItem(0);item.setText(QtCore.QCoreApplication.translate("MainWindow", "Кому"));del item
        self.main_table.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.main_table.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignCenter)
        list_mess=list(self.yandex.listdir(self.email+r'/Отправленные'))
        count_mess=len(list_mess);self.name_mess=[]
        self.main_table.setRowCount(count_mess)
        for x in list_mess:
            self.name_mess.append(x.name)
        del list_mess
        self.emails=[]
        self.themes=[]
        for x in range(count_mess):
            a=list(self.yandex.listdir(self.email+r'/Отправленные/'+self.name_mess[x]))
            self.emails.append(a[0].name[2:len(a[0].name)])
            self.themes.append(a[1].name[2:len(a[1].name)])
        self.emails.reverse()
        self.themes.reverse()
        self.name_mess.reverse()
        for x in range(count_mess):
            self.main_table.setItem(x,0,QtWidgets.QTableWidgetItem(self.emails[x]))
            self.main_table.setItem(x,1,QtWidgets.QTableWidgetItem(self.themes[x]))
        reconnect(self.main_table.cellDoubleClicked,self.resend_mess)
    def resend_mess(self,row,column):
        theme=self.themes[row]
        email=self.emails[row]
        name=self.name_mess[row]
        self.yandex.download(self.email+r'/Отправленные/'+name+r'/3_main/message.txt','message.txt')
        file_=open('message.txt','r')
        message=file_.read()
        file_.close()
        try:
            os.remove('message.txt')
        except:
            pass
        self.null_state()
        self.start_sending()
        self.theme_.setText(theme)
        self.email_.setText(email)
        self.main_text.setPlainText(message)
    def start_output(self):
        self.null_state()
        self.main_image.hide()
        self.main_table.show()
        item=self.main_table.horizontalHeaderItem(0);item.setText(QtCore.QCoreApplication.translate("MainWindow", "Кому"));del item
        self.main_table.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.main_table.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignCenter)
        list_mess=list(self.yandex.listdir(self.email+r'/Отправленные'))
        count_mess=len(list_mess);self.name_mess=[]
        self.main_table.setRowCount(count_mess)
        for x in list_mess:
            self.name_mess.append(x.name)
        del list_mess
        self.emails=[]
        self.themes=[]
        for x in range(count_mess):
            a=list(self.yandex.listdir(self.email+r'/Отправленные/'+self.name_mess[x]))
            self.emails.append(a[0].name[2:len(a[0].name)])
            self.themes.append(a[1].name[2:len(a[1].name)])
        self.emails.reverse()
        self.themes.reverse()
        self.name_mess.reverse()
        for x in range(count_mess):
            self.main_table.setItem(x,0,QtWidgets.QTableWidgetItem(self.emails[x]))
            self.main_table.setItem(x,1,QtWidgets.QTableWidgetItem(self.themes[x]))
        reconnect(self.main_table.cellDoubleClicked,self.output_folder)
    def output_folder(self,row,column):
        name=self.name_mess[row]
        self.null_state()
        self.main_image.hide()
        self.cancel_.setText('Отмена')
        self.cancel_.show()
        reconnect(self.cancel_.clicked,self.null_state)
        self.main_text.show()
        self.yandex.download(self.email+r'/Отправленные/'+name+r'/3_main/message.txt','message.txt')
        file_=open('message.txt','r')
        mess=file_.read()
        file_.close()
        try:
            os.remove('message.txt')
        except:
            pass
        self.main_text.setPlainText(mess)
        self.main_text.setReadOnly(True)
        self.email1.show()
        self.theme.show()
        self.email_.show()
        self.theme_.show()
        self.theme_.setText(self.themes[row])
        self.email_.setText(self.emails[row])
        self.email_.setReadOnly(True)
        self.theme_.setReadOnly(True)
    def send(self):
        email_name=str(self.email_.text())
        theme_name=str(self.theme_.text())
        if self.yandex.exists(r'app:/users/'+email_name+r'/Входящие') and self.email!=r'app:/users/'+email_name:
            last=0;end=False
            while not end:
                if self.yandex.exists(r'app:/users/'+email_name+r'/Входящие/message_'+str(last)):
                    last+=1
                else:
                    end=True
            last=str(last);
            inp=r'app:/users/'+email_name+r'/Входящие/message_'+last
            self.yandex.mkdir(inp)
            self.yandex.mkdir(inp+r'/1_'+self.login_urself)
            self.yandex.mkdir(inp+r'/2_'+theme_name)
            self.yandex.mkdir(inp+r'/3_main')
            file_=open('message.txt','w')
            file_.write(self.main_text.toPlainText())
            file_.close()
            self.yandex.upload('message.txt',inp+r'/3_main/message.txt')
            os.remove('message.txt')

            last=0;end=False
            while not end:
                if self.yandex.exists(self.email+r'/Отправленные/message_'+str(last)):
                    last+=1
                else:
                    end=True
            last=str(last)
            out=self.email+r'/Отправленные/message_'+last
            self.yandex.mkdir(out)
            new=new_thr(self.yandex,out,inp,self.login_urself,email_name,self.stop_output)
            new.start()
            QtWidgets.QMessageBox.about(self,'Отправка','Завершена успешно')
            self.null_state()
        else:
            QtWidgets.QMessageBox.about(self,'Ошибка','Неправильный e-mail')


    def cleaning_input(self):
        if QtWidgets.QMessageBox.question(self,'Очистка','Удалить всю папку?')==QtWidgets.QMessageBox.Yes:
            try:
                oper=self.yandex.remove(self.email+r'/Входящие',permanently=True,force_async=True)
                while self.yandex.get_operation_status(operation_id=oper.href)=='in-progress':
                    pass
            except:
                pass
            try:
                self.yandex.mkdir(self.email+r'/Входящие')
            except:
                pass
            QtWidgets.QMessageBox.about(self,'Очистка','Завершена')
            self.null_state()
    def cleaning_output(self):
        if QtWidgets.QMessageBox.question(self,'Очистка','Удалить всю папку?')==QtWidgets.QMessageBox.No:
            return 0
        try:
            oper=self.yandex.remove(self.email+r'/Отправленные',permanently=True,force_async=True)
            while self.yandex.get_operation_status(operation_id=oper.href)=='in-progress':
                pass
        except:
            pass
        try:
            self.yandex.mkdir(self.email+r'/Отправленные')
        except:
            pass
        QtWidgets.QMessageBox.about(self,'Очистка','Завершена')
        self.null_state()
    def cleaning_trash(self):
        if QtWidgets.QMessageBox.question(self,'Очистка','Удалить всю папку?')==QtWidgets.QMessageBox.No:
            return 0
        try:
            oper=self.yandex.remove(self.email+r'/Корзина',permanently=True,force_async=True)
            while self.yandex.get_operation_status(operation_id=oper.href)=='in-progress':
                pass
        except:
            pass
        try:
            self.yandex.mkdir(self.email+r'/Корзина')
        except:
            pass
        QtWidgets.QMessageBox.about(self,'Очистка','Завершена')
        self.null_state()
    def changeEvent(self,event):
        if event.type() == QtCore.QEvent.WindowStateChange: 
            if self.windowState() & QtCore.Qt.WindowMinimized: 
                self.showMaximized()
                event.ignore()
    def check_update(self):
        self.parent.yandex.download(r'app:/app/versions.txt','versions.txt')
        l=open('versions.txt','r')
        versions=l.read()
        l.close();del l;os.remove('versions.txt')
        num=versions.index('|')
        num=versions[0:num];del versions
        num=num.split('.')
        num.reverse()
        version_serv=0
        for x in range(0,len(num),1):
            version_serv+=(int(num[x])*(10**x))
        if self.version_<version_serv:
            QtWidgets.QMessageBox.about(self,'Обновление','Обновление требуется')
        else:
            QtWidgets.QMessageBox.about(self,'Обновление','Обновление не требуется')
    def update_program(self):
        self.parent.yandex.download(r'app:/app/versions.txt','versions.txt')
        l=open('versions.txt','r')
        versions=l.read()
        l.close();del l;os.remove('versions.txt')
        num=versions.index('|')
        num=versions[0:num]
        del versions
        try:
            self.parent.yandex.download(r'app:/app/versions/'+num+r'/app.zip','app.zip')
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


class Registartion(QtWidgets.QMainWindow, design1.Ui_MainWindow):
    def __init__(self,parent):
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
        elif len(a)>=60 or len(a)<=3:
            return 4
        elif b.find('|')>=0 or b.find('"')>=0 or b.find('?')>=0 or b.find('*')>=0 or b.find('>')>=0 or b.find('<')>=0 or b.find('-')>=0 or b.find(':')>=0 or b.find('/')>=0 or b.find('\\')>=0 or b.find('@')>=0 or b=='':
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
        elif ch==4:
            self.login.setText('Логин слишком маленький или большой')
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

class About(QtWidgets.QWidget, design3.Ui_About):
    def __init__(self,spec=False):
        super().__init__()
        self.setupUi(self)
        if not spec:
            self.plainTextEdit.setPlainText(QtCore.QCoreApplication.translate("About", "Это программа тестирует работу безсерверного общения по глобальной сети. Сервер в цепочке есть, но выступает лишь в роли хранилища. Программа ещё не финальная, поэтому обновляйте программу!"))
        else:
            self.plainTextEdit.setPlainText(QtCore.QCoreApplication.translate("About", "Код и дизайн делал: Shi Warai\n"
"VK: https://vk.com/shi_warai\n"
"Github: https://github.com/ShiWarai\n"
"Twitter: https://twitter.com/Shi_Warai\n"
"Facebook: https://www.facebook.com/profile.php?id=100015145179964"))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Auth()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()