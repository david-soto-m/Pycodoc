from xml.etree.ElementTree import parse
from pathlib import Path
import glob_objects.Generator as GEN

def metaConfig(configloc, generator=None):
    if Path(configloc).is_file():
        config=parse(configloc)
        configRoot=config.getroot()
        return(config, configRoot)
    elif generator is not None:
        generator(configloc)
        return metaConfig(configloc)

GConfig, GConfigRoot=metaConfig(str(Path.home())+'/.config/Pycodoc/GlobalConfig.xml', GEN.mainCfgGenerator)
Shortcuts, ShortRoot=metaConfig(GConfigRoot.find('Shortcuts/Path').text, GEN.shortCfgGenerator)
Behaviour, BehaviourRoot=metaConfig(GConfigRoot.find('Behaviour/Path').text, GEN.behaviourCfgGenerator)
Files, filesRoot=metaConfig(GConfigRoot.find('Files/Path').text, GEN.filesCfgGenerator)
History, histRoot=metaConfig(GConfigRoot.find('History/Path').text, GEN.historyCfgGenerator)
StyleLocs, styleLocsRoot=metaConfig(GConfigRoot.find('StyleLocs/Path').text, GEN.styleLocsCfgGenerator)
