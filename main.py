import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from random import randint
from PyQt5.QtGui import QColor, QBrush, QPainter


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.add_circle)

        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

    def add_circle(self):
        self.scene.clear()

        for i in range(2):
            diameter = randint(20, 70)
            color = QColor(255, 255, 0)
            brush = QBrush(color)

            x = randint(0, self.graphicsView.width() - diameter)
            y = randint(0, self.graphicsView.height() - diameter)

            ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
            ellipse.setBrush(brush)
            ellipse.setFlag(QGraphicsEllipseItem.ItemIsMovable)

            self.scene.addItem(ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
