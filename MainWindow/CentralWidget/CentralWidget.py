import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

class centralWidget(QW.QWidget):
	def __init__(self):
		super().__init__()
		self.defineLayout()
		self.split()
		self.emptyTabAdder(False)
		
	def defineTabBar(self):
		TabBar=QW.QTabWidget()
		TabBar.setTabsClosable(True)
		TabBar.setCornerWidget(self.defineTabButton())
		TabBar.tabCloseRequested.connect(self.tabDestroyer)
		return TabBar
	
	def defineTabButton(self):
		newTabButton=QW.QPushButton(QG.QIcon().fromTheme("tab-new"),"",self)
		newTabButton.clicked.connect(self.emptyTabAdder)
		return newTabButton
	
	def emptyTabAdder(self,pushed):
		for idx in range(self.CwidLayout.count()):
			self.CwidLayout.itemAt(idx).widget().addTab(QW.QTextEdit(),"tab")
	
	def tabAdder(self,filer):
		pass
	
	def tabDestroyer(self,index=None):
		if index is not None:
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().removeTab(index)
		else
			pass
	
	def defineLayout(self):
		self.CwidLayout=QW.QHBoxLayout()
		self.setLayout(self.CwidLayout)
		self.CwidLayout.addWidget(self.defineTabBar())
	
	def split(self):
		self.CwidLayout.addWidget(self.defineTabBar())
	
