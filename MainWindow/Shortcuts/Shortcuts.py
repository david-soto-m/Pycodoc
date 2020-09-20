from glob_objects import globalxml as GXML
import PyQt5.QtWidgets as QW

class Shortcutter():
	def __init__(self,parent):
		self.shcts=[]
		shct=GXML.GConfigRoot.find("Shortcuts/QuitTab").text
		
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.cwidg.tabDestroyer)
		
		shct=GXML.GConfigRoot.find("Shortcuts/Quit").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.mnb.exitAct.trigger)
		
		shct=GXML.GConfigRoot.find("Shortcuts/OpenFile").text
		if shct is not None :
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.tlb.fileopener.openfile.trigger)
		
		shct=GXML.GConfigRoot.find("Shortcuts/Split").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.cwidg.split)
		
		shct=GXML.GConfigRoot.find("Shortcuts/Unsplit").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.cwidg.unsplit)
		shct=GXML.GConfigRoot.find("Shortcuts/NewTab").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.tlb.combosearch.swid.setFocus)
		shct=GXML.GConfigRoot.find("Shortcuts/TriggerHistory").text
		if shct is not None:
			self.shcts.append(QW.QShortcut(shct,parent))
			self.shcts[len(self.shcts)-1].activated.connect(parent.tlb.histmen.hist.trigger)
