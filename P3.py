import sys
from PyQt5 import QtWidgets
from P3_ui import Ui_MainWindow



class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = ExampleApp()
window.show()
app.exec_()