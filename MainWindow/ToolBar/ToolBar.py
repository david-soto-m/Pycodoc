import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import glob_objects.globalxml as GXML
from pathlib import Path
from FileManage.fileElement import fileElement

class ToolBar():
	def __init__(self,parent):
		
		self.toolBar=QW.QToolBar(parent)
		
		self.histmen=historystuff(parent)
		self.fileopener=opener(parent)
		self.combosearch=searchWidg(parent)
		self.spliter=splitButton(parent)
		self.styler=styleButton(parent)
		
		self.toolBar.addAction(self.histmen)
		self.toolBar.addAction(self.styler)
		self.toolBar.addAction(self.spliter.split)
		self.toolBar.addAction(self.spliter.unsplit)
		self.toolBar.addAction(self.fileopener)
		self.toolBar.addWidget(self.combosearch)

class opener(QW.QAction):
	def __init__(self,parent,string=None):
		super().__init__()
		self.parent=parent
		self.setIcon(QG.QIcon().fromTheme("document-open"))
		self.setToolTip("Open a file")
		self.triggered.connect(self.OpenWidget)
		if type(string) is str:
			self.setText(string)
	
	def OpenWidget(self):
		home_dir = str(Path.home())
		fname = QW.QFileDialog.getOpenFileNames(caption='Open file',directory=home_dir)
		if fname[0]:
			for each in fname[0]:
				if Path(each).is_file():
					fielem=fileElement(each)
					self.parent.cwidg.tabAdder(fielem)

class historystuff(QW.QAction):
	def __init__(self,parent):
		super().__init__()
		self.counter=0
		self.parent=parent
		self.setIcon(QG.QIcon().fromTheme("shallow-history"))
		self.setToolTip("History")
		self.setMenu(self.histMenu())
		self.hovered.connect(self.refreshMenu)
		self.triggered.connect(self.triggerlast)
		
	def refreshMenu(self):
		self.counter=0
		self.setMenu(self.histMenu())
	
	def histMenu(self):
		self.actions=[]
		Menu=QW.QMenu()
		for child,index in zip(GXML.histRoot,range(len(GXML.histRoot))):
			Elem=fileElement(child)
			self.actions.append(QW.QAction(Elem.title.text))
			self.actions[index].setData(Elem)
			self.actions[index].triggered.connect(self.trigger)
			Menu.addAction(self.actions[index])
		return Menu
	
	def triggerlast(self,boolean=False):
		self.counter+=1
		if self.counter>int(GXML.GConfigRoot.find("History/Max").text):
			self.counter=1
		File=fileElement(GXML.histRoot.find("Elem"+"["+str(self.counter)+"]"))
		self.parent.cwidg.tabAdder(File,NoHist=True)
	
	def trigger(self,boolean=False):
		File=self.sender().data()
		self.parent.cwidg.tabAdder(File)

class styleButton(QW.QAction):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
		self.setIcon(QG.QIcon().fromTheme("text-style"))
		self.setToolTip("Style")
		self.setMenu(self.styleMenu())
		self.hovered.connect(self.refreshMenu)
		self.triggered.connect(self.triggerOpen)
		
	def refreshMenu(self):
		self.setMenu(self.styleMenu())
	
	def styleMenu(self):
		self.actions=[]
		Menu=QW.QMenu()
		for child,index in zip(GXML.styleLocsRoot.findall("Elem[@show='True']"),range(len(GXML.styleLocsRoot))):
			Elem=fileElement(child,style=True)
			self.actions.append(QW.QAction(Elem.title.text))
			self.actions[index].setData(Elem)
			self.actions[index].triggered.connect(self.trigger)
			Menu.addAction(self.actions[index])
		index=len(self.actions)
		self.actions.append(QW.QAction('Base'))
		self.actions[index].setData(None)
		self.actions[index].triggered.connect(self.trigger)
		Menu.addAction(self.actions[index])
		#index=len(self.actions)
		#self.actions.append(QW.QAction('Create new'))
		#self.actions[index].triggered.connect()
		#Menu.addAction(self.actions[index])
		return Menu
	def triggerOpen(self,boolean):
		print("here")
		home_dir=str(Path.home())
		fname=QW.QFileDialog.getOpenFileNames(caption='Open file',directory=home_dir)
		if fname[0]:
			for each in fname[0]:
				if Path(each).is_file() and Path(each).is_file():
					styleElem=fileElement(each,style=True)
					self.parent.cwidg.stylize(styleElem)
	def trigger(self,boolean):
		styleElem=self.sender().data()
		self.parent.cwidg.stylize(styleElem)

class searchWidg(QW.QComboBox):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
		expand=QW.QSizePolicy().Policy.Expanding
		self.setSizePolicy(expand,expand)
		self.searchMenu()
		self.setCurrentIndex(-1)
	
	def searchMenu(self):
		self.clear()
		self.setAcceptDrops(True)
		self.setEditable(True)
		self.activated.connect(self.comboChanged)
		
		self.Elem=[]
		for child in GXML.filesRoot.findall("Elem[@show='True']"):
			self.Elem.append(fileElement(child))
		self.Elem.sort(key=lambda indiv: indiv.fileStrPath())
		for item in self.Elem:
			self.addItem(item.title.text, QC.QVariant(item))
		self.setMaxVisibleItems(len(self.Elem))

	def comboChanged(self,idx):
		fielem=self.itemData(idx,0x100)
		if fielem is not None:
			self.parent.cwidg.tabAdder(fielem)
		else:
			fielem=fileElement(self.itemText(idx))
			self.parent.cwidg.tabAdder(fielem)

class splitButton():
	def __init__(self,parent):
		self.split=QW.QAction(parent)
		self.split.setIcon(QG.QIcon().fromTheme("view-split-effect"))
		self.split.setToolTip('Split')
		self.split.triggered.connect(parent.cwidg.split)
		
		self.unsplit=QW.QAction(parent)
		self.unsplit.setIcon(QG.QIcon().fromTheme("view-unsplit-effect"))
		self.unsplit.setToolTip('Split')
		self.unsplit.triggered.connect(parent.cwidg.unsplit)
