import PyQt5.QtWidgets as QW
class FilesWidget (QW.QWidget):
	def __init__(self):
		super().__init__()
		
		btn = QW.QPushButton('Quit me', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.clicked.connect(self.handle)
		
		
		horz=QW.QHBoxLayout()
		horz.addWidget(btn)
		
		self.setLayout(horz)
		
	def handle(self):
		self.hide()
