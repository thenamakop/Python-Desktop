import sys
from PyQt5 import QtWidgets as Q
from PyQt5 import QtCore as Qc

class MyWebBrowser:
    def __init__(self):
        super(MyWebBrowser, self)

        self.window = Q.QWidget()
        self.window.setWindowTitle("Namak's Web Browser")

        self.layout = Q.QtBoxLayout()
        self.horizontal = Q.QHBoxLayout()

        self.url_bar = Q.QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = Q.QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = Q.QPushButton("<-")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = Q.QPushButton("->")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = Q.QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(Q.QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()


app = Qc.QCoreApplication([])
window = MyWebBrowser
app.exec()
