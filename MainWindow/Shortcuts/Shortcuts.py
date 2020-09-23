from glob_objects import globalxml as GXML
import PyQt5.QtWidgets as QW

class Shortcutter():
	def __init__(self,parent):
		self.shcts=[]
		
		shct=GXML.ShortRoot.find("QuitTab").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.cwidg.tabDestroyer)
		
		shct=GXML.ShortRoot.find("Quit").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.mnb.exitAct.trigger)
		
		shct=GXML.ShortRoot.find("OpenFile").text
		if shct is not None :
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.tlb.fileopener.openfile.trigger)
		
		shct=GXML.ShortRoot.find("Split").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.cwidg.split)
		
		shct=GXML.ShortRoot.find("Unsplit").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.cwidg.unsplit)
		shct=GXML.ShortRoot.find("NewTab").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.tlb.combosearch.swid.setFocus)
		shct=GXML.ShortRoot.find("TriggerHistory").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.tlb.histmen.hist.trigger)
