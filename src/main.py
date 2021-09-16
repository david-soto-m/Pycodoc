#!/usr/bin/python3
import os
import sys
from PyQt5.QtWidgets import QApplication
from MainWindow.MainWindow import GuiApp
import glob_objects.globalxml as GXML
from pathlib import Path

def main():
	os.chdir(str(Path(__file__).parent)+"/")
	app=QApplication(sys.argv)
	ex=GuiApp()
	app.exec_()
	sys.exit(exiter())
	
def exiter():
	GXML.History.write(GXML.GConfigRoot.find("History/Path").text)
	GXML.Files.write(GXML.GConfigRoot.find("Files/Path").text)
	GXML.StyleLocs.write(GXML.GConfigRoot.find("StyleLocs/Path").text)
	GXML.Shortcuts.write(GXML.GConfigRoot.find("Shortcuts/Path").text)
	GXML.Behaviour.write(GXML.GConfigRoot.find("Behaviour/Path").text)
if __name__=="__main__":
        main()
