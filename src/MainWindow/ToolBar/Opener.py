from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtGui import QIcon
from FileManage.fileElement import fileElement
from pathlib import Path

class opener(QAction):
    def __init__(self, parent, string=None):
        super().__init__()
        self.parent=parent
        self.setIcon(QIcon().fromTheme('document-open'))
        self.setToolTip('Open a file')
        self.triggered.connect(self.OpenWidget)
        if type(string) is str:
            self.setText(string)

    def OpenWidget(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileNames(caption='Open file', directory=home_dir)
        if fname[0]:
            for each in fname[0]:
                if Path(each).is_file():
                    fielem=fileElement(each)
                    self.parent.cwidg.tabAdder(fielem)
