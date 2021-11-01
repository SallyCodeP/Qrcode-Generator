import pyqrcode
from threading import Thread
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import sleep
import sys

funfando = True
anima = False


class Qr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.all()
        self.GenerateButton.clicked.connect(self.ati)
        self.setFixedSize(375, 430)
        self.setWindowTitle('    Qr Generator')

    def ati(self):
        global funfando
        if funfando:
            Thread(target=self.actvate).start()
            funfando = False

    def animation(self):
        while anima:
            self.message.setText("Gerando...")
            self.message.setStyleSheet("color:black;")
            sleep(0.3)
            self.message.setText("Gerando..")
            sleep(0.3)
            self.message.setText("Gerando.")
            sleep(0.3)
        self.message.setText("O arquivo foi gerado!")
        sleep(2)
        self.message.setText("")

    def actvate(self):
        global funfando, anima
        link = self.Link_.text()
        name = self.FileName.text()
        if len(link) > 0 and len(name) > 0:
            anima = True
            Thread(target=self.animation).start()
            pyqrcode.create(link).svg(f"{name}.svg", scale=10)
            sleep(2)
            self.Link_.setText("")
            self.FileName.setText("")
            anima = False
            funfando = False
        else:
            self.message.setText("Erro")
            self.message.setStyleSheet("color: red")
            sleep(2)
            self.message.setText("")
            funfando = False

    def all(self):
        self.setObjectName("MainWindow")
        self.setStyleSheet("background-color: rgb(215, 248, 255);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Link_ = QtWidgets.QLineEdit(self.centralwidget)
        self.Link_.setGeometry(QtCore.QRect(26, 151, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.Link_.setFont(font)
        self.Link_.setStyleSheet("border-radius: 5px;\n"
                                 "background-color: rgb(255, 108, 248,0.4);\n"
                                 "border-style: outset;\n"
                                 "border-width: 1px;")
        self.Link_.setAlignment(QtCore.Qt.AlignCenter)
        self.Link_.setObjectName("Link_")
        self.GenerateButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(106, 291, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.GenerateButton.setFont(font)
        self.GenerateButton.setStyleSheet("border-radius: 15px;\n"
                                          "background-color: rgb(161, 238, 255);\n"
                                          "")
        self.GenerateButton.setObjectName("GenerateButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 211, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(96, 51, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_3.setObjectName("label_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(61, 41, 251, 61))
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255,0.5);\n"
                                    "border-radius: 10px;")
        self.listView.setObjectName("listView")
        self.FileName = QtWidgets.QLineEdit(self.centralwidget)
        self.FileName.setGeometry(QtCore.QRect(26, 241, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.FileName.setFont(font)
        self.FileName.setStyleSheet("border-radius: 5px;\n"
                                    "background-color: rgb(255, 108, 248,0.4);\n"
                                    "border-style: outset;\n"
                                    "border-width: 1px;")
        self.FileName.setAlignment(QtCore.Qt.AlignCenter)
        self.FileName.setObjectName("FileName")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(46, 351, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.message.setFont(font)
        self.message.setStyleSheet("background-color: rgb(255, 255, 255,0)")
        self.message.setObjectName("message")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(16, 111, 341, 241))
        self.listView_2.setStyleSheet("background-color:    white;\n"
                                      "border-radius: 10px;")
        self.listView_2.setObjectName("listView_2")
        self.listView_2.raise_()
        self.listView.raise_()
        self.Link_.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.FileName.raise_()
        self.GenerateButton.raise_()
        self.message.raise_()
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.GenerateButton.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "LINK"))
        self.label_2.setText(_translate("MainWindow", "File Name"))
        self.label_3.setText(_translate("MainWindow", "QRcode generator"))
        self.message.setText(_translate("MainWindow", "Não esqueça de colocar o protocolo http"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Qr()
    win.show()
    sys.exit(app.exec_())

