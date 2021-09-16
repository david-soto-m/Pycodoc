from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon
from MainWindow.CentralWidget.CentralWidget import centralWidget
from MainWindow.ToolBar.ToolBar import toolBar
from MainWindow.MenuBar.MenuBar import MenuBar
from MainWindow.Shortcuts.Shortcuts import Shortcutter

class GuiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.defineCentralWidget()
		
		
		self.setWindowTitle("Pycobrowser")
		self.setWindowIcon(QIcon('AppIcon/AppIcon.svg'))
		
		self.defineMenuBar()
		
		self.defineToolBar()
		
		self.defineShortcuts()
		
		self.show()
		a=auxsz();
		a.toscalescreen(self,center=False,scale=1)
	
	def defineMenuBar(self):
		self.mnb=MenuBar(self)
		self.setMenuBar(self.mnb)
		
	def defineToolBar(self):
		self.tlb=toolBar(self)
		self.addToolBar(self.tlb)
	
	def defineCentralWidget(self):
		self.cwidg=centralWidget(self)
		self.setCentralWidget(self.cwidg)
	
	def defineShortcuts(self):
		self.shctobj=Shortcutter(self)

class auxsz():
	def toscalescreen(self,Widg,scale=0.2,center=0):
		'''Scale not -1 Gives the app the same aspect ratio as the screen, and allows to center the app'''
		if scale>0:
			soup=QDesktopWidget().availableGeometry()
			Widg.resize(int(soup.width()*scale),int(soup.height()*scale))
		if center:
			self.centerapp(Widg)
	def centerapp(self,Widg):
		'''centers resized apps'''
		soup=QDesktopWidget().availableGeometry().center()
		spoon=Widg.frameGeometry()
		Widg.move(int(soup.x()-spoon.width()/2),int(soup.y()-spoon.height()/2))
