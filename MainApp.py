from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QPushButton
)
from instr import*
from second_src import*


class MainWin(QWidget):
    def __init__(self):
        '''Main Class for The App and containing the Main Window'''
        super().__init__()
        self.InitUI()
        self.set_App()
        self.Connect()
        self.show()

    def InitUI(self):
        self.vLine = QVBoxLayout()
        self.label1 = QLabel(txt_hello)
        self.disc_Label = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next)
        self.vLine.addWidget(self.label1, alignment = Qt.AlignLeft)
        self.vLine.addWidget(self.disc_Label, alignment = Qt.AlignLeft)
        self.vLine.addWidget(self.btn, alignment = Qt.AlignCenter)



    def set_App(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
        self.setLayout(self.vLine)

    def next_window(self):
        self.next = TestWin()
        self.hide()

    def Connect(self):
        self.btn.clicked.connect(self.next_window)


app = QApplication([])
Main_win = MainWin()
app.exec_()