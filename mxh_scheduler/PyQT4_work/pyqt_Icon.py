#!/usr/bin/python

# icon.py

import sys
from PyQt4 import QtGui


class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        #头两个参数是窗口的x和y位置。第三个是窗口的宽度，第四个是高度
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('C:\\Users\\Administrator\\Desktop\\favicon.ico'))


app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())