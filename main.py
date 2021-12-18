from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

import sys

useless = ["How useless it actually is...", "The most useless circle of all", "Useless detected! 100%",
           "Just close the window. Its still useless", "Can you do anything good?", "Useless has overwhelmed the app",
           "Uhh... Useless...", "The last circle was even less useless"]


class App(QMainWindow):
    draw = False

    def __init__(self):
        super(App, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Useless circles")
        self.pushButton.clicked.connect(self.enable)

    def paintEvent(self, qp: QPainter):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_useless_circle_for_free(qp)
            qp.end()

    def draw_useless_circle_for_free(self, qp: QPainter):
        self.label_2.setText(__import__("random").choice(useless))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(200, 75, *(__import__('random').randrange(0, 100),) * 2)

    def enable(self):
        self.draw = True
        self.repaint()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = App()
    b.show()
    sys.exit(a.exec())
