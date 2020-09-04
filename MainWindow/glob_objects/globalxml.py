import xml.etree.ElementTree as ET
#Master Config
GConfig=ET.parse('/home/david/Programming/Python/Pycodoc/config/GlobalConfig.xml')
GConfigRoot=GConfig.getroot()

#Parsing & Rooting
Files= ET.parse(GConfigRoot.find("Files/Path").text)
filesRoot=Files.getroot()
History=ET.parse(GConfigRoot.find("History/Path").text)
histRoot=History.getroot()

#Helper Classes
class fileElement():
	tup=("title","dir","name")
	def __init__(self,singleElement):
		self.title=singleElement.find(self.tup[0])
		self.direc=singleElement.find(self.tup[1])
		self.name=singleElement.find(self.tup[2])
	def createHistElement(self):
		elem=ET.Element("Elem")
		title=ET.SubElement(elem,self.tup[0])
		dire=ET.SubElement(elem,self.tup[1])
		name=ET.SubElement(elem,self.tup[2])
		title.text=self.title.text
		dire.text=self.direc.text
		name.text=self.name.text
		return elem
