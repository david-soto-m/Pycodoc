#!/usr/bin/python3
import os
import sys
from PyQt5.QtWidgets import QApplication
from MainWindow.MainWindow import GuiApp

def pathToRootOfProject():
	direc=__file__
	notthere=True
	idx=len(direc)-1
	while notthere:
		direc=direc[0:idx]
		idx-=1
		if direc[idx]=='/':
			notthere=False
	return direc

def main():
	os.chdir(pathToRootOfProject())
	app=QApplication(sys.argv)
	ex=GuiApp()
	app.exec_()
	sys.exit(exiter())
def exiter():
	print("End")
if __name__=="__main__":
	main()
