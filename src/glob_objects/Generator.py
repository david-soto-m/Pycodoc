from xml.etree.ElementTree import Element, SubElement, parse
from pathlib import Path
import glob_objects.globalxml as GXML


def mainCfgGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write('<Root></Root>')
    location = str(Path.home()) + '/.config/Pycodoc/'

    Config = parse(string)
    ConfigRoot = Config.getroot()

    Hist = Element('History')
    Behaviour = Element('Behaviour')
    Shortcuts = Element('Shortcuts')
    Files = Element('Files')
    styleLocs = Element('StyleLocs')

    HistPath = SubElement(Hist, 'Path')
    HistMax = SubElement(Hist, 'Max')
    HistMax.text = str(10)
    HistPath.text = location + 'History.xml'

    FilesPath = SubElement(Files, 'Path')
    FilesPath.text = location + 'Files.xml'

    BehaviourPath = SubElement(Behaviour, 'Path')
    BehaviourPath.text = location + 'Behaviour.xml'

    ShortcutsPath = SubElement(Shortcuts, 'Path')
    ShortcutsPath.text = location + 'Shortcuts.xml'

    styleLocsPath = SubElement(styleLocs, 'Path')
    styleLocsPath.text = location + 'StyleLoc.xml'

    ConfigRoot.append(Shortcuts)
    ConfigRoot.append(Behaviour)
    ConfigRoot.append(Files)
    ConfigRoot.append(styleLocs)
    ConfigRoot.append(Hist)
    Config.write(string)


def shortCfgGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write('<Shortcuts></Shortcuts>')

    Short = parse(string)
    ShortRoot = Short.getroot()

    shorts = []

    shorts.append(Element('TriggerHistory'))
    shorts.append(Element('NewTab'))
    shorts.append(Element('Split'))
    shorts.append(Element('Unsplit'))
    shorts.append(Element('Quit'))
    shorts.append(Element('QuitTab'))
    shorts.append(Element('OpenFile'))
    shorts.append(Element('ModifyShortcuts'))
    shorts.append(Element('ModifyBehaviours'))
    shorts.append(Element('ConfFiles'))
    shorts.append(Element('ConfStyle'))
    shorts.append(Element('Pandoc'))
    shorts.append(Element('AddStyle'))

    titles = [
        'Trigger History',
        'New Tab',
        'Split View',
        'Unsplit View',
        'Quit Pycodoc',
        'Quit Tab',
        'Open Files',
        'Modify Shortcuts',
        'Modify Behaviours',
        'Configure Files',
        'Configure Style Files',
        'View html (config specific)',
        'Create a style file'
    ]

    for shortcut, title in zip(shorts, titles):
        shortcut.set('Title', title)
        ShortRoot.append(shortcut)  # Needa add'em before we print'em
    Short.write(string)


def behaviourCfgGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write('<Behaviour></Behaviour>')

    Behaviour = parse(string)
    BehaviourRoot = Behaviour.getroot()

    hdepth = Element('HistDepth')
    hdepth.text = '15'
    BehaviourRoot.append(hdepth)
    BehaviourRoot.append(Element('TabBarAutoHide'))
    BehaviourRoot.append(Element('LastTabRemoved'))
    BehaviourRoot.append(Element('Pandoc'))
    BehaviourRoot.append(Element('Hpandoc'))

    Behaviour.write(string)


def filesCfgGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write('<Files></Files>')
    Files = parse(string)
    FilesRoot = Files.getroot()
    return FilesRoot


def historyCfgGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write('<Hist></Hist>')


def styleLocsCfgGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write('<styleLocs></styleLocs>')


def defaultfileGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write('''\
<html>
    <body>
        <h1>Some error has ocurred</h1>
        This file will contain a short manual in future releases
    </body>
</html>''')
    defFile = Element('Elem')
    defFile.set('show', 'False')
    defFile.set('default', 'True')
    defFile.set('error', 'True')
    path = SubElement(defFile, 'dir')
    path.text = str(direc) + '/'
    name = SubElement(defFile, 'name')
    name.text = p.name
    title = SubElement(defFile, 'title')
    title.text = p.stem

    GXML.filesRoot.append(defFile)
    GXML.Files.write(GXML.GConfigRoot.find('Files/Path').text)


def defaultStyleGenerator(string):
    p = Path(string)
    direc = p.parent
    direc.mkdir(exist_ok=True, parents=True)
    p.touch(exist_ok=True)
    with open(string, 'w+') as f:
        f.write(' ')
    defFile = Element('Elem')
    defFile.set('show', 'True')
    defFile.set('default', 'True')
    defFile.set('error', 'True')
    path = SubElement(defFile, 'dir')
    path.text = str(direc) + '/'
    name = SubElement(defFile, 'name')
    name.text = p.name
    title = SubElement(defFile, 'title')
    title.text = 'System Theme'

    GXML.styleLocsRoot.append(defFile)
    GXML.StyleLocs.write(GXML.GConfigRoot.find('StyleLocs/Path').text)
