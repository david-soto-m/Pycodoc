from glob_objects.globalxml import ShortRoot
from PyQt5.QtWidgets import QShortcut
from AuxWindows.StyleWidget import StyleWidget

class Shortcutter():
	def __init__(self,parent):
		self.parent=parent
		self.shcts=[]
		self.shct=[]
		
		self.addscht("QuitTab",parent.cwidg.tabDestroyer)
		self.addscht("Quit",parent.mnb.exitAct.trigger)
		self.addscht("OpenFile",parent.tlb.fileopener.trigger)
		self.addscht("Split",parent.cwidg.split)
		self.addscht("Unsplit",parent.cwidg.unsplit)
		self.addscht("NewTab",parent.tlb.combosearch.setFocus)
		self.addscht("TriggerHistory",parent.tlb.histmen.triggerlast)
		self.addscht("ConfFiles",parent.mnb.editFiles.trigger)
		self.addscht("ConfStyle",parent.mnb.editStyles.trigger)
		self.addscht("ModifyBehaviours",parent.mnb.behaviourSettings.trigger)
		self.addscht("ModifyShortcuts",parent.mnb.shortcutSettings.trigger)
		self.addscht("Pandoc",parent.cwidg.pandocize)
		self.sty=StyleWidget(self.parent)
		self.addscht("AddStyle",self.sty.showWid)
	
	def addscht(self,text,funct):
		self.shct.append(ShortRoot.find(text))
		if self.shct[-1].text is not None:
			self.shcts.append(QShortcut(self.shct[-1].text,self.parent))
			self.shcts[-1].activated.connect(funct)
		else:
			self.shct=self.shct[0:-1]
	def refresh(self):
		for elem in ShortRoot.findall("*"):
			try:
				idx=self.shct.index(elem)
				self.shcts[idx].setKey(elem.text)
			except:
				pass
