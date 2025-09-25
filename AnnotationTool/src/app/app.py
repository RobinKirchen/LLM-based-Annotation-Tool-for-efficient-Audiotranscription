import sys

from PyQt6.QtCore import QSize, Qt, QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget, QVBoxLayout
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.initUI()

  def initUI(self):
      self.setWindowTitle("QFileDialog Example")
      self.setGeometry(100, 100, 400, 300)
      centralWidget = QWidget()
      
      #Layout variable to easily change layouts later on when I try to design a good looking front end
      layout = QVBoxLayout()
      centralWidget.setLayout(layout)
      #set a Widget into the main window to create a custom layout cauze you cannot override the main window layout
      self.setCentralWidget(centralWidget)

      #Video Player 
      self.videoWidget = QVideoWidget()
      layout.addWidget(self.videoWidget)

      #Audio Player
      self.audio_output = QAudioOutput()
      player = QMediaPlayer()
      player.setAudioOutput(self.audio_output)
      player.setVideoOutput(self.videoWidget)
      self.player = player

      #Button to open File explorer
      self.button = QPushButton("Open File", self)
      self.button.setGeometry(150, 150, 100, 30)
      layout.addWidget(self.button)

      file = self.button.clicked.connect(self.openFileDialog)    
  
  
  #TODO: add filter for file types so that only audio/video files can be selected
  def openFileDialog(self):
      file_dialog = QFileDialog(self)
      file_dialog.setWindowTitle("Open File")
      file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
      file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

      if file_dialog.exec():
         selected_files = file_dialog.selectedFiles()
         print("Selected File:", selected_files[0])
         self.player.setSource(QUrl.fromLocalFile(selected_files[0]))
         self.player.play()




app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
