import os
from qtpy.QtWidgets import QGraphicsItem, QWidget, QPushButton, QHBoxLayout, QGraphicsProxyWidget, QLabel, QDialog, QVBoxLayout, QSpacerItem, QSizePolicy, QTableWidget, QTableWidgetItem
from qtpy.QtGui import QFont, QColor, QPen, QBrush, QPainterPath, QIcon
from qtpy.QtCore import Qt, QRectF

open_img_fa = "i64.ico"
put1 = os.path.dirname(__file__)
put = put1.replace("nodeeditor", "example_calculator")
path_img_fa = f'{put}\\nodes\\icons\\{open_img_fa}'

class QDMGraphicsNode(QGraphicsItem):
    def __init__(self, node: 'Node', parent: QWidget = None):
        super().__init__(parent)
        self.node = node

        self.hovered = False
        self._was_moved = False
        self._last_selected_state = False

        self.initSizes()
        self.initAssets()
        self.initUI()

        # Store the dialog as an attribute of the class
        self.dialog = None

    @property
    def content(self):
        return self.node.content if self.node else None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_label.setText(self._title)

    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

        self.initTitle()
        self.title = self.node.title

        self.initContent()

    def initSizes(self):
        self.width = 180
        self.height = 240
        self.edge_roundness = 10.0
        self.edge_padding = 10.0
        self.title_height = 24
        self.title_horizontal_padding = 10.0
        self.title_vertical_padding = 10.0

    def initAssets(self):
        self._title_color = Qt.white
        self._title_font = QFont("Ubuntu", 10)

        self._color = QColor("#7F000000")
        self._color_selected = QColor("#FF37A6FF") #для белой темы
        self._color_hovered = QColor("#FF37A6FF")

        self._pen_default = QPen(self._color)
        self._pen_default.setWidthF(2.0)
        self._pen_selected = QPen(self._color_selected)
        self._pen_selected.setWidthF(2.0)
        self._pen_hovered = QPen(self._color_hovered)
        self._pen_hovered.setWidthF(3.0)

        self._brush_title = QBrush(QColor("#dfdfdf"))
        self._brush_background = QBrush(QColor("#f2f2f2"))

    def onSelected(self):
        self.node.scene.grScene.itemSelected.emit()

    def doSelect(self, new_state=True):
        self.setSelected(new_state)
        self._last_selected_state = new_state
        if new_state: self.onSelected()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        for node in self.scene().scene.nodes:
            if node.grNode.isSelected():
                node.updateConnectedEdges()
        self._was_moved = True

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if self._was_moved:
            self._was_moved = False
            self.node.scene.history.storeHistory("Node moved", setModified=True)

            self.node.scene.resetLastSelectedStates()
            self.doSelect()
            self.node.scene._last_selected_items = self.node.scene.getSelectedItems()
            self.node.updateConnectedEdges()
            return
        if self._last_selected_state != self.isSelected() or self.node.scene._last_selected_items != self.node.scene.getSelectedItems():
            self.node.scene.resetLastSelectedStates()
            self._last_selected_state = self.isSelected()
            self.onSelected()
            self.node.updateConnectedEdges()

    def mouseDoubleClickEvent(self, event):
        self.node.onDoubleClicked(event)

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        self.hovered = True
        self.update()

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        self.hovered = False
        self.update()

    def boundingRect(self) -> QRectF:
        return QRectF(0, 0, self.width, self.height).normalized()

    def initTitle(self):
        self.title_widget = QWidget()
        self.title_widget.setFixedSize(self.width, self.title_height)
        self.title_layout = QHBoxLayout(self.title_widget)
        self.title_layout.setContentsMargins(0, 0, 0, 0)

        self.title_label = QLabel(self.node.title, self.title_widget)
        self.title_label.setFont(self._title_font)

        self.button = QPushButton("?", self.title_widget)
        self.button.clicked.connect(self.showPopup)
        ex_list = ['Значение', 'Результат', 'Сложение', 'Вычитание', 'Умножение', 'Деление', 'Комментарий', 'Сложение+', 'Умножение+']
        if self.node.title in ex_list:
            self.button.setFixedSize(0, 0)
        else:
            self.button.setFixedSize(25, 25)

        spacer = QSpacerItem(25, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.title_layout.addItem(spacer)
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.button)

        self.title_proxy = QGraphicsProxyWidget(self)
        self.title_proxy.setWidget(self.title_widget)
        self.title_proxy.setPos(0, 0)

        # Set background color to red
        self.title_widget.setStyleSheet("background-color: transparent;")

        self.button.setStyleSheet("""
            QPushButton {
                background-color: #dfdfdf;
                border-radius: 0px;
                border: 1px solid #dfdfdf;
            }
        """)

    def showPopup(self):
        if self.dialog is None:
            self.dialog = QDialog()
            self.dialog.setWindowTitle("Данные")
            self.dialog.setModal(False)
            self.dialog.setWindowIcon(QIcon(path_img_fa))

            layout = QVBoxLayout()

            if self.node.title == 'К1 Коэф партии':
                table_data = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
            elif self.node.title == 'К1а Коэф мат':
                table_data = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
                # label = QLabel("Принимает значения в виде строки.\nПример:\nx=2, y=4, z=6, ...\nи подставляет в формулу\nПример:\nx+y*z")
                # label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                # layout.addWidget(label)
                # self.dialog.setMinimumSize(200, 200)

            else:
                table_data = []

            if table_data:
                table = QTableWidget(len(table_data), len(table_data[0]))
                for row_idx, row in enumerate(table_data):
                    for col_idx, item in enumerate(row):
                        table.setItem(row_idx, col_idx, QTableWidgetItem(item))

                # Change the font color to white
                table.setStyleSheet("QTableWidget { color: white; }")
                layout.addWidget(table)

                self.dialog.setMinimumSize(200, 200)
                self.dialog.resize(table.sizeHint())

            elif self.node.title == 'Формула':
                label = QLabel("Принимает значения в виде строки\nПример:\n\nx=2, y=4, z=6, ...\n\nи подставляет в формулу\nПример:\n\nx+y*z...")
                label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                layout.addWidget(label)
                self.dialog.setMinimumSize(200, 200)

            else:
                label = QLabel("Нет данных для отображения")
                label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                layout.addWidget(label)
                self.dialog.setMinimumSize(200, 200)

            self.dialog.setLayout(layout)
        self.dialog.show()

    def initContent(self):
        if self.content is not None:
            self.content.setGeometry(self.edge_padding, self.title_height + self.edge_padding,
                                     self.width - 2 * self.edge_padding, self.height - 2 * self.edge_padding - self.title_height)

        self.grContent = self.node.scene.grScene.addWidget(self.content)
        self.grContent.node = self.node
        self.grContent.setParentItem(self)

    def setTitleStyle(self, font=None, color=None):
        if font:
            self.title_label.setFont(font)
        if color:
            palette = self.title_label.palette()
            palette.setColor(self.title_label.foregroundRole(), color)
            self.title_label.setPalette(palette)

    def setButtonStyle(self, font=None, color=None, bg_color=None):
        if font:
            self.button.setFont(font)
        if color:
            palette = self.button.palette()
            palette.setColor(self.button.foregroundRole(), color)
            self.button.setPalette(palette)
        if bg_color:
            self.button.setStyleSheet(f"background-color: {bg_color.name()};")

    def setButtonSize(self, width, height):
        self.button.setFixedSize(width, height)

    def setTitleBackgroundColor(self, color):
        self.title_widget.setStyleSheet(f"background-color: {color.name()};")

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self.width, self.title_height, self.edge_roundness, self.edge_roundness)
        path_title.addRect(0, self.title_height - self.edge_roundness, self.edge_roundness, self.edge_roundness)
        path_title.addRect(self.width - self.edge_roundness, self.title_height - self.edge_roundness, self.edge_roundness, self.edge_roundness)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self.title_height, self.width, self.height - self.title_height, self.edge_roundness, self.edge_roundness)
        path_content.addRect(0, self.title_height, self.edge_roundness, self.edge_roundness)
        path_content.addRect(self.width - self.edge_roundness, self.title_height, self.edge_roundness, self.edge_roundness)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())

        path_outline = QPainterPath()
        path_outline.addRoundedRect(-1, -1, self.width + 2, self.height + 2, self.edge_roundness, self.edge_roundness)
        painter.setBrush(Qt.NoBrush)
        if self.hovered:
            painter.setPen(self._pen_hovered)
            painter.drawPath(path_outline.simplified())
            painter.setPen(self._pen_default)
            painter.drawPath(path_outline.simplified())
        else:
            painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
            painter.drawPath(path_outline.simplified())

    def updateConnectedEdges(self):
        for socket in (self.node.inputs + self.node.outputs):
            if socket.hasEdge():
                for edge in socket.edges:
                    edge.updatePositions()
                    self.node.updateConnectedEdges()
