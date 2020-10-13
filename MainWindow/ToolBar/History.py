from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtGui import QIcon
from FileManage.fileElement import fileElement
import glob_objects.globalxml as GXML

class history(QAction):
	def __init__(self,parent):
		super().__init__()
		self.counter=0
		self.parent=parent
		self.setIcon(QIcon().fromTheme("shallow-history"))
		self.setToolTip("History")
		self.setMenu(self.histMenu())
		self.hovered.connect(self.refreshMenu)
		self.triggered.connect(self.triggerlast)
		
	def refreshMenu(self):
		self.counter=0
		self.setMenu(self.histMenu())
	
	def histMenu(self):
		self.actions=[]
		Menu=QMenu()
		for child,index in zip(GXML.histRoot,range(len(GXML.histRoot))):
			Elem=fileElement(child)
			self.actions.append(QAction(Elem.title.text))
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
