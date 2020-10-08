import glob_objects.globalxml as GXML
from PyQt5.QtWidgets import QTextBrowser
from FileManage.fileElement import fileElement
from pathlib import Path

class TextEditor(QTextBrowser):
	def __init__(self,files,papa,NoHist,styleFile=None):
		super().__init__(),
		self.parent=papa
		self.setAcceptDrops(True)
		self.setReadOnly(GXML.GConfigRoot.find("Behaviour/AllowEdits").text not in ["Yes","yes","Y","y"])
		if files.isFile():
			with open(files.fileStrPath(), 'r') as f:
				data = f.read()
				self.setText(data)
			if not NoHist:
				GXML.histRoot.insert(0,files.createHistElement())
				while len(list(GXML.histRoot))>int(GXML.GConfigRoot.find("History/Max").text)>-1:
					GXML.histRoot.remove(GXML.histRoot.find("Elem[last()]"))
		else:
			self.setReadOnly(True)
			errfile=GXML.filesRoot.find("Elem[@error='True']")
			if errfile is not None and errfile:
				files=fileElement(errfile)
			else:
				files=fileElement()
			if files.isFile():
				with open(files.fileStrPath(), 'r') as f:
					data = f.read()
					self.setText(data)
		self.stylize(styleFile)
	
	def stylize(self,styleFile):
		if styleFile is not None and styleFile.isstyle():
			with open(styleFile.fileStrPath(), 'r') as f:
				data = f.read()
				self.setStyleSheet(data)
		else:
			self.setStyleSheet('')
	
	def dragEnterEvent(self, e):
		if e.mimeData().hasUrls():
			e.accept()
		else:
			e.ignore()
	
	def dragMoveEvent(self,evie):
		pass
		#I don't have the slightest idea why but it doesn't work without the event override.
		#Maybe the implementation cancels the event by default, but that is quite messed up.
	
	def dropEvent(self,e):
		for url in e.mimeData().urls():
			if Path(url.path()).is_file():
				fielem=fileElement(url.path())
				self.parent.tabAdder(fielem)
