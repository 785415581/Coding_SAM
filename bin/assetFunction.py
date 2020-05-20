# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from functools import partial


class ConfigFunction():
    def __init__(self,widget):
        self.ui = widget

    def rightfunction(self):

        self.epsui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.epsui.tableWidget.customContextMenuRequested.connect(self.showContextMenu)  ####右键菜单
        self.contextMenu = QMenu()  # //创建QMenu
        self.actionA = self.contextMenu.addAction(u'创建')
        self.actionB = self.contextMenu.addAction(u'删除')
        self.actionC = self.contextMenu.addAction(u'创建目录')
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

    def showFields(self,pushbuttonPos,pos):
        x1 = pushbuttonPos.x()
        y1 = pushbuttonPos.y()
        x = pos.x()
        y = pos.y()
        print(x1,y1,x,y)
        self.fields.show()

    def add(self,widget):
        self.addAsset.show()
        self.addAsset.ui.pushButton.clicked.connect(partial(self.feedbackSql,widget))
        self.addAsset.ui.pushButton_2.clicked.connect(self.addAsset.close)

    def delRow(self):

        Items = self.epsui.tableWidget.selectedItems()
        assetList = [Items[i:i + 6] for i in range(0, len(Items), 6)]
        for i in assetList:
            sql = "DELETE FROM asset WHERE id={id} AND name={name} AND type={type}".format(id=i[0].text(),name=i[1].text(),type=i[2].text())
            print(sql)

        selected_items = [Items[i] for i in range(len(Items) - 1, -1, -7)]
        for items in selected_items:
            self.epsui.tableWidget.removeRow(self.epsui.tableWidget.indexFromItem(items).row())

    def feedbackSql(self,widget):

        if self.addAsset.ui.lineEdit.text() != '' and self.addAsset.ui.lineEdit_2.text() !='':
            rowCount = widget.tableWidget.rowCount()
            widget.tableWidget.insertRow(rowCount)
            print(rowCount,widget)
            print('rowCount')
        else:
            reply = QMessageBox.question(self, '提示', '资产名称和类型是必填字段', QMessageBox.Yes)

    def wranning(self):
        print(self.addAsset.ui.lineEdit.text())
        print(self.addAsset.ui.lineEdit_2.text())
        print('No message')
