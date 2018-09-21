#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from frminputbox_ui import Ui_frmInputBox
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *







class frmInputBox(QtGui.QWidget):
    resultsignal= pyqtSignal(str)   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
     
        self.ui = Ui_frmInputBox()

        self.ui.setupUi(self)

          
        self.setWindowModality(Qt.ApplicationModal)  #弹出子窗口时禁用主窗口(阻塞除当前窗体之外的所有的窗体)
        
        self.InitStyle()

    def InitStyle(self):
        self.setProperty("Form", True)                      #窗口始终处于顶层位置
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.mousePressed = False

        fontId = QFontDatabase.addApplicationFont(":/image/fontawesome-webfont.ttf")
        fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
        iconFont = QFont(fontName)

        ##关闭 
        iconFont.setPointSize(10)
        self.ui.btnMenu_Close.setFont(iconFont)
        self.ui.btnMenu_Close.setText(QChar(0xf00d))
        ##图标
        iconFont.setPointSize(12)
        self.ui.lab_Ico.setFont(iconFont)
        self.ui.lab_Ico.setText(QChar(0xf00a))
           
           
        self.ui.btnMenu_Close.clicked.connect(self.close)
        self.ui.btnOk.clicked.connect(self.okSlot)
        self.ui.btnCancel.clicked.connect(self.cancelSlot)

      


  

    def close(self):
        self.hide()

    def okSlot(self):
        self.resultsignal.emit(self.ui.txtValue.text())
        self.hide()
        self.ui.txtValue.setText("")
    def cancelSlot(self):
        self.hide()
        

        
 

    
    def mouseMoveEvent(self, e):
        if self.mousePressed == True:  #鼠标按下
            if e.buttons() and Qt.LeftButton:
                    self.move(e.globalPos() - self.mousePoint)
                    e.accept()
    
        


    def mousePressEvent(self,e):
        if e.button() == Qt.LeftButton:
            self.mousePressed = True
            self.mousePoint = e.globalPos() - self.pos()
            e.accept()
     

    def mouseReleaseEvent(self, e):
         self.mousePressed = False



    def SetMessage(self,title):
         
        self.ui.labInfo.setText(title)
        #self.ui.lab_Title.setText(u"是否保存当前内容？")
        self.ui.btnOk.setText(u"是(&Y)")
        self.ui.btnCancel.setText(u"否(&N)")


    #直接调用
    def ShowInputBox(self,title):
         
        self.ui.labInfo.setText(title)
        #self.ui.lab_Title.setText(u"是否保存当前内容？")
        self.ui.btnOk.setText(u"是(&Y)")
        self.ui.btnCancel.setText(u"否(&N)")

        self.show()
        
        

 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = frmInputBox()
    myapp.show()
    sys.exit(app.exec_())
