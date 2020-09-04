import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from ..glob_objects import globalxml as GXML

class ToolBar():
	def __init__(self,parent):
		
		self.toolBar=QW.QToolBar(parent)
		self.qacts=backnextact()
		self.histmen=historystuff()
		
		self.combosearch=searchWidg()
		
		self.toolBar.addAction(self.histmen.hist)
		self.toolBar.addAction(self.qacts.back)
		self.toolBar.addAction(self.qacts.ahead)
		self.toolBar.addAction(self.qacts.openfile)
		self.toolBar.addWidget(self.combosearch.swid)

class backnextact():
	
	def __init__(self):
		self.actions=[]
		
		self.back=QW.QAction()
		self.back.setIcon(QG.QIcon().fromTheme("go-previous"))
		self.back.setToolTip('Back')
		
		self.ahead=QW.QAction()
		self.ahead.setIcon(QG.QIcon().fromTheme("go-next"))
		self.ahead.setToolTip("Forward")
		
		self.openfile=QW.QAction()
		self.openfile.setIcon(QG.QIcon().fromTheme("document-open"))
		self.openfile.setToolTip("Open a file")
		
		
class historystuff(QW.QWidget):
	def __init__(self):
		super().__init__()
		
		self.actions=[]
		
		self.hist=QW.QAction()
		self.hist.setIcon(QG.QIcon().fromTheme("shallow-history"))
		self.hist.setToolTip("History")
		self.hist.setMenu(self.histMenu())
	
	def histMenu(self):
		Menu=QW.QMenu()
		for child,index in zip(GXML.histRoot,range(len(GXML.histRoot))):
			Elem=GXML.fileElement(child)
			self.actions.append(QW.QAction(Elem.title.text))
			self.actions[index].setData(Elem)
			self.actions[index].triggered.connect(self.trigger)
			Menu.addAction(self.actions[index])
		return Menu
	
	def trigger(self,boolean):
		File=self.sender().data()
		print(File.title.text)

class searchWidg():
	def __init__(self):
		self.swid=QW.QComboBox()
		self.swid.setEditable(True)
		self.swid.activated.connect(self.comboChanged)
		expand=QW.QSizePolicy().Policy.Expanding
		self.swid.setSizePolicy(expand,expand)
		
		for child in GXML.filesRoot.findall("Elem[@show='True']"):
			Elem=GXML.fileElement(child)
			self.swid.addItem(Elem.title.text,QC.QVariant(Elem))
		self.swid.setCurrentIndex(-1)
	
	def comboChanged(self,idx):
		fielem=self.swid.itemData(idx,0x100)
		if fielem is not None:
			GXML.histRoot.insert(0,fielem.createHistElement())
		else:
			pass
		while len(list(GXML.histRoot))>int(GXML.GConfigRoot.find("History/Max").text)>-1:
			GXML.histRoot.remove(GXML.histRoot.find("Elem[last()]"))
