import xml.etree.ElementTree as ET
from pathlib import Path

def MainConfigGenerator(string):
	with open(string,"w+") as f:
		f.write("<Root></Root>")
	
	Config= ET.parse(string)
	ConfigRoot=Config.getroot()
	
	Hist=ET.Element("History")
	Files=ET.Element("Files")
	
	Shortcuts=ET.Element("Shortcuts")
	Behaviour=ET.Element("Behaviour")
	
	HistPath=ET.SubElement(Hist,"Path")
	HistMax=ET.SubElement(Hist,"Max")
	HistMax.text=str(30)
	HistPath.text=str(Path.home())+"/.config/Pycodoc/History.xml"
	
	FilesPath=ET.SubElement(Files,"Path")
	FilesPath.text=str(Path.home())+"/.config/Pycodoc/Files.xml"
	
	
	ShortcutsPath=ET.SubElement(Shortcuts,"Path")
	ShortcutsPath.text=str(Path.home())+"/.config/Pycodoc/Shortcuts.xml"
	
	
	AH=ET.SubElement(Behaviour,"TabBarAutoHide")
	LTR=ET.SubElement(Behaviour,"LastTabRemoved")
	
	ConfigRoot.append(Hist)
	ConfigRoot.append(Files)
	ConfigRoot.append(Shortcuts)
	ConfigRoot.append(Behaviour)
	Config.write(string)

def ShortcutsConfig(string):
	with open(string,"w+") as f:
		f.write("<Shortcuts></Shortcuts>")
	
	Short= ET.parse(string)
	ShortRoot=Short.getroot()
	
	shorts=[]
	
	shorts.append(ET.Element("TriggerHistory"))
	shorts.append(ET.Element("MarkHistory"))
	shorts.append(ET.Element("NewTab"))
	shorts.append(ET.Element("Split"))
	shorts.append(ET.Element("Unsplit"))
	shorts.append(ET.Element("Quit"))
	shorts.append(ET.Element("OpenFile"))
	
	for el in shorts:
		ShortRoot.append(el)
	Short.write(string)
