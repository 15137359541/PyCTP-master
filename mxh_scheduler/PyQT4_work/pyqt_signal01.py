#!/usr/bin/python
# sigslot.py
import sys
from PyQt4 import QtGui, QtCore
class SigSlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('signal & slot')
        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        #我们显示一个lcd数字和一个滑块，我们可以通过拖拽滑块来改变lcs的数字显示。
        #将滑块的valueChanged()信号与lcd数字的display()插槽相关联。

        #连接方法有四个参数。sender是发送信号的对象，signal是它产生的信号，
        # receiver是接收信号的对象，最后的slot是相应信号的方法。
        self.connect(slider,  QtCore.SIGNAL('valueChanged(int)'), lcd,
                QtCore.SLOT('display(int)') )
        self.resize(250, 150)
app = QtGui.QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())