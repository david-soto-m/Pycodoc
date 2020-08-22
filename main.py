#!/usr/bin/python3

import sys
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

import centwidg as CW

class GuiApp(QW.QMainWindow):
	def __init__(self):
		super().__init__()
		self.defineMenuBar()
		#self.cwidg=CW.centralWidget()
		#self.setCentralWidget(self.cwidg)
		self.show()
		#a=auxsz();
		#a.toscalescreen(self,-1,1)
	def defineMenuBar(self):
		exitAct = QW.QAction('&Quit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(QW.qApp.quit)
		fileMenu = self.menuBar().addMenu('&File')
		fileMenu.addAction(exitAct)

def main():
	app=QW.QApplication(sys.argv)
	ex=GuiApp()
	sys.exit(app.exec_())
if __name__=="__main__":
	main()
