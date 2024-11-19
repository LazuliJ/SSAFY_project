# 로그인 시스템 만들기
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFormLayout, QLineEdit, QLabel

from ui_form import Ui_MainWindow

masid = "this_id"
maspwd = "this_password"
cnt = 0

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
        self.btn = QPushButton("로그인")
        self.btn.clicked.connect(self.check)
        self.lbl = QLabel("")

        self.id = QLineEdit()
        self.pwd = QLineEdit()

        self.formLayout.addRow("id", self.id)
        self.formLayout.addRow("password", self.pwd)

        self.mainLayout.addLayout(self.formLayout)
        self.mainLayout.addWidget(self.lbl)
        self.mainLayout.addWidget(self.btn)

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    def check(self):
        global cnt, masid, maspwd

        print(self.id.text())
        print(self.pwd.text())

        if (cnt == 3):
            self.lbl.setText("3회 이상 틀렸습니다. 관리자에게 문의하시기 바랍니다.")
            cnt = 4
        elif (cnt == 4):
            sys.exit()
        elif (self.id.text() == "" or self.pwd.text() == ""):
            self.lbl.setText("id 또는 pwd값이 유효하지 않습니다.")
        elif (len(self.pwd.text()) < 8):
            self.lbl.setText("pwd 길이가 너무 짧습니다.")
        elif (self.id.text() != masid or self.pwd.text() != maspwd):
            self.lbl.setText("id 또는 pwd값이 일치하지 않습니다.")
            cnt += 1
        else:
            self.lbl.setText("로그인 성공.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
