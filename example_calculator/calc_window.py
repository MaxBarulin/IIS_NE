import os


from nodeeditor.node_scene import Scene
from qtpy.QtGui import QIcon, QKeySequence
from qtpy.QtWidgets import QMdiArea, QWidget, QDockWidget, QAction, QMessageBox, QFileDialog, QMenu
from qtpy.QtCore import Qt, QSignalMapper

from nodeeditor.utils import loadStylesheets
from nodeeditor.node_editor_window import NodeEditorWindow
from example_calculator.calc_sub_window import CalculatorSubWindow
from example_calculator.calc_drag_listbox import QDMDragListbox, QDMDragListbox1, QDMDragListbox2, QDMDragListbox3
from nodeeditor.utils import dumpException, pp
from example_calculator.calc_conf import CALC_NODES
from nodeeditor.node_edge import EDGE_TYPE_BEZIER, EDGE_TYPE_DIRECT, EDGE_TYPE_SQUARE


# Enabling edge validators
from nodeeditor.node_edge import Edge
from nodeeditor.node_edge_validators import (
    edge_validator_debug,
    edge_cannot_connect_two_outputs_or_two_inputs,
    edge_cannot_connect_input_and_output_of_same_node
)
Edge.registerEdgeValidator(edge_validator_debug)
Edge.registerEdgeValidator(edge_cannot_connect_two_outputs_or_two_inputs)
Edge.registerEdgeValidator(edge_cannot_connect_input_and_output_of_same_node)


# images for the dark skin
import example_calculator.qss.nodeeditor_dark_resources

DEBUG = False

open_img_fa = "i64.ico"
put = os.path.dirname(__file__)
path_img_fa = f'{put}\\nodes\\icons\\{open_img_fa}'
print(path_img_fa)


class CalculatorWindow(NodeEditorWindow):

    def initUI(self):
        self.name_company = 'MaxB'
        self.name_product = 'IIS node editor'

        self.stylesheet_filename = os.path.join(os.path.dirname(__file__), "qss/nodeeditor.qss")
        loadStylesheets(
            os.path.join(os.path.dirname(__file__), "qss/nodeeditor.qss"),
            self.stylesheet_filename
        )

        self.empty_icon = QIcon(".")

        if DEBUG:
            print("Registered nodes:")
            pp(CALC_NODES)


        self.mdiArea = QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setViewMode(QMdiArea.TabbedView)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.setCentralWidget(self.mdiArea)

        self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.windowMapper = QSignalMapper(self)
        self.windowMapper.mapped[QWidget].connect(self.setActiveSubWindow)

        self.createNodesDock0()
        self.createNodesDock1()
        self.createNodesDock2()
        self.createNodesDock3()

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.updateMenus()

        self.readSettings()

        self.setWindowTitle("IIS node editor")
        self.setWindowIcon(QIcon(path_img_fa))

    def closeEvent(self, event):
        self.mdiArea.closeAllSubWindows()
        if self.mdiArea.currentSubWindow():
            event.ignore()
        else:
            self.writeSettings()
            event.accept()
            # hacky fix for PyQt 5.14.x
            import sys
            sys.exit(0)


    def createActions(self):
        super().createActions()

        self.actClose = QAction("Закрыть", self, statusTip="Close the active window", triggered=self.mdiArea.closeActiveSubWindow)
        self.actCloseAll = QAction("Закрыть все", self, statusTip="Close all the windows", triggered=self.mdiArea.closeAllSubWindows)
        self.actTile = QAction("Разместить", self, statusTip="Tile the windows", triggered=self.mdiArea.tileSubWindows)
        self.actCascade = QAction("Каскадом", self, statusTip="Cascade the windows", triggered=self.mdiArea.cascadeSubWindows)
        self.actNext = QAction("Следующее", self, shortcut=QKeySequence.NextChild, statusTip="Move the focus to the next window", triggered=self.mdiArea.activateNextSubWindow)
        self.actPrevious = QAction("Предыдущее", self, shortcut=QKeySequence.PreviousChild, statusTip="Move the focus to the previous window", triggered=self.mdiArea.activatePreviousSubWindow)

        self.actSeparator = QAction(self)
        self.actSeparator.setSeparator(True)

        self.actAbout = QAction("О проекте", self, statusTip="Show the application's About box", triggered=self.about)
        self.actBezier = QAction("1", self, statusTip="Bezier", triggered=self.socket)
        self.actDirect = QAction("2", self, statusTip="Direct", triggered=self.socket1)
        self.actSquare = QAction("3", self, statusTip="Square", triggered=self.socket2)

    def getCurrentNodeEditorWidget(self):
        """ we're returning NodeEditorWidget here... """
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def onFileNew(self):
        try:
            subwnd = self.createMdiChild()
            subwnd.widget().fileNew()
            subwnd.show()
        except Exception as e: dumpException(e)


    def onFileOpen(self):
        fnames, filter = QFileDialog.getOpenFileNames(self, 'Open graph from file', self.getFileDialogDirectory(), self.getFileDialogFilter())

        try:
            for fname in fnames:
                if fname:
                    existing = self.findMdiChild(fname)
                    if existing:
                        self.mdiArea.setActiveSubWindow(existing)
                    else:
                        # we need to create new subWindow and open the file
                        nodeeditor = CalculatorSubWindow()
                        if nodeeditor.fileLoad(fname):
                            self.statusBar().showMessage("File %s loaded" % fname, 5000)
                            nodeeditor.setTitle()
                            subwnd = self.createMdiChild(nodeeditor)
                            subwnd.show()
                        else:
                            nodeeditor.close()
        except Exception as e: dumpException(e)


    def about(self):
        QMessageBox.about(self, 'О пректе "ISS node editor"',
                "<b>ISS node editor</b> предназначен для создания пользовательских процессов расчета норм на различные виды работ машиностроения.<br><br>"
                "Процессы строятся из нод, что позволяет визуализировать их, легко добавлять, изменять и сохранять уже имеющиеся, а так же упростить отладку и контроль.<br><br>"
                "Такой подход упрощает обучение и маштабирование. Делает программу универсальной для разных задач.<br><br>"
                "<h1><a style='color: white; text-decoration:none' href='https://t.me/Cvela_siren'>Max B</a></h1>")


    def socket(self):
        # open_img_icons = "pars4_(БУТ)multi.exe"
        #
        # put = os.path.dirname(__file__)
        # print(put)
        #
        # path_img_icons = f'{put}\\{open_img_icons}'
        # print(path_img_icons)
        # os.startfile(path_img_icons)

        # self.sa = Edge
        # self.sa.edge_type = EDGE_TYPE_BEZIER
        print("1")

    def socket1(self):
        # self.sa = Edge
        # self.sa.edge_type = EDGE_TYPE_DIRECT
        print("2")

    def socket2(self):
        # self.sa = Edge
        # self.sa.edge_type = EDGE_TYPE_SQUARE
        print("3")


    def createMenus(self):
        super().createMenus()

        self.windowMenu = self.menuBar().addMenu("Окно")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("Помощь")
        self.helpMenu.addAction(self.actAbout)

        self.editMenu.aboutToShow.connect(self.updateEditMenu)

        self.menuBar().addSeparator()

        self.windowMenu1 = self.menuBar().addMenu("Доп")
        self.updateWindowMenu1()
        self.windowMenu1.aboutToShow.connect(self.updateWindowMenu1)

    def updateMenus(self):
        # print("update Menus")
        active = self.getCurrentNodeEditorWidget()
        hasMdiChild = (active is not None)

        self.actSave.setEnabled(hasMdiChild)
        self.actSaveAs.setEnabled(hasMdiChild)
        self.actClose.setEnabled(hasMdiChild)
        self.actCloseAll.setEnabled(hasMdiChild)
        self.actTile.setEnabled(hasMdiChild)
        self.actCascade.setEnabled(hasMdiChild)
        self.actNext.setEnabled(hasMdiChild)
        self.actPrevious.setEnabled(hasMdiChild)
        self.actSeparator.setVisible(hasMdiChild)

        self.updateEditMenu()

    def updateEditMenu(self):
        try:
            # print("update Edit Menu")
            active = self.getCurrentNodeEditorWidget()
            hasMdiChild = (active is not None)

            self.actPaste.setEnabled(hasMdiChild)

            self.actCut.setEnabled(hasMdiChild and active.hasSelectedItems())
            self.actCopy.setEnabled(hasMdiChild and active.hasSelectedItems())
            self.actDelete.setEnabled(hasMdiChild and active.hasSelectedItems())

            self.actUndo.setEnabled(hasMdiChild and active.canUndo())
            self.actRedo.setEnabled(hasMdiChild and active.canRedo())
        except Exception as e: dumpException(e)



    def updateWindowMenu(self):
        self.windowMenu.clear()

        toolbar_nodes = self.windowMenu.addAction("Системные")
        toolbar_nodes.setCheckable(True)
        toolbar_nodes.triggered.connect(self.onWindowNodesToolbar0)
        toolbar_nodes.setChecked(self.nodesDock0.isVisible())

        toolbar_nodes1 = self.windowMenu.addAction("Сверлильные")
        toolbar_nodes1.setCheckable(True)
        toolbar_nodes1.triggered.connect(self.onWindowNodesToolbar1)
        toolbar_nodes1.setChecked(self.nodesDock1.isVisible())

        toolbar_nodes2 = self.windowMenu.addAction("Токарные")
        toolbar_nodes2.setCheckable(True)
        toolbar_nodes2.triggered.connect(self.onWindowNodesToolbar2)
        toolbar_nodes2.setChecked(self.nodesDock2.isVisible())

        toolbar_nodes3 = self.windowMenu.addAction("Фрезерные")
        toolbar_nodes3.setCheckable(True)
        toolbar_nodes3.triggered.connect(self.onWindowNodesToolbar2)
        toolbar_nodes3.setChecked(self.nodesDock2.isVisible())



        self.windowMenu.addSeparator()

        self.windowMenu.addAction(self.actClose)
        self.windowMenu.addAction(self.actCloseAll)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.actTile)
        self.windowMenu.addAction(self.actCascade)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.actNext)
        self.windowMenu.addAction(self.actPrevious)
        self.windowMenu.addAction(self.actSeparator)

        windows = self.mdiArea.subWindowList()
        self.actSeparator.setVisible(len(windows) != 0)

        for i, window in enumerate(windows):
            child = window.widget()

            text = "%d %s" % (i + 1, child.getUserFriendlyFilename())
            if i < 9:
                text = '&' + text

            action = self.windowMenu.addAction(text)
            action.setCheckable(True)
            action.setChecked(child is self.getCurrentNodeEditorWidget())
            action.triggered.connect(self.windowMapper.map)
            self.windowMapper.setMapping(action, window)

    def updateWindowMenu1(self):

        self.windowMenu1.clear()
        s1 = self.windowMenu1.addAction(self.actBezier)

        s2 = self.windowMenu1.addAction(self.actDirect)

        s3 = self.windowMenu1.addAction(self.actSquare)

        #self.actBezier = QAction("Bezier", self, statusTip="Close the active window", triggered=self.mdiArea.closeActiveSubWindow)

       #bezierAct = self.windowMenu1.addAction("Bezier Edge")
        #bezierAct.setCheckable(True)


       #directAct = self.windowMenu1.addAction("Direct Edge")
        #directAct.setCheckable(True)


        #squareAct = self.windowMenu1.addAction("Square Edge")
        #squareAct.setCheckable(True)


        #context_menu = QMenu(self)
        #action = context_menu.exec_(self.mapToGlobal(event.pos()))
        #selected = None
        #item = self.scene.getItemAt(event.pos())
        #if hasattr(item, 'edge'):
        #    selected = item.edge


        #if selected and action == bezierAct: selected.edge_type = EDGE_TYPE_BEZIER
        #if selected and action == directAct: selected.edge_type = EDGE_TYPE_DIRECT
        #if selected and action == squareAct: selected.edge_type = EDGE_TYPE_SQUARE


    def onWindowNodesToolbar0(self):
        if self.nodesDock0.isVisible():
            self.nodesDock0.hide()
        else:
            self.nodesDock0.show()

    def onWindowNodesToolbar1(self):
        if self.nodesDock1.isVisible():
            self.nodesDock1.hide()
        else:
            self.nodesDock1.show()

    def onWindowNodesToolbar2(self):
        if self.nodesDock2.isVisible():
            self.nodesDock2.hide()
        else:
            self.nodesDock2.show()

    def createToolBars(self):
        pass


    def createNodesDock0(self):
        self.nodesListWidget = QDMDragListbox()

        self.nodesDock0 = QDockWidget("Системные")
        self.nodesDock0.setWidget(self.nodesListWidget)
        self.nodesDock0.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, self.nodesDock0)


    def createNodesDock1(self):
        self.nodesListWidget = QDMDragListbox1()

        self.nodesDock1 = QDockWidget("Сверлильные")
        self.nodesDock1.setWidget(self.nodesListWidget)
        self.nodesDock1.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, self.nodesDock1)


    def createNodesDock2(self):
        self.nodesListWidget = QDMDragListbox2()

        self.nodesDock2 = QDockWidget("Токарные")
        self.nodesDock2.setWidget(self.nodesListWidget)
        self.nodesDock2.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, self.nodesDock2)

    def createNodesDock3(self):
        self.nodesListWidget = QDMDragListbox3()

        self.nodesDock3 = QDockWidget("Фрезерные")
        self.nodesDock3.setWidget(self.nodesListWidget)
        self.nodesDock3.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, self.nodesDock3)

    def createStatusBar(self):
        self.statusBar().showMessage("Готово")

    def createMdiChild(self, child_widget=None):
        nodeeditor = child_widget if child_widget is not None else CalculatorSubWindow()
        subwnd = self.mdiArea.addSubWindow(nodeeditor)
        subwnd.setWindowIcon(self.empty_icon)
        # nodeeditor.scene.addItemSelectedListener(self.updateEditMenu)
        # nodeeditor.scene.addItemsDeselectedListener(self.updateEditMenu)
        nodeeditor.scene.history.addHistoryModifiedListener(self.updateEditMenu)
        nodeeditor.addCloseEventListener(self.onSubWndClose)
        return subwnd

    def onSubWndClose(self, widget, event):
        existing = self.findMdiChild(widget.filename)
        self.mdiArea.setActiveSubWindow(existing)

        if self.maybeSave():
            event.accept()
        else:
            event.ignore()


    def findMdiChild(self, filename):
        for window in self.mdiArea.subWindowList():
            if window.widget().filename == filename:
                return window
        return None


    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)