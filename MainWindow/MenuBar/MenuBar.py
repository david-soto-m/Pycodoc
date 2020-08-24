import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

class MenuBar():
	def __init__(self,parent):
		self.MenuBar=QW.QMenuBar(parent)
		
		exitAct = QW.QAction(QG.QIcon().fromTheme("application-exit"),'&Quit', parent)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(QW.qApp.quit)
		
		fileMenu = self.MenuBar.addMenu('&File')
		fileMenu.addAction(exitAct)
