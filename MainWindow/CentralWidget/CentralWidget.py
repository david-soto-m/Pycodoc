import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from ..glob_objects import globalxml as GXML

class centralWidget(QW.QWidget):
	def __init__(self):
		super().__init__()
		
		self.TabList=[]
		
		self.lastIdx=0
		
		self.defineLayout()
		self.tabAdder()
	
	def defineTabBar(self):
		TabBar=QW.QTabWidget()
		TabBar.setTabsClosable(True)
		TabBar.setCornerWidget(self.defineTabButton())
		TabBar.tabCloseRequested.connect(self.tabDestroyer)
		TabBar.currentChanged.connect(self.idxactualizer)
		TabBar.setAcceptDrops(True)
		return TabBar
	
	def defineTabButton(self):
		newTabButton=QW.QPushButton(QG.QIcon().fromTheme("tab-new"),"",self)
		newTabButton.clicked.connect(self.tabAdder)
		return newTabButton
	
	def idxactualizer(self,index):
		self.lastIdx=index
	
	def tabAdder(self,files=None):
		if type(files)==bool or files is None:
			self.TabList.append([None,"str"])
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(
					TextEditor(GXML.fileElement()), GXML.fileElement().title.text)
		elif type(files)==GXML.fileElement:
			self.TabList.append([files,None])
			pass
		
	def tabDestroyer(self,index=None):
		if  self.CwidLayout.itemAt(0).widget().count()>1:
			if index is not None:
				for idx in range(self.CwidLayout.count()):
					self.CwidLayout.itemAt(idx).widget().removeTab(index)
			else:
				self.tabDestroyer(self.lastIdx)
		else:
			QW.qApp.quit()

	def defineLayout(self):
		self.CwidLayout=QW.QHBoxLayout()
		self.setLayout(self.CwidLayout)
		self.CwidLayout.addWidget(self.defineTabBar())
	
	def split(self):
		self.CwidLayout.addWidget(self.defineTabBar())
		last=self.CwidLayout.count()-1
		for item in self.TabList:
			if item[0] is None:
				self.CwidLayout.itemAt(last).widget().addTab(
				TextEditor(GXML.fileElement()),GXML.fileElement().title.text)
			elif type(item[0])==GXML.fileElement:
				pass
	
	def unsplit(self):
		last=self.CwidLayout.count()-1
		if last>0:
			self.CwidLayout.itemAt(last).widget().hide()
			self.CwidLayout.removeItem(self.CwidLayout.itemAt(last))

class TextEditor(QW.QTextEdit):
	def __init__(self,files):
		super().__init__()
		self.setAcceptDrops(True)
		self.setReadOnly(True)
		if type(files) is GXML.fileElement:
			f = open(files.direc.text+files.name.text, 'r')
			with f:
				data = f.read()
				self.setText(data)
	def dragEnterEvent(self, e):
		if e.mimeData().hasUrls():
			print(e.mimeData().urls())
