from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QDesktopWidget, QLabel, QSpinBox, QCheckBox, QComboBox, QPushButton
from PyQt5.QtGui import QIcon
from glob_objects.globalxml import BehaviourRoot
from shutil import which

class BehaviourWidget (QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('Behaviour settings')
        self.setWindowIcon(QIcon('../data/AppIcon/AppIcon.svg'))

    def showWid(self):
        self.__init__(self.parent)
        L = QVBoxLayout()

        scrollLayout = self.centralLayout()

        globber = QWidget()
        globber.setLayout(scrollLayout)
        scroll = QScrollArea()
        scroll.setWidget(globber)
        scroll.setWidgetResizable(True)

        L.addWidget(scroll)
        L.addLayout(self.bottomBar())

        self.setLayout(L)

        geo = QDesktopWidget().availableGeometry()
        self.resize(self.sizeHint())
        self.move(int(geo.center().x() - self.width()/2), int(geo.center().y() - self.height()/2))


        self.show()

    def centralLayout(self):
        lay = QVBoxLayout()
        lay.addWidget(QLabel('Some changes may need a restart of the application in order to take effect'))
        lay.addLayout(self.tabBarAHLayout())
        if which('pandoc') is not None:
            lay.addLayout(self.pandocLayout())
            lay.addLayout(self.pandocbehaveLayout())
        lay.addLayout(self.lastTabLayout())
        lay.addLayout(self.behaviourLayout())

        return lay

    def behaviourLayout(self):
        lay = QHBoxLayout()
        lbl = QLabel('History Depth:')
        self.depth = QSpinBox()
        self.depth.setValue(int(BehaviourRoot.find('HistDepth').text))
        lay.addWidget(lbl)
        lay.addWidget(self.depth)
        return lay

    def tabBarAHLayout(self):
        lay = QHBoxLayout()
        lbl = QLabel('Automatically hide tab bar:')
        self.hiderTB = QCheckBox('\t\t')
        self.hiderTB.stateChanged.connect(self.changeTBAHLabel)

        boool = BehaviourRoot.find('TabBarAutoHide').text  in ['Remain', 'remain', 'R', 'r']
        self.hiderTB.setChecked(boool)
        self.changeTBAHLabel(boool)

        lay.addWidget(lbl)
        lay.addWidget(self.hiderTB)
        return lay

    def changeTBAHLabel(self, signal):
        if signal == False:
            self.hiderTB.setText('Hide\t')
        else:
            self.hiderTB.setText('Remain')

    def changeHtmlLayoutLabel(self, signal):
        if signal == False:
            self.beauHTML.setText('No\t')
        else:
            self.beauHTML.setText('Yes\t')

    def pandocLayout(self):
        lay = QHBoxLayout()
        lbl = QLabel('Enable pandoc:')
        self.pan = QCheckBox('\t\t')
        self.pan.stateChanged.connect(self.changeLayoutLabel)

        boool = BehaviourRoot.find('Pandoc').text  in ['Yes', 'yes', 'Y', 'y']
        self.pan.setChecked(boool)
        self.changeLayoutLabel(boool)

        lay.addWidget(lbl)
        lay.addWidget(self.pan)
        return lay

    def changeLayoutLabel(self, signal):
        if signal == False:
            self.pan.setText('No\t')
        else:
            self.pan.setText('Yes\t')

    def lastTabLayout(self):
        lay = QHBoxLayout()
        lbl = QLabel('When trying to close the last tab')
        self.lastTabCB = QComboBox()
        self.lastTabCB.addItem('show Welcome tab')
        self.lastTabCB.addItem('show no tab')
        self.lastTabCB.addItem('don\'t')
        self.lastTabCB.addItem('quit app')


        tr1 = {i: 0 for i in ['Welcome', 'welcome', 'W', 'w']}
        tr2 = {i: 1 for i in ['None', 'none', 'N', 'n']}
        tr3 = {i: 2 for i in ['Persist', 'persist', 'P', 'p']}
        tr1.update(tr2)
        tr1.update(tr3)

        try:
            state = tr1[BehaviourRoot.find('LastTabRemoved').text]
        except:
            state = 3
        self.lastTabCB.setCurrentIndex(state)

        lay.addWidget(lbl)
        lay.addWidget(self.lastTabCB)
        return lay

    def pandocbehaveLayout(self):
        lay = QHBoxLayout()
        lbl = QLabel('If pandoc is enabled non html files')
        self.hpandocCB = QComboBox()
        self.hpandocCB.addItem('Create html and show it')
        self.hpandocCB.addItem('Create html and don\'t show it')
        self.hpandocCB.addItem('Show a popup to confirm wether')
        self.hpandocCB.addItem('Shortcut to create and show html')


        tr1 = {i: 0 for i in ['Create and show', 'create; show', 'CS', 'cs']}
        tr2 = {i: 1 for i in ['Create', 'create', 'C', 'c']}
        tr3 = {i: 2 for i in ['Popup', 'popup', 'P', 'p']}
        tr4 = {i: 3 for i in ['Shortcut', 'shortcut', 'S', 's']}
        tr1.update(tr2)
        tr1.update(tr3)
        tr1.update(tr4)

        try:
            state = tr1[BehaviourRoot.find('Hpandoc').text]
        except:
            state = 0

        self.hpandocCB.setCurrentIndex(state)

        lay.addWidget(lbl)
        lay.addWidget(self.hpandocCB)
        return lay

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
        BehaviourRoot.find('HistDepth').text = str(self.depth.value())
        if self.hiderTB.isChecked():
            stri = 'R'
        else:
            stri = 'H'
        BehaviourRoot.find('TabBarAutoHide').text = stri

        tr = {0: 'W', 1: 'N', 2: 'P', 3: 'Q'}
        BehaviourRoot.find('LastTabRemoved').text = tr[self.lastTabCB.currentIndex()]

        if (which('pandoc') is not None):
            tr = {0: 'CS', 1: 'C', 2: 'P', 3: 'S'}
            BehaviourRoot.find('Hpandoc').text = tr[self.hpandocCB.currentIndex()]

        if (which('pandoc') is not None) and self.pan.isChecked():
            stri = 'Y'
        else:
            stri = 'N'
        BehaviourRoot.find('Pandoc').text = stri
        self.hide()

    def cancelHandle(self):
        self.hide()
