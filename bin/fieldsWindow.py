# -*- coding:utf-8 -*-
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from functools import partial

class Fields(QWidget):
    def __init__(self,parent=None):
        super(Fields, self).__init__(parent)
        self.setObjectName('fields')
        self.setStyleSheet('''#fields{border-image: url(E:/workSpace/Coding_SAM/resource/project/project1/bbb_thumb_t.jpg}''')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.initUi()
    def initUi(self):

        fields = ['缩略图','作者','流程','id','类型','创建人员']
        self.vlay = QVBoxLayout()
        for i in fields:
            checkBox = QCheckBox(i)
            self.vlay.addWidget(checkBox)
            checkBox.stateChanged.connect(partial(self.status,checkBox))

        finshBt = QPushButton('完成')
        finshBt.clicked.connect(self.close)
        self.vlay.addWidget(finshBt)
        self.setLayout(self.vlay)

    def status(self,widget):
        print(widget.text())

    # def show(self,userPos,pos):
    #     x1 = userPos.x()
    #     y1 = userPos.y()
    #     x = pos.x()
    #     y = pos.y()
    #     self.move(x+62,y+y1)
    #     self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     wind = Fields()
#     wind.show()
#     app.exec_()