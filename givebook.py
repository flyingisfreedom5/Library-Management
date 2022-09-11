import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main


con=sqlite3.connect('library.db')
cur=con.cursor()

class GiveBook(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management")
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
        lbl_title=QLabel("Lend Book",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        #######################Bottom Frame Design#######################
        self.book_combo=QComboBox(bottomFrame)
        self.book_combo.setStyleSheet("background-color:white")
        query="SELECT * FROM books WHERE book_status='Available'"
        books=cur.execute(query).fetchall()
        print(books)
        for book in books:
            self.book_combo.addItem(str(book[0])+"-"+book[1])
        self.member_combo=QComboBox(bottomFrame)
        self.member_combo.setStyleSheet("background-color:white")
        query2="SELECT * FROM members"
        members=cur.execute(query2).fetchall()
        for member in members:
            self.member_combo.addItem(str(member[0])+"-"+member[1])
        add_button=QPushButton("Lend Book",bottomFrame)
        add_button.clicked.connect(self.lendBook)
        bottom_layout.addRow(QLabel("Book Name :"),self.book_combo)
        bottom_layout.addRow(QLabel("Member :"),self.member_combo)
        bottom_layout.addRow(QLabel(""),add_button)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def lendBook(self):
       book=self.book_combo.currentText()
       book_id=book.split("-")[0]
       member=self.member_combo.currentText()
       member_id=member.split("-")[0]
       try:

           query="INSERT INTO 'borrows' (bbook_id,bmember_id) values(?,?)"
           cur.execute(query,(book_id,member_id))
           con.commit()
           cur.execute('UPDATE books SET book_status=? WHERE book_id=?',('Not Available',book_id))
           con.commit()
           QMessageBox.information(self,"Info!!!","Success!!!")


       except:
           QMessageBox.information(self, "Warning!!!", "Not Success!!!")

