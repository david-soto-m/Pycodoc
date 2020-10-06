import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import glob_objects.globalxml as GXML
import xml.etree.ElementTree as ET
from FileManage.fileElement import fileElement

class FilesWidget (QW.QWidget):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Files settings")
		self.setWindowIcon(QG.QIcon('AppIcon/AppIcon.svg'))
		
		self.itemElim=[]
		self.btnsElim=[]
		self.titleEdits=[]
		self.filePathEdits=[]
		self.showCBoxes=[]
		self.errorRBtns=[]
		self.defaultRBtns=[]
		
		self.scrollVert=QW.QVBoxLayout()
	
	def showWind(self):
		self.__init__()
		
		files=GXML.filesRoot
		
		vert=QW.QVBoxLayout()
		horz=QW.QHBoxLayout()
		scroll=QW.QScrollArea()
		
		self.defaultContainer=QW.QButtonGroup()
		self.errorContainer=QW.QButtonGroup()
		
		for child,index in zip(files,range(len(files))):
			Elem=fileElement(child)
			self.scrollVert.addLayout(self.listAdder(title=Elem.title.text, path=Elem.fileStrPath(), child=child))
		
		globber=QW.QWidget()
		globber.setLayout(self.scrollVert)
		globber.resize(globber.sizeHint())
		expand=QW.QSizePolicy().Policy.Expanding
		globber.setSizePolicy(expand,expand)
		
		scroll.setWidgetResizable(True)
		scroll.ensureWidgetVisible(globber,xMargin=10)
		scroll.setWidget(globber)
		
		vert.addWidget(scroll)
		
		newBtn = QW.QPushButton('New', self)
		newBtn.clicked.connect(self.newHandle)
		
		applyBtn = QW.QPushButton('Apply', self)
		applyBtn.clicked.connect(self.applyHandle)
		
		cancelBtn = QW.QPushButton('Cancel', self)
		cancelBtn.clicked.connect(self.cancelHandle)
		
		horz.addWidget(newBtn)
		horz.addStretch(1)
		horz.addWidget(applyBtn)
		horz.addWidget(cancelBtn)
		
		vert.addLayout(horz)
		
		self.setLayout(vert)
		
		geo=QW.QDesktopWidget().availableGeometry()
		#self.resize(geo.width()/2,geo.height()/2)
		self.resize(self.sizeHint())
		self.move(int(geo.center().x()-self.width()/2),int(geo.center().y()-self.height()/2))
		
		self.show()
	
	def listAdder(self,path="",title="",child=None):
		exppol=QW.QSizePolicy().Policy.Expanding
		minpol=QW.QSizePolicy().Policy.Fixed
		
		filelbl=QW.QLabel("File: ")
		titlelbl=QW.QLabel("Title: ")
		pathlbl=QW.QLabel("Path: ")
		
		filelbl.setSizePolicy(minpol,minpol)
		titlelbl.setSizePolicy(minpol,minpol)
		pathlbl.setSizePolicy(minpol,minpol)
		
		index=len(self.itemElim)
		
		self.itemElim.append(False)
		self.btnsElim.append(QW.QPushButton(QG.QIcon().fromTheme("list-remove"),'', self))
		self.titleEdits.append(QW.QLineEdit(title))
		self.filePathEdits.append(QW.QLineEdit(path))
		self.showCBoxes.append(QW.QCheckBox("Show on searchbar",self))
		self.defaultRBtns.append(QW.QRadioButton("Show on start",self))
		self.errorRBtns.append(QW.QRadioButton("Show on error",self))
		
		self.showCBoxes[index].setTristate(on=False)
		
		self.defaultContainer.addButton(self.defaultRBtns[index])
		self.errorContainer.addButton(self.errorRBtns[index])
		
		self.btnsElim[index].clicked.connect(self.elimHandler)
		if child is not None:
			self.showCBoxes[index].setChecked(child.get("show")=="True")
			self.defaultRBtns[index].setChecked(child.get("default")=="True")
			self.errorRBtns[index].setChecked(child.get("error")=="True")
		
		self.btnsElim[index].setSizePolicy(minpol,minpol)
		self.titleEdits[index].setSizePolicy(exppol,minpol)
		self.filePathEdits[index].setSizePolicy(exppol,minpol)
		self.showCBoxes[index].setSizePolicy(minpol,minpol)
		self.defaultRBtns[index].setSizePolicy(minpol,minpol)
		self.errorRBtns[index].setSizePolicy(minpol,minpol)
		
		h1=QW.QHBoxLayout()
		h2=QW.QHBoxLayout()
		h3=QW.QHBoxLayout()
		
		h1.addWidget(titlelbl)
		h1.addWidget(self.titleEdits[index])
		
		h2.addWidget(pathlbl)
		h2.addWidget(self.filePathEdits[index])
		
		h3.addWidget(self.showCBoxes[index])
		h3.addWidget(self.defaultRBtns[index])
		h3.addWidget(self.errorRBtns[index])
		h3.addWidget(self.btnsElim[index])
		
		microvert=QW.QVBoxLayout()
		
		microvert.addWidget(filelbl)
		microvert.addLayout(h1)
		microvert.addLayout(h2)
		microvert.addLayout(h3)
		
		return microvert

	def elimHandler(self):
		idx=self.btnsElim.index(self.sender())
		if self.itemElim[idx]==False:
			self.btnsElim[idx].setStyleSheet('QWidget { background-color: red}')
			self.itemElim[idx]=True
		else:
			self.btnsElim[idx].setStyleSheet('QWidget { background-color:}')
			self.itemElim[idx]=False
	
	def applyHandle(self):
		GXML.filesRoot.clear()
		for idx in range(len(self.itemElim)):
			if self.itemElim[idx]==False:
				elem=fileElement(self.filePathEdits[idx].text())
				if elem.isFile():
					elem.title.text=self.titleEdits[idx].text()
					xellie=elem.createFileElement(show=self.showCBoxes[idx].isChecked(), default=self.defaultRBtns[idx].isChecked(), error=self.errorRBtns[idx].isChecked())
					GXML.filesRoot.append(xellie)
		self.hide()
	
	def cancelHandle(self):
		self.hide()
	
	def newHandle(self):
		self.scrollVert.addLayout(self.listAdder())
