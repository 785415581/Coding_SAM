# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlDatabase

from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant, QItemSelectionModel,
                          pyqtSlot)

class CheckBoxHeader(QHeaderView):
    clicked = pyqtSignal(bool)

    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height()-self._width)/2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                self.clicked.emit(self.isOn)
                self.update()
        super(CheckBoxHeader, self).mousePressEvent(event)


class CheckboxSqlModel(QtSql.QSqlQueryModel):
    def __init__(self, column):
        super(CheckboxSqlModel, self).__init__()

        self.column = column
        self.checkboxes = list() #List of checkbox states
        self.first = list() #Used to initialize checkboxes

    #Make column editable
    def flags(self, index):
        flags = QtSql.QSqlQueryModel.flags(self, index)
        if index.column() == self.column:
            flags |= Qt.ItemIsUserCheckable
        return flags

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        col = index.column()

        if index.column() == self.column and role == Qt.CheckStateRole:
            #Used to initialize
            if row not in self.first :
                # print(row, col)
                index = self.createIndex(row, self.column)
                self.first.append(row)
                self.checkboxes.append(False)
                return Qt.Unchecked
            # #if checked
            elif self.checkboxes and self.checkboxes[row]:
                # print('-'*20)
                # print(row, col)
                # print(self.checkboxes[row])
                return Qt.Checked
            else:
                return Qt.Unchecked

        else:
            return QtSql.QSqlQueryModel.data(self, index, role)

    def setData0(self, index, value, role=Qt.DisplayRole):
        row = index.row()
        if index.column() == self.column and role == Qt.CheckStateRole:
            if value.toBool():
                self.checkboxes[row] = True
            else:
                self.checkboxes[row] = False
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def setData(self, index, value, role=Qt.DisplayRole):
        row = index.row()
        if index.column() == self.column and role == Qt.CheckStateRole:
            if value == Qt.Checked:
                self.checkboxes[row] = True
            else:
                self.checkboxes[row] = False
            self.dataChanged.emit(index, index, [Qt.CheckStateRole])
            return True
        else:
            return False

    def headerClick(self, isOn):
        self.beginResetModel()
        if isOn:
            print(self.first)
            self.checkboxes = self.first
        else:
            self.checkboxes = []

        self.endResetModel()

def on_data_changed(topleft, bottomRight, roles):
    if Qt.CheckStateRole in roles:
        row = topleft.row()
        isChecked = topleft.data(Qt.CheckStateRole) == Qt.Checked
        flag = QItemSelectionModel.Select if isChecked else QItemSelectionModel.Deselect
        for col in range(table_model3.columnCount()):
            ix = table_model3.index(row, col)
            tableView3.selectionModel().select(ix, flag)
                
if __name__ == '__main__':
    a = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName('C:/Users/mayn/Documents/Tencent Files/785415581/FileRecv/QTableView/db1/LibraryManagement.db')
    db.open()
    tableView3 = QTableView()
    tableView3.setMinimumSize(1000, 800)
    table_model3 = CheckboxSqlModel(0)
    table_model3.setQuery("select * from Book")
    tableView3.setModel(table_model3)
    tableView3.horizontalHeader().setStretchLastSection(True)
    tableView3.setShowGrid(False)
    table_model3.setHeaderData(0, Qt.Horizontal, "All")
    table_model3.setHeaderData(1, Qt.Horizontal, "Client Name")
    table_model3.setHeaderData(2, Qt.Horizontal, "Email Address")
    # table_model3.dataChanged.connect(on_data_changed)
    header = CheckBoxHeader()
    tableView3.setHorizontalHeader(header)
    header.clicked.connect(table_model3.headerClick)
    tableView3.setStyleSheet(
        'QHeaderView:section{Background-color:#cdcdcd; font-family: Arial Narrow; font-size: 15px; height: 30px;}')
    table_model3.insertColumn(0)
    tableView3.setColumnWidth(0, 30)
    tableView3.show()
    a.exec_()