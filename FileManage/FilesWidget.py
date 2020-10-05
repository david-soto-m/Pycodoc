import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import glob_objects.globalxml as GXML
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
	
	def showWind(self):
		files=GXML.filesRoot
		
		vert=QW.QVBoxLayout()
		horz=QW.QHBoxLayout()
		scrollVert=QW.QVBoxLayout()
		scroll=QW.QScrollArea()
		
		self.defaultContainer=QW.QButtonGroup()
		self.errorContainer=QW.QButtonGroup()
		
		for child,index in zip(files,range(len(files))):
			Elem=fileElement(child)
			
			exppol=QW.QSizePolicy().Policy.Expanding
			minpol=QW.QSizePolicy().Policy.Fixed
			
			filelbl=QW.QLabel("File: ")
			titl=QW.QLabel("Title: ")
			path=QW.QLabel("Path: ")
			
			titl.setSizePolicy(minpol,minpol)
			path.setSizePolicy(minpol,minpol)
			
			self.itemElim.append(False)
			self.btnsElim.append(QW.QPushButton(QG.QIcon().fromTheme("list-remove"),'', self))
			self.titleEdits.append(QW.QLineEdit(Elem.title.text))
			self.filePathEdits.append(QW.QLineEdit(Elem.fileStrPath()))
			self.showCBoxes.append(QW.QCheckBox("Show on searchbar",self))
			self.defaultRBtns.append(QW.QRadioButton("Show on start",self))
			self.errorRBtns.append(QW.QRadioButton("Show on error",self))
			
			self.defaultContainer.addButton(self.defaultRBtns[index])
			self.errorContainer.addButton(self.errorRBtns[index])
			
			self.btnsElim[index].clicked.connect(self.elimHandler)
			self.showCBoxes[index].setCheckState(child.get("show")=="True")
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
			
			h1.addWidget(titl)
			h1.addWidget(self.titleEdits[index])
			
			h2.addWidget(path)
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
			
			scrollVert.addLayout(microvert)
		
		globber=QW.QWidget()
		globber.setLayout(scrollVert)
		globber.resize(globber.sizeHint())
		expand=QW.QSizePolicy().Policy.Expanding
		globber.setSizePolicy(expand,expand)
		
		scroll.setWidgetResizable(True)
		scroll.ensureWidgetVisible(globber,xMargin=10)
		scroll.setWidget(globber)
		
		btn = QW.QPushButton('Apply', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.clicked.connect(self.handle)
		horz.addWidget(btn)
				
		vert.addWidget(scroll)
		vert.addLayout(horz)
		
		self.setLayout(vert)
		
		geo=QW.QDesktopWidget().availableGeometry()
		#self.resize(geo.width()/2,geo.height()/2)
		self.resize(self.sizeHint())
		self.move(int(geo.center().x()-self.width()/2),int(geo.center().y()-self.height()/2))
		
		self.show()
	
	def elimHandler(self):
		idx=self.btnsElim.index(self.sender())
		if self.itemElim[idx]==False:
			self.btnsElim[idx].setStyleSheet('QWidget { background-color: red}')
			self.itemElim[idx]=True
		else:
			self.btnsElim[idx].setStyleSheet('QWidget { background-color:}')
			self.itemElim[idx]=False
	
	def handle(self):
		self.hide()
		
		