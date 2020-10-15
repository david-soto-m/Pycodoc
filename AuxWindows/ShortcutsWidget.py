import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import glob_objects.globalxml as GXML
import xml.etree.ElementTree as ET
from FileManage.fileElement import fileElement 

class ShortcutsWidget (QW.QWidget):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
		lbl=QW.QLabel("Idiot")
		h1=QW.QHBoxLayout()
		h1.addWidget(lbl)
		self.setLayout(h1)
	def showWid(self):
		self.show()
 
