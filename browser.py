import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://www.example.com"))

        # Create the address bar
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url)

        # Create the back, forward, and refresh buttons
        self.back_button = QPushButton("<", self)
        self.back_button.clicked.connect(self.view.back)
        self.forward_button = QPushButton(">", self)
        self.forward_button.clicked.connect(self.view.forward)
        self.refresh_button = QPushButton("⟳", self)
        self.refresh_button.clicked.connect(self.view.reload)

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

    def load_url(self):
        url = QUrl(self.address_bar.text())
        self.view.load(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
