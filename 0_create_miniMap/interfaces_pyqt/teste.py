import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QVBoxLayout
from PyQt5.QtGui import QWindow
import tkinter as tk
from tkinter import Label, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Configurar a janela principal
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Integração PyQt e Tkinter")

        # Criar um QFrame como contêiner para o widget do Tkinter
        self.frame = QFrame(self)
        self.frame.setGeometry(50, 50, 200, 200)

        # Incorporar o widget do Tkinter dentro do QFrame
        self.embed_tkinter_widget()

    def embed_tkinter_widget(self):
        # Criar uma janela do Qt para encapsular o widget do Tkinter
        window = QWindow.fromWinId(tk.Tk().winfo_id())
        container = QWidget.createWindowContainer(window, self.frame)

        # Adicionar o contêiner à disposição vertical
        layout = QVBoxLayout(self.frame)
        layout.addWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
