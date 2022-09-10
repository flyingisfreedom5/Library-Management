import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

con=sqlite3.connect('library.db')
cur=con.cursor()

class AddBook(QWidget):
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
        img=QPixmap('icons/addbook.png')
        img_book.setPixmap(img)
        lbl_title=QLabel("Add Book",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        #######################Bottom Frame Design#######################
        self.name_entry=QLineEdit(bottomFrame)
        self.name_entry.setPlaceholderText("Name of Book")
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry=QLineEdit(bottomFrame)
        self.author_entry.setPlaceholderText("Name of Author")
        self.author_entry.setStyleSheet("background-color:white")
        self.page_entry=QLineEdit(bottomFrame)
        self.page_entry.setPlaceholderText("Page Size")
        self.page_entry.setStyleSheet("background-color:white")
        self.lan_entry=QLineEdit(bottomFrame)
        self.lan_entry.setPlaceholderText("Language")
        self.lan_entry.setStyleSheet("background-color:white")
        self.description=QTextEdit(bottomFrame)
        self.description.setStyleSheet("background-color:white")
        add_button=QPushButton("Add",bottomFrame)
        add_button.clicked.connect(self.addBook)
        bottom_layout.addRow(QLabel("Name :"),self.name_entry)
        bottom_layout.addRow(QLabel("Author :"),self.author_entry)
        bottom_layout.addRow(QLabel("Page :"),self.page_entry)
        bottom_layout.addRow(QLabel("Language :"),self.lan_entry)
        bottom_layout.addRow(QLabel("Description :"),self.description)
        bottom_layout.addRow(QLabel(""),add_button)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def addBook(self):
        name=self.name_entry.text()
        author=self.author_entry.text()
        page=self.page_entry.text()
        language=self.lan_entry.text()
        description=self.description.toPlainText()

        if(name and author and page and language and description !=""):
            try:
                query="INSERT INTO 'books' (book_name,book_author,book_page,book_details,book_language) VALUES (?,?,?,?,?)"
                cur.execute(query,(name,author,page,description,language))
                con.commit()
                self.name_entry.setText("")
                self.author_entry.setText("")
                self.page_entry.setText("")
                self.lan_entry.setText("")
                self.description.setText("")
                QMessageBox.information(self,"Warning!!!","Book has been added")

            except:
                QMessageBox.information(self,"Warning!!!","Book can not be added")
        else:
            QMessageBox.information(self, "Warning!!!", "Fields can not be empty")

        self.mainpage = main.Main()
        self.mainpage.tabs.update()