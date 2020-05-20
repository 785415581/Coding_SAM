#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import sys,os
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from PySide2.QtUiTools import QUiLoader

file_ = os.path.dirname(os.path.dirname(__file__))
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('E:/workSpace/Coding_SAM/data/projectInfo.ui')
        lay = QHBoxLayout()
        lay.addWidget(self.ui)
        self.setLayout(lay)


if __name__ == '__main__':
    # if sys.argv is None:
    #     sys.argv = []
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    app.exec_()