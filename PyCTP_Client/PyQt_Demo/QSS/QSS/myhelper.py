#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from frmmessagebox import frmMessageBox
from frminputbox import frmInputBox


class myHelper:
  
    #设置皮肤样式
    def SetStyle(self,styleName):
      
        file = QtCore.QFile(QString(':/image/%s.css' % (styleName)))
        
        file.open(QtCore.QFile.ReadOnly)
        qss = unicode(QString(file.readAll()))  
        file.close()

     
        qApp.setStyleSheet(qss)
        PaletteColor = qss[20:27]
        qApp.setPalette(QPalette(QColor(PaletteColor)))

        



        


    #加载中文字符
    def SetChinese(self):
   
        translator = QTranslator(qApp)
        translator.load(":/image/qt_zh_CN.qm")
        qApp.installTranslator(translator)
   


    #显示输入框
    def ShowInputBox(self,info):
            self.input= frmInputBox()
            self.input.SetMessage(info)
            self.input.show()
        

         

  

    #显示信息框,仅确定按钮
    def ShowMessageBoxInfo(self,info): 
        self.msg = frmMessageBox()
        self.msg.SetMessage(info, 0)
        self.msg.show()


    #显示错误框,仅确定按钮
    def ShowMessageBoxError(self,info):
        self.msg = frmMessageBox()
        self.msg.SetMessage(info, 2)
        self.msg.show()


    #显示询问框,确定和取消按钮
    def ShowMessageBoxQuesion(self,info):
            self.msg = frmMessageBox()
            self.msg.SetMessage(info, 1)
            return self.msg.show()



    #延时
    def Sleep(self,sec):
        dieTime = QTime.currentTime().addMSecs(sec)
        while QTime.currentTime() < dieTime :
            QCoreApplication.processEvents(QEventLoop.AllEvents, 100)
     
    
    #窗体居中显示
    def FormInCenter(self,frm):
    
        frmX = frm.width()
        frmY = frm.height()


        desktop =QApplication.desktop()

        width = desktop.width()

        height = desktop.height()

        frm.move((width - frmX)/2, (height - frmY)/2)

        frm.setMouseTracking(True)



    
    #文件是否存在
    def FileIsExist(self,strFile):
        tempFile = QFile(strFile)
        return tempFile.exists()
    



