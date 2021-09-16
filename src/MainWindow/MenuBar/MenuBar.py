from PyQt5.QtWidgets import QAction, QMenuBar, qApp
from PyQt5.QtGui import QIcon
from AuxWindows.FilesWidget import FilesWidget
from  AuxWindows.BehaviourWidget import BehaviourWidget
from  AuxWindows.ShortcutsWidget import ShortcutsWidget
from ..ToolBar.ToolBar import opener

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        fileMenu = self.addMenu('&File')

        #These (↓) actions are remembered in order to be accessed by shortcuts
        self.exitAct = QAction(QIcon().fromTheme("application-exit"), 'Quit', parent)
        self.exitAct.triggered.connect(qApp.quit)

        self.fileopener=opener(parent=parent, string="Open")#DRY AF

        fileMenu.addAction(self.exitAct)
        fileMenu.addAction(self.fileopener)

        settingsMenu = self.addMenu('&Settings')

        self.FilesManager=FilesWidget(parent)
        self.editFiles=QAction(QIcon().fromTheme("kt-queue-manager"), 'Configure Files', parent)
        self.editFiles.triggered.connect(self.FilesManager.showWind)

        self.StylesManager=FilesWidget(parent, style=True)
        self.editStyles=QAction(QIcon().fromTheme("color-management"), 'Configure Style Files', parent)
        self.editStyles.triggered.connect(self.StylesManager.showWind)

        self.shortcutsManager=ShortcutsWidget(parent)
        self.shortcutSettings=QAction(QIcon().fromTheme("configure-shortcuts"), 'Configure Shortcuts', parent)
        self.shortcutSettings.triggered.connect(self.shortcutsManager.showWid)

        self.behaviourManager=BehaviourWidget(parent)
        self.behaviourSettings=QAction(QIcon().fromTheme("settings-configure"), 'Configure Pycodoc', parent)
        self.behaviourSettings.triggered.connect(self.behaviourManager.showWid)


        settingsMenu.addAction(self.editFiles)
        settingsMenu.addAction(self.editStyles)
        settingsMenu.addSeparator()
        settingsMenu.addAction(self.shortcutSettings)
        settingsMenu.addAction(self.behaviourSettings)
