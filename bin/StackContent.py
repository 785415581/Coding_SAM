# -*- coding: utf-8 -*-
import os,sys

from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip
from widget.base import ListItemWidget,SearchLineEdit,Label
import video_player
from StackProject import *
from StackAsset import *
from PyQt5 import uic
from QureySQL import GetDataBase
from addAsset import AddUser
file_ = os.path.dirname(os.path.dirname(__file__))


#这是镜头预览窗口配置信息messageLabel
class MessageWidget(QWidget):
    def __init__(self,parent=None):
        super(MessageWidget, self).__init__(parent)
        self.setStyleSheet("""ProjectWidget{background-color:#366CB3}""")
        self.messagaList = MessageList()
        self.videoplayer = video_player.videoPlayer(self)
        self.vlay = QHBoxLayout()
        self.vlay.addWidget(self.messagaList)
        self.vlay.addWidget(self.videoplayer)
        self.vlay.setContentsMargins(0, 0, 0, 0)
        self.vlay.setSpacing(0)
        self.setLayout(self.vlay)
        self.getItemWidget()

    def getItemWidget(self):
        self.messagaList.navigationList.itemClicked.connect(self.playVideo)

    def playVideo(self, itemWidget, *args, **kwargs):
        print(itemWidget.getName(), itemWidget.getinfoMessage(),itemWidget.getVideoPath())
        fileName = itemWidget.getName()
        self.videoplayer.getfile(itemWidget.getVideoPath())
        self.videoplayer.player.play()


class MessageList(QScrollArea):
    def __init__(self, parent=None):
        super(MessageList, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent = parent
        self.frame = QWidget()
        self.setMinimumSize(240,580)
        self.setMaximumSize(240,1080)
        self.resize(240,1080)

        self.setWidget(self.frame)
        self.setWidgetResizable(True)
        self.frame.setMinimumWidth(240)

        with open(file_ + '/QSS/messageList.qss', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
            self.frame.setStyleSheet(style)

        self.setListViews()

        self.setLayouts()


    def setListViews(self):
        """定义承载功能的ListView"""

        self.navigationList = QListWidget()
        self.navigationList.setObjectName("navigationList")

        fileList = os.listdir(r'E:\workSpace\Coding_SAM\sucai\cutThumbnail')
        for i in fileList:
            widget = ListItemWidget(self.navigationList,file_ + '/sucai/cutThumbnail/'+i,i.split('.')[0],'超能陆战队',
                                    videoPath=file_ + '/sucai/'+i.split('.')[0] + '.mp4')

        self.navigationList.setCurrentRow(0)
        self.navigationList.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
        "QScrollBar::handle{background:lightgray; border:20px solid transparent; border-radius:50px;}"
        "QScrollBar::handle:hover{background:gray;}"
        "QScrollBar::sub-line{background:transparent;}"
        "QScrollBar::add-line{background:transparent;}")
        self.navigationList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

    def setLayouts(self):
        """定义布局。"""
        self.mainLayout = QVBoxLayout(self.frame)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.navigationList)



class User(QWidget):
    def __init__(self):
        super(User, self).__init__()
        self.setObjectName('user')
        self.ui = uic.loadUi(file_ + "/data/user.ui")
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lay = QHBoxLayout()
        self.lay.addWidget(self.ui)
        self.lay.setContentsMargins(0,0,0,0)
        self.lay.setSpacing(0)
        self.setLayout(self.lay)
        self.getData()
        self.rightFunction()
        self.ui.pushButton.clicked.connect(self.addUser)
    def getData(self):
        data = GetDataBase.getUserInfo()
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(len(data))
        for i in data:
            self.ui.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(i[0])))
            self.ui.tableWidget.setItem(rowCount, 1, QTableWidgetItem(i[1]))
            self.ui.tableWidget.setItem(rowCount, 2, QTableWidgetItem(str(i[2])))
            self.ui.tableWidget.setItem(rowCount, 3, QTableWidgetItem(i[3]))
            self.ui.tableWidget.setItem(rowCount, 4, QTableWidgetItem(i[4]))
            self.ui.tableWidget.setItem(rowCount, 5, QTableWidgetItem(i[5]))
            self.ui.tableWidget.setItem(rowCount, 6, QTableWidgetItem(i[6]))
            self.ui.tableWidget.setItem(rowCount, 7, QTableWidgetItem(i[7]))
            self.ui.tableWidget.setItem(rowCount, 8, QTableWidgetItem(i[8]))
            self.ui.tableWidget.setItem(rowCount, 9, QTableWidgetItem(i[9]))
            rowCount += 1

    def addUser(self):
        self.adduser = AddUser()
        self.adduser.show()

        self.adduser.ui.pushButton.clicked.connect(self.feedbackSql)
        self.adduser.ui.pushButton_2.clicked.connect(self.adduser.close)
    def feedbackSql(self):
        id = len(GetDataBase.getUserInfo())+1
        name = self.adduser.ui.lineEdit.text()
        age = self.adduser.ui.lineEdit_2.text()
        sex = self.adduser.ui.lineEdit_3.text()
        address = self.adduser.ui.lineEdit_4.text()
        department = self.adduser.ui.lineEdit_5.text()
        email = self.adduser.ui.lineEdit_6.text()
        phone = self.adduser.ui.lineEdit_7.text()
        account = self.adduser.ui.lineEdit_8.text()
        password = self.adduser.ui.lineEdit_9.text()
        sql = 'insert into user (id,name,age,sex,address,department,email,phone,account,password) values ({id},"{name}",{age},"{sex}","{address}","{department}","{email}","{phone}","{account}","{password}")' \
            .format(id=id, name=name, age=age, sex=sex, address=address,department=department,email=email, phone=phone,account=account,password=password)
        GetDataBase.UpDate('big',sql)
        QMessageBox.question(self, '提示', '创建成功', QMessageBox.Yes)
        self.adduser.close()
        self.update()
    def rightFunction(self):

        self.ui.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.ui.customContextMenuRequested.connect(self.rightContextMenu)  ####右键菜单
        self.contextMenu = QMenu()  # //创建QMenu
        self.actionA2 = self.contextMenu.addAction(u'增加')
        self.actionB2 = self.contextMenu.addAction(u'删除')
        self.actionC2 = self.contextMenu.addAction(u'更新')
        self.actionA2.triggered.connect(self.addUser)
        self.actionB2.triggered.connect(self.deletePipe2)
        self.actionC2.triggered.connect(self.update)

    def rightContextMenu(self, pos):
        self.contextMenu.popup(self.ui.mapToGlobal(pos))
        self.contextMenu.show()

    def deletePipe2(self):
        Items = self.ui.tableWidget.selectedItems()
        epsList = [Items[i:i + 5] for i in range(0, len(Items), 5)]
        for i in range(len(epsList)):
            sql = "DELETE FROM user WHERE id={id}".format(id=epsList[i][0].text())
            # GetDataBase.DelInfo('big',sql)
        # row = self.ui.tableWidget.currentRow()
        # print(row)

        rowNumberList = []
        for i in Items:
            rowNumber = self.ui.tableWidget.indexFromItem(i).row()
            if rowNumber not in rowNumberList:
                rowNumberList.append(rowNumber)
        rowNumberList.reverse()
        for i in rowNumberList:
            self.ui.tableWidget.removeRow(int(i))

    def update(self):

        rowcount= self.ui.tableWidget.rowCount()
        for items in range(rowcount,-1,-1):
            self.ui.tableWidget.removeRow(items)
        self.getData()

class StackWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(StackWidget, self).__init__(parent)
        self.parent = parent
        self.setStyleSheet('''MainWindow{background-color:#366CB3}''')
        #镜头播放列表
        self.messageContent = MessageWidget()
        #项目设置内容窗口
        self.projectContent = ProjectContet()
        #项目资产镜头窗口
        self.assetContent = AssetContet()
        self.user = User()

        self.addWidget(self.messageContent)
        self.addWidget(self.projectContent)
        self.addWidget(self.assetContent)
        self.addWidget(self.user)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = StackWidget()
    dialog.show()
    app.exec_()
