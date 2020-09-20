import xml.etree.ElementTree as ET
from pathlib import Path
import glob_objects.Generator as GEN

#Helper Functions

def mainconfig():
	configloc='/home/david/Programming/Python/Pycodoc/config/GlobalConfig.xml'
	if Path(configloc).is_file():
		#GEN.MainConfigGenerator()
		GConfig=ET.parse(configloc)
		GConfigRoot=GConfig.getroot()
		return(GConfig,GConfigRoot)
	else:
		GEN.MainConfigGenerator(configloc)
		return mainconfig()

#Master Config
GConfig,GConfigRoot=mainconfig()
#Parsing & Rooting
Files= ET.parse(GConfigRoot.find("Files/Path").text)
filesRoot=Files.getroot()
History=ET.parse(GConfigRoot.find("History/Path").text)
histRoot=History.getroot()
Shortcuts=ET.parse(GConfigRoot.find("Shortcuts/Path").text)
ShortRoot=Shortcuts.getroot()
