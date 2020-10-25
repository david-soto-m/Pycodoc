#!/usr/bin/python3
# An installer that will create a dektop file and try to add it to your apps menu
from pathlib import Path
from os import geteuid
def main ():
	path1=str(Path(__file__).parent.resolve())+"/main.py"
	path2=str(Path(__file__).parent.resolve())+"/AppIcon/AppIcon.svg"
	stri="[Desktop Entry]\nEncoding=UTF-8\nType=Application\nTerminal=false\nCategories=Development;Documentation\nExec=%s\nName=Pycodoc\nIcon=%s"% (path1,path2)
	if geteuid() == 0:
		target="/usr/share/applications/Pycodoc.desktop"
	else:
		target=str(Path.home())+"/.local/share/applications/Pycodoc.desktop"
	with open(target,"w+") as f:
		f.write(stri)
if __name__=="__main__":
	main()
