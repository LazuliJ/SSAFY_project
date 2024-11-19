# 회원가입창 만들기
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFormLayout, QLineEdit

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main()

    def main(self):
        self.setWindowTitle("python")
        self.setGeometry(0, 0, 300, 300)

        self.mainWidget = QWidget()

        self.mainLayout = QVBoxLayout()
        self.formLayout = QFormLayout(self)
        self.btn = QPushButton("회원가입")

        self.name = QLineEdit()
        self.age = QLineEdit()

        self.formLayout.addRow("name", self.name)
        self.formLayout.addRow("age", self.age)

        self.mainLayout.addLayout(self.formLayout)
        self.mainLayout.addWidget(self.btn)

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
