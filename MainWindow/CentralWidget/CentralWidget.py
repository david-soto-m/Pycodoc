import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import glob_objects.globalxml as GXML
from FileManage.fileElement import fileElement
from pathlib import Path

class centralWidget(QW.QWidget):
	def __init__(self):
		super().__init__()
		
		self.TabList=[]
		
		self.lastIdx=0
		
		self.currentStyle=None
		
		self.defineLayout()
		self.tabAdder(NoHist=True)
	
	def defineTabBar(self):
		TabBar=QW.QTabWidget()
		TabBar.setTabsClosable(True)
		TabBar.tabCloseRequested.connect(self.tabDestroyer)
		TabBar.currentChanged.connect(self.idxactualizer)
		TabBar.setTabBarAutoHide (GXML.GConfigRoot.find("Behaviour/TabBarAutoHide").text not in ["Remain","remain","R","r"])
		return TabBar
	
	def idxactualizer(self,index):
		self.lastIdx=index
	
	def tabAdder(self,files=None,NoHist=False):
		if type(files)==bool or files is None:
			self.TabList.append(None)
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(TextEditor(fileElement(),self,NoHist,self.currentStyle), fileElement().title.text)
		elif type(files)==fileElement:
			self.TabList.append(files)
			if files.isUnique():
				pass
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(TextEditor(files,self,NoHist,self.currentStyle), files.title.text)
			self.CwidLayout.itemAt(0).widget().setCurrentIndex(len(self.TabList)-1)
		
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
			elif (Behave in ["Persist","persist","P","p"]):
				pass #Not an error!!
			else:
				QW.qApp.quit()
	def stylize(self,styleFile):
		if styleFile is not None and styleFile.isUnique():
			pass
		self.currentStyle=styleFile
		for idx in range(self.CwidLayout.count()):
			for  tabidx in range(self.CwidLayout.itemAt(idx).widget().count()):
				self.CwidLayout.itemAt(idx).widget().widget(tabidx).stylize(styleFile)
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
				self.CwidLayout.itemAt(last).widget().addTab(TextEditor(elem,self,True),elem.title.text)
			elif type(item)==fileElement:
				self.CwidLayout.itemAt(last).widget().addTab(TextEditor(item,self,True),item.title.text)
	
	def unsplit(self):
		last=self.CwidLayout.count()-1
		if last>0:
			self.CwidLayout.itemAt(last).widget().hide()
			self.CwidLayout.removeItem(self.CwidLayout.itemAt(last))

class TextEditor(QW.QTextBrowser):
	def __init__(self,files,papa,NoHist,styleFile=None):
		super().__init__(),
		self.parent=papa
		self.setAcceptDrops(True)
		self.setReadOnly(GXML.GConfigRoot.find("Behaviour/AllowEdits") not in ["Yes","yes","Y","y"])
		if files.isFile():
			with open(files.fileStrPath(), 'r') as f:
				data = f.read()
				self.setText(data)
			if not NoHist:
				GXML.histRoot.insert(0,files.createHistElement())
				while len(list(GXML.histRoot))>int(GXML.GConfigRoot.find("History/Max").text)>-1:
					GXML.histRoot.remove(GXML.histRoot.find("Elem[last()]"))
		else :
			errfile=GXML.filesRoot.find("Elem[@error='True']")
			if errfile is not None and errfile:
				files=fileElement(errfile)
			else:
				files=fileElement()
			if files.isFile():
				with open(files.fileStrPath(), 'r') as f:
					data = f.read()
					self.setText(data)
		self.stylize(styleFile)
	
	def stylize(self,styleFile):
		if styleFile is not None and styleFile.isstyle():
			with open(styleFile.fileStrPath(), 'r') as f:
				data = f.read()
				self.setStyleSheet(data)
		else:
			self.setStyleSheet('')
	
	def dragEnterEvent(self, e):
		if e.mimeData().hasUrls():
			e.accept()
		else:
			e.ignore()
	
	def dragMoveEvent(self,evie):
		pass
		#I don't have the slightest idea why but it doesn't work without the event override.
		#Maybe the implementation cancels the event by default, but that is quite messed up.
	
	def dropEvent(self,e):
		for url in e.mimeData().urls():
			if Path(url.path()).is_file():
				fielem=fileElement(url.path())
				self.parent.tabAdder(fielem)
