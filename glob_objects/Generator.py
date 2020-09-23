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
	Files=ET.Element("Files")
	
	Shortcuts=ET.Element("Shortcuts")
	Behaviour=ET.Element("Behaviour")
	
	HistPath=ET.SubElement(Hist,"Path")
	HistMax=ET.SubElement(Hist,"Max")
	HistMax.text=str(30)
	HistPath.text=location+"History.xml"
	
	FilesPath=ET.SubElement(Files,"Path")
	FilesPath.text=location+"Files.xml"
	
	
	ShortcutsPath=ET.SubElement(Shortcuts,"Path")
	ShortcutsPath.text=location+"Shortcuts.xml"
	
	
	AH=ET.SubElement(Behaviour,"TabBarAutoHide")
	LTR=ET.SubElement(Behaviour,"LastTabRemoved")
	
	ConfigRoot.append(Hist)
	ConfigRoot.append(Files)
	ConfigRoot.append(Shortcuts)
	ConfigRoot.append(Behaviour)
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
	shorts.append(ET.Element("MarkHistory"))
	shorts.append(ET.Element("NewTab"))
	shorts.append(ET.Element("Split"))
	shorts.append(ET.Element("Unsplit"))
	shorts.append(ET.Element("Quit"))
	shorts.append(ET.Element("QuitTab"))
	shorts.append(ET.Element("OpenFile"))
	
	for el in shorts:
		ShortRoot.append(el)
	Short.write(string)

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
	path=ET.SubElement(defFile,"dir")
	path.text=str(direc)+"/"
	name=ET.SubElement(defFile,"name")
	name.text=p.name
	title=ET.SubElement(defFile,"title")
	title.text=p.stem
	
	GXML.filesRoot.append(defFile)
	GXML.Files.write(GXML.GConfigRoot.find("Files/Path").text)
