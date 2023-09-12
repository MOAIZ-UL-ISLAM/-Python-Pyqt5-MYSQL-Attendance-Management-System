from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Attandance Management System"))
        self.label_2.setText(_translate("Form", "Attandance "))
        self.label_3.setText(_translate("Form", "Management System"))
        self.label_5.setText(_translate("Form", "User"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Name"))
        self.label_6.setText(_translate("Form", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label_7.setText(_translate("Form", "Not an Admin?"))
        self.label_8.setText(_translate("Form", "Contact Your Adminstration"))


class LoginScreen(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.check_login)

    def check_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "admin" and password == "12345":
            self.close()  # Close the login screen
            self.next_screen = QtWidgets.QWidget()
            ui = Ui_Form2()
            ui.setupUi2(self.next_screen)
            self.next_screen.show()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")


class Ui_Form2(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(792, 535)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(440, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(440, 40, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(440, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 171, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"color:#000;\n"
"background-color:#c5c5c5;\n"
"border :2px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left: 7px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 30, 141, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"color:#000;\n"
"background-color:#c5c5c5;\n"
"border :2px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left: 7px;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(640, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.pushButton.setFont(font)
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
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 110, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"color:#000;\n"
"background-color:#c5c5c5;\n"
"border :2px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left: 7px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 80, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"color:#000;\n"
"background-color:#c5c5c5;\n"
"border :2px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left: 7px;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.retranslateUi2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi2(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Roll no"))
        self.label_4.setText(_translate("Form", "Attandance"))
        self.checkBox.setText(_translate("Form", "Present"))
        self.checkBox_2.setText(_translate("Form", "Absent"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Ahmed"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "20-xx-xx"))
        self.pushButton.setText(_translate("Form", "Add Student"))
        self.comboBox.setItemText(0, _translate("Form", "Bsc"))
        self.comboBox.setItemText(1, _translate("Form", "Diploma"))
        self.comboBox.setItemText(2, _translate("Form", "Ms"))
        self.label_6.setText(_translate("Form", "Semester"))
        self.label_7.setText(_translate("Form", "Courses"))
        self.comboBox_2.setItemText(0, _translate("Form", "1st"))
        self.comboBox_2.setItemText(1, _translate("Form", "2nd"))
        self.comboBox_2.setItemText(2, _translate("Form", "3rd"))
        self.comboBox_2.setItemText(3, _translate("Form", "4th"))
        self.comboBox_2.setItemText(4, _translate("Form", "5th"))
        self.comboBox_2.setItemText(5, _translate("Form", "6th"))
        self.comboBox_2.setItemText(6, _translate("Form", "7th"))
        self.comboBox_2.setItemText(7, _translate("Form", "8th"))

     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
