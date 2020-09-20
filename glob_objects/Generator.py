import xml.etree.ElementTree as ET
from pathlib import Path

def MainConfigGenerator(string):
	with open(string,"w+") as f:
		f.write("<Root>\n</Root>")
	
	Config= ET.parse(string)
	ConfigRoot=Config.getroot()
	
	Hist=ET.Element("History")
	Files=ET.Element("Files")
	
	Shortcuts=ET.Element("Shortcuts")
	Behaviour=ET.Element("Behaviour")
	
	HistPath=ET.SubElement(Hist,"Path")
	HistPath=ET.SubElement(Hist,"Max")
	HistPath.text=str(Path.home())+"/.config/Pycodoc/History"
	
	
	
	Config.close()
	
	'''Base='<Root>
	<History>
		<Path>/home/david/Programming/Python/Pycodoc/config/History.xml</Path>
		<Max>10</Max>
	</History>
	<Files>
		<Path>/home/david/Programming/Python/Pycodoc/config/Files.xml</Path>
	</Files>
	<Shortcuts>
		<TriggerHistory>Ctrl+H,H</TriggerHistory>
		<MarkHistory>Ctrl+H</MarkHistory>
		<NewTab>Ctrl+T</NewTab>gs
		<Split>Ctrl+Right</Split>
		<Unsplit>Ctrl+Left</Unsplit>
		<Quit>Ctrl+Q</Quit>
		<QuitTab>Ctrl+W</QuitTab>
		<OpenFile>Ctrl+O</OpenFile>
	</Shortcuts>
	<Behaviour>
		<TabBarAutoHide></TabBarAutoHide>
			<!--["Remain","remain","R","r"]|(.*)AutoHide-->
		<LastTabRemoved>N</LastTabRemoved>
			<!--["Welcome","welcome","W","w"]|["None","none","N","n"]|["Persist","persist","P","p"]|(.*)Quits-->
	</Behaviour>
</Root>'''
