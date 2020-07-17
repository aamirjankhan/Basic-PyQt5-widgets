import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
font = QFont("Times",12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using List Widget")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.enterRecord=QLineEdit(self)
        self.enterRecord.move(100, 50)
        self.listBox= QListWidget(self)
        self.listBox.move(100, 80)
        list1=["Batman","Superman","Spiderman"]
        self.listBox.addItems(list1)
        #for number in range(1,11):
        #    self.listBox.addItem(str(number))
        btnAdd=QPushButton("Add",self)
        btnDelete=QPushButton("Delete",self)
        btnGet=QPushButton("Get",self)
        btnDeleteAll=QPushButton("Delete all",self)
        btnAdd.move(370, 80)
        btnDelete.move(370, 110)
        btnDeleteAll.move(370, 140)
        btnGet.move(370, 170)
        btnGet.clicked.connect(self.Get)
        btnAdd.clicked.connect(self.Add)
        btnDelete.clicked.connect(self.Delete)
        btnDeleteAll.clicked.connect(self.DeleteAll)
        self.show()

    def Add(self):
        val=self.enterRecord.text()
        self.listBox.addItem(val)
        self.enterRecord.setText("")
    def Delete(self):
        id=self.listBox.currentRow()
        print(id)
        self.listBox.takeItem(id)
    def DeleteAll(self):
        self.listBox.clear()
    def Get(self):
        val=self.listBox.currentItem().text()
        print(val)

def main():
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
     main()
