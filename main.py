#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow.MainWindow import GuiApp

def main():
	app=QApplication(sys.argv)
	ex=GuiApp()
	sys.exit(app.exec_())
	
if __name__=="__main__":
	main()
