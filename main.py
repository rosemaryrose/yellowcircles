import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ok = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.ok = True
        self.repaint()

    def paintEvent(self, event):
        if self.ok:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 226, 5))
        a = randrange(30, 120)
        qp.drawEllipse(randrange(self.height() - a), randrange(self.width() - a), a, a)
        self.ok = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
