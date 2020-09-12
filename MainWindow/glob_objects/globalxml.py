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
		idx=stringy.rfind("/")
		idx1=stringy.rfind("\\")
		if idx>0:
			name=stringy[idx+1:len(stringy)]
		elif idx1>0:
			name=stringy[idx+1:len(stringy)]
			idx=idx1
		else:
			name=stringy
		direc=stringy[0:idx+1]
		idx=name.find(".")
		if idx>=1:
			title=name[0:idx]
		else:
			title=name
		return (title,direc,name)
	def formater(self):
		lists=self.name.text.rsplit(".")
		lists=[var for var in lists if var]
		if len(lists)>1:
			return lists[len(lists)-1]
		else:
			return ""
	def isformat(self,form):
		return form==self.formater()
	def createHistElement(self):
		elem=ET.Element("Elem")
		title=ET.SubElement(elem,self.tup[0])
		dire=ET.SubElement(elem,self.tup[1])
	
		name=ET.SubElement(elem,self.tup[2])
		title.text=self.title.text
		dire.text=self.direc.text
		name.text=self.name.text
		return elem
