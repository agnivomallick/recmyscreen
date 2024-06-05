from ui_recmyscreen import Ui_MainWindow  # import UI file
from PySide6.QtWidgets import *  # import PySide6's Qt Widgets
from PySide6.QtGui import QIcon  # import the Icon handler for PySide6
from PySide6.QtCore import QSize # import for sizing Icons
import resources.resources_rc  # I used resources. This resources_rc file is required for using the resources in resources folder

import pyscreenrec as psr  # pyscreenrec, screen recorder
import os  # os python package (already present in the standard library)


# ONLY WORKS ON WINDOWS. For changing the taskbar icon to the app icon.
try:
    from ctypes import windll
    
    appid="mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    
except ImportError:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        icon = QIcon()
        icon.addFile(u":/icons/video_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # add icon
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # adding the UI to the app
        
        self.setFixedSize(590, 562)  # no resizing
        
        self.ui.playbtn.clicked.connect(self.start_rec)  # adding event handler to play button
        self.ui.pausebtn.clicked.connect(self.pause_rec)  # adding event handler to pause button
        self.ui.stopbtn.clicked.connect(self.stop_rec)  # adding event handler to stop button
        
        
    def start_rec(self):
       
        """
        Starts the recording.
        
        Opens a file dialog and starts the recording.
        Saves it in the file in the file dialog.
        """
        
        global rec_manager  # need to use function-wide, so global.
        
        rec_manager = psr.ScreenRecorder()  # initialize with ScreenRecorder object
        
        file, _ = QFileDialog.getSaveFileName(self, 'Save file', os.getcwd(), "Video files (*.mp4)")
        # filedialog
        
        # If file is "" (none) then do nothing
        # else start the recording with the video file as a parameter.
        if file == '':
            return
        else:
            self.is_rec_started = True  # is rec started.
            
            rec_manager.start_recording(file)
            self.ui.pausebtn.setDisabled(False)   # enable pause, stop and disable play.
            self.ui.stopbtn.setDisabled(False)
            self.ui.playbtn.setDisabled(True)
            
            self.is_playing=True  # is playing will be set to yes.
            
            
    def pause_rec(self):
        
        """
        Pauses the screen recording.
        Checks is is playing variable is True or not.
        
        if True then it pauses and changes icon to play.
        else it starts to play.
        """
        if self.is_playing:
            rec_manager.pause_recording()
            
            icon_play = QIcon()
            icon_play.addFile(u":/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pausebtn.setIcon(icon_play)
            
            self.is_playing = False
          
        else:
            rec_manager.resume_recording()
            icon_pause = QIcon()
            icon_pause.addFile(u":/images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pausebtn.setIcon(icon_pause)

            self.is_playing = True
         
            
    def stop_rec(self):
        
        """
        Stops the recording and saves the file.
        Reverts the buttons to default config.
        """
        if self.is_rec_started:
            rec_manager.stop_recording()
            
            
            self.ui.pausebtn.setDisabled(True)
            self.ui.stopbtn.setDisabled(True)
            
            self.ui.playbtn.setEnabled(True)
            self.is_rec_started = False
            
         

    


     
        
if __name__=="__main__":
    app = QApplication()
    win=MainWindow()
    win.show()
    app.exec()