import csv
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('table.ui', self)
        self.load_table()
        self.update1()
        self.tableWidget.itemChanged.connect(self.update1)

    def load_table(self):
        with open('price.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title) + 1)
            self.tableWidget.setHorizontalHeaderLabels(title + ['Количество'])
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                self.tableWidget.setItem(i, 2, QTableWidgetItem('0'))
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

    def update1(self):
        res = 0
        for i in range(self.tableWidget.rowCount()):
            cost = int(self.tableWidget.item(i, 1).text())
            amount = int(self.tableWidget.item(i, 2).text())
            res += cost * amount
        self.allCost.setText(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
