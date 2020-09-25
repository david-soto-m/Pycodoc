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
		self.styler=cssButton(parent)
		
		self.toolBar.addAction(self.histmen.hist)
		self.toolBar.addAction(self.styler.style)
		self.toolBar.addAction(self.spliter.split)
		self.toolBar.addAction(self.spliter.unsplit)
		self.toolBar.addAction(self.fileopener.openfile)
		self.toolBar.addWidget(self.combosearch.swid)

class opener():
	def __init__(self,parent,string=None):
		self.parent=parent
		self.openfile=QW.QAction()
		self.openfile.setIcon(QG.QIcon().fromTheme("document-open"))
		self.openfile.setToolTip("Open a file")
		self.openfile.triggered.connect(self.OpenWidget)
		
		if type(string) is str:
			self.openfile.setText(string)
	def OpenWidget(self):
		home_dir = str(Path.home())
		fname = QW.QFileDialog.getOpenFileNames(caption='Open file',directory=home_dir)
		if fname[0]:
			for each in fname[0]:
				if Path(each).is_file():
					fielem=fileElement(each)
					self.parent.cwidg.tabAdder(fielem)

class historystuff(QW.QWidget):
	def __init__(self,parent):
		super().__init__()
		self.counter=0
		self.parent=parent
		self.hist=QW.QAction()
		self.hist.setIcon(QG.QIcon().fromTheme("shallow-history"))
		self.hist.setToolTip("History")
		self.hist.setMenu(self.histMenu())
		self.hist.hovered.connect(self.refreshMenu)
		self.hist.triggered.connect(self.triggerlast)
		
	def refreshMenu(self):
		self.counter=0
		self.hist.setMenu(self.histMenu())
	
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
	
	def triggerlast(self,boolean):
		self.counter+=1
		if self.counter>int(GXML.GConfigRoot.find("History/Max").text):
			self.counter=1
		File=fileElement(GXML.histRoot.find("Elem"+"["+str(self.counter)+"]"))
		self.parent.cwidg.tabAdder(File,NoHist=True)
	
	def trigger(self,boolean):
		File=self.sender().data()
		self.parent.cwidg.tabAdder(File)

class searchWidg():
	def __init__(self,parent):
		self.parent=parent
		self.swid=QW.QComboBox()
		self.swid.setEditable(True)
		self.swid.activated.connect(self.comboChanged)
		expand=QW.QSizePolicy().Policy.Expanding
		self.swid.setSizePolicy(expand,expand)
		self.Elem=[]
		for child in GXML.filesRoot.findall("Elem[@show='True']"):
			self.Elem.append(fileElement(child))
			self.swid.addItem(self.Elem[len(self.Elem)-1].title.text, QC.QVariant(self.Elem[len(self.Elem)-1]))
		self.swid.setCurrentIndex(-1)
	
	def comboChanged(self,idx):
		fielem=self.swid.itemData(idx,0x100)
		if fielem is not None:
			self.parent.cwidg.tabAdder(fielem)
		else:
			fielem=fileElement(self.swid.itemText(idx))
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
class cssButton(QW.QWidget):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
		self.style=QW.QAction()
		self.style.setIcon(QG.QIcon().fromTheme("text-css"))
		self.style.setToolTip("Style")
		self.style.setMenu(self.styleMenu())
		self.style.hovered.connect(self.refreshMenu)
		self.style.triggered.connect(self.triggerOpen)
		
	def refreshMenu(self):
		self.style.setMenu(self.styleMenu())
	
	def styleMenu(self):
		self.actions=[]
		Menu=QW.QMenu()
		for child,index in zip(GXML.cssLocsRoot.findall("Elem[@show='True']"),range(len(GXML.cssLocsRoot))):
			Elem=fileElement(child)
			self.actions.append(QW.QAction(Elem.title.text))
			self.actions[index].setData(Elem)
			self.actions[index].triggered.connect(self.trigger)
			Menu.addAction(self.actions[index])
		return Menu
	def triggerOpen(self,boolean):
		pass
	
	def trigger(self,boolean):
		File=self.sender().data()
		#self.parent.cwidg.tabAdder(File)
