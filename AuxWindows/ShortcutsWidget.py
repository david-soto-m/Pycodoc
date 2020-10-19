import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import glob_objects.globalxml as GXML
import xml.etree.ElementTree as ET
from FileManage.fileElement import fileElement 

class ShortcutsWidget (QW.QWidget):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
	
	def showWid(self):
		self.__init__(self.parent)
		L=QW.QVBoxLayout()
		scl=QW.QVBoxLayout()
		self.txts=[]
		
		for elem in GXML.ShortRoot.findall("*"):
			scl.addLayout(self.shctLayout(elem))
		
		globber=QW.QWidget()
		globber.setLayout(scl)
		scroll=QW.QScrollArea()
		scroll.setWidget(globber)
		scroll.setWidgetResizable(True)
		
		L.addWidget(scroll)
		L.addLayout(self.bottomBar())
		
		self.setLayout(L)
		
		geo=QW.QDesktopWidget().availableGeometry()
		self.resize(self.sizeHint())
		self.move(int(geo.center().x()-self.width()/2),int(geo.center().y()-self.height()/2))
		
		self.show()
	
	def shctLayout(self,elem):
		lbl=QW.QLabel(elem.get("Title")+":")
		txt=QW.QLineEdit(elem.text)
		
		exppol=QW.QSizePolicy().Policy.Expanding
		minpol=QW.QSizePolicy().Policy.Fixed
		
		lbl.setSizePolicy(exppol,minpol)
		txt.setSizePolicy(exppol,minpol)
		
		self.txts.append(txt)
		
		hz=QW.QHBoxLayout()
		
		hz.addWidget(lbl)
		hz.addWidget(txt)
		
		return hz
	
	def bottomBar(self):
		newBtn = QW.QPushButton('New', self)
		newBtn.clicked.connect(self.newHandle)
		applyBtn = QW.QPushButton('Apply', self)
		applyBtn.clicked.connect(self.applyHandle)
		cancelBtn = QW.QPushButton('Cancel', self)
		cancelBtn.clicked.connect(self.cancelHandle)
		
		horz=QW.QHBoxLayout()
		horz.addWidget(newBtn)
		horz.addStretch(1)
		horz.addWidget(applyBtn)
		horz.addWidget(cancelBtn)
		return horz
	
	def applyHandle(self):
		idx=0
		for elem in GXML.ShortRoot.findall("*"):
			elem.text=self.txts[idx].text()
			idx+=1
		self.parent.shctobj.refresh()
		self.hide()
	
	def cancelHandle(self):
		self.hide()
	
	def newHandle(self):
		pass
