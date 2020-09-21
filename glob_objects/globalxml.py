import xml.etree.ElementTree as ET
from pathlib import Path
import glob_objects.Generator as GEN

#Helper Functions

def mainConfig(configloc):
	if Path(configloc).is_file():
		GConfig=ET.parse(configloc)
		GConfigRoot=GConfig.getroot()
		return(GConfig,GConfigRoot)
	else:
		GEN.MainConfigGenerator(configloc)
		return mainconfig(configloc)

def shortConfig(configloc):
	if Path(configloc).is_file():
		Shortcuts=ET.parse(configloc)
		ShortRoot=Shortcuts.getroot()
		return(Shortcuts,ShortRoot)
	else:
		GEN.ShortcutsConfig(configloc)
		return shortConfig()

#def mainconfig():
	#configloc='/home/david/Programming/Python/Pycodoc/config/GlobalConfig.xml'
	#if Path(configloc).is_file():
		#GConfig=ET.parse(configloc)
		#GConfigRoot=GConfig.getroot()
		#return(GConfig,GConfigRoot)
	#else:
		#GEN.MainConfigGenerator(configloc)
		#return mainconfig()
#def mainconfig():
	#configloc='/home/david/Programming/Python/Pycodoc/config/GlobalConfig.xml'
	#if Path(configloc).is_file():
		#GConfig=ET.parse(configloc)
		#GConfigRoot=GConfig.getroot()
		#return(GConfig,GConfigRoot)
	#else:
		#GEN.MainConfigGenerator(configloc)
		#return mainconfig()
#Master Config
GConfig,GConfigRoot=mainConfig('/home/david/Programming/Python/Pycodoc/config/GlobalConfig.xml')
#Parsing & Rooting
Shortcuts,ShortRoot=shortConfig(GConfigRoot.find("Shortcuts/Path").text)

Files= ET.parse(GConfigRoot.find("Files/Path").text)
filesRoot=Files.getroot()
History=ET.parse(GConfigRoot.find("History/Path").text)
histRoot=History.getroot()
