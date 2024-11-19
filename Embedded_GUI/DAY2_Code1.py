# This Python file uses the following encoding: utf-8
import sys
from random import randint

# 예측기 기능 구현하기
# 빈칸 감지, Clear등의 기능은 아직 미구현 상태임에 유의

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFormLayout, QLineEdit, QWidget, QHBoxLayout, QSpinBox, QPushButton, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main()

    def main(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(0, 0, 300, 300)

        self.vlay = QVBoxLayout()
        self.form = QFormLayout(self)

        self.me = QLineEdit()
        self.other = QLineEdit()
        self.age = QSpinBox()

        self.form.addRow("본인: ", self.me)
        self.form.addRow("상대: ", self.other)
        self.form.addRow("상대나이: ", self.age)

        self.vlay.addLayout(self.form)

        self.check = QPushButton("결과확인")
        self.check.clicked.connect(self.cal)
        self.clear = QPushButton("Clear")

        self.vlay.addWidget(self.check)
        self.vlay.addWidget(self.clear)

        # menu
        self.menu = self.menuBar()
        self.menuFile = self.menu.addMenu("&File")

        # main display
        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)

    def cal(self):
        num = randint(0, 100)
        str_result = "NASA 공식에 의해, " + str(num) + "% 확률로 커플이 됩니다."
        self.msg = QMessageBox()
        self.msg.setText(str_result)
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Warning Warning")
        self.msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
