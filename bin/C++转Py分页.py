# _*_ coding:utf-8 _*_
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

class MyMainWindow(QWidget):
    def __int__(self,parent=None):
        super(MyMainWindow, self).__int__(parent)

        self.setMinimumWidth(600,300)
        self.setWindowTitle('qurey')

        #caozuohuju
        self.tableView = QTableView()
        self.totalPageLabel = QLabel('totle')
        self.currentPageLabel = QLabel('current')
        self.switchPageLineEdit = QLineEdit('switch')
        self.prevButton = QPushButton('prev')
        self.nextButton = QPushButton('next')
        self.switchPageButton = QPushButton('switch')

        self.operatorLayout = QHBoxLayout()
        self.operatorLayout.addWidget(self.prevButton)
        self.operatorLayout.addWidget(self.nextButton)
        self.operatorLayout.addWidget(self.switchPageButton)
        self.operatorLayout.addWidget(self.switchPageLineEdit)
        self.operatorLayout.addWidget(self.switchPageButton)
        self.operatorLayout.addWidget(QSplitter)


        self.tableView.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableView.verticalHeader().setResizeMode(QHeaderView.Stretch)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.operatorLayout)
        self.mainLayout.addWidget(self.tableView)


