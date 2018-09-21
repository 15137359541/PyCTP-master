# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tax_calc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(571, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Price_box = QtGui.QTextEdit(self.centralwidget)
        self.Price_box.setGeometry(QtCore.QRect(420, 110, 104, 71))
        self.Price_box.setObjectName(_fromUtf8("Price_box"))
        self.Price = QtGui.QLabel(self.centralwidget)
        self.Price.setGeometry(QtCore.QRect(102, 123, 57, 29))
        self.Price.setMaximumSize(QtCore.QSize(16777214, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Price.setFont(font)
        self.Price.setMouseTracking(False)
        self.Price.setObjectName(_fromUtf8("Price"))
        self.tax_rate = QtGui.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(460, 320, 42, 22))
        self.tax_rate.setProperty("value", 2)
        self.tax_rate.setObjectName(_fromUtf8("tax_rate"))
        self.calc_tax_button = QtGui.QPushButton(self.centralwidget)
        self.calc_tax_button.setGeometry(QtCore.QRect(100, 330, 75, 23))
        self.calc_tax_button.setObjectName(_fromUtf8("calc_tax_button"))
        self.results_widow = QtGui.QTextEdit(self.centralwidget)
        self.results_widow.setGeometry(QtCore.QRect(280, 430, 104, 71))
        self.results_widow.setObjectName(_fromUtf8("results_widow"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(150, 40, 273, 39))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Price.setText(_translate("MainWindow", "价格", None))
        self.calc_tax_button.setText(_translate("MainWindow", "计算", None))
        self.title.setText(_translate("MainWindow", "这是一个简单的label box", None))

