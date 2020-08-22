import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import centwidg as CW

class GuiApp(QW.QMainWindow):
	def __init__(self):
		super().__init__()
		self.defineMenuBar()
		self.setWindowIcon(QG.QIcon('AppIcon/AppIcon.svg'))
		self.cwidg=CW.centralWidget()
		self.setCentralWidget(self.cwidg)
		self.show()
		a=auxsz();
		a.toscalescreen(self,center=1)
	def defineMenuBar(self):
		exitAct = QW.QAction(QG.QIcon().fromTheme("application-exit"),'&Quit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct
		exitAct.triggered.connect(QW.qApp.quit)
		fileMenu = self.menuBar().addMenu('&File')
		fileMenu.addAction(exitAct)

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
