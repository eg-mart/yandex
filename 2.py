import csv
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('table.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
