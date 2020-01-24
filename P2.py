import sys
from PyQt5 import QtWidgets
from P2_ui import Ui_MainWindow
import P2_ui
import re

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.probel)
        self.pushButton_2.clicked.connect(self.polind)

    def probel(self):
        self.line = self.textEdit.toPlainText()
        self.lineEdit.setText(str(len(re.findall("\s",self.line))))

    def polind(self):
        self.line2 = self.textEdit_2.toPlainText().lower()
        self.line2 = self.line2.translate({ord(i): None for i in ',!?.'})
        self.words = self.line2.split(" ")
        for i in self.words:
            if i==i[::-1]: self.textEdit_3.append(i)

app = QtWidgets.QApplication(sys.argv)
window = ExampleApp()
window.show()
app.exec_()

