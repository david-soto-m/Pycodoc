import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from AuxWindows.FilesWidget import FilesWidget
from  AuxWindows.BehaviourWidget import BehaviourWidget
from  AuxWindows.ShortcutsWidget import ShortcutsWidget
from ..ToolBar import ToolBar as TB

class MenuBar(QW.QMenuBar):
	def __init__(self,parent):
		super().__init__(parent)
		fileMenu = self.addMenu('&File')
		
		#These (↓) actions are remembered in order to be accessed by shortcuts
		self.exitAct = QW.QAction(QG.QIcon().fromTheme("application-exit"),'Quit', parent)
		self.exitAct.triggered.connect(QW.qApp.quit)
		
		self.fileopener=TB.opener(parent=parent,string="Open")#DRY AF
		
		fileMenu.addAction(self.exitAct)
		fileMenu.addAction(self.fileopener)
		
		settingsMenu = self.addMenu('&Settings')
		
		self.FilesManager=FilesWidget(parent)
		self.editFiles=QW.QAction(QG.QIcon().fromTheme("kt-queue-manager"),'Configure Files', parent)
		self.editFiles.triggered.connect(self.FilesManager.showWind)
		
		self.StylesManager=FilesWidget(parent,style=True)
		self.editStyles=QW.QAction(QG.QIcon().fromTheme("color-management"),'Configure Style Files', parent)
		self.editStyles.triggered.connect(self.StylesManager.showWind)
		
		self.shortcutsManager=ShortcutsWidget(parent)
		self.shortcutSettings=QW.QAction(QG.QIcon().fromTheme("configure-shortcuts"),'Configure Shortcuts', parent)
		self.shortcutSettings.triggered.connect(self.shortcutsManager.showWid)
		
		self.behaviourManager=BehaviourWidget(parent)
		self.behaviourSettings=QW.QAction(QG.QIcon().fromTheme("settings-configure"),'Configure Pycodoc', parent)
		self.behaviourSettings.triggered.connect(self.behaviourManager.showWid)
		
		
		settingsMenu.addAction(self.editFiles)
		settingsMenu.addAction(self.editStyles)
		settingsMenu.addSeparator()
		settingsMenu.addAction(self.shortcutSettings)
		settingsMenu.addAction(self.behaviourSettings)
