import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class SliderLabel(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('SliderLabel')

        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setGeometry(30, 40, 100, 30)
        self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'), self.changeValue)


        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)


    def changeValue(self, value):
        pos = self.slider.value()

        if pos == 0:
            self.label.setPixmap(QtGui.QPixmap('F:\\pics\\1.jpg'))
        elif pos > 0 and pos <= 30:
            self.label.setPixmap(QtGui.QPixmap('F:\\pics\\2.jpg'))
        elif pos > 30 and pos < 80:
            self.label.setPixmap(QtGui.QPixmap('F:\\pics\\3.jpg'))
        else:
            self.label.setPixmap(QtGui.QPixmap('F:\\pics\\4.jpg'))

app = QtGui.QApplication(sys.argv)
icon = SliderLabel()
icon.show()
app.exec_()