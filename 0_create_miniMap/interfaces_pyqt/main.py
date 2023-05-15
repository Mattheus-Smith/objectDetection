# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):

    def button_search(self, line_edit):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*);;Python Files(*.py)")

        if fileName:
            line_edit.setText(fileName)

    def next_page(self):

        opcao = self.check_gps.isChecked()

        equipe1 = [self.eq1_jg1.text(), self.eq1_jg2.text(), self.eq1_jg3.text(), self.eq1_jg4.text()]
        equipe2 = [self.eq2_jg1.text(), self.eq2_jg2.text(), self.eq2_jg3.text(), self.eq2_jg4.text()]


        if (opcao):

            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.opcao1 = QtWidgets.QLabel(self.centralwidget)
        self.opcao1.setGeometry(QtCore.QRect(10, 10, 841, 31))
        self.opcao1.setAlignment(QtCore.Qt.AlignCenter)
        self.opcao1.setObjectName("opcao1")
        self.opcao2 = QtWidgets.QLabel(self.centralwidget)
        self.opcao2.setGeometry(QtCore.QRect(10, 190, 841, 31))
        self.opcao2.setAlignment(QtCore.Qt.AlignCenter)
        self.opcao2.setObjectName("opcao2")
        self.equipe1 = QtWidgets.QLabel(self.centralwidget)
        self.equipe1.setGeometry(QtCore.QRect(10, 240, 415, 21))
        self.equipe1.setAlignment(QtCore.Qt.AlignCenter)
        self.equipe1.setObjectName("equipe1")
        self.equipe2 = QtWidgets.QLabel(self.centralwidget)
        self.equipe2.setGeometry(QtCore.QRect(430, 240, 415, 21))
        self.equipe2.setAlignment(QtCore.Qt.AlignCenter)
        self.equipe2.setObjectName("equipe2")
        self.pg1_prox = QtWidgets.QPushButton(self.centralwidget)
        self.pg1_prox.setGeometry(QtCore.QRect(360, 480, 121, 41))
        self.pg1_prox.setObjectName("pg1_prox")

        self.pg1_prox.clicked.connect(self.next_page)

        self.check_camera = QtWidgets.QCheckBox(self.centralwidget)
        self.check_camera.setGeometry(QtCore.QRect(360, 100, 251, 20))
        self.check_camera.setObjectName("check_camera")
        self.check_gps = QtWidgets.QCheckBox(self.centralwidget)
        self.check_gps.setGeometry(QtCore.QRect(360, 60, 251, 20))
        self.check_gps.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.check_gps.setObjectName("check_gps")
        self.check_gps_camera = QtWidgets.QCheckBox(self.centralwidget)
        self.check_gps_camera.setGeometry(QtCore.QRect(360, 140, 251, 20))
        self.check_gps_camera.setObjectName("check_gps_camera")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 300, 411, 143))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.eq1_jg1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.eq1_jg1.setObjectName("eq1_jg1")
        self.horizontalLayout.addWidget(self.eq1_jg1)
        self.bt_eq1_jg1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_eq1_jg1.setObjectName("bt_eq1_jg1")
        self.bt_eq1_jg1.clicked.connect(lambda: self.button_search(self.eq1_jg1))
        self.horizontalLayout.addWidget(self.bt_eq1_jg1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.eq1_jg2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.eq1_jg2.setObjectName("eq1_jg2")
        self.horizontalLayout_2.addWidget(self.eq1_jg2)
        self.bt_eq1_jg2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_eq1_jg2.setObjectName("bt_eq1_jg2")
        self.bt_eq1_jg2.clicked.connect(lambda: self.button_search(self.eq1_jg2))
        self.horizontalLayout_2.addWidget(self.bt_eq1_jg2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.eq1_jg3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.eq1_jg3.setObjectName("eq1_jg3")
        self.horizontalLayout_3.addWidget(self.eq1_jg3)
        self.bt_eq1_jg3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_eq1_jg3.setObjectName("bt_eq1_jg3")
        self.bt_eq1_jg3.clicked.connect(lambda: self.button_search(self.eq1_jg3))
        self.horizontalLayout_3.addWidget(self.bt_eq1_jg3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.eq1_jg4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.eq1_jg4.setObjectName("eq1_jg4")
        self.horizontalLayout_4.addWidget(self.eq1_jg4)
        self.bt_eq1_jg4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_eq1_jg4.setObjectName("bt_eq1_jg4")
        self.bt_eq1_jg4.clicked.connect(lambda: self.button_search(self.eq1_jg4))
        self.horizontalLayout_4.addWidget(self.bt_eq1_jg4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(450, 300, 401, 143))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.eq2_jg1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.eq2_jg1.setObjectName("eq2_jg1")
        self.horizontalLayout_5.addWidget(self.eq2_jg1)
        self.bt_eq2_jg1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bt_eq2_jg1.setObjectName("bt_eq2_jg1")
        self.bt_eq2_jg1.clicked.connect(lambda: self.button_search(self.eq2_jg1))
        self.horizontalLayout_5.addWidget(self.bt_eq2_jg1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.eq2_jg2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.eq2_jg2.setObjectName("eq2_jg2")
        self.horizontalLayout_6.addWidget(self.eq2_jg2)
        self.bt_eq2_jg2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bt_eq2_jg2.setObjectName("bt_eq2_jg2")
        self.bt_eq2_jg2.clicked.connect(lambda: self.button_search(self.eq2_jg2))
        self.horizontalLayout_6.addWidget(self.bt_eq2_jg2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.eq2_jg3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.eq2_jg3.setObjectName("eq2_jg3")
        self.horizontalLayout_7.addWidget(self.eq2_jg3)
        self.bt_eq2_jg3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bt_eq2_jg3.setObjectName("bt_eq2_jg3")
        self.bt_eq2_jg3.clicked.connect(lambda: self.button_search(self.eq2_jg3))
        self.horizontalLayout_7.addWidget(self.bt_eq2_jg3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.eq2_jg4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.eq2_jg4.setObjectName("eq2_jg4")
        self.horizontalLayout_8.addWidget(self.eq2_jg4)
        self.bt_eq2_jg4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bt_eq2_jg4.setObjectName("bt_eq3_jg4")
        self.bt_eq2_jg1.clicked.connect(lambda: self.button_search(self.eq2_jg4))
        self.horizontalLayout_8.addWidget(self.bt_eq2_jg4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.opcao1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">1. Opção de registro</span></p></body></html>"))
        self.opcao2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">2. GPS dos jogadores</span></p></body></html>"))
        self.equipe1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#0055ff;\">Equipe 1:</span></p></body></html>"))
        self.equipe2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">Equipe 2:</span></p></body></html>"))
        self.pg1_prox.setText(_translate("MainWindow", "Próximo ->"))
        self.check_camera.setText(_translate("MainWindow", "Câmera"))
        self.check_gps.setText(_translate("MainWindow", "GPS"))
        self.check_gps_camera.setText(_translate("MainWindow", "GPS e Câmera"))
        self.label.setText(_translate("MainWindow", "jogador 1:"))
        self.bt_eq1_jg1.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "jogador 2:"))
        self.bt_eq1_jg2.setText(_translate("MainWindow", "PushButton"))
        self.label_3.setText(_translate("MainWindow", "jogador 3:"))
        self.bt_eq1_jg3.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "jogador 4:"))
        self.bt_eq1_jg4.setText(_translate("MainWindow", "PushButton"))
        self.label_5.setText(_translate("MainWindow", "jogador 1:"))
        self.bt_eq2_jg1.setText(_translate("MainWindow", "PushButton"))
        self.label_6.setText(_translate("MainWindow", "jogador 2:"))
        self.bt_eq2_jg2.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "jogador 3:"))
        self.bt_eq2_jg3.setText(_translate("MainWindow", "PushButton"))
        self.label_8.setText(_translate("MainWindow", "jogador 4:"))
        self.bt_eq2_jg4.setText(_translate("MainWindow", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())