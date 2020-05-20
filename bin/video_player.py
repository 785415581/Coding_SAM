# -*- coding: utf-8 -*-
import os,sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from urllib import parse
file_ = os.path.dirname(os.path.dirname(__file__))
class videoPlayer(QWidget):  # 视频播放类
    def __init__(self,parent=None):  # 构造函数
        super(videoPlayer, self).__init__(parent)  # 类的继承
        self.parent = parent
        self.length = 0  # 视频总时长
        self.position = 0  # 视频当前时长
        self.count = 0
        self.player_status = -1
        # 设置窗口
        self.setGeometry(300, 50, 1200, 800)  # 大小,与桌面放置位置

        # 设置窗口背景
        self.palette = QPalette()
        self.palette.setColor(QPalette.Background, Qt.white)
        self.setPalette(self.palette)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.now_position = QLabel("/  00:00")  # 目前时间进度
        self.all_duration = QLabel('00:00')  # 总的时间进度
        self.all_duration.setStyleSheet('''QLabel{color:#000000}''')
        self.now_position.setStyleSheet('''QLabel{color:#000000}''')

        # 视频插件
        self.video_widget = QVideoWidget(self)
        self.video_widget.setObjectName('videoWidget')
        # video_widget_color = "background-coloe:#ffffff"
        # self.video_widget.setStyleSheet(video_widget_color)

        # 布局容器
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.layout = QHBoxLayout()
        self.layout.setSpacing(15)  # 各个插件的间距

        # 设置播放器
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        # 设置播放按钮事件
        self.player.durationChanged.connect(self.get_duration_func)
        self.player.positionChanged.connect(self.progress)  # 媒体播放时发出信号
        self.player.mediaStatusChanged.connect(self.playerStatusChanged)
        self.player.error.connect(self.player_error)

        # 播放按钮
        self.play_btn = QPushButton(self)
        self.play_btn.setIcon(QIcon(file_ + '/resource/play_btn_icon.png'))  # 设置按钮图标,下同
        self.play_btn.setIconSize(QSize(35, 35))
        self.play_btn.setStyleSheet('''QPushButton{border:none;}QPushButton:hover{border:none;border-radius:35px;}''')
        self.play_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_btn.setToolTip("播放")
        self.play_btn.setFlat(True)
        self.play_btn.clicked.connect(self.start_button)

        # 音量条
        self.volume_slider = QSlider(Qt.Horizontal)  # 声音设置
        self.volume_slider.setMinimum(0)  # 音量0到100
        self.volume_slider.setMaximum(100)
        self.volume_slider.valueChanged.connect(self.volumes_change)
        self.volume_slider.setStyleSheet('''QSlider{}
QSlider::sub-page:horizontal:disabled{background: #00009C;  border-color: #999;  }
QSlider::add-page:horizontal:disabled{background: #eee;  border-color: #999; }
QSlider::handle:horizontal:disabled{background: #eee;  border: 1px solid #aaa;  border-radius: 4px;  }
QSlider::add-page:horizontal{background: #575757;  border: 0px solid #777;  height: 10px;border-radius: 2px; }
QSlider::handle:horizontal:hover{background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA,   stop:0.778409 rgba(255, 255, 255, 255));  width: 11px;  margin-top: -3px;  margin-bottom: -3px;  border-radius: 5px; }
QSlider::sub-page:horizontal{background: qlineargradient(x1:0, y1:0, x2:0, y2:1,   stop:0 #B1B1B1, stop:1 #c4c4c4);  background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,stop: 0 #5DCCFF, stop: 1 #1874CD);  border: 1px solid #4A708B;  height: 10px;  border-radius: 2px;  }
QSlider::groove:horizontal{border: 1px solid #4A708B;  background: #C0C0C0;  height: 5px;  border-radius: 1px;  padding-left:-1px;  padding-right:-1px;}
QSlider::handle:horizontal{background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,   stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));  width: 11px;  margin-top: -3px;  margin-bottom: -3px;  border-radius: 5px; }''')

        # 视频播放进度条
        self.video_slider = QSlider(Qt.Horizontal, self)  # 视频进度拖拖动
        self.video_slider.setMinimum(0)  # 视频进度0到100%
        # self.video_slider.setMaximum(100)
        self.video_slider.setSingleStep(1)
        self.video_slider.setGeometry(QRect(0, 0, 200, 10))
        self.video_slider.sliderReleased.connect(self.video_silder_released)
        self.video_slider.sliderPressed.connect(self.video_silder_pressed)

        self.video_slider.setStyleSheet('''QSlider{}
QSlider::sub-page:horizontal:disabled{background: #00009C;  border-color: #999;  }
QSlider::add-page:horizontal:disabled{background: #eee;  border-color: #999; }
QSlider::handle:horizontal:disabled{background: #eee;  border: 1px solid #aaa;  border-radius: 4px;  }
QSlider::add-page:horizontal{background: #575757;  border: 0px solid #777;  height: 10px;border-radius: 2px; }
QSlider::handle:horizontal:hover{background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA,   stop:0.778409 rgba(255, 255, 255, 255));  width: 11px;  margin-top: -3px;  margin-bottom: -3px;  border-radius: 5px; }
QSlider::sub-page:horizontal{background: qlineargradient(x1:0, y1:0, x2:0, y2:1,   stop:0 #B1B1B1, stop:1 #c4c4c4);  background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,stop: 0 #5DCCFF, stop: 1 #1874CD);  border: 1px solid #4A708B;  height: 10px;  border-radius: 2px;  }
QSlider::groove:horizontal{border: 1px solid #4A708B;  background: #C0C0C0;  height: 5px;  border-radius: 1px;  padding-left:-1px;  padding-right:-1px;}
QSlider::handle:horizontal{background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,   stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));  width: 11px;  margin-top: -3px;  margin-bottom: -3px;  border-radius: 5px; }''')

        # 静音按钮
        self.mute_button = QPushButton('')
        self.mute_button.clicked.connect(self.mute)
        self.mute_button.setIconSize(QSize(30, 30))
        self.mute_button.setStyleSheet('''QPushButton{border:none;}QPushButton:hover{border:none;}''')
        self.mute_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.mute_button.setToolTip("播放")
        self.mute_button.setFlat(True)
        self.mute_button.setIcon(QIcon(file_ + '/resource/sound_btn_icon.png'))

        # 暂停按钮
        self.pause_btn = QPushButton('')
        self.pause_btn.setIcon(QIcon(file_ + '/resource/stop_btn_icon.png'))
        self.pause_btn.clicked.connect(self.stop_button)
        self.pause_btn.setIconSize(QSize(35, 35))
        self.pause_btn.setStyleSheet('''QPushButton{border:none;}QPushButton:hover{border:none;}''')
        self.pause_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pause_btn.setToolTip("播放")
        self.pause_btn.setFlat(True)
        self.pause_btn.hide()

        # 音量值和音量显示标签
        self.volume_value = QLabel()
        self.volume_value.setText(' ' * 5)
        self.volume_value.setStyleSheet('''QLabel{color:#000000;}''')

        self.volume_t = QLabel()

        self.volume_t.setStyleSheet('''QLabel{color:#000000;}''')

        # 视频文件打开按钮
        self.open_btn = QPushButton('Open')
        self.open_btn.clicked.connect(self.getfile)

        # 全屏按钮
        self.screen_btn = QPushButton('')
        self.screen_btn.setIcon(QIcon(QPixmap(file_ + '/resource/fullsrceen_btn_icon.png')))
        self.screen_btn.setIconSize(QSize(38, 38))
        self.screen_btn.setStyleSheet(
            '''QPushButton{border:none;}QPushButton:hover{border:1px solid #F3F3F5;border-radius:35px;}''')
        self.screen_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.screen_btn.setToolTip("播放")
        self.screen_btn.setFlat(True)
        self.screen_btn.clicked.connect(self.fullscreen)

        # 添加按钮组件
        self.verticalLayout.addStretch()
        self.layout.addWidget(self.play_btn, 0, Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.pause_btn, 0, Qt.AlignCenter | Qt.AlignVCenter)  # 插件,与前一个模块的距离，位置

        self.layout.addWidget(self.all_duration, 0, Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.now_position, 0, Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.video_slider, 15, Qt.AlignVCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.mute_button, 0, Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.volume_slider, 0, Qt.AlignCenter | Qt.AlignVCenter)

        self.layout.addWidget(self.volume_value, 0, Qt.AlignCenter | Qt.AlignVCenter)

        # self.layout.addWidget(self.screen_btn)
        # self.layout.addWidget(self.open_btn)
        self.verticalLayout.addLayout(self.layout)

        # self.verticalLayout.addLayout(self.layout)
        self.setLayout(self.verticalLayout)

    def player_error(self, errorCode):
        print('error = ' + str(errorCode))
        try:
            if errorCode == 0:
                pass
            elif errorCode == 1:
                self.showAlertWindow('errorCode：1 \n\n无效视频源。')
            elif errorCode == 2:
                self.showAlertWindow('errorCode：2 \n\n不支持的媒体格式')
            elif errorCode == 3:
                self.showAlertWindow('errorCode：3 \n\n网络错误')
            elif errorCode == 4:
                self.showAlertWindow('errorCode：4 \n\n没有权限播放该视频')
            elif errorCode == 5:
                self.showAlertWindow('errorCode：5 \n\n视频服务不存在，无法继续播放。')
            else:
                self.showAlertWindow('未知错误')
        except:
            self.showAlertWindow('视频加载异常')

    def video_silder_pressed(self):
        if self.player.state != 0:
            self.player.pause()

    def playerStatusChanged(self, status):
        self.player_status = status
        if status == 7:
            self.play_btn.show()
            self.pause_btn.hide()

        # print('playerStatusChanged =' + str(status) + '...............')

    def resizeEvent(self, e):
        # print(e.size().width(), e.size().height())
        newSize = e.size()
        self.video_widget.setGeometry(0, 0, newSize.width(), newSize.height() - 50)
        # self.video_widget.setGeometry(0, 0, 0, 0)

    def closeEvent(self, e):
        self.player.stop()

    def get_duration_func(self, d):
        try:
            end_number = int(d / 1000 / 10) + 1
            # print('end_number = ' + str(end_number))
            sum = 0
            for n in range(1, end_number):
                sum = sum + n

            vv = int((100 / (d / 1000)) * (d / 1000))
            self.video_slider.setMaximum(d)
            # self.video_slider.setMaximum(vv + sum)
            # print(100 + sum)

            all_second = int(d / 1000 % 60)  # 视频播放时间
            all_minute = int(d / 1000 / 60)

            if all_minute < 10:

                if all_second < 10:

                    self.all_duration.setText('0' + str(all_minute) + ':0' + str(all_second))
                else:

                    self.all_duration.setText('0' + str(all_minute) + ':' + str(all_second))
            else:

                if all_second < 10:

                    self.all_duration.setText(str(all_minute) + ':0' + str(all_second))
                else:

                    self.all_duration.setText(str(all_minute) + ':' + str(all_second))
        except Exception as e:
            pass

    def mouseDoubleClickEvent(self, e):
        try:

            # print('mouseDoubleClickEvent................... = ' + str(self.player.state()))
            if self.player.state() == 2:
                # 视频暂停
                self.player.play()
                self.play_btn.hide()
                self.pause_btn.show()

            elif self.player.state() == 1:
                # 正在播放
                self.player.pause()
                self.play_btn.show()
                self.pause_btn.hide()
            else:
                # 视频停止
                self.play_btn.hide()
                self.pause_btn.show()
                self.player.setPosition(0)
                self.video_slider.setValue(0)
                self.player.play()
        except Exception as e:
            pass

    def start_button(self):  # 视频播放按钮
        try:

            self.play_btn.hide()
            self.pause_btn.show()

            if self.player_status == 7:
                self.video_slider.setValue(0)
                self.player.setPosition(0)

            self.player.play()
        except Exception as e:
            pass

    def stop_button(self):  # 视频暂停按钮
        self.play_btn.show()
        self.pause_btn.hide()
        self.player.pause()

    def getfile(self, filepath):  # 打开视频文件
        try:

            # print(str(filepath))
            url = QUrl.fromLocalFile(filepath)
            if url.isValid():
                self.player.setMedia(QMediaContent(url))  # 返回该文件地址,并把地址放入播放内容中
                self.player.setVolume(50)  # 设置默认打开音量即为音量条大小
                self.volume_value.setText(str(50))
                self.volume_slider.setValue(50)
            else:
                self.showAlertWindow('视频地址无效')

        except Exception as e:
            self.showAlertWindow()

    def clearVolumeValue(self):
        self.volume_value.setText(' ' * 4)

    def volumes_change(self):  # 拖动进度条设置声音
        try:
            size = self.volume_slider.value()
            if size:
                # 但进度条的值不为0时,此时音量不为静音,音量值即为进度条值
                self.player.setMuted(False)
                self.player.setVolume(size)
                volume_value = str(size) + ' ' * 4
                self.volume_value.setText(volume_value)
                # print(size)
                self.mute_button.setIcon(QIcon(file_ + '/resource/sound_btn_icon.png'))
            else:
                self.player.setMuted(True)
                self.mute_button.setIcon(QIcon(file_ + '/resource/mute_btn_icon.png'))
                self.player.setVolume(0)
                volume_value = '0' + ' ' * 4
                self.volume_value.setText(volume_value)

            if len(str(size)) == 1:
                volume_value = str(size) + ' ' * 4
            elif len(str(size)) == 2:
                volume_value = str(size) + ' ' * 3
            else:
                volume_value = str(size) + ' ' * 2

            self.volume_value.setText(volume_value)
        except Exception as e:
            pass

    def mute(self):
        try:
            if self.player.isMuted():
                self.mute_button.setIcon(QIcon(file_ + '/resource/sound_btn_icon.png'))
                self.player.setMuted(False)
                self.volume_slider.setValue(50)
                volume_value = '50' + ' ' * 4
                self.volume_value.setText(volume_value)
            else:
                self.mute_button.setIcon(QIcon(file_ + '/resource/mute_btn_icon.png'))
                self.player.setMuted(True)  # 若不为静音，则设置为静音，音量置为0
                self.volume_slider.setValue(0)
                volume_value = '0' + ' ' * 4
                self.volume_value.setText(volume_value)
        except Exception as e:
            pass

    def progress(self):  # 视频进度条自动释放与播放时间

        try:

            self.length = self.player.duration() + 1
            self.position = self.player.position()
            self.count += 1
            video_silder_maximum = self.video_slider.maximum()
            self.video_slider.setValue(self.position)
            now_second = int(self.position / 1000 % 60)
            now_minute = int(self.position / 1000 / 60)
            if now_minute < 10:
                if now_second < 10:
                    self.now_position.setText('/  0' + str(now_minute) + ':0' + str(now_second))
                else:
                    self.now_position.setText('/  0' + str(now_minute) + ':' + str(now_second))
            else:
                if now_second < 10:

                    self.now_position.setText('/  ' + str(now_minute) + ':0' + str(now_second))
                else:
                    # print('now_second > 10' + str(now_minute) + ':' + str(now_second))
                    self.now_position.setText('/  ' + str(now_minute) + ':' + str(now_second))
        except Exception as e:
            pass

    def video_silder_released(self):  # 释放滑条时,改变视频播放进度
        try:

            # print('video_silder_released......')
            if self.player.state() != 0:
                self.player.setPosition(self.video_slider.value())
                self.player.play()
            else:  # 如果视频是停止状态，则拖动进度条无效
                self.video_slider.setValue(0)
        except Exception as e:
            pass

    def fullscreen(self):
        self.showFullScreen()

    def keyPressEvent(self, event):  # 重新改写按键
        if event.key() == Qt.Key_Escape:
            self.winquit()

    def winquit(self):  # 退出窗口
        self.showNormal()

    def showAlertWindow(self, msg='视频加载出错！'):
        reply = QMessageBox.information(self,
                                        "消息框标题",
                                        msg,
                                        QMessageBox.Yes)

if __name__ == "__main__":  # 主函数

    app = QApplication(sys.argv)

    try:
        vp = videoPlayer()
        vp.show()
        filepath = 'E:/workSpace/Coding_SAM/sucai/EP001_SC001.mp4'
        filepath = parse.unquote(str(filepath), encoding='utf-8')
        vp.getfile(filepath.split('?')[0])

    except Exception as e:
        pass

    sys.exit(app.exec_())