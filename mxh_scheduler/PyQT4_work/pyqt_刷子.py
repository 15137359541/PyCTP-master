#!/usr/bin/python

# brushes.py

import sys
from PyQt4 import QtGui, QtCore


class Brushes(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')

    def paintEvent(self, event):
        paint = QtGui.QPainter()

        paint.begin(self)

        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense1Pattern)
        paint.setBrush(brush)
        paint.drawRect(130, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense2Pattern)
        paint.setBrush(brush)
        paint.drawRect(250, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense3Pattern)
        paint.setBrush(brush)
        paint.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.DiagCrossPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense5Pattern)
        paint.setBrush(brush)
        paint.drawRect(130, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense6Pattern)
        paint.setBrush(brush)
        paint.drawRect(250, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense7Pattern)
        paint.setBrush(brush)
        paint.drawRect(250, 105, 90, 60)

        brush.setStyle(QtCore.Qt.HorPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 195, 90, 60)

        brush.setStyle(QtCore.Qt.VerPattern)
        paint.setBrush(brush)
        paint.drawRect(130, 195, 90, 60)

        brush.setStyle(QtCore.Qt.BDiagPattern)
        paint.setBrush(brush)
        paint.drawRect(250, 195, 90, 60)

        paint.end()

app = QtGui.QApplication(sys.argv)
dt = Brushes()
dt.show()
app.exec_()