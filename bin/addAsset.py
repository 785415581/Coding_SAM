# -*- coding: utf-8 -*-
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
file_ = os.path.dirname(os.path.dirname(__file__))

class Addasset(QWidget):
    def __init__(self):
        super(Addasset, self).__init__()
        self.setObjectName('addAsset')
        self.ui = uic.loadUi(file_ + "/data/addAsset.ui")
        self.ui.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.uifile = uifile
        # self.ui = uic.loadUi(self.uifile)
        self.setWindowFlags(Qt.FramelessWindowHint)
        lay = QVBoxLayout()
        lay.addWidget(self.ui)
        self.setLayout(lay)

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:

            self.ui.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False
class AddEps(QWidget):
    def __init__(self):
        super(AddEps, self).__init__()
        self.setObjectName('addAsset')
        self.ui = uic.loadUi(file_ + "/data/addEps.ui")
        self.ui.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        lay = QVBoxLayout()
        lay.addWidget(self.ui)
        self.setLayout(lay)

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:

            self.ui.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False
class AddAssetTask(QWidget):
    def __init__(self):
        super(AddAssetTask, self).__init__()
        self.setObjectName('addAssetTask')
        self.ui = uic.loadUi(file_ + "/data/addAssetTask.ui")
        self.ui.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        lay = QVBoxLayout()
        lay.addWidget(self.ui)
        self.setLayout(lay)

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:

            self.ui.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False
class AddShot(QWidget):
    def __init__(self):
        super(AddShot, self).__init__()
        self.setObjectName('addShot')
        self.ui = uic.loadUi(file_ + "/data/addShot.ui")
        self.ui.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        lay = QVBoxLayout()
        lay.addWidget(self.ui)
        self.setLayout(lay)

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:

            self.ui.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False
class AddShotTask(QWidget):
    def __init__(self):
        super(AddShotTask, self).__init__()
        self.setObjectName('addShot')
        self.ui = uic.loadUi(file_ + "/data/addShotTask.ui")
        self.ui.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        lay = QVBoxLayout()
        lay.addWidget(self.ui)
        self.setLayout(lay)

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:

            self.ui.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False
class AddUser(QWidget):
    def __init__(self):
        super(AddUser, self).__init__()
        self.setObjectName('addUser')
        self.ui = uic.loadUi(file_ + "/data/addUser.ui")
        self.ui.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        lay = QVBoxLayout()
        lay.addWidget(self.ui)
        self.setLayout(lay)

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:

            self.ui.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddEps()
    window.show()
    app.exec_()