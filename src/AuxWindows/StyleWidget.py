from PyQt5.QtWidgets import (
    QWidget,
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QLineEdit,
    QLabel,
    QPushButton,
    QDesktopWidget,
    QColorDialog,
    QFontDialog,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from FileManage.fileElement import fileElement
from pathlib import Path
from glob_objects.globalxml import GConfigRoot, styleLocsRoot


class StyleWidget (QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def showWid(self):
        self.__init__(self.parent)
        self.setWindowTitle('Style Creator')
        self.setWindowIcon(QIcon('../data/AppIcon/AppIcon.svg'))
        self.dictio = {
            'color': '',
            'background-color': '',
            'selection-color': '',
            'selection-background-color': '',
            'font-family': '',
            'font-weight': '',
            'font-style': '',
            'font-size': '',
            'text-decoration': '',
            }

        minpol = QSizePolicy().Policy.Fixed

        L = QVBoxLayout()

        self.lbl = QTextEdit('''\
<h1>Lorem ipsum</h1>
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque
porro quisquam est, qui do<u>lorem ipsum</u> quia <u>dolor sit amet</u>,
consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut
labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam,
quis nostrum exercitationem ullam corporis suscipit laboriosam, <b>nisi ut
aliquid ex ea commodi consequatur</b>? Quis autem vel eum iure reprehenderit
qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui
dolorem eum fugiat quo voluptas nulla pariatur?\
''')
        self.lbl.setStyleSheet('QTextEdit{}')
        L.addWidget(self.lbl)

        horx = QHBoxLayout()
        namelbl = QLabel('Style name: ')
        namelbl.setSizePolicy(minpol, minpol)
        self.name = QLineEdit()
        horx.addWidget(namelbl)
        horx.addWidget(self.name)
        L.addLayout(horx)

        fnt = QPushButton('Font')
        fnt.clicked.connect(self.fontLauncher)
        L.addWidget(fnt)

        bcl = QPushButton('Background Colour')
        bcl.clicked.connect(self.bColorLauncher)
        L.addWidget(bcl)

        cl = QPushButton('Text Colour')
        cl.clicked.connect(self.colorLauncher)
        L.addWidget(cl)

        bscl = QPushButton('Selection Background Colour')
        bscl.clicked.connect(self.bSelColorLauncher)
        L.addWidget(bscl)

        scl = QPushButton('Selection Text Colour')
        scl.clicked.connect(self.selColorLauncher)
        L.addWidget(scl)

        L.addLayout(self.bottomBar())

        self.setLayout(L)

        geo = QDesktopWidget().availableGeometry()
        self.resize(self.sizeHint())
        self.move(
            int(geo.center().x()-self.width()/2),
            int(geo.center().y()-self.height()/2)
        )

        self.show()

    def colorLauncher(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.dictio['color'] = col.name()
            self.lbl.setStyleSheet(
                self.lbl.styleSheet()[: -1]
                + '\n\tcolor: %s;}' % col.name()
            )

    def bColorLauncher(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.dictio['background-color'] = col.name()
            self.lbl.setStyleSheet(
                self.lbl.styleSheet()[:-1]
                + '\n\tbackground-color: %s;}' % col.name()
            )

    def selColorLauncher(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.dictio['selection-color'] = col.name()
            self.lbl.setStyleSheet(
                self.lbl.styleSheet()[:-1]
                + '\n\tselection-color: %s;}' % col.name()
            )

    def bSelColorLauncher(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.dictio['selection-background-color'] = col.name()
            self.lbl.setStyleSheet(
                self.lbl.styleSheet()[:-1]
                + '\n\tselection-background-color: %s;}' % col.name()
                )

    def fontLauncher(self):
        fontd = QFontDialog()
        font, ok = fontd.getFont(self)
        if ok:
            self.dictio['font-family'] = font.family()
            self.dictio['font-size'] = str(font.pointSize())

            dic = {
                0: 'Thin',
                12: 'ExtraLight',
                25: 'Light',
                50: 'Normal',
                57: 'Medium',
                63: 'DemiBold',
                75: 'Bold',
                81: 'ExtraBold',
                87: 'Black'}
            try:
                stri = dic[font.weight()]
            except:
                stri = 'normal'
            self.dictio['font-weight'] = stri

            dic = {0: 'normal', 1: 'italic', 2: 'oblique'}
            try:
                stri = dic[font.style()]
            except:
                stri = 'normal'
            self.dictio['font-style'] = stri

            self.dictio['text-decoration'] = ''
            if font.strikeOut():
                self.dictio['text-decoration'] = 'line-through'
            if font.underline():
                self.dictio['text-decoration'] += ' underline'

            self.lbl.setFont(font)

    def createHandle(self):
        if self.name.text() == '':
            QMessageBox.question(
                self,
                'Error',
                'You need a name for the style',
                QMessageBox.Ok,
                QMessageBox.Ok
            )
        else:
            stri = 'QTextEdit{\n'
            for item in self.dictio:
                stri += '\t%s: %s;\n' % (item, self.dictio[item])
            stri += '}'
            namePath = str(
                Path(
                    GConfigRoot.find('StyleLocs/Path').text
                ).parent
            )
            + '/'
            + self.name.text()
            + '.css'
            elem = fileElement(namePath, style=True)
            xmly = elem.createFileElement()
            styleLocsRoot.append(xmly)

            with open(namePath, 'w+') as f:
                f.write(stri)

            self.parent.tlb.combosearch.searchMenu()
            self.hide()

    def cancelHandle(self):
        self.hide()

    def bottomBar(self):
        applyBtn = QPushButton('Create', self)
        applyBtn.clicked.connect(self.createHandle)
        cancelBtn = QPushButton('Cancel', self)
        cancelBtn.clicked.connect(self.cancelHandle)

        horz = QHBoxLayout()
        horz.addStretch(1)
        horz.addWidget(applyBtn)
        horz.addWidget(cancelBtn)
        return horz
