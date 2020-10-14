import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import glob_objects.globalxml as GXML
import xml.etree.ElementTree as ET
from FileManage.fileElement import fileElement 

class SettingsWidget (QW.QWidget):
	def __init__(self, parent=None):
		super().__init__()
		self.parent=parent
	def showWid(self):
		
		pass
