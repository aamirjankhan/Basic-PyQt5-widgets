import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
font = QFont("Times",12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Timer Widget")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.colorLable= QLabel(self)
        self.colorLable.setStyleSheet("background-color:green")
        self.colorLable.resize(250,150)
        self.colorLable.move(130,80)
        btnStart=QPushButton("Start",self)
        btnStop=QPushButton("Stop",self)
        btnStart.move(150, 250)
        btnStop.move(250, 250)
        btnStart.clicked.connect(self.start)
        btnStop.clicked.connect(self.stop)
        self.timer=QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.changeColor)
        self.value=0


        self.show()

    def changeColor(self):
        if self.value == 0:
            self.colorLable.setStyleSheet("background-color:yellow")
            self.value = 1
        else:
            self.colorLable.setStyleSheet("background-color:red")
            self.value = 0

    def start(self):
        self.timer.start()
    def stop(self):
        self.timer.stop()

def main():
    App= QApplication(sys.argv)
    window=Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == "__main__":
     main()
