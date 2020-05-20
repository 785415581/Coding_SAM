# -*- coding: utf-8 -*-
import os,sys
from functools import partial
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip
file_ = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_)
from widget.base import ListItemWidget,SearchLineEdit,Label
import video_player
from StackContent import *
from UserInfo import UserInfo
# from imp import reload
# reload(StackContent)
from QureySQL import GetDataBase

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setObjectName('MainWindow')
        self.setStyleSheet("""MainWindow{background-color:#366CB3}""")
        self.setWindowTitle('SAM')
        self.moves()
        self.navigation = Navigation(self)
        # self.messagelist = MessageList(self)
        self.search = SearchLineArea(self)
        self.titlebar = TitleBar(self)
        self.titleinfo = TitleInfo(self)
        self.content = StackWidget(self)
        self.userInfo = UserInfo()

        self.setLayouts()
        # 窗口透明度动画类
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(1000)  # 持续时间1秒
        # 执行淡入
        self.doShow()
        self.navigationSlot()

    def doShow(self):
        try:
            # 尝试先取消动画完成后关闭窗口的信号
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # 透明度范围从0逐渐增加到1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # 动画完成则关闭窗口
        # 透明度范围从1逐渐减少到0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def setLayouts(self):

        self.verLayout1 = QVBoxLayout()
        self.verLayout1.addWidget(self.titlebar)
        self.verLayout1.addWidget(self.titleinfo)

        self.hlay = QHBoxLayout()
        self.hlay.addWidget(self.search)
        self.hlay.addLayout(self.verLayout1)

        self.verLayout2 = QVBoxLayout()
        self.verLayout2.addLayout(self.hlay)
        self.verLayout2.addWidget(self.content)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.navigation)
        self.mainLayout.addLayout(self.verLayout2)

        self.mainLayout.setAlignment(self.navigation,Qt.AlignLeft)
        self.mainLayout.setAlignment(self.verLayout2,Qt.AlignAbsolute)
        self.mainLayout.setStretch(0,60)
        self.mainLayout.setStretch(1,100)
        self.mainLayout.setStretch(2,500000)
        self.mainLayout.setContentsMargins(1, 1, 1, 1)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)

    def moves(self):
        self.desktop = QDesktopWidget()
        self.w = self.desktop.width()
        self.h = self.desktop.height()
        self.move(self.w*0.09,self.h*0.16)

    def _changeNormalButton(self):
        # 切换到恢复窗口大小按钮
        try:
            self.showMaximized()  # 先实现窗口最大化
            self.titlebar.buttonMaximum.setIcon(QIcon(file_ + '/resource/normal.png'))
            self.titlebar.buttonMaximum.setToolTip("恢复")  # 更改按钮提示
            self.titlebar.buttonMaximum.disconnect()  # 断开原本的信号槽连接
            self.titlebar.buttonMaximum.clicked.connect(self._changeMaxButton)  # 重新连接信号和槽
        except:
            pass

    def _changeMaxButton(self):
        # 切换到最大化按钮
        try:
            self.showNormal()
            self.titlebar.buttonMaximum.setIcon(QIcon(file_ + '/resource/maxButton.png'))
            self.titlebar.buttonMaximum.setToolTip("最大化")
            self.titlebar.buttonMaximum.disconnect()
            self.titlebar.buttonMaximum.clicked.connect(self._changeNormalButton)
        except:
            pass

    def navigationSlot(self):
        self.navigation.iconLabel.clicked.connect(lambda :self.userInfo.show(self.navigation.iconLabel.pos(),self.pos()))
        self.navigation.messageLabel.clicked.connect(partial(self.asd,self.navigation.messageLabel))
        self.navigation.orignaziLabel.clicked.connect(partial(self.asd,self.navigation.orignaziLabel))
        self.navigation.projectLabel.clicked.connect(partial(self.asd,self.navigation.projectLabel))
        self.navigation.projectSettingLabel.clicked.connect(partial(self.asd,self.navigation.projectSettingLabel))
        self.navigation.settingLabel.clicked.connect(self.close)



    def asd(self,widget):

        self.titleinfo.nickName.setText(widget.objectName())
        self.content.setCurrentIndex(widget.index)

    def showUserInfo(self):

        print(self.pos())
        print(self.navigation.iconLabel.pos())

        # print('111111111')


class Navigation(QFrame):

    def __init__(self, parent=None, navigationName = ''):
        """最右侧导航栏"""
        super(Navigation, self).__init__(parent)
        self.setObjectName('Navigation')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent = parent
        self.navigationName = navigationName
        self.setMinimumSize(60,100)
        self.setMaximumSize(60,1080)
        self.resize(60,640)
        with open(file_ + '/QSS/navigation.qss', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
        self.setLabels()
        # self.connect_and_emit()
        self.setLayouts()

    def setLabels(self):
        """创建所需的所有标签。"""
        self.iconLabel = Label()
        self.iconLabel.setObjectName('')
        self.iconLabel.setMaximumSize(35,35)
        self.iconLabel.setPixmap(QPixmap(file_ + '/resource/format.png'))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setCursor(Qt.PointingHandCursor)

        self.messageLabel = Label()
        self.messageLabel.index = 0
        self.messageLabel.setObjectName('镜头审片')
        self.messageLabel.setMaximumSize(25,25)
        self.messageLabel.setPixmap(QPixmap(file_ + '/resource/icon_信息2.png'))
        self.messageLabel.setScaledContents(True)
        self.messageLabel.setCursor(Qt.PointingHandCursor)

        self.orignaziLabel = Label()
        self.orignaziLabel.index = 1
        self.orignaziLabel.setObjectName('项目管理')
        self.orignaziLabel.setMaximumSize(25,25)
        self.orignaziLabel.setPixmap(QPixmap(file_ + '/resource/组织架构.png'))
        self.orignaziLabel.setScaledContents(True)
        self.orignaziLabel.setCursor(Qt.PointingHandCursor)

        self.projectLabel = Label()
        self.projectLabel.index = 2
        self.projectLabel.setObjectName('项目')
        self.projectLabel.setMaximumSize(25,25)
        self.projectLabel.setPixmap(QPixmap(file_ + '/resource/icon_采购数量.png'))
        self.projectLabel.setScaledContents(True)
        self.projectLabel.setCursor(Qt.PointingHandCursor)

        self.projectSettingLabel = Label()
        self.projectSettingLabel.index = 3
        self.projectSettingLabel.setObjectName('员工信息')
        self.projectSettingLabel.setMaximumSize(25,25)
        self.projectSettingLabel.setPixmap(QPixmap(file_ + '/resource/icon_设置.png'))
        self.projectSettingLabel.setScaledContents(True)
        self.projectSettingLabel.setCursor(Qt.PointingHandCursor)

        self.applicationLabel = Label()
        self.applicationLabel.index = 4
        self.applicationLabel.setObjectName('')
        self.applicationLabel.setMaximumSize(25,25)
        # self.applicationLabel.setIcon(QIcon('icon_应用.png'))
        self.applicationLabel.setPixmap(QPixmap(file_ + '/resource/icon_应用.png'))
        self.applicationLabel.setScaledContents(True)
        self.applicationLabel.setCursor(Qt.PointingHandCursor)

        self.settingLabel = Label()
        self.settingLabel.index = 5
        self.settingLabel.setObjectName('')
        self.settingLabel.setMaximumSize(25,25)
        self.settingLabel.setPixmap(QPixmap(file_ + '/resource/icon_shezhi.png'))
        self.settingLabel.setScaledContents(True)
        self.settingLabel.setCursor(Qt.PointingHandCursor)

    def setLayouts(self):
        """设置布局。"""
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addSpacing(20)
        self.mainLayout.addWidget(self.iconLabel)
        self.mainLayout.addSpacing(20)
        self.mainLayout.addWidget(self.messageLabel)
        self.mainLayout.addSpacing(20)
        self.mainLayout.addWidget(self.orignaziLabel)
        self.mainLayout.addSpacing(20)
        self.mainLayout.addWidget(self.projectLabel)
        self.mainLayout.addSpacing(20)
        self.mainLayout.addWidget(self.projectSettingLabel)
        self.mainLayout.addSpacing(20)
        self.mainLayout.addWidget(self.applicationLabel)
        self.mainLayout.addStretch(1)
        self.mainLayout.addWidget(self.settingLabel)
        self.mainLayout.addSpacing(10)
        self.setLayout(self.mainLayout)

    # 事件。
    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = True
            self.parent.m_DragPosition = event.globalPos()-self.parent.pos()
            event.accept()
        # if event.buttons() == Qt.LeftButton:   //没有父类继承错误
        #     self.m_drag = True
        #     self.m_DragPosition = event.globalPos()-self.pos()
        #     event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.parent.move(event.globalPos()-self.parent.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = False


class SearchLineArea(QFrame):
    def __init__(self,parent = None):
        super(SearchLineArea, self).__init__()
        self.parent = parent
        self.setObjectName('searchline')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("QFrame{background-color:#fbfbfb}")
        self.setMinimumSize(240,80)
        self.setMaximumSize(240,80)

        self.lineEdit = SearchLineEdit()
        self.labelAdd = QLabel()
        self.labelAdd.setFixedSize(20,20)
        self.labelAdd.setPixmap(QPixmap(file_ + '/resource/add.png'))
        self.labelAdd.setScaledContents(True)
        self.labelAdd.setCursor(Qt.PointingHandCursor)

        self.setLayouts()
    def setLayouts(self):

        self.verLayot = QHBoxLayout()
        self.verLayot.addWidget(self.lineEdit)
        self.verLayot.addSpacing(5)
        self.verLayot.addWidget(self.labelAdd)
        self.verLayot.addSpacing(10)

        self.horLayout = QVBoxLayout()
        self.horLayout.addSpacing(30)
        self.horLayout.addLayout(self.verLayot)
        self.setLayout(self.horLayout)

    # 事件。
    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = True
            self.parent.m_DragPosition = event.globalPos()-self.parent.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.parent.move(event.globalPos()-self.parent.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = False

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

        # 定义3个事件函数，方便扩展。
        self.navigationListFunction = self.none
        self.nativeListFunction = self.none
        self.singsFunction = self.none

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

        for i in range(100):
            widget = ListItemWidget(self.navigationList,file_ + '/resource/format.png','EP_0' + str(i),'[自定义表情]',videoPath='')
            # self.navigationList.itemDoubleClicked.connect(partial(self.getInfo,widget))
        self.navigationList.addItem(QListWidgetItem(QIcon(file_ + '/resource/movie.png'), " 发现音乐"))
        self.navigationList.addItem(QListWidgetItem(QIcon(file_ + '/resource/movie.png'), " 私人FM"))

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

    # 功能。
    def getInfo(self,widget,*args, **kwargs):
        print(widget.getName(),widget.getinfoMessage(),widget.getVideoPath())
        # pass

    def none(self):
        pass

class TitleBar(QWidget):
    def __init__(self, parent=None):

        super(TitleBar, self).__init__(parent)

        self.parent = parent
        self.setMaximumWidth(1920)
        self.setMinimumWidth(800)

        self.setMaximumHeight(20)
        self.setMinimumHeight(20)

        with open(file_ + '/QSS/titleBar.qss', 'r',encoding='utf-8') as f:
            style = f.read()
            self.setStyleSheet(style)

        self.setAttribute(Qt.WA_StyledBackground, True)

        palette = self.palette()
        palette.setColor(palette.Window, QColor(242, 243, 245))
        self.setPalette(palette)

        # 布局
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)


        # 中间伸缩条
        layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 利用Webdings字体来显示图标
        font = self.font() or QFont()
        font.setFamily('Webdings')

        # 最小化按钮
        self.buttonMinimum = QPushButton(QIcon(file_ + '/resource/minButton.png'),'',self,objectName='buttonMinimum')
        self.buttonMinimum.clicked.connect(self.parent.doClose)
        layout.addWidget(self.buttonMinimum)

        # 最大化/还原按钮
        self.buttonMaximum = QPushButton(QIcon(file_ + '/resource/maxButton.png'),'',self,objectName='buttonMaximum')
        self.buttonMaximum.clicked.connect(self.parent._changeNormalButton)

        layout.addWidget(self.buttonMaximum)

        # 关闭按钮
        self.buttonClose = QPushButton(QIcon(file_ + '/resource/closeButton.png'),'',self,objectName='buttonClose')
        # self.buttonClose = QPushButton(b'\xef\x81\xb2'.decode("utf-8"), self,objectName='buttonClose')

        self.buttonClose.clicked.connect(self.parent.close)

        layout.addWidget(self.buttonClose)



    def setHeight(self, height=20):
        """设置标题栏高度"""
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        # 设置右边按钮的大小
        self.buttonMinimum.setMinimumSize(30, height)
        self.buttonMinimum.setMaximumSize(30, height)
        self.buttonMaximum.setMinimumSize(30, height)
        self.buttonMaximum.setMaximumSize(30, height)
        self.buttonClose.setMinimumSize(30, height)
        self.buttonClose.setMaximumSize(30, height)



    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:

            self.parent.m_drag = True
            self.parent.m_DragPosition = event.globalPos()-self.parent.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.parent.move(event.globalPos()-self.parent.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = False

class TitleInfo(QWidget):
    def __init__(self,parent = None):
        super(TitleInfo, self).__init__(parent)
        self.parent = parent
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_StyledBackground, True)
        with open(file_ + '/QSS/titleInfo.qss', 'r',encoding='utf-8') as f:
            style = f.read()
            self.setStyleSheet(style)
        self.setMaximumHeight(60)
        self.setMinimumHeight(60)
        self.nickName = QLabel()
        self.nickName.setObjectName('nickNameLabel')
        self.nickName.setText(u'SAM')
        self.detail = QLabel()
        self.detail.setObjectName('detailLabel')
        self.detail.setText('这是一条测试信息')
        self.lay = QHBoxLayout()
        self.lay.addSpacing(10)
        self.lay.addWidget(self.nickName)
        # self.lay.addWidget(self.detail)
        self.lay.setAlignment(self.nickName,Qt.AlignLeft)
        self.lay.setContentsMargins(0,0,0,0)
        self.lay.setSpacing(0)
        self.setLayout(self.lay)

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = True
            self.parent.m_DragPosition = event.globalPos()-self.parent.pos()
            event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.parent.move(event.globalPos()-self.parent.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = False

    def mouseDoubleClickEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.showMaximized()

class Content(QWidget):
    def __init__(self,parent=None):
        super(Content, self).__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.parent = parent
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("""QWidget{background-color: #C0C0C0}""")

    # 事件。
    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        #继承父类使用self.parent
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = True
            self.parent.m_DragPosition = event.globalPos()-self.parent.pos()
            event.accept()
        # if event.buttons() == Qt.LeftButton:   //没有父类继承错误
        #     self.m_drag = True
        #     self.m_DragPosition = event.globalPos()-self.pos()
        #     event.accept()
    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.parent.move(event.globalPos()-self.parent.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = False

def start():
    app = QApplication(sys.argv)

    main = MainWindow()

    main.show()

    app.exec_()

#
if __name__ == '__main__':

    start()
