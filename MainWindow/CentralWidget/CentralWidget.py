import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

class centralWidget(QW.QWidget):
	def __init__(self):
		super().__init__()
		self.defineTabBar()
	
	def defineTabBar(self):
		self.tabBar=QW.QTabWidget()
		self.tabBar.setCornerWidget(self.defineTabButton())
		for i in range(4):
			self.tabBar.addTab(QW.QTextEdit(),"tab"+str(i))
	
	def defineTabButton(self):
		newTabButton=QW.QPushButton(QG.QIcon().fromTheme("tab-new"),"",self)
		newTabButton.clicked.connect(self.tabAdder)
		return newTabButton
	
	def tabAdder(self,pushed):
		self.tabBar.addTab(QW.QTextEdit(),"added tab")
