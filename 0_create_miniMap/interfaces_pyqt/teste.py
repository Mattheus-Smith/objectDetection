import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Círculos e Linha')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Desenha os círculos
        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        circle_radius = 25
        center_x = self.width() / 2
        center_y = self.height() / 2

        # Posiciona os círculos como vértices de um triângulo equilátero
        circle1_center = QPoint(center_x, center_y - 150)
        circle2_center = QPoint(center_x - 130, center_y + 75)
        circle3_center = QPoint(center_x + 130, center_y + 75)

        painter.drawEllipse(circle1_center.x() - circle_radius, circle1_center.y() - circle_radius, 2 * circle_radius, 2 * circle_radius)
        painter.drawEllipse(circle2_center.x() - circle_radius, circle2_center.y() - circle_radius, 2 * circle_radius, 2 * circle_radius)
        painter.drawEllipse(circle3_center.x() - circle_radius, circle3_center.y() - circle_radius, 2 * circle_radius, 2 * circle_radius)

        # Desenha as linhas para formar o polígono convexo
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawLine(circle1_center, circle2_center)
        painter.drawLine(circle2_center, circle3_center)
        painter.drawLine(circle3_center, circle1_center)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec_())
