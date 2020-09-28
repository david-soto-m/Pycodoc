import xml.etree.ElementTree as ET
import glob_objects.globalxml as GXML
import glob_objects.Generator as GEN
from pathlib import Path

class fileElement():
	tup=("title","dir","name")
	def __init__(self,singleElement=None, style=False):
		self.style=style
		if type(singleElement) is ET.Element:
			self.title=singleElement.find(self.tup[0])
			self.direc=singleElement.find(self.tup[1])
			self.name=singleElement.find(self.tup[2])
		elif type(singleElement) is str:
			p=Path(singleElement)
			elem=ET.Element("Elem")
			elem.set("show","True")
			title=ET.SubElement(elem,self.tup[0])
			direc=ET.SubElement(elem,self.tup[1])
			name=ET.SubElement(elem,self.tup[2])
			title.text=p.stem
			direc.text=str(p.parent)+"/"
			name.text=p.name
			self.title=title
			self.direc=direc
			self.name=name
		elif type(singleElement)==type(None):
			defaultElement=GXML.filesRoot.find("Elem[@default='True']")
			try:
				self.title=defaultElement.find(self.tup[0])
				self.direc=defaultElement.find(self.tup[1])
				self.name=defaultElement.find(self.tup[2])
			except:
				GEN.defaultfileGenerator(str(Path.home())+"/.config/Pycodoc/Default")
				self.__init__()
	
	def isstyle(self):
		return self.style
	
	def isFormat(self,form):
		return form==Path(name).suffix
	
	def isFile(self):
		return Path(self.fileStrPath()).is_file()
	
	def isUnique(self):
		if self.style:
			searchBasket=GXML.styleLocsRoot
		else:
			searchBasket=GXML.filesRoot
		a=searchBasket.findall("Elem[name='"+self.name.text+"'][dir='"+self.direc.text+"']")
		return len(a)==0
	
	def asUrl(self):
		return Path(self.fileStrPath()).as_uri()
	
	def fileStrPath(self):
		return self.direc.text+self.name.text
	
	def createHistElement(self):
		elem=ET.Element("Elem")
		title=ET.SubElement(elem,self.tup[0])
		dire=ET.SubElement(elem,self.tup[1])
		name=ET.SubElement(elem,self.tup[2])
		title.text=self.title.text
		dire.text=self.direc.text
		name.text=self.name.text
		return elem
 
