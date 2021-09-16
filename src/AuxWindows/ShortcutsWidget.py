from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QDesktopWidget, QSizePolicy, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from glob_objects.globalxml import ShortRoot

class ShortcutsWidget (QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Shortcut settings")
        self.setWindowIcon(QIcon('AppIcon/AppIcon.svg'))

    def showWid(self):
        self.__init__(self.parent)
        L = QVBoxLayout()
        scl = QVBoxLayout()
        self.txts = []

        for elem in ShortRoot.findall("*"):
            scl.addLayout(self.shctLayout(elem))

        globber = QWidget()
        globber.setLayout(scl)
        scroll = QScrollArea()
        scroll.setWidget(globber)
        scroll.setWidgetResizable(True)

        L.addWidget(scroll)
        L.addLayout(self.bottomBar())

        self.setLayout(L)

        geo = QDesktopWidget().availableGeometry()
        self.resize(self.sizeHint())
        self.move(int(geo.center().x()-self.width()/2), int(geo.center().y()-self.height()/2))

        self.show()

    def shctLayout(self, elem):
        lbl = QLabel(elem.get("Title")+":")
        txt = QLineEdit(elem.text)

        exppol = QSizePolicy().Policy.Expanding
        minpol = QSizePolicy().Policy.Fixed

        lbl.setSizePolicy(exppol, minpol)
        txt.setSizePolicy(exppol, minpol)

        self.txts.append(txt)

        hz = QHBoxLayout()

        hz.addWidget(lbl)
        hz.addWidget(txt)

        return hz

    def bottomBar(self):
        applyBtn = QPushButton('Apply', self)
        applyBtn.clicked.connect(self.applyHandle)
        cancelBtn = QPushButton('Cancel', self)
        cancelBtn.clicked.connect(self.cancelHandle)

        horz = QHBoxLayout()
        horz.addStretch(1)
        horz.addWidget(applyBtn)
        horz.addWidget(cancelBtn)
        return horz

    def applyHandle(self):
        idx = 0
        for elem in ShortRoot.findall("*"):
            elem.text = self.txts[idx].text()
            idx += 1
        self.parent.shctobj.refresh()
        self.hide()

    def cancelHandle(self):
        self.hide()
