from PyQt5.QtWidgets import QToolBar
from .History import history
from .Opener import opener
from .SearchWidg import searchWidg
from .SplitButton import splitButton
from .StyleButton import styleButton

class toolBar(QToolBar):

    def __init__(self, parent):
        super().__init__(parent)

        self.histmen=history(parent)
        self.fileopener=opener(parent)
        self.combosearch=searchWidg(parent)
        self.spliter=splitButton(parent)
        self.styler=styleButton(parent)

        self.addAction(self.histmen)
        self.addAction(self.styler)
        self.addAction(self.spliter.split)
        self.addAction(self.spliter.unsplit)
        self.addAction(self.fileopener)
        self.addWidget(self.combosearch)
