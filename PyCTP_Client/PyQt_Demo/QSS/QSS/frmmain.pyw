#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from frmmain_ui import Ui_frmMain
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import Qt


from myhelper import myHelper
from frmmessagebox import frmMessageBox
from frminputbox import frmInputBox





class MyForm(QtGui.QDialog):
   def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
     
        self.ui = Ui_frmMain()

        self.ui.setupUi(self)
        self.InitStyle()
        self.ui.button.clicked.connect(self.button_clicked)
        self.ui.button2.clicked.connect(self.button2_clicked)
        self.ui.button3.clicked.connect(self.button3_clicked)
        self.ui.button4.clicked.connect(self.button4_clicked)
        
   
       
        self.ui.cboxStyle.currentIndexChanged.connect(self.indexchanged)
        self.myhelper=myHelper()
        self.myhelper.SetChinese()
        
        self.frmmessagebox=frmMessageBox()
        self.frminputbox = frmInputBox()
        
        
      
        
        self.ui.cboxStyle.setCurrentIndex(6)
       

      
   def InitStyle(self):
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint)
        self.location = self.geometry()
        self.max = False
        self.mousePressed = False
        self.ui.lab_Title.installEventFilter(self)
        self.ui.textEdit.installEventFilter(self)


        fontId = QFontDatabase.addApplicationFont(":/image/fontawesome-webfont.ttf")
        fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
        iconFont = QFont(fontName)
      
        ##关闭 
        iconFont.setPointSize(10)
        self.ui.btnMenu_Close.setFont(iconFont)
        self.ui.btnMenu_Close.setText(QChar(0xf00d))
        ##最大化
        iconFont.setPointSize(10)
        self.ui.btnMenu_Max.setFont(iconFont)
        self.ui.btnMenu_Max.setText(QChar(0xf096))

        ##最小化
        iconFont.setPointSize(10)
        self.ui.btnMenu_Min.setFont(iconFont)
        self.ui.btnMenu_Min.setText(QChar(0xf068))

        ##图标
        iconFont.setPointSize(12)
        self.ui.lab_Ico.setFont(iconFont)
        self.ui.lab_Ico.setText(QChar(0xf00a))
           
           
        self.ui.btnMenu_Close.clicked.connect(self.close)
        self.ui.btnMenu_Max.clicked.connect(self.Max)
        self.ui.btnMenu_Min.clicked.connect(self.Min)




         

           

        


   def eventFilter(self,watched,event):

        
       
      
        
        if watched == self.ui.lab_Title:  
            if event.type() == QEvent.MouseButtonDblClick:
                self.Max()
              
      
               
        return QDialog.eventFilter(self,watched,event)


  


   def close(self):
         sys.exit(app.exec_())
        

        
  
   def Max(self):
         if self.max:
             self.setGeometry(self.location)
             self.ui.btnMenu_Max.setToolTip(u"最大化")
         else:
             self.location = self.geometry()
             self.setGeometry(QApplication.desktop().availableGeometry())
             self.ui.btnMenu_Max.setToolTip(u"还原")
       
        
         if self.max==True:
             self.max=False
         else:
             self.max=True
        
        
            


   def Min(self):
        self.showMinimized()
      


    
   def mouseMoveEvent(self, e):
        if self.mousePressed == True:  #鼠标按下
            if e.buttons() and Qt.LeftButton:
                if self.max==False: #不是最大化
                    self.move(e.globalPos() - self.mousePoint)
                    e.accept()
    
        


   def mousePressEvent(self,e):
        if e.button() == Qt.LeftButton:
            self.mousePressed = True
            self.mousePoint = e.globalPos() - self.pos()
            e.accept()
     

   def mouseReleaseEvent(self, e):
         self.mousePressed = False



   def indexchanged(self):
       
        item = self.ui.cboxStyle.currentText()  #itemText(0)得到第一项的内容
        self.myhelper.SetStyle(item)

     

   def button_clicked(self):
        self.myhelper.ShowMessageBoxInfo(u'恭喜你获得我公司送出的1000万元大礼一份!')

   def button2_clicked(self):
      
      self.frmmessagebox.resultsignal.connect(self.recv)      
      self.frmmessagebox.ShowMessageBoxQuesion(u"确定真的不要我了吗？")
      
           
   def button3_clicked(self):
      self.myhelper.ShowMessageBoxError(u"天空飘来五个字!")
   def button4_clicked(self):
      self.frminputbox.resultsignal.connect(self.recv2)
      self.frminputbox.ShowInputBox(u"请输入姓名：")
       
    
     
   def recv(self,s):
      
      if s == 1:
            self.myhelper.ShowMessageBoxInfo(u"你好狠心啊!")
      else:
            self.myhelper.ShowMessageBoxInfo(u"亲爱的,我就知道你不会离开我的!")


   def recv2(self,s):
      self.myhelper.ShowMessageBoxInfo(u"您输入的是："+s)
      
           
    
    
        


      
 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
