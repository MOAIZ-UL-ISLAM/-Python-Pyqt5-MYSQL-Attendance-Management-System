from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,\
QLabel, QLineEdit, QTableWidget, \
QTableWidgetItem, QComboBox, QHBoxLayout
from PyQt5.QtCore import Qt
import mysql.connector
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form2")
        Form.resize(787, 540)
        Form.setMinimumSize(QtCore.QSize(650, 540))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 0, 511, 551))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(152, 152, 152);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(470, 220, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(410, 260, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(-4, -8, 311, 551))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 130, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"color:#000;\n"
"background-color:#c5c5c5;\n"
"border :2px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left: 7px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"color:#000;\n"
"background-color:#c5c5c5;\n"
"border :2px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left:7px;\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(98, 98, 98);\n"
"color:#fff;\n"
"border: 2px solid #000;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"color:#000;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(31, 31, 31);\n"
"color:#fff;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 450, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi2(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form2", "Attandance Management System"))
        self.label_2.setText(_translate("Form2", "Attandance "))
        self.label_3.setText(_translate("Form2", "Management System"))
        self.label_5.setText(_translate("Form2", "User"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Name"))
        self.label_6.setText(_translate("Form2", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Form2", "Password"))
        self.pushButton.setText(_translate("Form2", "Login"))
        self.label_7.setText(_translate("Form2", "Not an Admin?"))
        self.label_8.setText(_translate("Form2", "Contact Your Adminstration"))


class LoginScreen(QtWidgets.QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)

        self.pushButton.clicked.connect(self.check_login)


    def check_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "admin" and password == "12345":
            self.close()  # Close the login screen
            subprocess.run("C:/Users/moaiz/AppData/Local/Programs/Python/Python311/python.exe lastmodified.py",shell=True)
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())






