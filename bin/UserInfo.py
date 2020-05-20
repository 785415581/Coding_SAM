# -*- coding: utf-8 -*-
import os,sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from widget.base import ListItemWidget,SearchLineEdit,Label

class UserInfo():

    def __init__(self):
        super(UserInfo, self).__init__()
        # 从文件中加载UI定义

        self.ui = uic.loadUi("E:/workSpace/Coding_SAM/data/UserInfo.ui")
        self.ui.setStyleSheet('''#Form{background-color:#FAFAFA}''')
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.nickIcon.setMaximumSize(80,80)
        self.ui.nickIcon.setPixmap(QPixmap('C:/Users/mayn/Pictures/test.png'))
        self.ui.nickIcon.setScaledContents(True)
        self.ui.nickIcon.setCursor(Qt.PointingHandCursor)

        self.ui.nickName.setText(u'秦加薪')
        self.ui.status.setText(u'在线')
        self.ui.email.setText(u'邮箱:')
        self.ui.emailaddr.setText(u'785415581@qq.com')
        # self.ui.emailaddr.setAlignment(Qt.AlignLeft)
        self.ui.apartment.setText(u'部门:')
        self.ui.apartmentaddr.setText(u'技术部')
        # self.ui.apartmentaddr.setAlignment(Qt.AlignLeft)
        self.ui.senderMessage.setText(u'发送信息')
        self.ui.senderMessage.setStyleSheet('''#senderMessage{background-color:#366CB3;	font-size:15px;font-weight:normal;font-family:Microsoft YaHei;font-color:white;}''')
        self.closeLabel = Label()
        self.closeLabel.setPixmap(QPixmap('E:/workSpace/Coding_SAM//resource/closeLabel.png'))
        self.closeLabel.setMaximumSize(20,20)
        self.closeLabel.setScaledContents(True)
        self.closeLabel.setCursor(Qt.PointingHandCursor)
        self.ui.horizontalLayout_4.insertWidget(1,self.closeLabel)

        self.closeLabel.clicked.connect(self.ui.close)

    def show(self,userPos,pos):
        x1 = userPos.x()
        y1 = userPos.y()
        x = pos.x()
        y = pos.y()
        self.ui.move(x+62,y+y1)
        self.ui.show()

# # #
# app = QApplication([])
# stats = UserInfo()
# stats.ui.show()
# app.exec_()