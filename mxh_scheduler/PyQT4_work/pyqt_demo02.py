#!/usr/bin/python

# burning.py

import sys
from PyQt4 import QtGui, QtCore


class Widget(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QLabel.__init__(self, parent)
        self.setMinimumSize(1, 30)
        self.parent = parent
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)

        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        paint.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()
        cw = self.parent.cw
        step = int(round(w / 10.0))


        till = int(((w / 750.0) * cw))
        full = int(((w / 750.0) * 700))

        if cw >= 700:
            paint.setPen(QtGui.QColor(255, 255, 255))
            paint.setBrush(QtGui.QColor(255, 255, 184))
            paint.drawRect(0, 0, full, h)
            paint.setPen(QtGui.QColor(255, 175, 175))
            paint.setBrush(QtGui.QColor(255, 175, 175))
            paint.drawRect(full, 0, till-full, h)
        else:
            paint.setPen(QtGui.QColor(255, 255, 255))
            paint.setBrush(QtGui.QColor(255, 255, 184))
            paint.drawRect(0, 0, till, h)


        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, QtCore.Qt.SolidLine)
        paint.setPen(pen)
        paint.setBrush(QtCore.Qt.NoBrush)
        paint.drawRect(0, 0, w-1, h-1)

        j = 0

        for i in range(step, 10*step, step):
            paint.drawLine(i, 0, i, 5)
            metrics = paint.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            paint.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1

        paint.end()

class Burning(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.cw = 75

        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setRange(1, 750)
        self.slider.setValue(75)
        self.slider.setGeometry(30, 40, 150, 30)

        self.wid = Widget(self)

        self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'), self.changeValue)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Burning')

    def changeValue(self, event):
        self.cw = self.slider.value()
        self.wid.repaint()


app = QtGui.QApplication(sys.argv)
dt = Burning()
dt.show()
app.exec_()