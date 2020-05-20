# -*- coding: utf-8 -*-
import os, sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class AddProject(QWidget):
    def __init__(self,parent=None):
        super(AddProject, self).__init__(parent)
        self.ui = uic.loadUi("E:/workSpace/Coding_SAM/data/addProject.ui")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent = parent
        self.ui.pushButton.setFixedSize(50,50)
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