from glob_objects.globalxml import (
    histRoot,
    BehaviourRoot,
    filesRoot,
    styleLocsRoot,
)
from PyQt5.QtWidgets import QTextBrowser
from FileManage.fileElement import fileElement
from pathlib import Path


class TextEditor(QTextBrowser):
    def __init__(self, files, papa, NoHist, styleFile=None):
        super().__init__(),
        self.parent = papa
        self.setAcceptDrops(True)
        self.setReadOnly(True)
        self.files = files
        if files.isFile():
            with open(files.fileStrPath(), 'r') as f:
                data = f.read()
                self.setText(data)
            if not NoHist:
                histRoot.insert(0, files.createHistElement())
                while (len(list(histRoot))
                       > int(BehaviourRoot.find('HistDepth').text)
                       > -1):
                    histRoot.remove(histRoot.find('Elem[last()]'))
        else:
            self.setReadOnly(True)
            errfile = filesRoot.find('Elem[@error=\'True\']')
            if errfile is not None and errfile:
                files = fileElement(errfile)
            else:
                files = fileElement()
            if files.isFile():
                with open(files.fileStrPath(), 'r') as f:
                    data = f.read()
                    self.setText(data)
        self.stylize(styleFile)

    def stylize(self, styleFile):
        if styleFile is not None and styleFile.isstyle():
            with open(styleFile.fileStrPath(), 'r') as f:
                data = f.read()
                self.setStyleSheet(data)
        else:
            errstyle = styleLocsRoot.find('Elem[@error=\'True\']')
            if errstyle is not None and errstyle:
                style = fileElement(errstyle, style=True)
            else:
                style = fileElement(style=True)
            if style.isFile():
                with open(style.fileStrPath(), 'r') as f:
                    data = f.read()
                    self.setStyleSheet(data)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, evie):
        ''' I don't have the slightest idea why but it doesn't work without the
        event override. Maybe the implementation cancels the event by default,
        but that is quite messed up.
        '''
        pass

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            if Path(url.path()).is_file():
                fielem = fileElement(url.path())
                self.parent.tabAdder(fielem)
