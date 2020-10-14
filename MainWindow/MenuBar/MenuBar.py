import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from AuxWindows.FilesWidget import FilesWidget
from  AuxWindows.SettingsWidget import SettingsWidget
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
		
		editMenu = self.MenuBar.addMenu('&Settings')
		
		self.StylesManager=FilesWidget(parent,style=True)
		self.editStyles=QW.QAction(QG.QIcon().fromTheme("color-management"),'&Configure Style Files', parent)
		self.editStyles.triggered.connect(self.StylesManager.showWind)
		
		self.FilesManager=FilesWidget(parent)
		self.editFiles=QW.QAction(QG.QIcon().fromTheme("kt-queue-manager"),'&Configure Files', parent)
		self.editFiles.triggered.connect(self.FilesManager.showWind)
		
		self.settingsManager=SettingsWidget(parent)
		self.editSettings=QW.QAction(QG.QIcon().fromTheme("settings-configure"),'&Configure Pycodoc', parent)
		self.editSettings.triggered.connect(self.settingsManager.showWid)
		
		editMenu.addAction(self.editFiles)
		editMenu.addAction(self.editStyles)
		editMenu.addAction(self.editSettings)
