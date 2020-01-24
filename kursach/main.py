# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kursach/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from kursach.func import *
import numpy as np

class Ui_MainWindow(object):
    def close_win(self):
        self.window.close()
        MainWindow.show()

    def open_win1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_HelpWindow_1()
        self.ui.setupUi(self.window)
        self.ui.pushButton.clicked.connect(self.close_win)
        MainWindow.hide()
        self.window.show()

    def open_win2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_HelpWindow_2()
        self.ui.setupUi(self.window)
        self.ui.pushButton.clicked.connect(self.close_win)
        MainWindow.hide()
        self.window.show()

    def open_win3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_ResultWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def g_direction(self):
        if ((abs(self.stack[0] - self.cur_stack[0]) == 2) and (abs(self.stack[1] - self.cur_stack[1]) == 1) or
            (abs(self.stack[0] - self.cur_stack[0]) == 1) and (abs(self.stack[1] - self.cur_stack[1]) == 2)):
            return True
        else:  return False

    def trans(self, stack):
        if stack[1]==0: return "A"+str(stack[0]+1)
        if stack[1]==1: return "B"+str(stack[0]+1)
        if stack[1]==2: return "C"+str(stack[0]+1)

    def check_finish_1(self):
        res = 1
        for i in range(3):
            item = self.tableWidget.item(0,i)
            if item.text() != "♞": res = 0

            item = self.tableWidget.item(2, i)
            if item.text() != "♘": res = 0
        return res

    def check_finish_2(self):
        for i in range(3):
            for j in range(3):
                if self.mass[i,j] == 3:
                    self.open_win3()
                    self.ui.label.setText("Победил пользователь!")
                    self.set_default_2()
                    return False

                if self.mass[i, j] == -3:
                    self.open_win3()
                    self.ui.label.setText("Победил компьютер!")
                    self.set_default_2()
                    return False
        return True


    def check_1(self):
            self.cur_stack = (self.tableWidget.currentRow(), self.tableWidget.currentColumn())
            item = self.tableWidget.currentItem()
            if (item.text() == "" and self.g_direction()):
                item_old = self.tableWidget.item(self.stack[0],self.stack[1])
                item.setText(item_old.text())
                item_old.setText("")

                item_h = QtWidgets.QTableWidgetItem()
                item_h.setText(item.text())
                self.tableWidget_2.setItem(self.count, 0, item_h)

                item_h = QtWidgets.QTableWidgetItem()
                item_h.setText(self.trans(self.stack))
                self.tableWidget_2.setItem(self.count, 1, item_h)

                item_h = QtWidgets.QTableWidgetItem()
                item_h.setText(self.trans(self.cur_stack))
                self.tableWidget_2.setItem(self.count, 2, item_h)

                if self.check_finish_1() == 1:
                    self.open_win3()
                    self.ui.label.setText("Фигуры переставлены!")
                    self.set_default_1()

                self.count = self.count + 1

            self.stack= self.cur_stack


    def check_2(self):
        self.stack = (self.tableWidget_3.currentRow(), self.tableWidget_3.currentColumn())
        item = self.tableWidget_3.currentItem()
        if item.text() == "":
            item.setText("O")
            self.mass[0, self.stack[0]] = self.mass[0, self.stack[0]] + 1
            self.mass[1, self.stack[1]] = self.mass[1, self.stack[1]] + 1
            if self.stack[0] == self.stack[1]:   self.mass[2, 0] = self.mass[2 , 0] + 1
            if 2-self.stack[0] == self.stack[1]:   self.mass[2, 1] = self.mass[2, 1] + 1

            if self.check_finish_2():
                flag = True
                i = 0; j = 0
                while (flag and i<3):
                    while (flag and j<3):
                        item = self.tableWidget_3.item(i,j)
                        if item.text() == "":
                            item.setText("X")
                            self.mass[0,i] = self.mass[0, i] -1
                            self.mass[1,j] = self.mass[1,j] -1
                            if i == j:   self.mass[2, 0] = self.mass[2, 0] -1
                            if 2 - i == j:   self.mass[2, 1] = self.mass[2, 1] -1
                            flag = False
                        j = j + 1
                    j = 0
                    i = i + 1

                if flag:
                    self.open_win3()
                    self.ui.label.setText("Ничья!")
                    self.set_default_2()
                self.check_finish_2()

    def set_default_1(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "♘"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "♘"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "♘"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "♞"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "♞"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "♞"))

        self.stack = (0,0)
        self.count = 0
        self.tableWidget.setCurrentCell(0,0)

        for i in range(3):
            item = self.tableWidget.item(1, i)
            item.setText("")

        self.tableWidget_2.clearContents()

    def set_default_2(self):
        for i in range(3):
            for j in range(3):
                item = self.tableWidget_3.item(j, i)
                item.setText("")
        self.mass = np.array([0]*9).astype(int).reshape(3,3)

        self.compFirst = False
        self.pushButton_3.setEnabled(True)

    def comp_ferst(self):
        self.compFirst = True
        self.set_default_2()
        item = self.tableWidget_3.item(0,0)

        item.setText("X")
        self.mass[0, 0] = self.mass[0, 0] - 1
        self.mass[1, 0] = self.mass[1, 0] - 1
        if 0 == 0:   self.mass[2, 0] = self.mass[2, 0] - 1
        self.pushButton_3.setEnabled(False)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 751, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 381, 391))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        for i in range(3):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(45)
                font.setBold(False)
                font.setItalic(False)
                font.setUnderline(False)
                font.setWeight(50)
                item.setFont(font)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.verticalHeader().setDefaultSectionSize(120)
        self.tableWidget.verticalHeader().setMinimumSectionSize(120)
        self.tableWidget.clicked.connect(self.check_1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(490, 50, 201, 421))
        self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(51)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(51)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(22)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(210, 450, 100, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.set_default_1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(220, 20, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(550, 20, 151, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(230, 40, 371, 371))
        self.tableWidget_3.setRowCount(3)
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)

        for i in range(3):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem()
                item.setText("")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                font = QtGui.QFont()
                font.setPointSize(45)
                font.setBold(False)
                font.setItalic(False)
                font.setUnderline(False)
                font.setWeight(50)
                item.setFont(font)
                self.tableWidget_3.setItem(i, j, item)

        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(120)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(120)
        self.tableWidget_3.clicked.connect(self.check_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 440, 100, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 440, 171, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.compFirst = False
        self.pushButton_2.clicked.connect(self.set_default_2)
        self.pushButton_3.clicked.connect(self.comp_ferst)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(self.open_win1)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.triggered.connect(self.open_win2)
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.set_default_1()
        self.set_default_2()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Курсовая Пустошилов Д.В."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "А"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "♘"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "♘"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "♘"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "♞"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "♞"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "♞"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Фигура"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Откуда"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Куда"))
        self.pushButton.setText(_translate("MainWindow", "Заново"))
        self.label.setText(_translate("MainWindow", "Игровое поле"))
        self.label_2.setText(_translate("MainWindow", "Таблица ходорв"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Переставь фигуры"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "А"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Заново"))
        self.pushButton_3.setText(_translate("MainWindow", "Начать компьютеру"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Крестики-нолики"))
        self.menu.setTitle(_translate("MainWindow", "Игры"))
        self.menu_2.setTitle(_translate("MainWindow", "О игре"))
        self.action_2.setText(_translate("MainWindow", "Переставь фигуры"))
        self.action_3.setText(_translate("MainWindow", "Крестики-нолики"))
        self.action_4.setText(_translate("MainWindow", "Выход"))

class Ui_HelpWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 281, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Об игре Переставь фигуры"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Цель игры Переставь фигуры: делая ходы чёрными и белыми конями, поменять их местами. То есть все белые на клетках третьей строки, все чёрные — первой. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Есть метки противника и занимать одну ячейку двумя метками нельзя.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Напоминание: конь ходит буквой Г (три ячейки в одном направлении и одну — в боковом).</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Закрыть"))

class Ui_HelpWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(304, 258)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 281, 181))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Об игре Крестики-нолики"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Цель игры Крестики-нолики: последовательно делая ходы, заполнить одну стороку, или столбец, или диагонал одинаковыми сиволами. Ходы компьютера имеют метку X, игрока — O. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Есть метки противника и занимать одну ячейку двумя метками нельзя.</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Закрыть"))

class Ui_ResultWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 154)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 171, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Результаты"))
        self.label.setText(_translate("MainWindow", ""))

if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.action_4.triggered.connect(MainWindow.close)
        MainWindow.show()
        sys.exit(app.exec_())

    except Exception as err: print(err)