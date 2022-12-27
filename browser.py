import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://www.google.com"))

        # Create the address bar
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url)

        # Create the back, forward, and refresh buttons
        self.back_button = QPushButton("<", self)
        self.back_button.clicked.connect(self.view.back)
        self.back_button.setIcon(QIcon("back.png"))
        self.forward_button = QPushButton(">", self)
        self.forward_button.clicked.connect(self.view.forward)
        self.forward_button.setIcon(QIcon("forward.png"))
        self.refresh_button = QPushButton("⟳", self)
        self.refresh_button.clicked.connect(self.view.reload)
        self.refresh_button.setIcon(QIcon("refresh.png"))

        # Create the layout
        layout = QVBoxLayout()
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.forward_button)
        nav_layout.addWidget(self.refresh_button)
        nav_layout.addWidget(self.address_bar)
        layout.addLayout(nav_layout)
        layout.addWidget(self.view)
        self.setLayout(layout)

        # Set the stylesheet
        self.setStyleSheet('''
            QLineEdit {
                border: 1px solid #999;
                border-radius: 3px;
                padding: 5px;
                font-size: 16px;
            }
            QPushButton {
                border: 1px solid #999;
                border-radius: 3px;
                background-color: #a9a9a9;
                font-size: 16px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #000000;
            }
        ''')

    def load_url(self):
        url = QUrl(self.address_bar.text())
        self.view.load(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
