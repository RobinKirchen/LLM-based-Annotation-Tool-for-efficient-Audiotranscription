from PyQt6.QtCore import Qt, QAbstractTableModel

#Defines a model to be used by QtTableView
# Needs to have the functions rowCount, columnCount, data
#

class TableModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
    
  def rowCount(self, parent=None):
    return len(self._data)
  
  def columnCount(self, parent=None):
    return len(self._data[0]) if self._data else 0
  
  #  roll parameter is required by the function call. see documentation
  def data(self, index, role = Qt.ItemDataRole.DisplayRole):
    if role == Qt.ItemDataRole.DisplayRole:
      return self._data[index.row()][index.column()]