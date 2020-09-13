import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import MainWindow.CentralWidget.CentralWidget as CW
import MainWindow.ToolBar.ToolBar as TB
import MainWindow.MenuBar.MenuBar as MB

class GuiApp(QW.QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.defineCentralWidget()
		
		self.defineTitleBar()
		self.defineMenuBar()
		
		self.defineToolBar()
		
		self.defineShortcuts()
		
		self.show()
		a=auxsz();
		a.toscalescreen(self,center=True)
	
	def defineTitleBar(self):
		self.setWindowTitle("Pycobrowser")
		self.setWindowIcon(QG.QIcon('AppIcon/AppIcon.svg'))
	
	def defineMenuBar(self):
		self.mnb=MB.MenuBar(self)
		self.setMenuBar(self.mnb.MenuBar)
		
	def defineToolBar(self):
		self.tlb=TB.ToolBar(self)
		self.addToolBar(self.tlb.toolBar)
	
	def defineCentralWidget(self):
		self.cwidg=CW.centralWidget()
		self.setCentralWidget(self.cwidg)
	
	def defineShortcuts(self):
		self.shcts=[]
		
		self.shcts.append(QW.QShortcut("Ctrl+W",self))
		self.shcts[len(self.shcts)-1].activated.connect(self.cwidg.tabDestroyer)
		
		self.shcts.append(QW.QShortcut("Ctrl+Q",self))
		self.shcts[len(self.shcts)-1].activated.connect(self.mnb.exitAct.trigger)
		
		self.shcts.append(QW.QShortcut("Ctrl+O",self))
		self.shcts[len(self.shcts)-1].activated.connect(self.tlb.fileopener.openfile.trigger)

class auxsz():
	def toscalescreen(self,Widg,scale=0.2,center=0):
		'''Scale not -1 Gives the app the same aspect ratio as the screen, and allows to center the app'''
		if scale>0:
			soup=QW.QDesktopWidget().availableGeometry()
			Widg.resize(int(soup.width()*scale),int(soup.height()*scale))
		if center:
			self.centerapp(Widg)
	def centerapp(self,Widg):
		'''centers resized apps'''
		soup=QW.QDesktopWidget().availableGeometry().center()
		spoon=Widg.frameGeometry()
		Widg.move(int(soup.x()-spoon.width()/2),int(soup.y()-spoon.height()/2))
