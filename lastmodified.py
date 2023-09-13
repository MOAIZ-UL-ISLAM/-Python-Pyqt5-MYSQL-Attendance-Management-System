from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,\
QLabel, QLineEdit, QTableWidget, \
QTableWidgetItem, QComboBox, QHBoxLayout
from PyQt5.QtCore import Qt
import mysql.connector


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(792, 535)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -10, 801, 551))
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
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(420, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(420, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("QComboBox{\n"
"color:#000;\n"
"background-color:#c5c5c5;\n"
"border :1px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left: 7px;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 150, 741, 371))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"color:#000;\n"
"background-color:#ccc;\n"
"border :2px solid rgb(25, 25, 25);\n"
"border-radius: 12px;\n"
"padding-left: 7px;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Roll no"))
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
        self.label_4.setText(_translate("Form", "Attandance"))
        self.comboBox_3.setItemText(0, _translate("Form", "absent"))
        self.comboBox_3.setItemText(1, _translate("Form", "present"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Roll no"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Courses"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Semester"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Status"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Actions"))


    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='moaiz',
            password='Moaiz0404@',
            database='student',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.conn.cursor()

    def add_student(self):
        print('add student working...')
        name = self.lineEdit.text()
        roll_no = self.lineEdit_2.text()
        course = self.comboBox.currentText()
        semester = self.comboBox_2.currentText()
        attendance = self.comboBox_3.currentText()

        if not name or not roll_no or not course or not semester or not attendance:
            print("Please enter all fields")
            return

        # Insert data into MySQL database
        self.cursor.execute("INSERT INTO students (name, rollno, course, semester, attendance) "
                            "VALUES (%s, %s, %s, %s, %s)",
                            (name, roll_no, course, semester, attendance))
        self.conn.commit()

        # Refresh table
        self.populate_table()


    def populate_table(self):
        # Clear existing data
        self.tableWidget.setRowCount(0)

        # Retrieve data from MySQL database
        self.cursor.execute("SELECT * FROM students")
        data = self.cursor.fetchall()

        # Populate tableWidget
        for row_idx, row_data in enumerate(data):
            self.tableWidget.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_idx, col_idx, item)

            # Add buttons for actions
            update_button = QPushButton("Update")
            update_button.setFixedWidth(60)
            update_button.clicked.connect(lambda _, row=row_idx: self.update_student(row))  # Pass row index to update_student
            delete_button = QPushButton("Delete")
            delete_button.setFixedWidth(60)
            delete_button.clicked.connect(lambda _, row=row_idx: self.delete_student(row))  # Pass row index to delete_student

            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(delete_button)
            button_layout.setAlignment(Qt.AlignCenter)

            container = QWidget()
            container.setLayout(button_layout)

            # Add buttons to the last column (Actions)
            self.tableWidget.setCellWidget(row_idx, 6, container)

            # Set column width for the "Actions" column
            self.tableWidget.setColumnWidth(6, 150)  # Adjust the width value as needed

            # Set row height to ensure buttons are fully visible
            self.tableWidget.setRowHeight(row_idx, 40)  # Adjust the height value as needed

    def update_student(self, row_idx):
        # Get data from tableWidget
        name = self.tableWidget.item(row_idx, 1).text()
        roll_no = self.tableWidget.item(row_idx, 2).text()
        course = self.tableWidget.item(row_idx, 3).text()
        semester = self.tableWidget.item(row_idx, 4).text()
        attendance = self.tableWidget.item(row_idx, 5).text()  # Get attendance as text

        # Check if attendance is either 'absent' or 'present'
        if attendance not in ['absent', 'present']:
            print("Invalid attendance value:", attendance)
            return

        # Update data in MySQL database
        self.cursor.execute("UPDATE students SET name=%s, rollno=%s, course=%s, semester=%s, attendance=%s "
                            "WHERE rollno=%s",
                            (name, roll_no, course, semester, attendance, roll_no))
        self.conn.commit()

    # Refresh table
        self.populate_table()

    def delete_student(self, row):
        # Get roll_no from tableWidget
        roll_no = self.tableWidget.item(row, 2).text()  # Adjusted column index to 2 (Roll no)

        # Delete data from MySQL database
        self.cursor.execute("DELETE FROM students WHERE rollno=%s", (roll_no,))
        self.conn.commit()

        # Refresh table
        self.populate_table()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.populate_table()  # Add this line to populate the table initially
    ui.pushButton.clicked.connect(ui.add_student)
    Form.show()
    sys.exit(app.exec_())





