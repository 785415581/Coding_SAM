# -*- coding:utf-8 -*-
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

file_ = os.path.dirname(os.path.dirname(__file__))
class ListItemWidget(QListWidgetItem):
    def __init__(self,listWidget,avtarPic,groupName,infoMessage,videoPath=''):
        '''

        :param listWidget: 继承的父类listWidget
        :param avtarPic: 群聊图片（或者头像） #(url)
        :param groupName: 群聊名称（标题）
        :param infoMessage: 半透明字体
        '''
        super(ListItemWidget, self).__init__()
        self.avtarPic = avtarPic
        self.groupName = groupName
        self.infoMessage = infoMessage
        self.videoPath = videoPath
        self.widgets = QWidget(listWidget)
        self.widgets.setStyleSheet("background:transparent;")

        self.typeLabel = QLabel(self.widgets)
        self.typeLabel.setObjectName('typeLabel')
        self.myPix = QPixmap(self.avtarPic)
        self.typeLabel.setFixedSize(40, 40)
        self.typeLabel.setPixmap(self.myPix)
        self.typeLabel.setScaledContents(True)
        self.typeLabel.setStyleSheet("QLabel{padding-left:1px;padding-right:1px;}")

        self.fontArea = QWidget(self.widgets)
        self.fontArea.setFixedSize(120,65)

        self.textLabel = QLabel(self.fontArea)
        self.textLabel.setText(self.groupName)

        self.totalCopyLabel = QLabel(self.fontArea)
        self.totalCopyLabel.setObjectName('totalCopyLabel')
        self.totalCopyLabel.setText(infoMessage)
        self.totalCopyLabel.setStyleSheet('QLabel{color: #8C8C8C;font-size:12px;}')

        self.backArea = QWidget(self.widgets)
        self.backArea.setFixedSize(20, 32)


        self.openFolderButton = QPushButton(self.widgets)
        self.openFolderButton.setObjectName('openFolderButton')
        self.icon = QIcon(file_ + '/resource/movie.png')
        self.openFolderButton.setIcon(self.icon)
        self.openFolderButton.setIconSize(QSize(24, 24))
        self.openFolderButton.setProperty('index', 2)
        self.openFolderButton.setStyleSheet("QPushButton{ margin-left:25px;margin-right:25px;border:none; color:white; background:none; }QPushButton:hover{color:#FFFFFF; background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0% ), stop:1 rgba(200, 200, 200, 60% )); }\
                                                            QPushButton:pressed{ color:white; background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0% ), stop:1 rgba(200, 200, 200, 80% )); }")

        self.verLayout = QVBoxLayout()
        self.verLayout.addWidget(self.textLabel)
        self.verLayout.addWidget(self.totalCopyLabel)
        self.verLayout.addSpacing(10)
        self.fontArea.setLayout(self.verLayout)

        self.horLayout = QHBoxLayout()
        self.horLayout.setContentsMargins(0, 0, 0, 0)
        self.horLayout.addWidget(self.typeLabel)
        self.horLayout.addWidget(self.fontArea)
        self.horLayout.addWidget(self.backArea)
        self.horLayout.addWidget(self.openFolderButton)
        self.widgets.setLayout(self.horLayout)

        self.size = self.sizeHint()
        self.setSizeHint(QSize(56,56))
        listWidget.addItem(self)
        self.widgets.setSizeIncrement(56,56)
        listWidget.setItemWidget(self, self.widgets)

    def getPic(self):
        return self.avtarPic
    def getName(self):
        return self.groupName
    def getinfoMessage(self):
        return self.infoMessage
    def getVideoPath(self):
        return self.videoPath
class SearchLineEdit(QLineEdit):
    """创建一个可自定义图片的输入框。"""

    def __init__(self, parent=None):
        super(SearchLineEdit, self).__init__()
        self.setObjectName("SearchLine")
        self.parent = parent
        self.setMinimumSize(180, 23)
        with open(file_ + '/QSS/searchLine.qss', 'r') as f:
            self.setStyleSheet(f.read())
        self.setPlaceholderText("搜索")
        self.setTextMargins(3, 0, 19, 0)
        self.spaceItem = QSpacerItem(150, 10, QSizePolicy.Expanding)
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addSpacerItem(self.spaceItem)
        self.mainLayout.addSpacing(10)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)

class Label(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

class PushButtonMenu(QPushButton):
    def __init__(self,parent=None,text='',*args,**kwargs):
        super(PushButtonMenu, self).__init__(parent)
        self.parent = parent
        self.parse = args
        self.setText(text)
        self.initMenu()


    def initMenu(self):
        self.menu = QMenu(self)
        # 替换menu的鼠标释放事件达到选择性不关闭菜单
        self.menu.mouseReleaseEvent = self._menu_mouseReleaseEvent
        menuItem = self.parse[0]
        for i in menuItem:
            self.menu.addAction(i,self._checkAction)

        # self.menu.addAction('菜单1', self._checkAction)
        # self.menu.addAction('菜单2', self._checkAction)
        # self.menu.addAction(QAction('菜单3', self.menu, triggered=self._checkAction))
        action = QAction('菜单4', self.menu, triggered=self._checkAction)
        # 添加自定义的属性,判断该属性可以关闭菜单
        action.setProperty('canHide', True)
        self.menu.addAction(action)
        for action in self.menu.actions():
            # 循环设置可勾选
            action.setCheckable(True)
        self.setMenu(self.menu)

    def _menu_mouseReleaseEvent(self, event):
        action = self.menu.actionAt(event.pos())
        if not action:
            # 没有找到action就交给QMenu自己处理
            return QMenu.mouseReleaseEvent(self.menu, event)
        if action.property('canHide'):  # 如果有该属性则给菜单自己处理
            return QMenu.mouseReleaseEvent(self.menu, event)
        # 找到了QAction则只触发Action
        action.activate(action.Trigger)

    def _checkAction(self):
        # 三个action都响应该函数
        # print(self.menu.actions())
        # print('\n'.join(['{}\t选中：{}'.format(
        #     action.text(), action.isChecked()) for action in self.menu.actions()]))
        itemLis = []
        for action in self.menu.actions():
            if action.isChecked() == True:
                itemLis.append(action.text())
        print(itemLis)
        return itemLis

            # print(action.text(),action.isChecked())
            # if action.isChecked:
        #         print(action.text())
        #         itemLis.append(action.text())
        # return itemLis