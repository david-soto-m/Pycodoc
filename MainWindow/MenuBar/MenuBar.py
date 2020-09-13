import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from ..ToolBar import ToolBar as TB

class MenuBar():
	def __init__(self,parent):
		self.MenuBar=QW.QMenuBar(parent)
		
		self.exitAct = QW.QAction(QG.QIcon().fromTheme("application-exit"),'&Quit', parent)
		self.exitAct.triggered.connect(QW.qApp.quit)
		
		self.fileopener=TB.opener("&Open")
		
		fileMenu = self.MenuBar.addMenu('&File')
		fileMenu.addAction(self.exitAct)
		fileMenu.addAction(self.fileopener.openfile)
