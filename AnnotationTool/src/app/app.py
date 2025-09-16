import sys

from PyQt6.QtCore import QSize, Qt 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")
    self.setMinimumSize(400, 300)
    button = QPushButton("Click me")

    self.setCentralWidget(button)





app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
