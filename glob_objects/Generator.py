import xml.etree.ElementTree as ET
from pathlib import Path
import glob_objects.globalxml as GXML

def mainCfgGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write("<Root></Root>")
	location=str(Path.home())+"/.config/Pycodoc/"
	
	Config=ET.parse(string)
	ConfigRoot=Config.getroot()
	
	Hist=ET.Element("History")
	Behaviour=ET.Element("Behaviour")
	Shortcuts=ET.Element("Shortcuts")
	Files=ET.Element("Files")
	styleLocs=ET.Element("StyleLocs")
	
	
	HistPath=ET.SubElement(Hist,"Path")
	HistMax=ET.SubElement(Hist,"Max")
	HistMax.text=str(10)
	HistPath.text=location+"History.xml"
	
	FilesPath=ET.SubElement(Files,"Path")
	FilesPath.text=location+"Files.xml"
	
	BehaviourPath=ET.SubElement(Behaviour,"Path")
	BehaviourPath.text=location+"Behaviour.xml"
	
	ShortcutsPath=ET.SubElement(Shortcuts,"Path")
	ShortcutsPath.text=location+"Shortcuts.xml"
	
	styleLocsPath=ET.SubElement(styleLocs,"Path")
	styleLocsPath.text=location+"StyleLoc.xml"
	
	
	ConfigRoot.append(Shortcuts)
	ConfigRoot.append(Behaviour)
	ConfigRoot.append(Files)
	ConfigRoot.append(styleLocs)
	ConfigRoot.append(Hist)
	Config.write(string)

def shortCfgGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write("<Shortcuts></Shortcuts>")
	
	Short=ET.parse(string)
	ShortRoot=Short.getroot()
	
	shorts=[]
	
	shorts.append(ET.Element("TriggerHistory"))
	shorts.append(ET.Element("NewTab"))
	shorts.append(ET.Element("Split"))
	shorts.append(ET.Element("Unsplit"))
	shorts.append(ET.Element("Quit"))
	shorts.append(ET.Element("QuitTab"))
	shorts.append(ET.Element("OpenFile"))
	shorts.append(ET.Element("ModifyShortcuts"))
	shorts.append(ET.Element("ModifyBehaviours"))
	shorts.append(ET.Element("ConfFiles"))
	shorts.append(ET.Element("ConfStyle"))
	
	titles=["Trigger History","New Tab","Split View","Unsplit View","Quit Pycodoc", "Quit Tab", "Open Files","Modify Shortcuts","Modify Behaviours","Configure Files","Configure Style Files"]
	
	for shortcut,title in zip(shorts,titles):
		shortcut.set("Title",title)
		ShortRoot.append(shortcut)#Needa add'em before we print'em
	Short.write(string)

def behaviourCfgGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write("<Behaviour></Behaviour>")
	
	Behaviour=ET.parse(string)
	BehaviourRoot=Behaviour.getroot()
	
	hdepth=ET.Element("HistDepth")
	hdepth.text="15"
	BehaviourRoot.append(hdepth)
	BehaviourRoot.append(ET.Element("TabBarAutoHide"))
	BehaviourRoot.append(ET.Element("LastTabRemoved"))
	BehaviourRoot.append(ET.Element("AllowEdits"))
	#BehaviourRoot.append(ET.Element("Pandoc"))
	
	Behaviour.write(string)

def filesCfgGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write("<Files></Files>")
	Files=ET.parse(string)
	FilesRoot=Files.getroot()

def historyCfgGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write("<Hist></Hist>")

def styleLocsCfgGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write("<styleLocs></styleLocs>")

def defaultfileGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write("This file will contain a short manual in future releases")
	defFile=ET.Element("Elem")
	defFile.set("show","False")
	defFile.set("default","True")
	defFile.set("error","True")
	path=ET.SubElement(defFile,"dir")
	path.text=str(direc)+"/"
	name=ET.SubElement(defFile,"name")
	name.text=p.name
	title=ET.SubElement(defFile,"title")
	title.text=p.stem
	
	GXML.filesRoot.append(defFile)
	GXML.Files.write(GXML.GConfigRoot.find("Files/Path").text)

def defaultStyleGenerator(string):
	p=Path(string)
	direc=p.parent
	direc.mkdir(exist_ok=True,parents=True)
	p.touch(exist_ok=True)
	with open(string,"w+") as f:
		f.write(" ")
	defFile=ET.Element("Elem")
	defFile.set("show","True")
	defFile.set("default","True")
	defFile.set("error","True")
	path=ET.SubElement(defFile,"dir")
	path.text=str(direc)+"/"
	name=ET.SubElement(defFile,"name")
	name.text=p.name
	title=ET.SubElement(defFile,"title")
	title.text="System Theme"
	
	GXML.styleLocsRoot.append(defFile)
	GXML.StyleLocs.write(GXML.GConfigRoot.find("StyleLocs/Path").text)

