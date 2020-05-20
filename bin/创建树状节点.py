#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TreeWidget(QMainWindow):

    def __init__(self, parent=None):
        super(TreeWidget, self).__init__(parent)
        self.resize(500,400)
        self.setWindowTitle('TreeWidget')
        self.intUI()
        # self.initAnimation()
        self.rightfunction()
    def intUI(self):
        self.tree = QTreeWidget(self)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)######允许右键产生子菜单
        self.tree.clicked.connect(self.onClicked)
        self.f_item = self.tree.headerItem()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['Key'])
        root = TreeWidgetItem(self.tree)
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
        self.tree.addTopLevelItem(root)
        self.setCentralWidget(self.tree)



    def change(self):
        print('a')

    def rightfunction(self):
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)######允许右键产生子菜单
        self.tree.customContextMenuRequested.connect(self.showContextMenu)####右键菜单
        self.contextMenu = QMenu(self)  #   //创建QMenu
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

    # def initAnimation(self):
    #     # 按钮动画
    #     self._animation = QPropertyAnimation(self.contextMenu, b'geometry', self,
    #         easingCurve=QEasingCurve.Linear, duration=300)
    #     # easingCurve 修改该变量可以实现不同的效果

    def save(self):
        topItem = self.tree.topLevelItem(0)
        childCount = topItem.childCount()

        # def getChild():
        #     for index in range(childCount):
        #         chileItem = topItem.child(index)
        #         chileItemText = chileItem.text(0)
        #         print(chileItemText)
        # getChild()

        print('1111')

    def showContextMenu(self, pos):
        self.contextMenu.popup(self.mapToGlobal(pos))
        self.contextMenu.show()

    def addName(self):
        column = self.tree.currentColumn()
        item = self.tree.currentItem()
        child1 = TreeWidgetItem(item)
        child1.setText(0, 'child1')

    def insertName(self):

        item = self.tree.currentItem()
        child1 = TreeWidgetItem(item)
        child1.setText(0, 'child1')

    def expandTree(self):
        item = self.tree.currentItem()
        item.setExpanded(True)
        # self.tree.setItemsExpandable(item,True)

    def delete(self):
        try:
            # 尝试删除子节点（通过其父节点，调用removeChild函数进行删除）
            currNode = self.tree.currentItem()
            parent1 = currNode.parent()
            parent1.removeChild(currNode)
        except Exception:
            # 遇到异常时删除根节点
            try:
                rootIndex = self.tree.indexOfTopLevelItem(currNode)
                self.tree.takeTopLevelItem(rootIndex)
            except Exception:
                print(Exception)

    def reName(self):
        column = self.tree.currentColumn()
        item = self.tree.currentItem()
        item.setFlags(Qt.ItemIsEnabled|Qt.ItemIsEditable)
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
class TreeWidgetItem(QTreeWidgetItem):
    def __init__(self,parent=None):
        super(TreeWidgetItem, self).__init__(parent)
        self.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tp = TreeWidget()
    tp.show()
    app.exec_()
