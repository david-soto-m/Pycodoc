import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import glob_objects.globalxml as GXML
from FileManage.fileElement import fileElement

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
		TabBar.setTabBarAutoHide (GXML.GConfigRoot.find("Behaviour/TabBarAutoHide").text not in ["Remain","remain","R","r"])
		return TabBar
	
	def defineTabButton(self):
		newTabButton=QW.QPushButton(QG.QIcon().fromTheme("tab-new"),"",self)
		newTabButton.clicked.connect(self.tabAdder)
		return newTabButton
	
	def idxactualizer(self,index):
		self.lastIdx=index
	
	def tabAdder(self,files=None):
		if type(files)==bool or files is None:
			self.TabList.append(None)
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(
					TextEditor(fileElement()),fileElement().title.text)
		elif type(files)==fileElement:
			self.TabList.append(files)
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(
					TextEditor(files), files.title.text)
		
	def tabDestroyer(self,index=None):
		if  self.CwidLayout.itemAt(0).widget().count()>1:
			if index is not None:
				for idx in range(self.CwidLayout.count()):
					self.CwidLayout.itemAt(idx).widget().removeTab(index)
				self.TabList.pop(index)
			else:
				self.tabDestroyer(self.lastIdx)
		elif self.CwidLayout.itemAt(0).widget().count()==1:
			Behave=GXML.GConfigRoot.find("Behaviour/LastTabRemoved").text
			if (Behave in ["Welcome","welcome","W","w"]):
				for idx in range(self.CwidLayout.count()):
					self.CwidLayout.itemAt(idx).widget().removeTab(0)
				self.TabList.pop(0)
				self.tabAdder()
			elif (Behave in ["None","none","N","n"]):
				for idx in range(self.CwidLayout.count()):
					self.CwidLayout.itemAt(idx).widget().removeTab(0)
				self.TabList.pop(0)
				pass
			elif (Behave in ["Persist","persist","P","p"]):
				pass
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
			if item is None:
				elem=fileElement()
				self.CwidLayout.itemAt(last).widget().addTab(TextEditor(elem),elem.title.text)
			elif type(item)==fileElement:
				self.CwidLayout.itemAt(last).widget().addTab(TextEditor(item),item.title.text)
	
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
		if type(files) is fileElement:
			f = open(files.direc.text+files.name.text, 'r')
			with f:
				data = f.read()
				self.setText(data)
	def dragEnterEvent(self, e):
		if e.mimeData().hasUrls():
			print(e.mimeData().urls())
