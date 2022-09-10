import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main


con=sqlite3.connect('library.db')
cur=con.cursor()

class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,450,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.setStyleSheet("background-color:white")
        main_layout=QVBoxLayout()
        topFrame=QFrame(self)
        topFrame.setStyleSheet("background-color:white")
        top_layout=QHBoxLayout(topFrame)
        bottomFrame=QFrame(self)
        bottom_layout=QFormLayout(bottomFrame)
        bottomFrame.setStyleSheet("font:15pt Times Bold;background-color:#fcc324")

        img_book=QLabel(topFrame)
        img=QPixmap('icons/addperson.png')
        img_book.setPixmap(img)
        lbl_title=QLabel("Add Member",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        #######################Bottom Frame Design#######################
        self.name_entry=QLineEdit(bottomFrame)
        self.name_entry.setPlaceholderText("Name of Member")
        self.name_entry.setStyleSheet("background-color:white")
        self.phone_entry=QLineEdit(bottomFrame)
        self.phone_entry.setPlaceholderText("Member's phone number")
        self.phone_entry.setStyleSheet("background-color:white")
        add_button=QPushButton("Add",bottomFrame)
        add_button.clicked.connect(self.addMember)
        bottom_layout.addRow(QLabel("Name :"),self.name_entry)
        bottom_layout.addRow(QLabel("Phone :"),self.phone_entry)

        bottom_layout.addRow(QLabel(""),add_button)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def addMember(self):
        name=self.name_entry.text()
        phone=self.phone_entry.text()


        if(name and phone  !=""):
            try:
                query="INSERT INTO 'members' (member_name,member_phone) VALUES (?,?)"
                cur.execute(query,(name,phone))
                con.commit()
                self.name_entry.setText("")
                self.phone_entry.setText("")
                QMessageBox.information(self,"Warning!!!","Member has been added")
            except:
                QMessageBox.information(self,"Warning!!!","<Member> can not be added")
        else:
            QMessageBox.information(self, "Warning!!!", "Fields can not be empty")

