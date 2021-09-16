from glob_objects.globalxml import BehaviourRoot, filesRoot, styleLocsRoot
from PyQt5.QtWidgets import QWidget, QTabWidget, QInputDialog, QHBoxLayout, QMessageBox, qApp
from FileManage.fileElement import fileElement
from .TextEditor import TextEditor
from subprocess import check_output
class centralWidget(QWidget):
	def __init__(self,parent=None):
		super().__init__()
		self.parent=parent
		self.TabList=[]
		
		self.lastIdx=0
		
		self.currentStyle=None
		
		self.defineLayout()
		self.tabAdder(NoHist=True)
	
	def defineTabBar(self):
		TabBar=QTabWidget()
		TabBar.setTabsClosable(True)
		TabBar.tabCloseRequested.connect(self.tabDestroyer)
		TabBar.currentChanged.connect(self.idxactualizer)
		TabBar.setTabBarAutoHide (BehaviourRoot.find("TabBarAutoHide").text not in ["Remain","remain","R","r"])
		return TabBar
	
	def idxactualizer(self,index):
		self.lastIdx=index
	
	def tabAdder(self,files=None,NoHist=False,pandoc=False):
		if type(files)==bool or files is None:
			self.TabList.append(None)
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(TextEditor( fileElement(), self, NoHist, self.currentStyle), fileElement().title.text)
		elif type(files)==fileElement :
			if (BehaviourRoot.find("Pandoc").text in ["Yes", "yes", "Y", "y"] and
				not files.isFormat(".html")):
				boool=True
				if BehaviourRoot.find("Hpandoc").text in ["Shortcut","shortcut","S","s"] and not pandoc:
					boool=False
				if BehaviourRoot.find("Hpandoc").text in ["Popup","popup","P","p"]:
					mboxans=QMessageBox.question(self.parent,'Confirmation',
												'Do you want to see the html file',
												QMessageBox.Yes|QMessageBox.No,
												QMessageBox.Yes)
					boool=(mboxans==QMessageBox.Yes)
				if boool:
					phill=fileElement(files.htmlize())
					if not phill.isFile():
						res=check_output(["pandoc","-s",files.fileStrPath(),"-o",files.htmlize()])
					if not (BehaviourRoot.find("Hpandoc").text in["Create","create","C","c"]):
						files=fileElement(files.htmlize())
			self.TabList.append(files)
			
			if files.isUnique() and files.isFile():
				text,ok=QInputDialog.getText(self,'Title','Enter the title of:',text=files.title.text)
				if ok:
					files.title.text=str(text)
					filesRoot.append(files.createFileElement())
					self.parent.tlb.combosearch.searchMenu()
			for idx in range(self.CwidLayout.count()):
				self.CwidLayout.itemAt(idx).widget().addTab(TextEditor( files, self, NoHist, self.currentStyle), files.title.text)
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
			Behave=BehaviourRoot.find("LastTabRemoved").text
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
				pass #Not a mistake!!
			else:
				qApp.quit()
	
	def pandocize(self):
		files=self.TabList[self.lastIdx]
		if (BehaviourRoot.find("Hpandoc").text in ["Shortcut","shortcut","S","s"] and
			BehaviourRoot.find("Pandoc").text in ["Yes", "yes", "Y", "y"] and 
			not files.isFormat(".html")):
			self.tabAdder(files,pandoc=True)
	
	def stylize(self,styleFile):
		if styleFile is not None and styleFile.isUnique():
			text,ok=QInputDialog.getText(self,'Title','Enter the title of:',text=styleFile.title.text)
			if ok:
				styleFile.title.text=str(text)
				styleLocsRoot.append(styleFile.createFileElement())
		self.currentStyle=styleFile
		for idx in range(self.CwidLayout.count()):
			for  tabidx in range(self.CwidLayout.itemAt(idx).widget().count()):
				self.CwidLayout.itemAt(idx).widget().widget(tabidx).stylize(styleFile)
	
	def defineLayout(self):
		self.CwidLayout=QHBoxLayout()
		self.setLayout(self.CwidLayout)
		self.CwidLayout.addWidget(self.defineTabBar())
	
	def split(self):
		self.CwidLayout.addWidget(self.defineTabBar())
		last=self.CwidLayout.count()-1
		for item in self.TabList:
			if item is None:
				elem=fileElement()
				self.CwidLayout.itemAt(last).widget().addTab(TextEditor(elem, self, True, self.currentStyle), elem.title.text)
			elif type(item)==fileElement:
				self.CwidLayout.itemAt(last).widget().addTab(TextEditor(item, self, True, self.currentStyle), item.title.text)
	
	def unsplit(self):
		last=self.CwidLayout.count()-1
		if last>0:
			self.CwidLayout.itemAt(last).widget().hide()
			self.CwidLayout.removeItem(self.CwidLayout.itemAt(last))

