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
	
	def __init__(self,singleElement=None):
		if type(singleElement) is ET.Element:
			self.title=singleElement.find(self.tup[0])
			self.direc=singleElement.find(self.tup[1])
			self.name=singleElement.find(self.tup[2])
		elif type(singleElement) is str:
			elem=ET.Element("Elem")
			elem.set("show","True")
			title=ET.SubElement(elem,self.tup[0])
			direc=ET.SubElement(elem,self.tup[1])
			name=ET.SubElement(elem,self.tup[2])
			title.text,direc.text,name.text=self.beheader(singleElement)
			self.title=title
			self.direc=direc
			self.name=name
		elif type(singleElement)==type(None):
			defaultElement=filesRoot.find("Elem[@default='True']")
			try:
				self.title=defaultElement.find(self.tup[0])
				self.direc=defaultElement.find(self.tup[1])
				self.name=defaultElement.find(self.tup[2])
			except:
				pass
	def beheader(self,stringy):
		direc=stringy
		notthere=True
		idx=len(direc)-1
		while notthere:
			direc=direc[0:idx]
			idx-=1
			if  direc[idx]=='/'or direc[idx]=='\\':
				notthere=False
		print(stringy)
		name=stringy[idx+1:len(stringy)]
		print(name,";",direc)
		return ("stupid",direc,name)
	
	def createHistElement(self):
		elem=ET.Element("Elem")
		title=ET.SubElement(elem,self.tup[0])
		dire=ET.SubElement(elem,self.tup[1])
	
		name=ET.SubElement(elem,self.tup[2])
		title.text=self.title.text
		dire.text=self.direc.text
		name.text=self.name.text
		return elem
