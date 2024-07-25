from qtpy.QtGui import QPixmap, QIcon, QDrag
from qtpy.QtCore import QSize, Qt, QByteArray, QDataStream, QMimeData, QIODevice, QPoint
from qtpy.QtWidgets import QListWidget, QAbstractItemView, QListWidgetItem

from example_calculator.calc_conf import CALC_NODES, get_class_from_opcode, LISTBOX_MIMETYPE
from nodeeditor.utils import dumpException


class QDMDragListbox(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setIconSize(QSize(32, 32))
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)

        self.addMyItems()


    def addMyItems(self):
        #print(CALC_NODES)
        keys = list(CALC_NODES.keys())
        keys.sort()
        ex_list = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23]
        for key in keys:
            if key in ex_list:
                continue
            else:
                node = get_class_from_opcode(key)
                self.addMyItem(node.op_title, node.icon, node.op_code)


    def addMyItem(self, name, icon=None, op_code=0):
        item = QListWidgetItem(name, self) # can be (icon, text, parent, <int>type)
        pixmap = QPixmap(icon if icon is not None else ".")
        item.setIcon(QIcon(pixmap))
        item.setSizeHint(QSize(32, 32))

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)

        # setup data
        item.setData(Qt.UserRole, pixmap)
        item.setData(Qt.UserRole + 1, op_code)


    def startDrag(self, *args, **kwargs):
        try:
            item = self.currentItem()
            op_code = item.data(Qt.UserRole + 1)

            pixmap = QPixmap(item.data(Qt.UserRole))


            itemData = QByteArray()
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            dataStream << pixmap
            dataStream.writeInt(op_code)
            dataStream.writeQString(item.text())

            mimeData = QMimeData()
            mimeData.setData(LISTBOX_MIMETYPE, itemData)

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(QPoint(pixmap.width() // 2, pixmap.height() // 2))
            drag.setPixmap(pixmap)

            drag.exec_(Qt.MoveAction)

        except Exception as e: dumpException(e)


class QDMDragListbox1(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setIconSize(QSize(32, 32))
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)

        self.addMyItems()


    def addMyItems(self):
        print(CALC_NODES)
        keys = list(CALC_NODES.keys())
        keys.sort()
        ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 20, 21, 22, 23, 24, 25]
        for key in keys:
            if key in ex_list:
                continue
            else:
                node = get_class_from_opcode(key)
                self.addMyItem(node.op_title, node.icon, node.op_code)


    def addMyItem(self, name, icon=None, op_code=0):
        item = QListWidgetItem(name, self) # can be (icon, text, parent, <int>type)
        pixmap = QPixmap(icon if icon is not None else ".")
        item.setIcon(QIcon(pixmap))
        item.setSizeHint(QSize(32, 32))

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)

        # setup data
        item.setData(Qt.UserRole, pixmap)
        item.setData(Qt.UserRole + 1, op_code)


    def startDrag(self, *args, **kwargs):
        try:
            item = self.currentItem()
            op_code = item.data(Qt.UserRole + 1)

            pixmap = QPixmap(item.data(Qt.UserRole))


            itemData = QByteArray()
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            dataStream << pixmap
            dataStream.writeInt(op_code)
            dataStream.writeQString(item.text())

            mimeData = QMimeData()
            mimeData.setData(LISTBOX_MIMETYPE, itemData)

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(QPoint(pixmap.width() // 2, pixmap.height() // 2))
            drag.setPixmap(pixmap)

            drag.exec_(Qt.MoveAction)

        except Exception as e: dumpException(e)


class QDMDragListbox2(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setIconSize(QSize(32, 32))
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)

        self.addMyItems()


    def addMyItems(self):
        print(CALC_NODES)
        keys = list(CALC_NODES.keys())
        keys.sort()
        ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25]
        for key in keys:
            if key in ex_list:
                continue
            else:
                node = get_class_from_opcode(key)
                self.addMyItem(node.op_title, node.icon, node.op_code)


    def addMyItem(self, name, icon=None, op_code=0):
        item = QListWidgetItem(name, self) # can be (icon, text, parent, <int>type)
        pixmap = QPixmap(icon if icon is not None else ".")
        item.setIcon(QIcon(pixmap))
        item.setSizeHint(QSize(32, 32))

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)

        # setup data
        item.setData(Qt.UserRole, pixmap)
        item.setData(Qt.UserRole + 1, op_code)


    def startDrag(self, *args, **kwargs):
        try:
            item = self.currentItem()
            op_code = item.data(Qt.UserRole + 1)

            pixmap = QPixmap(item.data(Qt.UserRole))


            itemData = QByteArray()
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            dataStream << pixmap
            dataStream.writeInt(op_code)
            dataStream.writeQString(item.text())

            mimeData = QMimeData()
            mimeData.setData(LISTBOX_MIMETYPE, itemData)

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(QPoint(pixmap.width() // 2, pixmap.height() // 2))
            drag.setPixmap(pixmap)

            drag.exec_(Qt.MoveAction)

        except Exception as e: dumpException(e)


class QDMDragListbox3(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setIconSize(QSize(32, 32))
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)

        self.addMyItems()


    def addMyItems(self):
        print(CALC_NODES)
        keys = list(CALC_NODES.keys())
        keys.sort()
        ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        for key in keys:
            if key in ex_list:
                continue
            else:
                node = get_class_from_opcode(key)
                self.addMyItem(node.op_title, node.icon, node.op_code)


    def addMyItem(self, name, icon=None, op_code=0):
        item = QListWidgetItem(name, self) # can be (icon, text, parent, <int>type)
        pixmap = QPixmap(icon if icon is not None else ".")
        item.setIcon(QIcon(pixmap))
        item.setSizeHint(QSize(32, 32))

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)

        # setup data
        item.setData(Qt.UserRole, pixmap)
        item.setData(Qt.UserRole + 1, op_code)


    def startDrag(self, *args, **kwargs):
        try:
            item = self.currentItem()
            op_code = item.data(Qt.UserRole + 1)

            pixmap = QPixmap(item.data(Qt.UserRole))


            itemData = QByteArray()
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            dataStream << pixmap
            dataStream.writeInt(op_code)
            dataStream.writeQString(item.text())

            mimeData = QMimeData()
            mimeData.setData(LISTBOX_MIMETYPE, itemData)

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(QPoint(pixmap.width() // 2, pixmap.height() // 2))
            drag.setPixmap(pixmap)

            drag.exec_(Qt.MoveAction)

        except Exception as e: dumpException(e)