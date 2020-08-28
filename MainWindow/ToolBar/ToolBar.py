import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import xml.etree.ElementTree as ET

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

class fileElement():
	def __init__(self,singleElement):
		self.title=singleElement.find("title")
		self.direc=singleElement.find("dir")
		self.name=singleElement.find("name")

class searchWidg():
	def __init__(self):
		self.swid=QW.QComboBox()
		self.swid.setEditable(True)
		self.swid.setCurrentIndex(-1)
		self.swid.activated.connect(self.comboChanged)
		self.swid.setSizeAdjustPolicy(self.swid.SizeAdjustPolicy.AdjustToContents)
		
		tree = ET.parse('./config/Files.xml')
		root = tree.getroot()
		
		for child in root.iter("Elem"):
			Elem=fileElement(child);
			self.swid.addItem(Elem.title.text,QC.QVariant([Elem.direc.text,Elem.name.text]))
	
	def comboChanged(self,idx):
		if idx==0:
			print("idx 0:",self.swid.itemData(idx,0x100))
		else:
			print("idx 1:",self.swid.itemData(idx,0x100))
