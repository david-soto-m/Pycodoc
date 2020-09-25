import xml.etree.ElementTree as ET
from pathlib import Path
import glob_objects.Generator as GEN

def metaConfig(configloc,generator=None):
	if Path(configloc).is_file():
		config=ET.parse(configloc)
		configRoot=config.getroot()
		return(config,configRoot)
	elif generator is not None:
		generator(configloc)
		return metaConfig(configloc)

GConfig,GConfigRoot=metaConfig(str(Path.home())+"/.config/Pycodoc/GlobalConfig.xml", GEN.mainCfgGenerator)
Shortcuts,ShortRoot=metaConfig(GConfigRoot.find("Shortcuts/Path").text, GEN.shortCfgGenerator)
Files,filesRoot=metaConfig(GConfigRoot.find("Files/Path").text, GEN.filesCfgGenerator)
History,histRoot=metaConfig(GConfigRoot.find("History/Path").text,GEN.historyCfgGenerator)
CssLocs,cssLocsRoot=metaConfig(GConfigRoot.find("CssLocs/Path").text,GEN.cssLocsCfgGenerator)
