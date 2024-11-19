# MainWindow에서 1개의 vertical 레이아웃 밑에 각각 1개의 수직, 수평 레이아웃 넣기
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget

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

        self.mainLayout = QVBoxLayout()
        self.headLayout = QHBoxLayout()
        self.bodyLayout = QVBoxLayout()

        self.btnh1 = QPushButton("ONE")
        self.btnh2 = QPushButton("TWO")
        self.btnh3 = QPushButton("THREE")

        self.headLayout.addWidget(self.btnh1)
        self.headLayout.addWidget(self.btnh2)
        self.headLayout.addWidget(self.btnh3)

        self.btnv1 = QPushButton("ONE")
        self.btnv2 = QPushButton("TWO")
        self.btnv3 = QPushButton("THREE")

        self.bodyLayout.addWidget(self.btnv1)
        self.bodyLayout.addWidget(self.btnv2)
        self.bodyLayout.addWidget(self.btnv3)

        self.mainLayout.addLayout(self.headLayout)
        self.mainLayout.addLayout(self.bodyLayout)

        mainWidget = QWidget()
        mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
