import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

class ToolBar():
	def __init__(self,parent):
		
		self.toolBar=QW.QToolBar(parent)
		self.qacts=backnextact()
		
		self.combosearch=searchWidg()
		
		self.toolBar.addAction(self.qacts.back)
		self.toolBar.addAction(self.qacts.ahead)

class backnextact():
	def __init__(self):
		self.back=QW.QAction()
		self.back.setIcon(QG.QIcon().fromTheme("go-previous"))
		self.back.setToolTip('Back')
		
		self.ahead=QW.QAction()
		self.ahead.setIcon(QG.QIcon().fromTheme("go-next"))
		self.ahead.setToolTip("Forward")

class searchWidg():
	def __init__(self):
		pass
