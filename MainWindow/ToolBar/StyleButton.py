from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtGui import QIcon
from pathlib import Path
from FileManage.fileElement import fileElement
import glob_objects.globalxml as GXML

class styleButton(QAction):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
		self.setIcon(QIcon().fromTheme("text-css"))
		self.setToolTip("Style")
		self.setMenu(self.styleMenu())
		self.hovered.connect(self.refreshMenu)
		self.triggered.connect(self.triggerOpen)
		
	def refreshMenu(self):
		self.setMenu(self.styleMenu())
	
	def styleMenu(self):
		self.actions=[]
		Menu=QMenu()
		for child,index in zip(GXML.styleLocsRoot.findall("Elem[@show='True']"),range(len(GXML.styleLocsRoot))):
			Elem=fileElement(child,style=True)
			self.actions.append(QAction(Elem.title.text))
			self.actions[index].setData(Elem)
			self.actions[index].triggered.connect(self.trigger)
			Menu.addAction(self.actions[index])
		index=len(self.actions)
		self.actions.append(QAction('Base'))
		self.actions[index].setData(None)
		self.actions[index].triggered.connect(self.trigger)
		Menu.addAction(self.actions[index])
		return Menu
	def triggerOpen(self,boolean):
		print("here")
		home_dir=str(Path.home())
		fname=QFileDialog.getOpenFileNames(caption='Open file',directory=home_dir)
		if fname[0]:
			for each in fname[0]:
				if Path(each).is_file() and Path(each).is_file():
					styleElem=fileElement(each,style=True)
					self.parent.cwidg.stylize(styleElem)
	def trigger(self,boolean):
		styleElem=self.sender().data()
		self.parent.cwidg.stylize(styleElem)
