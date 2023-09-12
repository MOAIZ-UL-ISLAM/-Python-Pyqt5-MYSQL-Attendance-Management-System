
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(792, 535)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 0, 801, 551))
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
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 131, 31))
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
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 761, 351))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(640, 20, 71, 31))
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

        self.retranslateUi2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi2(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Attandance Management"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Roll no"))
        self.label_4.setText(_translate("Form", "Attandance"))
        self.checkBox.setText(_translate("Form", "Present"))
        self.checkBox_2.setText(_translate("Form", "Absent"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Roll No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Department"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Actions"))
        self.pushButton.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi2(Form)
    Form.show()
    sys.exit(app.exec_())



# class NextScreen(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(QtWidgets.QLabel("Welcome to the next screen!"))
#         self.setLayout(layout)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     login_screen = LoginScreen()
#     login_screen.show()
#     sys.exit(app.exec_())