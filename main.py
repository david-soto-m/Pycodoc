#!/usr/bin/python3
import os
import sys
from PyQt5.QtWidgets import QApplication
from MainWindow.MainWindow import GuiApp
import glob_objects.globalxml as GXML
import xml.etree.ElementTree as ET
from pathlib import Path

def main():
	os.chdir(str(Path(__file__).parent)+"/")
	app=QApplication(sys.argv)
	ex=GuiApp()
	app.exec_()
	sys.exit(exiter())
	
def exiter():
	GXML.History.write(GXML.GConfigRoot.find("History/Path").text)
if __name__=="__main__":
        main()
