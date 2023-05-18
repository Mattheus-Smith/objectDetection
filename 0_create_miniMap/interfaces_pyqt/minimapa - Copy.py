from PyQt5 import QtCore, QtGui, QtWidgets

class BallWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ball_radius = 5  # Tamanho dos círculos
        self.ball_x = 0
        self.ball_y = 0

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_ball_position)
        self.timer.start(20)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(brush)

        painter.drawEllipse(self.ball_x, self.ball_y, self.ball_radius, self.ball_radius)

    def update_ball_position(self):
        self.ball_x += 1
        self.ball_y += 1

        self.update()  # Redraw the widget


class Ui_MainWindow(object):

    def drawLines(self):
        # Criar QPainter para desenhar as linhas
        painter = QtGui.QPainter(self.lineFrame)
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))

        # Obter as coordenadas dos centros dos círculos
        center1 = self.label1.geometry().center()
        center2 = self.label2.geometry().center()
        center3 = self.label3.geometry().center()

        # Desenhar as linhas entre os centros dos círculos
        painter.drawLine(center1, center2)
        painter.drawLine(center2, center3)
        painter.drawLine(center3, center1)

        # Finalizar o desenho
        painter.end()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 991, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Criar QLabel para exibir a imagem
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 991, 400))
        self.label.setScaledContents(True)  # Redimensionar a imagem para preencher todo o espaço
        self.label.setPixmap(QtGui.QPixmap(".\\../campo_futebol_menor.png"))  # Substitua pelo caminho da imagem desejada

        # Create and add the BallWidget to the frame
        self.ball_widget = BallWidget(self.frame)
        self.ball_widget.setGeometry(QtCore.QRect(0, 0, self.frame.width(), self.frame.height()))
        self.ball_widget.setObjectName("ball_widget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 420, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 420, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 420, 93, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 420, 93, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(160, 420, 160, 31))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 520, 141, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 520, 141, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # Criar QLabel para exibir os círculos
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(100, 100, 10, 10))  # Posição do primeiro círculo
        self.label1.setStyleSheet("background-color: red; border-radius: 5px;")

        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(200, 200, 10, 10))  # Posição do segundo círculo
        self.label2.setStyleSheet("background-color: red; border-radius: 5px;")

        self.label3 = QtWidgets.QLabel(self.frame)
        self.label3.setGeometry(QtCore.QRect(300, 100, 10, 10))  # Posição do terceiro círculo
        self.label3.setStyleSheet("background-color: red; border-radius: 5px;")

        # Criar QFrame para exibir as linhas
        self.lineFrame = QtWidgets.QFrame(self.frame)
        self.lineFrame.setGeometry(QtCore.QRect(0, 0, 991, 400))  # Dimensões do lineFrame igual à imagem
        self.lineFrame.setStyleSheet("background-color: transparent;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Desenhar as linhas
        self.drawLines()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Pause"))
        self.pushButton_2.setText(_translate("MainWindow", "Play"))
        self.pushButton_3.setText(_translate("MainWindow", "Proximo"))
        self.pushButton_4.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">Equipe 1:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Equipe 2:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
