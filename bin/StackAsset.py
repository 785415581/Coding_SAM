# -*- coding: utf-8 -*-
import os, sys
from io import StringIO
import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from widget.base import ListItemWidget, SearchLineEdit, Label
from PyQt5 import uic
from widget.base import PushButtonMenu
from functools import partial
from fieldsWindow import Fields
from addAsset import Addasset,AddEps,AddAssetTask,AddShot,AddShotTask
from addProject import AddProject
from QureySQL import GetDataBase

file_ = os.path.dirname(os.path.dirname(__file__))

style = '''
QTabWidget::pane
{
	border: 1px;
	background:white;
}
QTabWidget::tab-bar
{
	background:white;
	subcontrol-position:center;
}
 
QTabBar::tab
 
{
min-width:75px;
min-height:55px;
background:white;
}
 
QTabBar::tab:selected
 
{
color: rgb(36,197,219);
background:white;
}
 
QTabBar::tab:!selected
 
{
color: black;
background:white;
}
QTabBar::tab:hover
{
color: rgb(36,197,219);
background:white;
}
'''


class MessageList(QScrollArea):
    def __init__(self, parent=None):
        super(MessageList, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent = parent
        self.frame = QWidget()
        self.setMinimumSize(240, 580)
        self.setMaximumSize(240, 1080)
        self.resize(240, 1080)

        self.setWidget(self.frame)
        self.setWidgetResizable(True)
        self.frame.setMinimumWidth(240)

        with open(file_ + '/QSS/messageList.qss', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
            self.frame.setStyleSheet(style)
        self.setListViews()
        self.setLayouts()
        self.rightfunction()

    def setListViews(self):
        """定义承载功能的ListView"""

        self.navigationList = QListWidget()
        self.navigationList.setObjectName("navigationList")
        database = GetDataBase.getDatabases()
        for i in database:
            databaseInfor = GetDataBase.getDatabeseInfo(i)
            chineseName = databaseInfor['chinesename']
            projectCode = databaseInfor['databasecode']
            projectThmunail = file_ + '/project/' + i + '/projectConfig/picture/' + i + '.jpg'
            ListItemWidget(self.navigationList, projectThmunail, chineseName, projectCode,videoPath='')
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

    def rightfunction(self):

        self.navigationList.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.navigationList.customContextMenuRequested.connect(self.showContextMenu)  ####右键菜单
        self.contextMenu = QMenu()  # //创建QMenu
        self.actionB = self.contextMenu.addAction(u'删除')
        self.actionD = self.contextMenu.addAction((u'刷新'))
        self.actionB.triggered.connect(self.deleteProject)
        self.actionD.triggered.connect(self.update)

    def showContextMenu(self, pos):
        self.contextMenu.popup(self.navigationList.mapToGlobal(pos))
        self.contextMenu.show()

    def deleteProject(self):
        item = self.navigationList.currentItem()
        if item:
            projectCode = item.getinfoMessage()
            # GetDataBase.deleteDatabse(projectCode)
            self.navigationList.removeItemWidget(self.navigationList.takeItem(self.navigationList.row(item)))

    def update(self):
        self.navigationList.clear()
        database = GetDataBase.getDatabases()
        for i in database:
            databaseInfor = GetDataBase.getDatabeseInfo(i)
            chineseName = databaseInfor['chinesename']
            projectCode = databaseInfor['databasecode']
            projectThmunail = file_ + '/project/' + i + '/projectConfig/picture/' + i + '.jpg'
            if os.path.isfile(projectThmunail):
                ListItemWidget(self.navigationList, projectThmunail, chineseName, projectCode, videoPath='')
            else:
                projectThmunail = file_ + '/project/' +  'origin.jpg'
                ListItemWidget(self.navigationList, projectThmunail, chineseName, projectCode, videoPath='')

class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        self.setStyleSheet(style)
        self.resize(516,800)
        # print(itemWidget.getName(), itemWidget.getinfoMessage(), itemWidget.getVideoPath())
        # self.projectCode = 'big'
        # self.projectName = u"大熊兔之兔王"

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        self.addTab(self.tab1, "项目详情")
        self.addTab(self.tab2, "集数")
        self.addTab(self.tab3, "资产")
        self.addTab(self.tab4, "资产任务")
        self.addTab(self.tab5, "镜头")
        self.addTab(self.tab6, "镜头任务")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()

        self.currentChanged.connect(self.changePage)

        #扩展窗口
        self.fields = Fields()


    def changePage(self,index):
        try:
            if index == 1:
                page = 'Episode'
                data = GetDataBase.getEpsInfo(self.projectCode)
                rowCount = self.epsui.tableWidget.rowCount()
                self.epsui.tableWidget.setRowCount(len(data))
                for i in data:
                    self.epsui.tableWidget.setItem(rowCount,0,QTableWidgetItem(str(i['id'])))
                    self.epsui.tableWidget.setItem(rowCount,1,QTableWidgetItem(i['number']))
                    self.epsui.tableWidget.setItem(rowCount,2,QTableWidgetItem(i['createtime']))
                    self.epsui.tableWidget.setItem(rowCount,3,QTableWidgetItem(i['creator']))
                    self.epsui.tableWidget.setItem(rowCount,4,QTableWidgetItem(i['project']))
                    rowCount += 1
            elif index == 2:
                page = 'Asset'
                data = GetDataBase.getAssetInfo(self.projectCode)
                rowCount = self.assetui.tableWidget.rowCount()
                self.assetui.tableWidget.setRowCount(len(data))
                for i in data:
                    combBox = QComboBox()
                    combBox.addItems(['character','prop','scenes'])
                    combBox.setCurrentText(i['type'])
                    combBox.currentTextChanged.connect(partial(self.shotTaskChangeStatus,i['id'],page,combBox))
                    self.assetui.tableWidget.setItem(rowCount,0,QTableWidgetItem(str(i['id'])))
                    self.assetui.tableWidget.setItem(rowCount,1,QTableWidgetItem(i['name']))
                    # self.assetui.tableWidget.setItem(rowCount,2,QTableWidgetItem(i['type']))
                    self.assetui.tableWidget.setCellWidget(rowCount,2,combBox)
                    self.assetui.tableWidget.setItem(rowCount,3,QTableWidgetItem(i['project']))
                    self.assetui.tableWidget.setItem(rowCount,4,QTableWidgetItem(i['createtime']))
                    self.assetui.tableWidget.setItem(rowCount,5,QTableWidgetItem(i['auther']))
                    rowCount += 1
            elif index == 3:
                page = 'AssetTask'
                data = GetDataBase.getAssetTaskInfo(self.projectCode)
                rowCount = self.assetTaskui.tableWidget.rowCount()
                self.assetTaskui.tableWidget.setRowCount(len(data))
                for i in data:
                    combBox = QComboBox()
                    combBox.addItems(['character','prop','scenes'])
                    combBox.setCurrentText(i['type'])
                    combBox1 = QComboBox()
                    pipeline = eval(GetDataBase.getProjectInfo(self.projectCode)[0]['assetpipeline'])['asset']
                    lis = [x for x in pipeline.values()]
                    combBox1.addItems(lis)
                    combBox1.setCurrentText(i['pipeline'])
                    self.assetTaskui.tableWidget.setItem(rowCount,0,QTableWidgetItem(str(i['id'])))
                    self.assetTaskui.tableWidget.setItem(rowCount,1,QTableWidgetItem(i['chinesename']))
                    self.assetTaskui.tableWidget.setItem(rowCount,2,QTableWidgetItem(i['type']))
                    self.assetTaskui.tableWidget.setItem(rowCount,3,QTableWidgetItem(i['pipeline']))
                    self.assetTaskui.tableWidget.setItem(rowCount,4,QTableWidgetItem(i['producer']))
                    self.assetTaskui.tableWidget.setItem(rowCount,5,QTableWidgetItem(i['status']))
                    rowCount += 1
            elif index == 4:
                page = 'Shot'

                data = GetDataBase.getShotInfo(self.projectCode)
                rowCount = self.shotui.tableWidget.rowCount()
                self.shotui.tableWidget.setRowCount(len(data))
                for i in data:
                    self.shotui.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(i['id'])))
                    self.shotui.tableWidget.setItem(rowCount, 1, QTableWidgetItem(i['shot_name']))
                    self.shotui.tableWidget.setItem(rowCount, 2, QTableWidgetItem(i['shot_pipeline']))
                    self.shotui.tableWidget.setItem(rowCount, 3, QTableWidgetItem(i['shot_startframe']))
                    self.shotui.tableWidget.setItem(rowCount, 4, QTableWidgetItem(i['shot_endframe']))
                    self.shotui.tableWidget.setItem(rowCount, 5, QTableWidgetItem(i['shot_totaleframe']))
                    self.shotui.tableWidget.setItem(rowCount, 6, QTableWidgetItem(i['shot_descrip']))
                    rowCount += 1
            elif index == 5:
                page = 'ShotTask'

                data = GetDataBase.getShotTaskInfo(self.projectCode)
                rowCount = self.shotTaskui.tableWidget.rowCount()
                self.shotTaskui.tableWidget.setRowCount(len(data))
                for i in data:
                    combBox = QComboBox()
                    combBox.addItems(['work','wait','approve'])
                    combBox.setCurrentText(i['task_status'])
                    combBox.currentTextChanged.connect(partial(self.shotTaskChangeStatus,i['id'],page,combBox))
                    self.shotTaskui.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(i['id'])))
                    self.shotTaskui.tableWidget.setItem(rowCount, 1, QTableWidgetItem(i['task_name']))
                    self.shotTaskui.tableWidget.setItem(rowCount, 2, QTableWidgetItem(i['task_descrip']))
                    self.shotTaskui.tableWidget.setCellWidget(rowCount,3,combBox)
                    self.shotTaskui.tableWidget.setItem(rowCount, 4, QTableWidgetItem(i['task_user']))
                    self.shotTaskui.tableWidget.setItem(rowCount, 5, QTableWidgetItem(i['task_type']))
                    rowCount += 1
        except:
            pass

    def shotTaskChangeStatus(self,id,model,combBox):
        if model == 'Asset':
            id = id
            type = combBox.currentText()
            print(id, type)
            sql = "UPDATE asset SET  type= '{type}' WHERE id ='{id}'".format(type=type,id=id)
            print(sql)
            GetDataBase.UpDate(self.projectCode,sql)
        if model == 'ShotTask':
            id = id
            status = combBox.currentText()
            print(id, status)
            sql = "UPDATE shottask SET  task_status= '{status}' WHERE id ='{id}'".format(status=status,id=id)
            print(sql)
            GetDataBase.UpDate(self.projectCode,sql)

    def getProjectName(self,itemWidget):
        self.setCurrentIndex(0)
        self.projectName = itemWidget.getName()
        self.projectCode = itemWidget.getinfoMessage()
        borderImage = file_ + '/project/' + self.projectCode + '/projectConfig/picture/' + self.projectCode + '.jpg'
        BgImage = file_ + '/project/' + self.projectCode + '/projectConfig/picture/' + 'BG_' +self.projectCode + '.jpg'
        self.ui.pushButton.setIcon(QIcon(borderImage))

        palette = QPalette()
        icon = QPixmap(BgImage)

        palette.setBrush(self.ui.widget.backgroundRole(), QBrush(icon))  # 添加背景图片
        self.ui.widget.setPalette(palette)

        self.ui.label.setObjectName('projectName')
        self.ui.label.setStyleSheet("#projectName{color:rgb(250,250,250);font-size:20px;font-weight:normal;font-family:Microsoft YaHei;}")
        self.ui.label.setText(self.projectName)
        self.ui.label_5.setText(self.projectName)

        print(itemWidget.getName(), itemWidget.getinfoMessage(), itemWidget.getVideoPath())



    def tab1UI(self,projectCode='big'):
        self.ui = uic.loadUi(file_ + "/data/projectInfo.ui")

        self.ui.tabWidget.setTabText(0,'详情')
        self.ui.tabWidget.setTabText(1,'数据')
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.pushButton.setFixedSize(168,138)
        self.ui.pushButton.setObjectName('projectThum')
        borderImage = file_ + '/project/' + projectCode + '/projectConfig/picture/' + projectCode + '.jpg'
        self.ui.pushButton.setIcon(QIcon(borderImage))
        self.ui.label.setObjectName('projectName')
        self.ui.label.setStyleSheet("#projectName{color:rgb(250,250,250);font-size:20px;font-weight:normal;font-family:Microsoft YaHei;}")
        self.ui.label.setText('大熊兔之兔王')

        self.ui.widget.setObjectName('projectBG')
        self.ui.widget.setStyleSheet('#projectBG{border-image: url(E:/workSpace/Coding_SAM/project/big/projectConfig/picture/BG_big.jpg)}')

        layout = QHBoxLayout()
        layout.addWidget(self.ui)
        layout.setContentsMargins(0,0,0 ,0)
        #为这个tab命名显示出来，第一个参数是哪个标签，第二个参数是标签的名字
        self.setTabText(0, "项目详情")
        # 在标签1中添加这个帧布局
        self.tab1.setLayout(layout)

#-------------------------------镜头
    def tab2UI(self):
        self.epsui = uic.loadUi(file_ + "/data/eps.ui")
        self.epsui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.rightfunction()
        self.epsui.pushButton_2.clicked.connect(partial(self.add,self.epsui))
        layout = QHBoxLayout()
        layout.addWidget(self.epsui)
        layout.setContentsMargins(0,0,0 ,0)
        self.setTabText(1, "集数")
        self.tab2.setLayout(layout)


    def rightfunction(self):

        self.epsui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.epsui.tableWidget.customContextMenuRequested.connect(self.showContextMenu)  ####右键菜单
        self.contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.contextMenu.addAction(u'创建')
        self.actionB = self.contextMenu.addAction(u'删除')
        self.actionD = self.contextMenu.addAction((u'刷新'))
        self.actionA.triggered.connect(partial(self.add,self.epsui))
        self.actionB.triggered.connect(self.delRow)
        self.actionD.triggered.connect(self.update)

    def showContextMenu(self, pos):
        self.contextMenu.popup(self.epsui.tableWidget.mapToGlobal(pos))
        self.contextMenu.show()

    def update(self):
        index = self.currentIndex()
        rowcount= self.epsui.tableWidget.rowCount()
        for items in range(rowcount,-1,-1):
            self.epsui.tableWidget.removeRow(items)
        self.changePage(index)

    def add(self,widget):

        self.addEps = AddEps()
        try:
            mixId = GetDataBase.getEpsInfo(self.projectCode)[-1]['id']+1
            self.addEps.ui.lineEdit.setPlaceholderText('最小序号为%s'%mixId)
            self.addEps.ui.lineEdit.setValidator(QIntValidator(mixId, 999999))
        except:
            pass
        data = GetDataBase.getDatabases()
        self.addEps.ui.comboBox.addItems(data)
        self.addEps.ui.comboBox.setCurrentText(self.projectCode)

        self.addEps.ui.pushButton_2.clicked.connect(partial(self.feedbackSql,widget))
        self.addEps.ui.pushButton.clicked.connect(self.addEps.close)
        self.addEps.show()
    def delRow(self):

        Items = self.epsui.tableWidget.selectedItems()
        epsList = [Items[i:i + 5] for i in range(0, len(Items), 5)]
        for i in range(len(epsList)):
            sql = "DELETE FROM eps WHERE id={id} AND number='{number}'".format(id=epsList[i][0].text(),number=epsList[i][1].text())
            GetDataBase.DelInfo(self.projectCode,sql)
            print(sql)
        rowNumberList = []
        for i in Items:
            rowNumber = self.epsui.tableWidget.indexFromItem(i).row()
            if rowNumber not in rowNumberList:
                rowNumberList.append(rowNumber)
        rowNumberList.reverse()
        for i in rowNumberList:
            self.epsui.tableWidget.removeRow(int(i))

    def feedbackSql(self,widget):
        id = self.addEps.ui.lineEdit.text()
        number = self.addEps.ui.lineEdit_2.text()
        createTime = datetime.datetime.now().strftime('%Y%m%d%I%M%S')
        creator = self.addEps.ui.lineEdit_3.text()
        project = self.addEps.ui.comboBox.currentText()
        data = {'id':int(id),'number':number,'createTime':int(createTime),'creator':creator,'project':project}
        print(data)
        if self.addEps.ui.lineEdit.text() != '' and self.addEps.ui.lineEdit_2.text() != '' :
            rowCount = widget.tableWidget.rowCount()
            widget.tableWidget.insertRow(rowCount)
            widget.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(id)))
            widget.tableWidget.setItem(rowCount, 1, QTableWidgetItem(number))
            widget.tableWidget.setItem(rowCount, 2, QTableWidgetItem(createTime))
            widget.tableWidget.setItem(rowCount, 3, QTableWidgetItem(creator))
            widget.tableWidget.setItem(rowCount, 4, QTableWidgetItem(project))
            GetDataBase.creatEpsInfo(project,data)
            QMessageBox.question(self, '提示', '创建成功', QMessageBox.Yes)
            self.addEps.close()
        else:
            reply = QMessageBox.question(self, '提示', '资产名称和类型是必填字段', QMessageBox.Yes)

    def createPath(self):
        path = self.projectCode+'/publish/'
        pass


#------------------------------------------------------------资产
    def tab3UI(self):
        self.assetui = uic.loadUi(file_ + "/data/asset.ui")
        self.assetTaskui = uic.loadUi(file_ + "/data/assetTask.ui")
        self.assetui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.assetui.pushButton_2.clicked.connect(partial(self.tab3add,self.assetui))
        self.tab3rightfunction()
        layout = QHBoxLayout()
        layout.addWidget(self.assetui)
        layout.setContentsMargins(0,0,0 ,0)
        self.setTabText(2, "资产")
        self.tab3.setLayout(layout)

    def tab3rightfunction(self):

        self.assetui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.assetui.tableWidget.customContextMenuRequested.connect(self.tab3showContextMenu)  ####右键菜单
        self.tab3contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.tab3contextMenu.addAction(u'创建')
        self.actionB = self.tab3contextMenu.addAction(u'删除')
        self.actionC = self.tab3contextMenu.addAction(u'创建目录')
        self.actionD = self.tab3contextMenu.addAction((u'刷新'))
        self.actionE = self.tab3contextMenu.addAction(u'分配任务')
        self.actionA.triggered.connect(partial(self.tab3add,self.assetui))
        self.actionB.triggered.connect(self.tab3delRow)
        self.actionD.triggered.connect(self.tab3update)
        self.actionE.triggered.connect(partial(self.tab3assign,self.assetTaskui))

    def tab3showContextMenu(self, pos):
        self.tab3contextMenu.popup(self.assetui.tableWidget.mapToGlobal(pos))
        self.tab3contextMenu.show()
    def tab3assign(self,widget):
        self.tab4add(widget)

    def tab3update(self):
        index = self.currentIndex()
        rowcount= self.assetui.tableWidget.rowCount()
        for items in range(rowcount,-1,-1):
            self.assetui.tableWidget.removeRow(items)
        self.changePage(index)

    def tab3add(self,widget):

        self.addAsset = Addasset()
        self.addAsset.ui.comboBox.addItems(['Props','Scenes','Character'])
        self.addAsset.ui.comboBox.setCurrentText('Props')
        data = GetDataBase.getDatabases()
        self.addAsset.ui.comboBox_2.addItems(data)
        self.addAsset.ui.comboBox_2.setCurrentText(self.projectCode)
        try:
            mixId = GetDataBase.getAssetInfo(self.projectCode)[-1]['id']+1
            self.addAsset.ui.lineEdit.setPlaceholderText('最小序号为%s'%mixId)
            self.addAsset.ui.lineEdit.setValidator(QIntValidator(mixId, 999999))
        except:
            pass
        self.addAsset.show()
        self.addAsset.ui.pushButton_2.clicked.connect(partial(self.tab3feedbackSql,widget))
        self.addAsset.ui.pushButton.clicked.connect(self.addAsset.close)

    def tab3delRow(self):

        Items = self.assetui.tableWidget.selectedItems()
        epsList = [Items[i:i + 6] for i in range(0, len(Items), 6)]
        for i in range(len(epsList)):
            sql = "DELETE FROM asset WHERE id={id}".format(id=epsList[i][0].text())
            GetDataBase.DelInfo(self.projectCode,sql)
        rowNumberList = []
        for i in Items:
            rowNumber = self.assetui.tableWidget.indexFromItem(i).row()
            if rowNumber not in rowNumberList:
                rowNumberList.append(rowNumber)
        rowNumberList.reverse()
        for i in rowNumberList:
            self.assetui.tableWidget.removeRow(int(i))

    def tab3feedbackSql(self,widget):
        id = self.addAsset.ui.lineEdit.text()
        name = self.addAsset.ui.lineEdit_2.text()
        types = self.addAsset.ui.comboBox.currentText()
        createTime = datetime.datetime.now().strftime('%Y%m%d%I%M%S')
        creator = self.addAsset.ui.lineEdit_6.text()
        project = self.addAsset.ui.comboBox_2.currentText()
        data = {'id':int(id),'name':name,'types':types,'createTime':int(createTime),'creator':creator,'project':project}
        print(data)
        if self.addAsset.ui.lineEdit.text() != '' and self.addAsset.ui.lineEdit_2.text() != '' :
            rowCount = widget.tableWidget.rowCount()
            widget.tableWidget.insertRow(rowCount)
            widget.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(id)))
            widget.tableWidget.setItem(rowCount, 1, QTableWidgetItem(name))
            widget.tableWidget.setItem(rowCount, 2, QTableWidgetItem(types))
            widget.tableWidget.setItem(rowCount, 3, QTableWidgetItem(project))
            widget.tableWidget.setItem(rowCount, 4, QTableWidgetItem(createTime))
            widget.tableWidget.setItem(rowCount, 5, QTableWidgetItem(creator))
            GetDataBase.creatAssetInfo(project,data)
            QMessageBox.question(self, '提示', '创建成功', QMessageBox.Yes)
            self.addAsset.close()
        else:
            reply = QMessageBox.question(self, '提示', '资产名称和类型是必填字段', QMessageBox.Yes)


# ------------------------------------------------------------资产任务
    def tab4UI(self):
        self.assetTaskui = uic.loadUi(file_ + "/data/assetTask.ui")
        self.assetTaskui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.assetTaskui.pushButton_2.clicked.connect(partial(self.tab4add,self.assetTaskui))
        self.tab4rightfunction()
        layout = QHBoxLayout()
        layout.addWidget(self.assetTaskui)
        layout.setContentsMargins(0,0,0 ,0)
        self.setTabText(3, "资产任务")
        self.tab4.setLayout(layout)

    def tab4rightfunction(self):

        self.assetTaskui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.assetTaskui.tableWidget.customContextMenuRequested.connect(self.tab4showContextMenu)  ####右键菜单
        self.tab4contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.tab4contextMenu.addAction(u'创建')
        self.actionB = self.tab4contextMenu.addAction(u'删除')
        self.actionC = self.tab4contextMenu.addAction(u'创建目录')
        self.actionD = self.tab4contextMenu.addAction((u'刷新'))
        self.actionA.triggered.connect(partial(self.tab4add,self.assetTaskui))
        self.actionB.triggered.connect(self.tab4delRow)
        self.actionD.triggered.connect(self.tab4update)

    def tab4showContextMenu(self, pos):
        self.tab4contextMenu.popup(self.assetTaskui.tableWidget.mapToGlobal(pos))
        self.tab4contextMenu.show()

    def tab4update(self):
        index = self.currentIndex()
        rowcount= self.assetTaskui.tableWidget.rowCount()
        for items in range(rowcount,-1,-1):
            self.assetTaskui.tableWidget.removeRow(items)
        self.changePage(index)


    def tab4add(self,widget):
        self.addAssetTask = AddAssetTask()
        self.addAssetTask.ui.comboBox.addItems(['Props', 'Scenes', 'Character'])
        self.addAssetTask.ui.comboBox.setCurrentText('Props')
        data = ['work','wait','approve']
        self.addAssetTask.ui.comboBox_2.addItems(data)
        self.addAssetTask.ui.comboBox_2.setCurrentText('work')
        dic = eval(GetDataBase.getProjectInfo(self.projectCode)[0]['assetpipeline'])['asset']
        lis = [x for x in dic.keys()]
        self.addAssetTask.ui.comboBox_3.addItems(lis)
        self.addAssetTask.ui.comboBox_3.setCurrentText('mod')
        try:
            mixId = GetDataBase.getAssetTaskInfo(self.projectCode)[-1]['id']+1
            self.addAssetTask.ui.lineEdit.setPlaceholderText('最小序号为%s' % mixId)
            self.addAssetTask.ui.lineEdit.setValidator(QIntValidator(mixId, 999999))
        except:
            pass
        self.addAssetTask.show()
        self.addAssetTask.ui.pushButton_2.clicked.connect(partial(self.tab4feedbackSql, widget))
        self.addAssetTask.ui.pushButton.clicked.connect(self.addAssetTask.close)

    def tab4delRow(self):

        Items = self.assetTaskui.tableWidget.selectedItems()
        epsList = [Items[i:i + 6] for i in range(0, len(Items), 6)]
        for i in range(len(epsList)):
            sql = "DELETE FROM assettask WHERE id={id}".format(id=epsList[i][0].text())
            GetDataBase.DelInfo(self.projectCode,sql)
        rowNumberList = []
        for i in Items:
            rowNumber = self.assetTaskui.tableWidget.indexFromItem(i).row()
            if rowNumber not in rowNumberList:
                rowNumberList.append(rowNumber)
        rowNumberList.reverse()
        for i in rowNumberList:
            self.assetTaskui.tableWidget.removeRow(int(i))

    def tab4feedbackSql(self,widget):
        id = self.addAssetTask.ui.lineEdit.text()
        name = self.addAssetTask.ui.lineEdit_2.text()
        types = self.addAssetTask.ui.comboBox.currentText()
        pipeline = self.addAssetTask.ui.comboBox_3.currentText()
        creator = self.addAssetTask.ui.lineEdit_4.text()
        status = self.addAssetTask.ui.comboBox_2.currentText()
        data = {'id':int(id),'name':name,'types':types,'pipeline':pipeline,'creator':creator,'status':status}
        print(data)
        if self.addAssetTask.ui.lineEdit.text() != '' and self.addAssetTask.ui.lineEdit_2.text() != '' :
            rowCount = widget.tableWidget.rowCount()
            widget.tableWidget.insertRow(rowCount)
            widget.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(id)))
            widget.tableWidget.setItem(rowCount, 1, QTableWidgetItem(name))
            widget.tableWidget.setItem(rowCount, 2, QTableWidgetItem(types))
            widget.tableWidget.setItem(rowCount, 3, QTableWidgetItem(pipeline))
            widget.tableWidget.setItem(rowCount, 4, QTableWidgetItem(creator))
            widget.tableWidget.setItem(rowCount, 5, QTableWidgetItem(status))
            GetDataBase.creatAssetTaskInfo(self.projectCode,data)
            QMessageBox.question(self, '提示', '创建成功', QMessageBox.Yes)
            self.addAssetTask.close()
        else:
            reply = QMessageBox.question(self, '提示', '资产名称和类型是必填字段', QMessageBox.Yes)


# ------------------------------------------------------------镜头
    def tab5UI(self):
        self.shotui = uic.loadUi(file_ + "/data/shot.ui")
        self.shotui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.shotui.pushButton_2.clicked.connect(partial(self.tab5add,self.shotui))
        self.tab5rightfunction()
        layout = QHBoxLayout()
        layout.addWidget(self.shotui)
        layout.setContentsMargins(0,0,0 ,0)
        self.setTabText(4, "镜头")
        self.tab5.setLayout(layout)

    def tab5rightfunction(self):

        self.shotui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.shotui.tableWidget.customContextMenuRequested.connect(self.tab5showContextMenu)  ####右键菜单
        self.tab5contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.tab5contextMenu.addAction(u'创建')
        self.actionB = self.tab5contextMenu.addAction(u'删除')
        self.actionC = self.tab5contextMenu.addAction(u'创建目录')
        self.actionD = self.tab5contextMenu.addAction((u'刷新'))
        self.actionA.triggered.connect(partial(self.tab5add,self.assetTaskui))
        self.actionB.triggered.connect(self.tab5delRow)
        self.actionD.triggered.connect(self.tab5update)

    def tab5showContextMenu(self, pos):
        self.tab5contextMenu.popup(self.shotui.tableWidget.mapToGlobal(pos))
        self.tab5contextMenu.show()

    def tab5update(self):
        index = self.currentIndex()
        rowcount= self.shotui.tableWidget.rowCount()
        for items in range(rowcount,-1,-1):
            self.shotui.tableWidget.removeRow(items)
        self.changePage(index)

    def tab5add(self,widget):
        self.addShot = AddShot()
        try:
            mixId = GetDataBase.getShotInfo(self.projectCode)[-1]['id']+1
            self.addShot.ui.lineEdit.setPlaceholderText('最小序号为%s' % mixId)
            self.addShot.ui.lineEdit.setValidator(QIntValidator(mixId, 999999))
        except:
            pass
        self.addShot.ui.spinBox.valueChanged.connect(self.tab5setTotalFrame)
        self.addShot.ui.spinBox_2.valueChanged.connect(self.tab5setTotalFrame)
        self.addShot.ui.spinBox.textChanged.connect(self.tab5setTotalFrame)
        self.addShot.ui.spinBox_2.textChanged.connect(self.tab5setTotalFrame)
        self.addShot.show()
        self.addShot.ui.pushButton_2.clicked.connect(partial(self.tab5feedbackSql, widget))
        self.addShot.ui.pushButton.clicked.connect(self.addShot.close)

    def tab5delRow(self):

        Items = self.shotui.tableWidget.selectedItems()
        epsList = [Items[i:i + 6] for i in range(0, len(Items), 6)]
        for i in range(len(epsList)):
            sql = "DELETE FROM shot WHERE id={id}".format(id=epsList[i][0].text())
            GetDataBase.DelInfo(self.projectCode,sql)
        rowNumberList = []
        for i in Items:
            rowNumber = self.shotui.tableWidget.indexFromItem(i).row()
            if rowNumber not in rowNumberList:
                rowNumberList.append(rowNumber)
        rowNumberList.reverse()
        for i in rowNumberList:
            self.shotui.tableWidget.removeRow(int(i))

    def tab5feedbackSql(self,widget):
        id = self.addShot.ui.lineEdit.text()
        shot_name = self.addShot.ui.lineEdit_2.text()
        shot_pipeline = self.addShot.ui.lineEdit_3.text()
        shot_startframe = self.addShot.ui.spinBox.value()
        shot_endframe = self.addShot.ui.spinBox_2.value()
        shot_totalframe = self.addShot.ui.lineEdit_6.text()
        shot_descrip = self.addShot.ui.lineEdit_7.text()
        data = {'id':int(id),'shot_name':shot_name,'shot_pipeline':shot_pipeline,'shot_startframe':shot_startframe,'shot_endframe':shot_endframe,'shot_totalframe':shot_totalframe,'shot_descrip':shot_descrip}
        print(data)
        if self.addShot.ui.lineEdit.text() != '' and self.addShot.ui.lineEdit_2.text() != '' :
            rowCount = widget.tableWidget.rowCount()
            widget.tableWidget.insertRow(rowCount)
            widget.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(id)))
            widget.tableWidget.setItem(rowCount, 1, QTableWidgetItem(shot_name))
            widget.tableWidget.setItem(rowCount, 2, QTableWidgetItem(shot_pipeline))
            widget.tableWidget.setItem(rowCount, 3, QTableWidgetItem(shot_startframe))
            widget.tableWidget.setItem(rowCount, 4, QTableWidgetItem(shot_endframe))
            widget.tableWidget.setItem(rowCount, 5, QTableWidgetItem(shot_totalframe))
            widget.tableWidget.setItem(rowCount, 6, QTableWidgetItem(shot_descrip))
            GetDataBase.creatShotInfo(self.projectCode,data)
            QMessageBox.question(self, '提示', '创建成功', QMessageBox.Yes)
            self.addShot.close()
        else:
            reply = QMessageBox.question(self, '提示', '资产名称和类型是必填字段', QMessageBox.Yes)


    def tab5setTotalFrame(self):
        startFrame = self.addShot.ui.spinBox.value()
        endFrame = self.addShot.ui.spinBox_2.value()
        totalFrame = int(endFrame) - int(startFrame)
        self.addShot.ui.lineEdit_6.setText(str(totalFrame))


# ------------------------------------------------------------镜头任务
    def tab6UI(self):
        self.shotTaskui = uic.loadUi(file_ + "/data/shotTask.ui")
        self.shotTaskui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.shotTaskui.pushButton_2.clicked.connect(partial(self.tab6add,self.shotTaskui))
        self.tab6rightfunction()
        layout = QHBoxLayout()
        layout.addWidget(self.shotTaskui)
        layout.setContentsMargins(0,0,0 ,0)
        self.setTabText(5, "镜头任务")
        self.tab6.setLayout(layout)


    def tab6rightfunction(self):

        self.shotTaskui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.shotTaskui.tableWidget.customContextMenuRequested.connect(self.tab6showContextMenu)  ####右键菜单
        self.tab6contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.tab6contextMenu.addAction(u'创建')
        self.actionB = self.tab6contextMenu.addAction(u'删除')
        self.actionC = self.tab6contextMenu.addAction(u'创建目录')
        self.actionD = self.tab6contextMenu.addAction((u'刷新'))
        self.actionA.triggered.connect(partial(self.tab6add,self.shotTaskui))
        self.actionB.triggered.connect(self.tab6delRow)
        self.actionD.triggered.connect(self.tab6update)

    def tab6showContextMenu(self, pos):
        self.tab6contextMenu.popup(self.shotTaskui.tableWidget.mapToGlobal(pos))
        self.tab6contextMenu.show()

    def tab6update(self):
        index = self.currentIndex()
        rowcount= self.shotTaskui.tableWidget.rowCount()
        for items in range(rowcount,-1,-1):
            self.shotTaskui.tableWidget.removeRow(items)
        self.changePage(index)

    def tab6add(self,widget):
        self.addShotTask = AddShotTask()
        self.addShotTask.ui.comboBox.addItems([u'工作中',u'等待中',u'通过'])
        self.addShotTask.ui.comboBox_2.addItems([u'layout',u'comp',u'light'])
        try:
            mixId = GetDataBase.getShotInfo(self.projectCode)[-1]['id']+1
            self.addShotTask.ui.lineEdit_3.setPlaceholderText('最小序号为%s' % mixId)
            self.addShotTask.ui.lineEdit_3.setValidator(QIntValidator(mixId, 999999))
        except:
            pass
        self.addShotTask.show()
        self.addShotTask.ui.pushButton_2.clicked.connect(partial(self.tab6feedbackSql, widget))
        self.addShotTask.ui.pushButton.clicked.connect(self.addShotTask.close)
    def tab6delRow(self):
        Items = self.shotTaskui.tableWidget.selectedItems()
        epsList = [Items[i:i + 6] for i in range(0, len(Items), 6)]
        for i in range(len(epsList)):
            sql = "DELETE FROM shottask WHERE id={id}".format(id=epsList[i][0].text())
            GetDataBase.DelInfo(self.projectCode,sql)

        rowNumberList = []
        for i in Items:
            rowNumber = self.shotTaskui.tableWidget.indexFromItem(i).row()
            if rowNumber not in rowNumberList:
                rowNumberList.append(rowNumber)

        rowNumberList.reverse()
        for i in rowNumberList:
            self.shotTaskui.tableWidget.removeRow(int(i))

    def tab6feedbackSql(self,widget):

        id = self.addShotTask.ui.lineEdit_3.text()
        task_name = self.addShotTask.ui.lineEdit.text()
        task_descrip = self.addShotTask.ui.lineEdit_2.text()
        task_status = self.addShotTask.ui.comboBox.currentText()
        task_user = self.addShotTask.ui.lineEdit_4.text()
        task_type = self.addShotTask.ui.comboBox_2.currentText()
        data = {'id':int(id),'task_name':task_name,'task_descrip':task_descrip,'task_status':task_status,'task_user':task_user,'task_type':task_type}

        if self.addShotTask.ui.lineEdit.text() != '' and self.addShotTask.ui.lineEdit_2.text() != '' :
            rowCount = widget.tableWidget.rowCount()
            widget.tableWidget.insertRow(rowCount)
            combBox = QComboBox()
            combBox.addItems(['work', 'wait', 'approve'])
            combBox.setCurrentText(task_status)
            widget.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(id)))
            widget.tableWidget.setItem(rowCount, 1, QTableWidgetItem(task_name))
            widget.tableWidget.setItem(rowCount, 2, QTableWidgetItem(task_descrip))
            widget.tableWidget.setCellWidget(rowCount, 3, combBox)
            widget.tableWidget.setItem(rowCount, 4, QTableWidgetItem(task_user))
            widget.tableWidget.setItem(rowCount, 5, QTableWidgetItem(task_type))
            GetDataBase.creatShotTaskInfo(self.projectCode,data)
            QMessageBox.question(self, '提示', '创建成功', QMessageBox.Yes)
            self.addShotTask.close()
        else:
            reply = QMessageBox.question(self, '提示', '资产名称和类型是必填字段', QMessageBox.Yes)


class AssetContet(QWidget):
    def __init__(self, parent=None):
        super(AssetContet, self).__init__(parent)
        self.message = MessageList()
        self.content = TabDemo()
        self.lay = QHBoxLayout()
        self.lay.addWidget(self.message)
        self.lay.addWidget(self.content)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.setSpacing(0)
        self.setLayout(self.lay)
        self.message.navigationList.itemClicked.connect(self.content.getProjectName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AssetContet()
    window.show()
    app.exec_()
