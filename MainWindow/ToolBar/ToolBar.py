import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from ..glob_objects import globalxml as GXML

class ToolBar():
	def __init__(self,parent):
		
		self.toolBar=QW.QToolBar(parent)
		self.qacts=backnextact()
		
		self.combosearch=searchWidg()
		
		self.toolBar.addAction(self.qacts.back)
		self.toolBar.addAction(self.qacts.ahead)
		self.toolBar.addWidget(self.combosearch.swid)

class backnextact():
	def __init__(self):
		self.back=QW.QAction()
		self.back.setIcon(QG.QIcon().fromTheme("go-previous"))
		self.back.setToolTip('Back')
		
		self.ahead=QW.QAction()
		self.ahead.setIcon(QG.QIcon().fromTheme("go-next"))
		self.ahead.setToolTip("Forward")

class searchWidg():
	def __init__(self):
		self.swid=QW.QComboBox()
		self.swid.setEditable(True)
		self.swid.activated.connect(self.comboChanged)
		self.swid.setSizeAdjustPolicy(self.swid.SizeAdjustPolicy.AdjustToContents)
		
		for child in GXML.filesRoot.findall("Elem[@show='True']"):
			Elem=GXML.fileElement(child)
			self.swid.addItem(Elem.title.text,QC.QVariant(Elem))
		self.swid.setCurrentIndex(-1)
	
	def comboChanged(self,idx):
		fielem=self.swid.itemData(idx,0x100)
		GXML.histRoot.insert(0,fielem.createHistElement())
		while len(list(GXML.histRoot))>int(GXML.GConfigRoot.find("History/Max").text)>-1:
			GXML.histRoot.remove(GXML.histRoot.find("Elem[last()]"))
