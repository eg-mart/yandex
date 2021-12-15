import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('films.ui', self)
        self.btn_search.clicked.connect(self.search)
        self.load_labels()

    def load_labels(self):
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        genres = cur.execute('SELECT title FROM genres').fetchall()
        for genre in genres:
            self.comboBox.addItem(genre[0])

    def search(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
