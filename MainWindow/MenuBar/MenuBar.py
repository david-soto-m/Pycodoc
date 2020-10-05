import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import FileManage.FilesWidget as FW
from ..ToolBar import ToolBar as TB

class MenuBar():
	def __init__(self,parent):
		self.MenuBar=QW.QMenuBar(parent)
		
		fileMenu = self.MenuBar.addMenu('&File')
		
		#These (↓) actions are remembered in order to be accessed by shortcuts
		self.exitAct = QW.QAction(QG.QIcon().fromTheme("application-exit"),'&Quit', parent)
		self.exitAct.triggered.connect(QW.qApp.quit)
		
		self.fileopener=TB.opener(parent=parent,string="&Open")#DRY AF
		
		fileMenu.addAction(self.exitAct)
		fileMenu.addAction(self.fileopener)
		
		editMenu = self.MenuBar.addMenu('&Edit')
		
		self.editStyles=QW.QAction(QG.QIcon().fromTheme("color-management"),'&Manage Styles', parent)
		
		self.FilesManager=FW.FilesWidget()
		self.editFiles=QW.QAction(QG.QIcon().fromTheme("kt-queue-manager"),'&Manage Files', parent)
		self.editFiles.triggered.connect(self.FilesManager.showWind)
		
		editMenu.addAction(self.editFiles)
		editMenu.addAction(self.editStyles)
		
