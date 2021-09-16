from PyQt5.QtWidgets import QComboBox, QSizePolicy 
from PyQt5.QtCore import QVariant
from glob_objects.globalxml import filesRoot
from FileManage.fileElement import fileElement

class searchWidg(QComboBox):
    def __init__(self, parent):
        super().__init__()
        self.parent=parent
        expand=QSizePolicy().Policy.Expanding
        self.setSizePolicy(expand, expand)
        self.setAcceptDrops(True)
        self.setEditable(True)
        self.activated.connect(self.comboChanged)
        self.searchMenu()
        self.setCurrentIndex(-1)

    def searchMenu(self):
        self.clear()
        self.Elem=[]
        for child in filesRoot.findall("Elem[@show='True']"):
            self.Elem.append(fileElement(child))
        self.Elem.sort(key=lambda indiv: indiv.fileStrPath())
        pathsep=""
        for item in self.Elem:
            if pathsep!=item.direc.text and pathsep!="":
                self.insertSeparator(self.count())
            self.addItem(item.title.text, QVariant(item))
            pathsep=item.direc.text
        self.setMaxVisibleItems(self.count())
        self.setCurrentIndex(-1)

    def comboChanged(self, idx):
        fielem=self.itemData(idx, 0x100)
        if fielem is not None:
            self.parent.cwidg.tabAdder(fielem)
        else:
            fielem=fileElement(self.itemText(idx))
            self.parent.cwidg.tabAdder(fielem)
