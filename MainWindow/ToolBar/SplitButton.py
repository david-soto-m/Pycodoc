from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class splitButton():
	def __init__(self,parent):
		self.split=QAction(parent)
		self.split.setIcon(QIcon().fromTheme("view-split-effect"))
		self.split.setToolTip('Split')
		self.split.triggered.connect(parent.cwidg.split)
		
		self.unsplit=QAction(parent)
		self.unsplit.setIcon(QIcon().fromTheme("view-unsplit-effect"))
		self.unsplit.setToolTip('Split')
		self.unsplit.triggered.connect(parent.cwidg.unsplit)
