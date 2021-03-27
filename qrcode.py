import pyqrcode
from threading import Thread
from PyQt5 import uic, QtWidgets


win = QtWidgets.QApplication([])
top = uic.loadUi('qrgenerator.ui')
from time import sleep
funfando = True
anima = False

def animation():
    while anima:
        top.message.setText("Gerando...")
        top.message.setStyleSheet("color:black;")
        sleep(0.3)
        top.message.setText("Gerando..")
        sleep(0.3)
        top.message.setText("Gerando.")
        sleep(0.3)
    top.message.setText("O arquivo foi gerado!")
    sleep(2)
    top.message.setText("")



def actvate():
    global funfando, anima
    link = top.Link_.text()
    name = top.FileName.text()
    if len(link) > 0 and len(name) > 0:
        anima = True
        Thread(target=animation).start()
        pyqrcode.create(link).svg(f"{name}.svg",scale=10)
        sleep(2)
        top.Link_.setText("")
        top.FileName.setText("")
        anima = False
        funfando = False
    else:
        top.message.setText("Erro")
        top.message.setStyleSheet("color: red")
        sleep(2)
        top.message.setText("")
        funfando = False


def ati():
    global funfando
    if funfando == True:
        Thread(target=actvate).start()
        funfando = False




top.GenerateButton.clicked.connect(ati)
top.setFixedSize(375, 430)
top.setWindowTitle('    Qr Generator')
top.show()
win.exec()
