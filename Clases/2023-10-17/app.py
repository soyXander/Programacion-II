from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.comboBox.currentTextChanged.connect(self.onChange)
        self.btnAdd.clicked.connect(self.onAdd)
        self.btnRemove.clicked.connect(self.onRemove)

    def onChange(self):
        print(self.comboBox.currentText())
        print(self.comboBox.currentIndex())
    
    def onAdd(self):
        text = self.addText.text()
        self.comboBox.addItem(text)

    def onRemove(self):
        i = self.comboBox.currentIndex()
        self.comboBox.removeItem(i)

app = QApplication([])
windows = MiVentana()
windows.show()

app.exec()
