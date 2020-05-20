# -*- coding: utf-8 -*-
import subprocess, sys, os



ffmpegPath = r"E:\ffmpeg\bin\ffmpeg.exe"
ffplayPath = r"E:\ffmpeg\bin\ffplay.exe"
ffprobePath = r"E:\ffmpeg\bin\ffprobe.exe"


class CutSplicingVdeio(object):

    def __init__(self):
        pass

    # dercription CutSplicingVdeio this class function
    def instructions(self):
        dercription = "vdeio and image transform,vdeio other opreation"
        return dercription

    # use it can cut a video part
    def cutOutVideo(self, ffmpegPath, CurMediaPath, videoStartTime, videoEndTime, videoSaveDir):
        CurMediaPath = CurMediaPath.decode('utf-8')
        videoSaveDir = videoSaveDir.decode('utf-8')
        cmd = ffmpegPath + ' -y -i ' + CurMediaPath + ' -ss ' + videoStartTime + ' -t ' + videoEndTime + \
              ' -acodec copy -vcodec copy -async 1 ' + videoSaveDir
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # get video dercription
    def getVideoData(self, videoPath):
        videoPath = videoPath.decode('utf-8')
        cmd = ffprobePath + " -loglevel quiet print_format json -show_packets -show_streams " + videoPath
        # cmd=cmd.encode(sys.getfilesystemencoding())
        # print cmd.encode(sys.getfilesystemencoding())
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = result.stdout.read()
        return out

    # video decomposition image
    def videoTransImage(self, CurMediaPath, imageSaveDir):
        CurMediaPath = CurMediaPath.decode('utf-8')
        imageSaveDir = imageSaveDir.decode('utf-8')
        (filePath, tempfilename) = os.path.split(CurMediaPath);
        cmd = ffmpegPath + " -i " + CurMediaPath + " " + imageSaveDir + "\\" + tempfilename.split(".")[0] + "_%03d.jpg"
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # image Composition video
    def ImageTransVideo(self, imagePath, videoSaveDir):
        imagePath = imagePath.decode('utf-8')
        videoSaveDir = videoSaveDir.decode('utf-8')
        cmd = ffmpegPath + " -i " + imagePath + " " + videoSaveDir
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # cut out a 352x240 size image,strat key
    def cutVideoImage_resolution(self, videoPath, fileName, resolution):
        videoPath = videoPath.decode('utf-8')
        fileName = fileName.decode('utf-8')
        cmd = ffmpegPath + " -i " + videoPath + " -y " + \
              " -t 0.001" + " -s " + resolution + " " + fileName
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # cut out a 352x240 size image,time key
    def cutVideoImage_reAndTime(self, videoPath, fileName, resolution, time):
        videoPath = videoPath.decode('utf-8')
        # print videoPath
        fileName = fileName.decode('utf-8')
        cmd = ffmpegPath + " -i " + "\"" + (videoPath) + "\"" + " -y " + " -ss " + str(time) \
              + " -t 0.001 -s " + resolution + " " + str(fileName)
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # video front keytime key Composition gif image
    def videoKeyRange_Gif(self, videoPath, fileName, keytime):
        videoPath = videoPath.decode('utf-8')
        fileName = fileName.decode('utf-8')
        cmd = ffmpegPath + " -i " + videoPath + " -vframes " + str(keytime) + " -y -f gif " + fileName
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # image transform format
    def imageFormatTrans(self, imagePath, imageSavePath):
        # (filePath,tempfilename) = os.path.split(imagePath);
        tempName = imageSavePath.split('.')[-1]

        imageSavePath = imageSavePath.decode('utf-8')
        imagePath = imagePath.decode('utf-8')
        cmd = ffmpegPath + " -y -i " + imagePath + " -ac 1 -acodec libamr_nb \
        -ar 8000 -ab 12200 -s 176x144 -b 128 -r 15 " + imageSavePath
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # video transform format,can success but velocity lower
    def videoFormatTrans(self, videoPath, videoSavePath):
        videoPath = videoPath.decode('utf-8')
        videoSavePath = videoSavePath.decode('utf-8')
        filepath, filename = os.path.split(videoSavePath)
        cmd = ffmpegPath + " -i " + videoPath + " -max_muxing_queue_size 1024  -ab 128 -acodec libmp3lame -ac 1 -ar 22050 -r 29.97 -qscale 6 -y " + videoSavePath
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # transcribe Screen， success run
    def transcribeScreen(self, filePath):
        filePath = filePath.decode('utf-8')
        cmd = ffmpegPath + "  -f gdigrab -framerate 60 -offset_x 0 -offset_y 0 -video_size 1366x768 -i desktop " + filePath
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")

        subprocess.call(cmd, shell=True)

    # broadcast Video
    def broadcastVideo(self, filepath):
        filepath = filepath.decode('utf-8')
        cmd = ffplayPath + " " + filepath
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)  # use laptop camera broadcast screen,no try ;

    def cameraAddVideo(self, filepath):

        # ffmpeg -f dshow -i video="USB 2861 Device" -f dshow -i audio="线路 (3- USB Audio Device)" -vcodec libx264 -acodec aac -strict -2 mycamera.mkv
        filepath = filepath.decode('utf-8')

        cmd = ffmpegPath + " -f dshow -i video=" + "\"" + "Lenovo EasyCamera" + "\"" + " -f dshow \
-i audio=" + "\"" + "Mic in at front panel (black) (" + "\"" + " -vcodec libx264 -acodec aac -strict -2 " + filepath
        # cmd1=ffmpegPath + " -f dshow -i video=" +  "\"" + "Lenovo EasyCamera" + "\"" + " -f avi " + " -vcodec libx264 -acodec aac -strict -2 " + filepath
        # print cmd
        cmd = cmd.encode(sys.getfilesystemencoding())
        # cmd1=cmd1.encode(sys.getfilesystemencoding())

        if "?" in cmd:
            cmd = cmd.replace("?", "")
            # cmd1=cmd1.replace("?","")

        subprocess.call(cmd, shell=True)

    # get good Quality video ,can't run
    def getQualityVideo(self, videoPath, videoSavePath):

        videoPath = videoPath.decode('utf-8')
        videoSavePath = videoSavePath.decode('utf-8')
        filepath, filename = os.path.split(videoSavePath)
        cmd = ffmpegPath + " -i " + videoPath + " -target film-dvd -s 720x352 max_muxing_queue_size 1024 \
             -maxrate 7350000 -b 3700000 -sc_threshold 1000000000 \
             -trellis -cgop -g 12 -bf 2 -qblur 0.3 -qcomp 0.7 -dc 10 -mbd 2\
             -aspect 16:9 -pass 2 -an -f mpeg2video " + videoSavePath
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # audio format transform
    def audioTransFormat(self, filepath, filesavepath):

        filepath = filepath.decode('utf-8')
        filesavepath = filesavepath.decode('utf-8')
        cmd = ffmpegPath + " -i " + filepath + " " + filesavepath
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        subprocess.call(cmd, shell=True)

    # video add watermask
    def videoAddWatermask(self, videopath, waterpath, videosavepath):
        videopath = videopath.decode('utf-8')
        waterpath = waterpath.decode('utf-8')
        videosavepath = videosavepath.decode('utf-8')
        cmd1 = ffmpegPath + " -i " + videopath + " -i " + waterpath + " -filter_complex "
        cmd2 = '''" overlay=x=150:y=80 " '''
        cmd = cmd1 + cmd2 + videosavepath
        cmd = cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd = cmd.replace("?", "")
        print
        cmd

        subprocess.call(cmd, shell=True)


vp = CutSplicingVdeio()  # class instance


# videoStartTime = "00:00:0.0"
# videoEndTime = "00:00:8.0"
# videoSaveDir1=r"‪E:\animation\Wisp_03.mov"
# videoPath = r"‪E:\liucheng\emo\01.mp4"
# filePath=r"C:\Users\Administrator\Desktop\_HUDSence24.mov"
# imageSaveDir = r"\E:\liucheng\emo"
# fileName1 = r"D:\wu.jpg"
# print vp.instructions()#return class dercription


# vp.cutOutVideo(ffmpegPath,filePath,videoStartTime,videoEndTime,videoSaveDir)#according to video give a StartTime and  give a EndTime segmentation video;
# print vp.getVideoData(CurMediaPath)#return video dercription
# print
# vp.getVideoData(filePath)  # return video data
# vp.videoTransImage(videoPath,imageSaveDir)#according to give a video frames decomposition image
# vp.ImageTransVideo(imagePath,videoSaveDir)#according to give a Sequence frames composition video
# vp.cutVideoImage_resolution(videoPath,fileName,resolution)#according to give a resolution Screenshot(first key)
# vp.cutVideoImage_reAndTime(videoPath,fileName1,"520x520",12)#according to give a resolution and time Screenshot(give time key)
# vp.videoKeyRange_Gif(videoPath,fileName,keytime)#according to give a time composition front keytime key gif
# vp.imageFormatTrans("D:/1.jpg","C:/Users/Administrator/Desktop/root/text.png")#according to give a image format transform
# vp.videoFormatTrans(r"E:\my.avi",r"E:\001.avi")#according to give a video format transform
# vp.transcribeScreen(r"C:\Users\Administrator\Desktop\transcribe.avi")#according to give a video filepath (transcribe Screen)
# vp.broadcastVideo(videoSaveDir)##according to give a video filepath broadcast Video
# vp.cameraAddVideo(filePath)##according to give a video filepath laptop camera shooting video
# vp.audioTransFormat(filepath,filesavepath)##according to give  video filepath and filesavepath format transform

# vp.videoFormatTrans(filePath,r"E:\Wisp_03_3.mov")
filePath = r"E:\workSpace\Coding_SAM\sucai\EP001_SC007.mp4"
vp.cutVideoImage_reAndTime(filePath,r"E:\workSpace\Coding_SAM\sucai\cutThumbnail\EP001_SC007.png","512x512",2)
# vp.videoAddWatermask(r"‪E:\liucheng\emo\01.mp4",r"‪‪E:\liucheng\emo\tree.png",r"‪E:\liucheng\emo\01_1.mp4")



