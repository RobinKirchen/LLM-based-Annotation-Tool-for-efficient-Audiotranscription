import sys
import whisper
from tableModel import TableModel
from PyQt6.QtCore import QSize, Qt, QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QTableView
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.initUI()

  def initUI(self):
    self.setWindowTitle("QFileDialog Example")
    self.setGeometry(600, 200, 800, 600)
    centralWidget = QWidget()
    
    #Layout variable to easily change layouts later on when I try to design a good looking front end
    centralLayout = QVBoxLayout()
    centralWidget.setLayout(centralLayout)
    #set a Widget into the main window to create a custom layout cauze you cannot override the main window layout
    self.setCentralWidget(centralWidget)

    #Video Player
    self.videoWidget = QVideoWidget()

    #set stretch=1 so player keeps its original size otherwise layout prioritizes equal spacing
    centralLayout.addWidget(self.videoWidget, stretch=1)

    #Audio Player
    self.audio_output = QAudioOutput()
    player = QMediaPlayer()
    player.setAudioOutput(self.audio_output)
    player.setVideoOutput(self.videoWidget)
    self.player = player

    #control Bar for player
    #TODO's: 
    # add interactive progress bar
    # add rewind and fast forward buttons with set intervalls (e.g skipp 5s on use)
    # change play and pause into a single button. This can be achieved by checking self.player.playbackState() 
    # (current state of the player) and compare it to QMediaPlayer.PlaybackState.PlayingState to check if the player is in play state      
    # change buttons to display icons instead of text
    videoControls = QWidget(parent=centralWidget)
    videoControlsLayout = QHBoxLayout()
    videoControls.setLayout(videoControlsLayout)
    centralLayout.addWidget(videoControls)

    #Play Button
    playButton = QPushButton("Play",parent=videoControls)
    playButton.setFixedSize(60,25)
    videoControlsLayout.addWidget(playButton)
    playButton.clicked.connect(self.player.play)
    
    #Pause Button
    pauseButton = QPushButton("Pause",parent=videoControls)
    pauseButton.setFixedSize(60,25)
    videoControlsLayout.addWidget(pauseButton)
    pauseButton.clicked.connect(self.player.pause)
    
    #Button to open File explorer
    self.button = QPushButton("Open File", self)
    self.button.setGeometry(150, 150, 100, 30)
    centralLayout.addWidget(self.button)
    
    self.button.clicked.connect(self.openFileDialog)
    
    self.button = QPushButton("Generate", self)
    self.button.setGeometry(150, 150, 100, 30)
    centralLayout.addWidget(self.button)
    self.button.clicked.connect(self.generateTranscript)
    
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
      self.current_file = selected_files[0]
      print("FIle:", selected_files[0])
  
  def fillTable(self,data):
    model = TableModel(data)
    #Non local variable cauze table content will be changed later on
    self.results = QTableView()
    self.results.setModel(model)
    self.centralWidget().layout().addWidget(self.results)
  
         
  def generateTranscript(self):
    #File not found error due to ffmpeg not being installed
    # -> TODO done: install ffmpeg on windows. Set environment variable
    model = whisper.load_model("turbo")
    print(self.current_file)
    result = model.transcribe(self.current_file)
    content = result["segments"]
    data = []
    for entry in content:
      data.append([entry["text"], entry["start"], entry["end"]])
    print(data)
    self.fillTable(data)


app = QApplication(sys.argv)

# Create a Qt widget, which will be the main window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


