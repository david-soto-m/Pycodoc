from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QDesktopWidget,
    QSizePolicy,
    QButtonGroup,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QCheckBox,
    QLabel
)
from PyQt5.QtGui import QIcon
from glob_objects.globalxml import styleLocsRoot, filesRoot
from FileManage.fileElement import fileElement


class FilesWidget (QWidget):
    def __init__(self, parent=None, style=False):
        super().__init__()
        self.parent = parent
        self.style = style
        if self.style:
            self.setWindowTitle('Style files settings')
        else:
            self.setWindowTitle('Files settings')

        self.setWindowIcon(QIcon('../data/AppIcon/AppIcon.svg'))

        self.itemElim = []
        self.btnsElim = []
        self.titleEdits = []
        self.filePathEdits = []
        self.showCBoxes = []
        self.errorRBtns = []
        self.defaultRBtns = []

        self.scrollVert = QVBoxLayout()

    def showWind(self):
        self.__init__(self.parent, self.style)

        if self.style:
            files = styleLocsRoot
        else:
            files = filesRoot

        vert = QVBoxLayout()

        self.defaultContainer = QButtonGroup()
        self.errorContainer = QButtonGroup()

        for child, index in zip(files, range(len(files))):
            Elem = fileElement(child)
            self.scrollVert.addLayout(
                self.listAdder(
                    title=Elem.title.text,
                    path=Elem.fileStrPath(),
                    child=child
                )
            )

        globber = QWidget()
        globber.setLayout(self.scrollVert)
        scroll = QScrollArea()
        scroll.setWidget(globber)
        scroll.setWidgetResizable(True)

        vert.addWidget(scroll)

        vert.addLayout(self.bottomBar())

        self.setLayout(vert)

        geo = QDesktopWidget().availableGeometry()
        self.resize(self.sizeHint())
        self.move(
            int(geo.center().x() - self.width()/2),
            int(geo.center().y() - self.height()/2)
        )

        self.show()

    def listAdder(self, path='', title='', child=None):
        exppol = QSizePolicy().Policy.Expanding
        minpol = QSizePolicy().Policy.Fixed

        filelbl = QLabel('File: ')
        titlelbl = QLabel('Title: ')
        pathlbl = QLabel('Path: ')

        filelbl.setSizePolicy(minpol, minpol)
        titlelbl.setSizePolicy(minpol, minpol)
        pathlbl.setSizePolicy(minpol, minpol)

        index = len(self.itemElim)

        self.itemElim.append(False)
        self.btnsElim.append(
            QPushButton(
                QIcon().fromTheme('list - remove'),
                '',
                self
            )
        )
        self.titleEdits.append(QLineEdit(title))
        self.filePathEdits.append(QLineEdit(path))
        if self.style:
            self.showCBoxes.append(QCheckBox('Show on menu', self))
        else:
            self.showCBoxes.append(QCheckBox('Show on searchbar', self))
        self.defaultRBtns.append(QRadioButton('Show on start', self))
        self.errorRBtns.append(QRadioButton('Show on error', self))

        self.showCBoxes[index].setTristate(on=False)

        self.defaultContainer.addButton(self.defaultRBtns[index])
        self.errorContainer.addButton(self.errorRBtns[index])

        self.btnsElim[index].clicked.connect(self.elimHandler)
        if child is not None:
            self.showCBoxes[index].setChecked(child.get('show') == 'True')
            self.defaultRBtns[index].setChecked(child.get('default') == 'True')
            self.errorRBtns[index].setChecked(child.get('error') == 'True')

        self.btnsElim[index].setSizePolicy(minpol, minpol)
        self.titleEdits[index].setSizePolicy(exppol, minpol)
        self.filePathEdits[index].setSizePolicy(exppol, minpol)
        self.showCBoxes[index].setSizePolicy(minpol, minpol)
        self.defaultRBtns[index].setSizePolicy(minpol, minpol)
        self.errorRBtns[index].setSizePolicy(minpol, minpol)

        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        h3 = QHBoxLayout()

        h1.addWidget(titlelbl)
        h1.addWidget(self.titleEdits[index])

        h2.addWidget(pathlbl)
        h2.addWidget(self.filePathEdits[index])

        h3.addWidget(self.showCBoxes[index])
        h3.addWidget(self.defaultRBtns[index])
        h3.addWidget(self.errorRBtns[index])
        h3.addWidget(self.btnsElim[index])

        microvert = QVBoxLayout()

        microvert.addWidget(filelbl)
        microvert.addLayout(h1)
        microvert.addLayout(h2)
        microvert.addLayout(h3)

        return microvert

    def elimHandler(self):
        idx = self.btnsElim.index(self.sender())
        if not self.itemElim[idx]:
            self.btnsElim[idx].setStyleSheet(
                'QWidget { background-color: red}'
            )
            self.itemElim[idx] = True
        else:
            self.btnsElim[idx].setStyleSheet('QWidget { background-color:}')
            self.itemElim[idx] = False

    def applyHandle(self):
        if self.style:
            styleLocsRoot.clear()
            for idx in range(len(self.itemElim)):
                if not self.itemElim[idx]:
                    elem = fileElement(
                        self.filePathEdits[idx].text(),
                        style=True
                    )
                    if elem.isFile() and elem.isFormat('.css'):
                        elem.title.text = self.titleEdits[idx].text()
                        xellie = elem.createFileElement(
                            show=self.showCBoxes[idx].isChecked(),
                            default=self.defaultRBtns[idx].isChecked(),
                            error=self.errorRBtns[idx].isChecked()
                        )
                        styleLocsRoot.append(xellie)
        else:
            filesRoot.clear()
            for idx in range(len(self.itemElim)):
                if not self.itemElim[idx]:
                    elem = fileElement(self.filePathEdits[idx].text())
                    if elem.isFile():
                        elem.title.text = self.titleEdits[idx].text()
                        xellie = elem.createFileElement(
                            show=self.showCBoxes[idx].isChecked(),
                            default=self.defaultRBtns[idx].isChecked(),
                            error=self.errorRBtns[idx].isChecked()
                        )
                        filesRoot.append(xellie)
            self.parent.tlb.combosearch.searchMenu()
        self.hide()

    def cancelHandle(self):
        self.hide()

    def newHandle(self):
        self.scrollVert.addLayout(self.listAdder())

    def bottomBar(self):
        newBtn = QPushButton('New', self)
        newBtn.clicked.connect(self.newHandle)
        applyBtn = QPushButton('Apply', self)
        applyBtn.clicked.connect(self.applyHandle)
        cancelBtn = QPushButton('Cancel', self)
        cancelBtn.clicked.connect(self.cancelHandle)

        horz = QHBoxLayout()
        horz.addWidget(newBtn)
        horz.addStretch(1)
        horz.addWidget(applyBtn)
        horz.addWidget(cancelBtn)
        return horz
