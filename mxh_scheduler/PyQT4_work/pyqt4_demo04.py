import sys
from PyQt4 import QtCore, QtGui, uic
from tax_calc import Ui_MainWindow


# #.ui文件地址
# qtCreatorFile = "C:\\Users\\Administrator\\Desktop\\tax_calc.ui"  # Enter file here.
# #这个文件将会被内置的函数载入:
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #clicked是一个内置的函数,当有按钮被点击的时候它会被自动调用
        self.calc_tax_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        #.toPlainText() 是一个内置的可以读取输入框中的值的函数
        price = int(self.Price_box.toPlainText())
        #value()是读取spinbox中值的函数
        tax = self.tax_rate.value()
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        #调用了setText() 函数
        self.results_widow.setText(total_price_string)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())