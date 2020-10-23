from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtGui import QIcon
from pathlib import Path
from FileManage.fileElement import fileElement
from AuxWindows.StyleWidget import StyleWidget
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
		self.styleCreator=StyleWidget()
	
	def refreshMenu(self):
		self.setMenu(self.styleMenu())
	
	def styleMenu(self):
		self.actions=[]
		Menu=QMenu()
		for child in GXML.styleLocsRoot.findall("Elem[@show='True']"):
			Elem=fileElement(child,style=True)
			self.actions.append(QAction(Elem.title.text))
			self.actions[-1].setData(Elem)
			self.actions[-1].triggered.connect(self.trigger)
			Menu.addAction(self.actions[-1])
		
		self.actions.append(QAction('Create Style'))
		self.actions[-1].triggered.connect(self.styleCreator.show())
		Menu.addAction(self.actions[-1])
		
		return Menu
	
	def triggerOpen(self,boolean):
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
