# -*- coding: utf-8 -*-
import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from widget.base import ListItemWidget, SearchLineEdit, Label
from addProject import AddProject
from QureySQL import GetDataBase
from PyQt5 import uic
import datetime
import shutil
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
color: rgb(250,250,250);
background:white;
'''

class MessageList(QScrollArea):
    def __init__(self, parent=None):
        super(MessageList, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent = parent
        self.frame = QWidget()
        self.setMinimumSize(240, 240)
        self.setMaximumSize(240, 1080)
        self.resize(240, 1080)

        self.setWidget(self.frame)
        self.setWidgetResizable(True)
        self.frame.setMinimumWidth(240)

        self.addProject = QPushButton(u'添加项目')
        self.addProject.clicked.connect(self.AddProject)

        with open(file_ + '/QSS/messageList.qss', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
            self.frame.setStyleSheet(style)
        self.setListViews()
        self.setLayouts()
        self.rightfunction()
        self.addProject = AddProject()

    def AddProject(self):
        self.addProject.ui.comboBox.addItems(GetDataBase.getDatabases())
        self.addProject.show()
        self.addProject.ui.BlueButton.clicked.connect(self.openFileFloer)
        self.addProject.ui.pushButton.clicked.connect(self.asdasd)
        self.addProject.ui.pushButton_2.clicked.connect(self.addProject.close)

    def openFileFloer(self):
        if not self.addProject.ui.lineEdit.text() == '':
            filePath = QFileDialog.getOpenFileName(self,"Open Image", file_, "Image Files (*.png *.jpg *.bmp)")
            fileName = os.path.basename(filePath[0])

            projectPath = (file_ + '\\project\\' +self.addProject.ui.lineEdit.text() + '\\' + 'projectConfig\\picture').replace('/','\\')
            if not os.path.exists(projectPath):
                os.makedirs(projectPath)
                newFile = projectPath + '\\' + self.addProject.ui.lineEdit.text() + '.' + 'jpg'
                shutil.copyfile(filePath[0],newFile)
                self.addProject.ui.BlueButton.setText('')
                self.addProject.ui.BlueButton.setIcon(QIcon(newFile))
        else:
            pass
    def asdasd(self):

        modelDatabase = self.addProject.ui.comboBox.currentText()
        newDatabase = self.addProject.ui.lineEdit.text()
        chinesename = self.addProject.ui.lineEdit_2.text()
        dateTime = datetime.datetime.now().strftime('%Y%m%d%I%M%S')
        auther = self.addProject.ui.lineEdit_4.text()
        infor = {}
        infor["databasecode"] = newDatabase
        infor["chinesename"] = chinesename
        infor["date"] = dateTime
        infor["auther"] = auther
        print(newDatabase,chinesename,auther,infor)
        if newDatabase != '' and chinesename != '' and auther != '':
            GetDataBase.AddProject(newDatabase,infor,modelDatabase)
            QMessageBox.question(self, '提示', '创建成功', QMessageBox.Yes)
            self.addProject.close()
            self.update()
        else:
            QMessageBox.question(self, '提示', '字段不准为空', QMessageBox.Yes)



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
            if os.path.isfile(projectThmunail):
                ListItemWidget(self.navigationList, projectThmunail, chineseName, projectCode, videoPath='')
            else:
                projectThmunail = file_ + '/project/' +  'origin.jpg'
                ListItemWidget(self.navigationList, projectThmunail, chineseName, projectCode, videoPath='')

        self.navigationList.setCurrentRow(0)
        self.navigationList.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
                                                              "QScrollBar::handle{background:lightgray; border:20px solid transparent; border-radius:50px;}"
                                                              "QScrollBar::handle:hover{background:gray;}"
                                                              "QScrollBar::sub-line{background:transparent;}"
                                                              "QScrollBar::add-line{background:transparent;}")
        self.navigationList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.navigationList.setCurrentRow(0)
    def setLayouts(self):
        """定义布局。"""
        self.mainLayout = QVBoxLayout(self.frame)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.navigationList)
        self.mainLayout.addWidget(self.addProject)

    # 功能。
    def getInfo(self, widget, *args, **kwargs):
        print(widget.getName(), widget.getinfoMessage(), widget.getVideoPath())
        # pass

    def rightfunction(self):

        self.navigationList.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.navigationList.customContextMenuRequested.connect(self.showContextMenu)  ####右键菜单
        self.contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.contextMenu.addAction(u'创建')
        self.actionB = self.contextMenu.addAction(u'删除')
        self.actionD = self.contextMenu.addAction((u'刷新'))
        self.actionA.triggered.connect(self.AddProject)
        self.actionB.triggered.connect(self.deleteProject)
        self.actionD.triggered.connect(self.update)

    def showContextMenu(self, pos):
        self.contextMenu.popup(self.navigationList.mapToGlobal(pos))
        self.contextMenu.show()

    def deleteProject(self):
        item = self.navigationList.currentItem()
        if item:
            projectCode = item.getinfoMessage()
            GetDataBase.deleteDatabse(projectCode)
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


class ConfigPanl(QWidget):
    def __init__(self,parent=None):
        super(ConfigPanl, self).__init__(parent)
        self.message = MessageList()
        self.message.navigationList.itemClicked.connect(self.projectSetting)
        lay = QHBoxLayout()
        self.ui = uic.loadUi(file_ + "/data/ProjectConfig.ui")
        self.ui.tabWidget.setStyleSheet(style)
        self.ui.tabWidget.setTabText(0,'资产')
        self.ui.tabWidget.setTabText(1,'镜头')
        self.ui.tabWidget.setCurrentIndex(0)
        self.f_item = self.ui.treeWidget.headerItem()
        self.ui.treeWidget.setColumnCount(1)
        self.ui.treeWidget.setHeaderLabels(['路径'])
        self.ui.assetTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.shotTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        root = TreeWidgetItem(self.ui.treeWidget)
        root.setText(0, 'Big')
        child1 = TreeWidgetItem(root)
        child1.setText(0, 'asset')
        child2 = TreeWidgetItem(root)
        child2.setText(0, 'shot')
        child3 = TreeWidgetItem(child1)
        child3.setText(0, 'work')
        child4 = TreeWidgetItem(child1)
        child4.setText(0, 'publish')
        child5 = TreeWidgetItem(child2)
        child5.setText(0, 'work')
        child6 = TreeWidgetItem(child2)
        child6.setText(0, 'publish')
        self.ui.treeWidget.addTopLevelItem(root)
        lay.addWidget(self.message)
        lay.addWidget(self.ui)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        self.setLayout(lay)
        self.rightfunction()
        self.Listrightfunction() #资产的
        self.tabelWidget2RightFunction() #镜头的
    def rightfunction(self):
        self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.ui.treeWidget.customContextMenuRequested.connect(self.showContextMenu)  ####右键菜单
        self.contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.contextMenu.addAction(u'插入')
        self.actionB = self.contextMenu.addAction(u'删除')
        self.actionC1 = self.contextMenu.addAction(u'展开')
        self.actionC = self.contextMenu.addAction(u'重命名')
        self.actionA1 = self.contextMenu.addAction(u'插入类型')
        self.actionD = self.contextMenu.addAction(u'保存')
        self.actionA.triggered.connect(self.addName)
        self.actionB.triggered.connect(self.delete)
        self.actionC.triggered.connect(self.reName)
        self.actionC1.triggered.connect(self.expandTree)
        self.actionA1.triggered.connect(self.insertName)
        self.actionD.triggered.connect(self.save)

    def showContextMenu(self, pos):
        self.contextMenu.popup(self.ui.treeWidget.mapToGlobal(pos))
        self.contextMenu.show()

    def save(self):
        rootPath = []
        result = self.getRootList(self.ui.treeWidget)
        for i in result:
            path = '/'.join(i)
            rootPath.append(path)
        sql = "UPDATE project SET projectpath= "
        sql += '"{rootPath}" WHERE name ='.format(rootPath=rootPath)
        sql += "'{name}'".format(name=self.projectCode)
        GetDataBase.UpDate(self.projectCode,sql)
        QMessageBox.question(self, '提示', '保存成功', QMessageBox.Yes)
        '''Big/asset/work
           Big/asset/publish
           Big/shot/work
           Big/shot/publish
        '''

    def getRootLevel(self,child_root, result):
        '''
        根据子节点查找父节点
        '''
        result.append(child_root.text(0))
        par_root = child_root.parent()
        if par_root:
            self.getRootLevel(par_root, result)

    def getRootList(self,tree_widget):
        child_root = []
        it = QTreeWidgetItemIterator(tree_widget)
        while it:
            item = it.value()
            if not item:
                break
            if not item.childCount():
                child_root.append(item)
            it += 1

        result = []
        for i in child_root:
            temp = []
            self.getRootLevel(i, temp)
            result.append(temp[::-1])
        return result


    def addName(self):
        column = self.ui.treeWidget.currentColumn()
        item = self.ui.treeWidget.currentItem()
        child1 = TreeWidgetItem(item)
        child1.setText(0, 'name')

    def insertName(self):

        item = self.tree.currentItem()
        child1 = TreeWidgetItem(item)
        child1.setText(0, 'child1')

    def expandTree(self):
        try:
            item = self.tree.currentItem()
            item.setExpanded(True)
            # self.tree.setItemsExpandable(item,True)
        except:
            pass

    def delete(self):
        try:
            # 尝试删除子节点（通过其父节点，调用removeChild函数进行删除）
            currNode = self.ui.treeWidget.currentItem()
            parent1 = currNode.parent()
            parent1.removeChild(currNode)
        except Exception:
            # 遇到异常时删除根节点
            try:
                rootIndex = self.ui.treeWidget.indexOfTopLevelItem(currNode)
                self.ui.treeWidget.takeTopLevelItem(rootIndex)
            except Exception:
                print(Exception)

    def reName(self):
        column = self.ui.treeWidget.currentColumn()
        item = self.ui.treeWidget.currentItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
        # self.tree.editItem(item,column)

    def onClicked(self):
        # 将之前选中的子项目背景色还原
        self.f_item.setBackground(0, QColor(255, 255, 255))
        # 获取当前选中项
        item = self.tree.currentItem()
        # 设置当前选择项背景
        item.setBackground(0, QColor('#AFEEEE'))
        # 更新前选中项
        self.f_item = item

    def allItems(self):
        pass

    def Listrightfunction(self):
        self.ui.assetTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.ui.assetTableWidget.customContextMenuRequested.connect(self.ListshowContextMenu)  ####右键菜单
        self.ListcontextMenu = QMenu()  # //创建QMenu
        self.ListactionA = self.ListcontextMenu.addAction(u'增加')
        self.ListactionB = self.ListcontextMenu.addAction(u'删除')
        self.ListactionC = self.ListcontextMenu.addAction(u'保存')
        self.ListactionA.triggered.connect(self.addPipe)
        self.ListactionB.triggered.connect(self.deletePipe)
        self.ListactionC.triggered.connect(self.savePipe)
    def addPipe(self):
        totalRow = self.ui.assetTableWidget.rowCount()
        currntRow = totalRow + 1
        self.ui.assetTableWidget.setRowCount(currntRow)
        self.ui.assetTableWidget.setItem(currntRow-1,0,QTableWidgetItem(''))
        self.ui.assetTableWidget.setItem(currntRow-1,1,QTableWidgetItem(''))
        # print(self.message.navigationList.currentItem().getName())

    def deletePipe(self):
        selectItem = self.ui.assetTableWidget.selectedItems()
        print(selectItem)
        selected_items = [selectItem[i] for i in range(len(selectItem) - 1, -1, -7)]
        for items in selected_items:
            self.ui.assetTableWidget.removeRow(self.ui.assetTableWidget.indexFromItem(items).row())
    def savePipe(self):

        totalRow = self.ui.assetTableWidget.rowCount()
        pipeline = {}
        assetPipeline = {}
        for row in range(totalRow):
            item = self.ui.assetTableWidget.item(row,0).text()
            item1 = self.ui.assetTableWidget.item(row,1).text()
            pipeline[item] = item1
        assetPipeline['asset'] = pipeline
        sql = "UPDATE project SET assetpipeline= "
        sql += '"{assetPipeline}" WHERE name ='.format(assetPipeline=assetPipeline)
        sql += "'{name}'".format(name=self.projectCode)
        GetDataBase.UpDate(self.projectCode,sql)
        QMessageBox.question(self, '提示', '保存成功', QMessageBox.Yes)

    def ListshowContextMenu(self, pos):
        self.ListcontextMenu.popup(self.ui.assetTableWidget.mapToGlobal(pos))
        self.ListcontextMenu.show()

    def projectSetting(self,item):

        self.projectCode = item.getinfoMessage()
        result = GetDataBase.getProjectInfo(self.projectCode)
        print(result)
        if result[0]['assetpipeline'] != None:
            assetPipeline = eval(result[0]['assetpipeline'])
            self.ui.assetTableWidget.setRowCount(len(assetPipeline['asset'].keys()))
            for i,key in enumerate(assetPipeline['asset']):
                self.ui.assetTableWidget.setItem(i,0,QTableWidgetItem(key))
                self.ui.assetTableWidget.setItem(i,1,QTableWidgetItem(assetPipeline['asset'][key]))
        if result[0]['shotpipeline'] != None:
            shotPipeline = eval(result[0]['shotpipeline'])
            self.ui.shotTableWidget.setRowCount(len(shotPipeline['shot'].keys()))
            for i,key in enumerate(shotPipeline['shot']):
                self.ui.shotTableWidget.setItem(i,0,QTableWidgetItem(key))
                self.ui.shotTableWidget.setItem(i,1,QTableWidgetItem(shotPipeline['shot'][key]))


    def tabelWidget2RightFunction(self):

        self.ui.shotTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.ui.shotTableWidget.customContextMenuRequested.connect(self.tabelWidget2RightContextMenu)  ####右键菜单
        self.ListcontextMenu2 = QMenu()  # //创建QMenu
        self.ListactionA2 = self.ListcontextMenu2.addAction(u'增加')
        self.ListactionB2 = self.ListcontextMenu2.addAction(u'删除')
        self.ListactionC2 = self.ListcontextMenu2.addAction(u'保存')
        self.ListactionA2.triggered.connect(self.addPipe2)
        self.ListactionB2.triggered.connect(self.deletePipe2)
        self.ListactionC2.triggered.connect(self.savePipe2)
    def tabelWidget2RightContextMenu(self, pos):
        self.ListcontextMenu2.popup(self.ui.shotTableWidget.mapToGlobal(pos))
        self.ListcontextMenu2.show()
    def addPipe2(self):
        totalRow = self.ui.shotTableWidget.rowCount()
        currntRow = totalRow + 1
        self.ui.shotTableWidget.setRowCount(currntRow)
        self.ui.shotTableWidget.setItem(currntRow-1,0,QTableWidgetItem(''))
        self.ui.shotTableWidget.setItem(currntRow-1,1,QTableWidgetItem(''))
    def deletePipe2(self):
        selectItem = self.ui.shotTableWidget.selectedItems()
        print(selectItem)
        selected_items = [selectItem[i] for i in range(len(selectItem) - 1, -1, -7)]
        for items in selected_items:
            self.ui.shotTableWidget.removeRow(self.ui.shotTableWidget.indexFromItem(items).row())
    def savePipe2(self):

        totalRow = self.ui.shotTableWidget.rowCount()
        pipeline = {}
        shotpipeline = {}
        for row in range(totalRow):
            item = self.ui.shotTableWidget.item(row,0).text()
            item1 = self.ui.shotTableWidget.item(row,1).text()
            pipeline[item] = item1
        shotpipeline['shot'] = pipeline
        sql = "UPDATE project SET shotpipeline= "
        sql += '"{shotpipeline}" WHERE name ='.format(shotpipeline=shotpipeline)
        sql += "'{name}'".format(name=self.projectCode)

        GetDataBase.UpDate(self.projectCode,sql)
        QMessageBox.question(self, '提示', '保存成功', QMessageBox.Yes)


class TreeWidgetItem(QTreeWidgetItem):
    def __init__(self, parent=None):
        super(TreeWidgetItem, self).__init__(parent)
        self.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)


class ProjectContet(QWidget):
    def __init__(self, parent=None):
        super(ProjectContet, self).__init__(parent)
        self.content = ConfigPanl()
        self.lay = QHBoxLayout()
        self.lay.addWidget(self.content)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.setSpacing(0)
        self.setLayout(self.lay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProjectContet()
    window.show()
    app.exec_()
