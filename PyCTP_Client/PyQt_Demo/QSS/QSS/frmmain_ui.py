# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmmain.ui'
#
# Created: Wed Oct 21 20:48:42 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName(_fromUtf8("frmMain"))
        frmMain.resize(703, 646)
        frmMain.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(frmMain)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_title = QtGui.QWidget(frmMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_title.sizePolicy().hasHeightForWidth())
        self.widget_title.setSizePolicy(sizePolicy)
        self.widget_title.setMinimumSize(QtCore.QSize(100, 33))
        self.widget_title.setObjectName(_fromUtf8("widget_title"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_title)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lab_Ico = QtGui.QLabel(self.widget_title)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Ico.sizePolicy().hasHeightForWidth())
        self.lab_Ico.setSizePolicy(sizePolicy)
        self.lab_Ico.setMinimumSize(QtCore.QSize(30, 0))
        self.lab_Ico.setText(_fromUtf8(""))
        self.lab_Ico.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_Ico.setObjectName(_fromUtf8("lab_Ico"))
        self.horizontalLayout_2.addWidget(self.lab_Ico)
        self.lab_Title = QtGui.QLabel(self.widget_title)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Title.sizePolicy().hasHeightForWidth())
        self.lab_Title.setSizePolicy(sizePolicy)
        self.lab_Title.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.lab_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_Title.setObjectName(_fromUtf8("lab_Title"))
        self.horizontalLayout_2.addWidget(self.lab_Title)
        self.widget_menu = QtGui.QWidget(self.widget_title)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setObjectName(_fromUtf8("widget_menu"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_menu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnMenu_Min = QtGui.QPushButton(self.widget_menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Min.sizePolicy().hasHeightForWidth())
        self.btnMenu_Min.setSizePolicy(sizePolicy)
        self.btnMenu_Min.setMinimumSize(QtCore.QSize(31, 0))
        self.btnMenu_Min.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Min.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Min.setText(_fromUtf8(""))
        self.btnMenu_Min.setFlat(True)
        self.btnMenu_Min.setObjectName(_fromUtf8("btnMenu_Min"))
        self.horizontalLayout.addWidget(self.btnMenu_Min)
        self.btnMenu_Max = QtGui.QPushButton(self.widget_menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Max.sizePolicy().hasHeightForWidth())
        self.btnMenu_Max.setSizePolicy(sizePolicy)
        self.btnMenu_Max.setMinimumSize(QtCore.QSize(31, 0))
        self.btnMenu_Max.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Max.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Max.setText(_fromUtf8(""))
        self.btnMenu_Max.setFlat(True)
        self.btnMenu_Max.setObjectName(_fromUtf8("btnMenu_Max"))
        self.horizontalLayout.addWidget(self.btnMenu_Max)
        self.btnMenu_Close = QtGui.QPushButton(self.widget_menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Close.sizePolicy().hasHeightForWidth())
        self.btnMenu_Close.setSizePolicy(sizePolicy)
        self.btnMenu_Close.setMinimumSize(QtCore.QSize(40, 0))
        self.btnMenu_Close.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Close.setText(_fromUtf8(""))
        self.btnMenu_Close.setFlat(True)
        self.btnMenu_Close.setObjectName(_fromUtf8("btnMenu_Close"))
        self.horizontalLayout.addWidget(self.btnMenu_Close)
        self.horizontalLayout_2.addWidget(self.widget_menu)
        self.verticalLayout.addWidget(self.widget_title)
        self.widget_main = QtGui.QWidget(frmMain)
        self.widget_main.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_main)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.cboxStyle = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboxStyle.sizePolicy().hasHeightForWidth())
        self.cboxStyle.setSizePolicy(sizePolicy)
        self.cboxStyle.setObjectName(_fromUtf8("cboxStyle"))
        self.cboxStyle.addItem(_fromUtf8(""))
        self.cboxStyle.addItem(_fromUtf8(""))
        self.cboxStyle.addItem(_fromUtf8(""))
        self.cboxStyle.addItem(_fromUtf8(""))
        self.cboxStyle.addItem(_fromUtf8(""))
        self.cboxStyle.addItem(_fromUtf8(""))
        self.cboxStyle.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.cboxStyle)
        self.spinBox = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.btnChangeStyle = QtGui.QPushButton(self.groupBox_3)
        self.btnChangeStyle.setMinimumSize(QtCore.QSize(90, 0))
        self.btnChangeStyle.setObjectName(_fromUtf8("btnChangeStyle"))
        self.horizontalLayout_6.addWidget(self.btnChangeStyle)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.button = QtGui.QPushButton(self.groupBox_4)
        self.button.setMinimumSize(QtCore.QSize(90, 0))
        self.button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button.setObjectName(_fromUtf8("button"))
        self.horizontalLayout_7.addWidget(self.button)
        self.button2 = QtGui.QPushButton(self.groupBox_4)
        self.button2.setMinimumSize(QtCore.QSize(90, 0))
        self.button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button2.setObjectName(_fromUtf8("button2"))
        self.horizontalLayout_7.addWidget(self.button2)
        self.toolButton = QtGui.QToolButton(self.groupBox_4)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_7.addWidget(self.toolButton)
        self.button3 = QtGui.QPushButton(self.groupBox_4)
        self.button3.setMinimumSize(QtCore.QSize(90, 0))
        self.button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button3.setObjectName(_fromUtf8("button3"))
        self.horizontalLayout_7.addWidget(self.button3)
        self.button4 = QtGui.QPushButton(self.groupBox_4)
        self.button4.setMinimumSize(QtCore.QSize(90, 0))
        self.button4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button4.setObjectName(_fromUtf8("button4"))
        self.horizontalLayout_7.addWidget(self.button4)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox = QtGui.QGroupBox(self.widget_main)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.dateEdit = QtGui.QDateEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.frame = QtGui.QFrame(self.widget_main)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.frame)
        self.groupBox_2 = QtGui.QGroupBox(self.widget_main)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeWidget = QtGui.QTreeWidget(self.tab)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.toolBox = QtGui.QToolBox(self.tab_3)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page.setObjectName(_fromUtf8("page"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.toolBox)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalSlider = QtGui.QSlider(self.groupBox_2)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.horizontalLayout_5.addWidget(self.verticalSlider)
        self.verticalScrollBar = QtGui.QScrollBar(self.groupBox_2)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.horizontalLayout_5.addWidget(self.verticalScrollBar)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.progressBar = QtGui.QProgressBar(self.widget_main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 20))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalSlider = QtGui.QSlider(self.widget_main)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.horizontalScrollBar = QtGui.QScrollBar(self.widget_main)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
        self.verticalLayout_2.addWidget(self.horizontalScrollBar)
        self.verticalLayout.addWidget(self.widget_main)

        self.retranslateUi(frmMain)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(_translate("frmMain", "PyQt自定义UI演示", None))
        self.lab_Title.setText(_translate("frmMain", "PyQt自定义UI演示", None))
        self.btnMenu_Min.setToolTip(_translate("frmMain", "最小化", None))
        self.btnMenu_Max.setToolTip(_translate("frmMain", "最大化", None))
        self.btnMenu_Close.setToolTip(_translate("frmMain", "关闭", None))
        self.label.setText(_translate("frmMain", "风格样式", None))
        self.cboxStyle.setItemText(0, _translate("frmMain", "black", None))
        self.cboxStyle.setItemText(1, _translate("frmMain", "white", None))
        self.cboxStyle.setItemText(2, _translate("frmMain", "blue", None))
        self.cboxStyle.setItemText(3, _translate("frmMain", "gray", None))
        self.cboxStyle.setItemText(4, _translate("frmMain", "brown", None))
        self.cboxStyle.setItemText(5, _translate("frmMain", "dev", None))
        self.cboxStyle.setItemText(6, _translate("frmMain", "silvery", None))
        self.btnChangeStyle.setText(_translate("frmMain", "主窗体", None))
        self.lineEdit.setText(_translate("frmMain", "今天天气不错", None))
        self.button.setText(_translate("frmMain", "信息框", None))
        self.button2.setText(_translate("frmMain", "询问框", None))
        self.toolButton.setText(_translate("frmMain", "...", None))
        self.button3.setText(_translate("frmMain", "错误框", None))
        self.button4.setText(_translate("frmMain", "输入框", None))
        self.radioButton.setText(_translate("frmMain", "男", None))
        self.radioButton_2.setText(_translate("frmMain", "女", None))
        self.checkBox.setText(_translate("frmMain", "中国", None))
        self.checkBox_2.setText(_translate("frmMain", "美国", None))
        self.comboBox.setItemText(0, _translate("frmMain", "测试项目1", None))
        self.comboBox.setItemText(1, _translate("frmMain", "测试项目2", None))
        self.comboBox.setItemText(2, _translate("frmMain", "测试项目3", None))
        self.pushButton_4.setText(_translate("frmMain", "不可用按钮", None))
        self.textEdit.setHtml(_translate("frmMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.假如你想要一件东西，就放它走。它若能回来找你，就永远属于你；它若不回来，那根本就不是你的。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.一个人会落泪，是因为痛；一个人之所以痛，是因为在乎；一个人之所以在乎，是因为有感觉；一个人之所以有感觉，仅因为你是一个人！所以，你有感觉，在乎，痛过，落泪了，说明你是完整不能再完整的一个人。难过的时候，原谅自己，只不过是一个人而已，没有必要把自己看的这么坚不可摧。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.如果真的有一天，某个回不来的人消失了，某个离不开的人离开了，也没关系。时间会把最正确的人带到你的身边，在此之前，你所要做的，是好好的照顾自己。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.你可以沉默不语，不管我的着急；你可以不回信息，不顾我的焦虑；你可以将我的关心，说成让你烦躁的原因；你可以把我的思念，丢在角落不屑一顾。你可以对着其他人微笑，你可以给别人拥抱，你可以对全世界好，却忘了我一直的伤心。------ 你不过是仗着我喜欢你，而那，却是唯一让我变得卑微的原因。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.生命中有一些人与我们擦肩了，却来不及遇见；遇见了，却来不及相识；相识了，却来不及熟悉；熟悉了，却还是要说再见。------ 对自己好点，因为一辈子不长；对身边的人好点，因为下辈子不一定能遇见。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.0岁出场，10岁成长，20岁彷徨，30岁定向，40岁打拼，50岁回望，60岁告老，70岁搓麻，80岁晒太阳，90岁躺床上，100岁挂墙上。生的伟大，死的凄凉，能牵手的时候，请别肩并肩，能拥抱的时候，请别手牵手，能相爱的时候，请别说分开。一生就这么短暂而已。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.时候，希望自己快点长大，长大了，却发现遗失了童年；单身时，开始羡慕恋人的甜蜜，恋爱时，怀念单身时的自由。——— 很多事物，没有得到时总觉得美好，得到之后才开始明白：“我们得到的同时也在失去。”</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8.面对， 不一定最难过。 孤独， 不一定不快乐。 得到， 不一定能长久。 失去， 不一定不再拥有。 不要因为寂寞而错爱， 不要因為错爱而寂寞一生。</p></body></html>", None))
        self.treeWidget.headerItem().setText(0, _translate("frmMain", "学号", None))
        self.treeWidget.headerItem().setText(1, _translate("frmMain", "成绩", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("frmMain", "061104023", None))
        self.treeWidget.topLevelItem(0).setText(1, _translate("frmMain", "105", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("frmMain", "061104056", None))
        self.treeWidget.topLevelItem(1).setText(1, _translate("frmMain", "245", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("frmMain", "061104065", None))
        self.treeWidget.topLevelItem(2).setText(1, _translate("frmMain", "265", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMain", "选项卡1", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("frmMain", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("frmMain", "2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("frmMain", "3", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("frmMain", "学号", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("frmMain", "成绩", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("frmMain", "061104023", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("frmMain", "105", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("frmMain", "061104025", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("frmMain", "108", None))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("frmMain", "061104056", None))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("frmMain", "235", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMain", "选项卡2", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("frmMain", "学生信息管理", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("frmMain", "教师信息管理", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMain", "选项卡3", None))

import frmmain_rc
