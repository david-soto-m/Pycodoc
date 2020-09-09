import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from ..glob_objects import globalxml as GXML

class centralWidget(QW.QWidget):
	def __init__(self):
		super().__init__()
		
		self.lastIdx=0
		
		self.defineLayout()
		self.split()
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
	
	def tabAdder(self,files=True):
		if type(files)==bool:
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(TextEditor(self.CwidLayout.itemAt(idx).widget()),"Welcome")
		elif type(files)==GXML.fileElement:
			pass

	def tabDestroyer(self,index=None):
		if index is not None:
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().removeTab(index)
		else:
			self.tabDestroyer(self.lastIdx)

	def defineLayout(self):
		self.CwidLayout=QW.QHBoxLayout()
		self.setLayout(self.CwidLayout)
		self.CwidLayout.addWidget(self.defineTabBar())
	
	def split(self):
		self.CwidLayout.addWidget(self.defineTabBar())
	
class TextEditor(QW.QTextEdit):
	def __init__(self,parent=None,files=None):
		super().__init__(parent)
		self.setAcceptDrops(True)
		self.setReadOnly(True)
	def dragEnterEvent(self, e):
		if e.mimeData().hasUrls():
			e.accept()
			print("accepted")
		else:
			print("ignored")
			e.ignore()
