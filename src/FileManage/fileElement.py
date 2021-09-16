from xml.etree.ElementTree import Element, SubElement
from glob_objects.globalxml import filesRoot, styleLocsRoot
from glob_objects.Generator import defaultfileGenerator, defaultStyleGenerator
from pathlib import Path

class fileElement():
	tup=("title","dir","name")
	def __init__(self,singleElement=None, style=False):
		self.style=style
		if type(singleElement) is Element:
			self.title=singleElement.find(self.tup[0])
			self.direc=singleElement.find(self.tup[1])
			self.name=singleElement.find(self.tup[2])
		elif type(singleElement) is str:
			singleElement=singleElement.lstrip()
			if singleElement[0:7]=="file://":
				singleElement=singleElement[7:]
			if singleElement[0]=="~":
				singleElement=str(Path.home())+singleElement[1:]
			p=Path(singleElement)
			elem=Element("Elem")
			title=SubElement(elem,self.tup[0])
			direc=SubElement(elem,self.tup[1])
			name=SubElement(elem,self.tup[2])
			title.text=p.stem
			direc.text=str(p.parent)+"/"
			name.text=p.name
			self.title=title
			self.direc=direc
			self.name=name
		elif type(singleElement)==type(None)and style==False:
			defaultElement=filesRoot.find("Elem[@default='True']")
			try:
				self.title=defaultElement.find(self.tup[0])
				self.direc=defaultElement.find(self.tup[1])
				self.name=defaultElement.find(self.tup[2])
			except:
				defaultfileGenerator(str(Path.home())+"/.config/Pycodoc/Default")
				self.__init__()
		elif type(singleElement)==type(None)and style==True:
			defaultElement=styleLocsRoot.find("Elem[@default='True']")
			try:
				self.title=defaultElement.find(self.tup[0])
				self.direc=defaultElement.find(self.tup[1])
				self.name=defaultElement.find(self.tup[2])
			except:
				defaultStyleGenerator(str(Path.home())+"/.config/Pycodoc/System_Theme.css")
				self.__init__(style=True)
	
	def isstyle(self):
		return self.style
	
	def isFormat(self,form):
		return form==Path(self.fileStrPath()).suffix
	
	def isFile(self):
		return Path(self.fileStrPath()).is_file()
	
	def isUnique(self):
		if self.style:
			searchBasket=styleLocsRoot
		else:
			searchBasket=filesRoot
		a=searchBasket.findall("Elem[name='"+self.name.text+"'][dir='"+self.direc.text+"']")
		return len(a)==0
	
	def asUrl(self):
		return Path(self.fileStrPath()).as_uri()
	
	def fileStrPath(self):
		return self.direc.text+self.name.text
	
	def htmlize(self):
		a=Path(self.fileStrPath())
		return str(a.parent)+"/"+a.stem+".html"
	
	def createHistElement(self):
		elem=Element("Elem")
		title=SubElement(elem,self.tup[0])
		dire=SubElement(elem,self.tup[1])
		name=SubElement(elem,self.tup[2])
		title.text=self.title.text
		dire.text=self.direc.text
		name.text=self.name.text
		return elem
	
	def createFileElement(self,show=True,default=False,error=False):
		elem=Element("Elem")
		if show==True: elem.set("show","True")
		if default==True: elem.set("default","True")
		if error==True: elem.set("error","True")
		title=SubElement(elem,self.tup[0])
		dire=SubElement(elem,self.tup[1])
		name=SubElement(elem,self.tup[2])
		title.text=self.title.text
		dire.text=self.direc.text
		name.text=self.name.text
		return elem
