from qtpy.QtGui import QImage
from qtpy.QtCore import QRectF, QRect, Qt
from qtpy.QtWidgets import QButtonGroup,QRadioButton ,QLabel, QPlainTextEdit, QPushButton, QLineEdit, QVBoxLayout, QSpinBox
from math import prod

from nodeeditor.node_node import Node, NodeMulti
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.node_graphics_node import QDMGraphicsNode
from nodeeditor.node_socket import LEFT_CENTER, RIGHT_CENTER
from nodeeditor.utils import dumpException
import os

style = '''
QPlainTextEdit {
    color: #fff;    
}
'''

open_img_icons = "status_icons.png"

put = os.path.dirname(__file__)
print(put)

path_img_icons = f'{put}\\nodes\\icons\\{open_img_icons}'


class CalcGraphicsNodeTest(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 200
        self.height = 90
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 160
        self.height = 74
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNodeResult(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 160
        self.height = 74
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNodeSmall(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 110
        self.height = 74
        self.edge_roundness = 0  ### закругление ноды
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsText(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 170
        self.height = 170
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNodeComboBox(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 240
        self.height = 90
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNodeTable(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 170
        self.height = 100
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNodeTable2(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 170
        self.height = 122
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 10
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNodeComboBox_2(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 260
        self.height = 90
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcGraphicsNodeComboBox_4(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 260
        self.height = 180
        self.edge_roundness = 0
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage(path_img_icons)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty(): offset = 0.0
        if self.node.isInvalid(): offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CalcContent(QDMNodeContentWidget):
    def initUI(self):
        lbl = QLabel(self.node.content_label, self)
        lbl.setGeometry(8, 14, 100, 14)
        lbl.setObjectName(self.node.content_label_objname)


class CalcContentFormula(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("1", self)
        self.edit.setGeometry(0, 0, 150, 45)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setObjectName(self.node.content_label_objname)


class CalcContent_input_name(QDMNodeContentWidget):
    def initUI(self):
        lbl = QLabel(self.node.content_label, self)
        lbl.setObjectName(self.node.content_label_objname)
        lbl.setGeometry(8, 4, 100, 14)
        lbl_1 = QLabel(self.node.content_label_1, self)
        lbl_1.setObjectName(self.node.content_label_objname)
        lbl_1.setGeometry(8, 26, 100, 14)
        lbl_2 = QLabel(self.node.content_label_2, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(104, 15, 50, 14)
        lbl_2.setAlignment(Qt.AlignRight | Qt.AlignCenter)


class CalcContent_TURN_1(QDMNodeContentWidget):
    def initUI(self):
        layout = QVBoxLayout()

        # Метка для отображения текущего значения
        self.label = QLabel("Выбрано: 1")
        layout.addWidget(self.label)

        # Создаем QButtonGroup для того, чтобы обеспечить выбор только одной кнопки
        self.radio_group = QButtonGroup(self)
        self.radio_1 = QRadioButton("1")
        self.radio_2 = QRadioButton("2")
        self.radio_3 = QRadioButton("3")
        #self.radio_group.buttonClicked.connect(self.on_radio_value_changed)
                # Создаем три радиокнопки

        # Добавляем радиокнопки в группу
        self.radio_group.addButton(self.radio_1)
        self.radio_group.addButton(self.radio_2)
        self.radio_group.addButton(self.radio_3)

        # Устанавливаем начальное значение
        self.radio_1.setChecked(True)

        # Добавляем радиокнопки в макет
        layout.addWidget(self.radio_1)
        layout.addWidget(self.radio_2)
        layout.addWidget(self.radio_3)

        self.radio_1.toggled.connect(lambda: self.on_radio_value_changed_1(self.radio_1))
        self.radio_2.toggled.connect(lambda: self.on_radio_value_changed_2(self.radio_2))
        self.radio_3.toggled.connect(lambda: self.on_radio_value_changed_3(self.radio_3))

        # Устанавливаем макет для контента ноды
        self.setLayout(layout)

    def on_radio_value_changed_1(self, radio_button):
        """Обработка выбора радиокнопки"""
        if radio_button.isChecked():
            self.radio_1.setChecked(True)
            # Обновляем метку с выбранным значением
            self.label.setText(f"Выбрано1: {radio_button.text()}")
            # Уведомляем ноду, что значение изменилось
            self.node.update_logic(radio_button.text())

    def on_radio_value_changed_2(self, radio_button):
        """Обработка выбора радиокнопки"""
        if radio_button.isChecked():
            self.radio_2.setChecked(True)
            # Обновляем метку с выбранным значением
            self.label.setText(f"Выбрано2: {radio_button.text()}")
            # Уведомляем ноду, что значение изменилось
            self.node.update_logic(radio_button.text())


    def on_radio_value_changed_3(self, radio_button):
        """Обработка выбора радиокнопки"""
        if radio_button.isChecked():
            self.radio_3.setChecked(True)
            # Обновляем метку с выбранным значением
            self.label.setText(f"Выбрано3: {radio_button.text()}")
            # Уведомляем ноду, что значение изменилось
            self.node.update_logic(radio_button.text())


class CalcContent_input_name_2(QDMNodeContentWidget):
    def initUI(self):
        lbl = QLabel(self.node.content_label, self)
        lbl.setObjectName(self.node.content_label_objname)
        lbl.setGeometry(8, 6, 100, 14)
        lbl_1 = QLabel(self.node.content_label_1, self)
        lbl_1.setObjectName(self.node.content_label_objname)
        lbl_1.setGeometry(8, 28, 100, 14)
        lbl_2 = QLabel(self.node.content_label_2, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(8, 50, 100, 14)
        lbl_3 = QLabel(self.node.content_label_3, self)
        lbl_3.setObjectName(self.node.content_label_objname)
        lbl_3.setGeometry(114, 28, 50, 14)
        lbl_3.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        # button = QPushButton(self)
        # button.setGeometry(0, 0, 160, 25)
        # button.setText('qqqqqqqqqqqqqqqqqqqqqqqq')
        #self.button.clicked.connect(self.button_action)


class CalcContent_1(QDMNodeContentWidget):
    def initUI(self):
        self.plainTextEdit = QPlainTextEdit(self.node.content, self)
        self.plainTextEdit.setObjectName(self.node.content_label_objname)
        self.plainTextEdit.setGeometry(QRect(0, 0, 160, 136))
        self.plainTextEdit.setStyleSheet(style)

        #lbl = QLabel(self.node.content_label, self)
        #lbl.setObjectName(self.node.content_label_objname)


class CalcNodePerem(NodeMulti):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeSmall
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, inputs):
        return 123

    def evalImplementation(self):
        i1 = self.getInputs(0)  ###################ВАЖНО ДЛЯ МУЛЬТИЕДЖ

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            self.eval()
            return None

        else:
            ddd = []
            s = len(i1)
            print(i1)
            print(f"---{s}")
            for i in range(s):
                val = self.evalOperation(i1[i].eval())
                ddd.append(str(val))

            string_all = ", ".join(ddd)
            itog = ""
            res_list = []
            perem_list = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
                          "z", "x", "c", "v"]
            if "=" in string_all:
                self.value = str(string_all)

            else:
                for i in range(len(ddd)):
                    perem_num = f"{perem_list[i]}={ddd[i]}"
                    res_list.append(perem_num)
                    itog = ", ".join(res_list)

                self.value = str(itog)

            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return self.value

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:
            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res['value'] = self.value
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            value = data['value']
            self.value = value
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcNodeTURN1(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNode
    NodeContent_class = CalcContent_TURN_1

    def __init__(self, scene, inputs=[2,2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.radbut = None
        self.content = CalcContent_TURN_1(self)
        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def update_logic(self, new_value):
        self.radbut = float(new_value)
        self.markDirty(True)
        print(f"update_logic radbut-{self.radbut}")
        self.eval()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER


    def evalOperation(self, input1, input2):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)

        if i1 is None or i2 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            #self.eval()
            return None

        else:

            val = self.evalOperation(i1.eval(), i2.eval())
            self.value = val #Это то, что идет на выход

            # if self.radbut == 1:
            #     return self.logic_1()
            # elif self.radbut == 2:
            #     return self.logic_2()
            # elif self.radbut == 3:
            #     return self.logic_3()

            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return self.value

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:
            val = self.evalImplementation()
            print(f"---val{val}")

            if self.radbut == 1:
                return self.logic_1()
            elif self.radbut == 2:
                return self.logic_2()
            elif self.radbut == 3:
                return self.logic_3()

            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()


    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res['value'] = self.value
        res['radbut'] = self.radbut
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            value = data['value']
            radbut = data["radbut"]
            self.radbut = radbut
            self.update_logic(self.radbut)
            self.value = value
            return True & res
        except Exception as e:
            dumpException(e)
        return res

    def logic_1(self):
        """Логика для значения 12.5"""
        print("Выполнение логики для значения 1")
        result = "1112"
        return self.value

    def logic_2(self):
        """Логика для значения 6.3"""
        print("Выполнение логики для значения 2")
        result = "2223"
        return self.value

    def logic_3(self):
        """Логика для значения 1.6"""
        print("Выполнение логики для значения 3")
        result = "3334"
        return self.value


class CalcNodeMulti1(NodeMulti):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeSmall
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, inputs):
        return 123

    def evalImplementation(self):
        i1 = self.getInputs(0)  ###################ВАЖНО ДЛЯ МУЛЬТИЕДЖ

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            self.eval()
            return None

        else:
            ddd = []
            s = len(i1)
            print(f"---{s}")
            for i in range(s):
                val = self.evalOperation(i1[i].eval())
                ddd.append(float(val))

            self.value = prod(ddd)
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return self.value

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res['value'] = self.value
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            value = data['value']
            self.value = value
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcNodeMulti(NodeMulti):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeSmall
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, inputs):
        return 123

    def evalImplementation(self):
        i1 = self.getInputs(0)  ###################ВАЖНО ДЛЯ МУЛЬТИЕДЖ

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            self.eval()
            return None

        else:
            ddd = []
            s = len(i1)
            print(f"---{s}")
            for i in range(s):
                val = self.evalOperation(i1[i].eval())
                ddd.append(float(val))

            self.value = sum(ddd)
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return self.value

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res['value'] = self.value
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            value = data['value']
            self.value = value
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcNodeFormula(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeResult
    NodeContent_class = CalcContentFormula

    def __init__(self, scene, inputs=[2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalOperation(self, inputs):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            print('112211')
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res['value'] = self.content.edit.text()
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            value = data['value']
            self.content.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeSmall
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2, 2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input1, input2):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval(), i2.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        return res


class CalcNodeResultTest(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeResult
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2, 2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input1, input2):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)

        if i1 is None or i2 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval(), i2.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        return res


class CalcNodeResult(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeResult
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2, 2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input1, input2):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)

        if i1 is None or i2 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval(), i2.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        return res


class CalcNode_lbl(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNode
    NodeContent_class = CalcContent_input_name

    def __init__(self, scene, inputs=[2, 2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input1, input2):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)

        if i1 is None or i2 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval(), i2.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return str(val)

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        return res


class CalcNodeText(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNode
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2, 2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input1, input2):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)

        if i1 is None or i2 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.evalChildren()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval(), i2.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        return res


class CalcText(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsText
    NodeContent_class = CalcContent_1

    def __init__(self, scene, inputs=[], outputs=[]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.evalChildren()  #self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input1, input2):
        return 123

    def evalImplementation(self):
        i1 = self.value

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.evalChildren()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        print('FFFFFFFFFFFFFFFF')

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        return res


class CalcTable(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeTable
    NodeContent_class = CalcContent_input_name_2

    def __init__(self, scene, inputs=[2, 2, 2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()
        self.markDirty(False)
        self.markInvalid(False)
        self.grNode.setToolTip("")

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input1, input2, input3):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)
        i3 = self.getInput(2)

        if i1 is None or i2 is None or i3 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval(), i2.eval(), i3.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return self.value

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:

            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res['value'] = self.value
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            value = data['value']
            self.value = value
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcTable2(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNodeTable2
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, value, value_1, value_2):
        return 123

    def evalImplementation(self):
        i1 = self.value

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val

            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res["value"] = self.content.edit.currentIndex()
        res["value2"] = self.content.edit_1.currentIndex()
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            value = data['value']
            value2 = data['value2']
            print(value)
            self.content.edit.setCurrentIndex(value)
            self.content.edit_1.setCurrentIndex(value2)
            return True & res

        except Exception as e:
            dumpException(e)
        return res


class CalcTable3(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_input_2"

    GraphicsNode_class = CalcGraphicsNode
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input2):
        return 123

    def evalImplementation(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def evalImplementation_1(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def eval_1(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            if self.content.edit.currentText() == "На столе или плите без крепления (с упором)":
                print(self.content.edit.currentText())
                self.content.edit_1.clear()
                self.content.edit_1.addItem("Без выверки")
                self.content.edit_1.addItem("С выверкой")

            if self.content.edit.currentText() == "В тисках":
                print(self.content.edit.currentText())
                self.content.edit_1.clear()
                self.content.edit_1.addItem("Без выверки (УСП-16)")
                self.content.edit_1.addItem("С выверкой")

            if self.content.edit.currentText() == "В кулачках самоцентрирующего патрона":
                self.content.edit_1.clear()
                self.content.edit_1.addItem("-")
            #
            if self.content.edit.currentText() == "На столе с пневмоприводом":
                self.content.edit_1.clear()
                self.content.edit_1.addItem("-")
            #
            if self.content.edit.currentText() == "На столе с креплением 2-я болтами и планками":
                self.content.edit_1.clear()
                self.content.edit_1.addItem("Без выверки")
                self.content.edit_1.addItem("С выверкой простой")
                self.content.edit_1.addItem("С выверкой сложной")
            #
            if self.content.edit.currentText() == "Сбоку стола с выверкой":
                self.content.edit_1.clear()
                self.content.edit_1.addItem("В одной плоскости")
                self.content.edit_1.addItem("В двух плоскостях")
            val = self.evalImplementation_1()
            return val

        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def onInputChanged_1(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval_1()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res["value"] = self.content.edit.currentIndex()
        res["value2"] = self.content.edit_1.currentIndex()
        res["val_res"] = self.value
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            val_res = data['val_res']
            value = data['value']
            value2 = data['value2']
            print(value)
            self.content.edit.setCurrentIndex(value)
            self.content.edit_1.setCurrentIndex(value2)
            self.value = val_res
            return True & res

        except Exception as e:
            dumpException(e)
        return res


class CalcTable5(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNode
    NodeContent_class = CalcContent

    def __init__(self, scene, inputs=[2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def evalOperation(self, input2):
        return f'P-'

    def evalImplementation(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def evalImplementation_1(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def evalImplementation_2(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def evalImplementation_3(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def evalImplementation_4(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperation(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def eval_1(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            if self.content.edit.currentText() == "В самоцентр. патроне":
                print(self.content.edit.currentText())
                self.content.edit_1.clear()
                self.content.edit_1.addItem("В кулачках")
                self.content.edit_1.addItem("В кулачках с центр.")
                self.content.edit_1.addItem("В кулачках с центр. люнет.")
                self.content.edit_1.addItem("В кулачках с люнет.")
                self.content.edit_1.addItem("В кулачках с разрезн. втул.")

            if self.content.edit.currentText() == "В 4х кулачковом патроне":
                print(self.content.edit.currentText())
                self.content.edit_1.clear()
                self.content.edit_1.addItem("Дет. цилиндр. формы")
                self.content.edit_1.addItem("Дет. фасонной и короб. формы")
                self.content.edit_1.addItem("В кулачках с центр.")
                self.content.edit_1.addItem("В кулачках с центр. люнет.")
                self.content.edit_1.addItem("В центрах с крепл. кулач.")
                self.content.edit_1.addItem("В кулачках с люнет.")

            if self.content.edit.currentText() == "В центрах":
                print(self.content.edit.currentText())
                self.content.edit_1.clear()
                self.content.edit_1.addItem("С надев. хомут.")
                self.content.edit_1.addItem("С надев. хомут. люнет.")
                self.content.edit_1.addItem("Без надев. хомут.")
                self.content.edit_1.addItem("Без надев. хомут. люнет.")

            if self.content.edit.currentText() == "На оправке":
                self.content.edit_1.clear()
                self.content.edit_1.addItem("На концевой оправке")
                self.content.edit_1.addItem("На центровой оправке")
            #
            if self.content.edit.currentText() == "На планшайбе с угол.":
                self.content.edit_1.clear()
                self.content.edit_1.addItem("С крепл. болтами и планками")
                self.content.edit_1.addItem("С угол. с крепл. болтами и планками")

            val = self.evalImplementation()
            return val

        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def eval_2(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выверкой по диам. и торц.")

            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с центр.":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выверкой по диам.")

            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выверкой по диам.")

            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с разрезн. втул.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("-")

            if self.content.edit_1.currentText() == "В кулачках с люнет.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выверкой по диам.")
            #

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выверкой по диам.")
                self.content.edit_2.addItem("С выверкой по диам. и торц.")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выв. в одн. плоскости")
                self.content.edit_2.addItem("С выв. в двух плоскостях")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выверкой по диам.")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")
                self.content.edit_2.addItem("С выверкой по диам.")

            if self.content.edit_1.currentText() == "В центрах с крепл. кулач.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("Без выверки")

            if self.content.edit_1.currentText() == "В кулачках c люнет.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("С выверкой по диам.")

            if self.content.edit.currentText() == "Дет. цилиндр. формы" and self.content.edit_1.currentText() == "В кулачках с разрезн. втул.":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("-")

            #

            if self.content.edit_1.currentText() == "С надев. хомут.":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("-")
                self.content.edit_2.addItem("1000")
                self.content.edit_2.addItem("2000")
                self.content.edit_2.addItem("3000")
                self.content.edit_2.addItem("5000")
                self.content.edit_2.addItem("10000")

            if self.content.edit_1.currentText() == "С надев. хомут. люнет.":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("1000")
                self.content.edit_2.addItem("2000")
                self.content.edit_2.addItem("3000")
                self.content.edit_2.addItem("5000")
                self.content.edit_2.addItem("10000")

            if self.content.edit_1.currentText() == "Без надев. хомут.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("-")
                self.content.edit_2.addItem("1000")
                self.content.edit_2.addItem("2000")
                self.content.edit_2.addItem("3000")
                self.content.edit_2.addItem("5000")
                self.content.edit_2.addItem("10000")

            if self.content.edit_1.currentText() == "Без надев. хомут. люнет.":
                self.content.edit_2.clear()
                self.content.edit_2.addItem("1000")
                self.content.edit_2.addItem("2000")
                self.content.edit_2.addItem("3000")
                self.content.edit_2.addItem("5000")
                self.content.edit_2.addItem("10000")
            #

            if self.content.edit_1.currentText() == "На концевой оправке":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("На гладк. или шлиц. оправке")
                self.content.edit_2.addItem("На резьб. оправке")
                self.content.edit_2.addItem("На разжим. оправке с зажим.")

            if self.content.edit_1.currentText() == "На центровой оправке":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("На гладк. или шлиц. оправке")
                self.content.edit_2.addItem("На оправке с креп. гайкой")
                self.content.edit_2.addItem("На разжим. оправке с креп. гайкой.")

            #

            if self.content.edit_1.currentText() == "С крепл. болтами и планками":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("С центр. приспособ. без выверки")
                self.content.edit_2.addItem("С выверкой в одн. плоскости")
                self.content.edit_2.addItem("С выверкой в двух плоскостях")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("С центр. приспособ. без выверки")
                self.content.edit_2.addItem("С выверкой в одн. плоскости")
                self.content.edit_2.addItem("С выверкой в двух плоскостях")

            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с люнет.":
                print(self.content.edit.currentText())
                self.content.edit_2.clear()
                self.content.edit_2.addItem("С выверкой по диам.")
            ##

            val = self.evalImplementation()
            return val

        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def eval_3(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            ##
            if self.content.edit_1.currentText() == "В кулачках" and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            if self.content.edit_1.currentText() == "В кулачках" and self.content.edit_2.currentText() == "С выверкой по диам. и торц.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")

            #
            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("0.1")
            #
            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("0.1")
            #
            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с люнет." and self.content.edit_2.currentText() == "С выверкой по диам.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
            ##
            if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с разрезн. втул." and self.content.edit_2.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            ##
            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")

            #
            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")
            #
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с люнет." and self.content.edit_2.currentText() == "С выверкой по диам.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")
            ##
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В центрах с крепл. кулач." and self.content.edit_2.currentText() == "Без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            ##
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "1000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "2000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "3000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "5000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "10000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            ##
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "1000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "2000":
                print(self.content.edit.currentText())
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "3000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "5000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "10000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            ##
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "1000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "2000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "3000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "5000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "10000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            ##
            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "1000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "2000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "3000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "5000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "10000":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            ##
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("Без крепления")
                self.content.edit_3.addItem("С креп. гайкой и шайбой")
                self.content.edit_3.addItem("С поджатием задним центр.")

            #
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На резьб. оправке":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("Без контрогайки")
                self.content.edit_3.addItem("С контрогайкой")

            #
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с зажим.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("Центром задн. бабки")
                self.content.edit_3.addItem("Болтом или гайкой")

            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("При свободном надевании дет.")
                self.content.edit_3.addItem("При тугом надевании дет.")
            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На оправке с креп. гайкой":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("С быстросъёмной шайбой")
                self.content.edit_3.addItem("С простой шайбой")
            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с креп. гайкой.":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            ##
            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С центр. приспособ. без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")

            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")
            #
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С центр. приспособ. без выверки":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("-")
            #
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")
            #
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях":
                print(self.content.edit.currentText())
                self.content.edit_3.clear()
                self.content.edit_3.addItem("1.0")
                self.content.edit_3.addItem("0.5")
                self.content.edit_3.addItem("0.1")
                self.content.edit_3.addItem("0.05")
                self.content.edit_3.addItem("0.01")

            val = self.evalImplementation()
            return val

        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def eval_4(self):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return f'{self.value}'

        try:
            ##
            if self.content.edit_1.currentText() == "В кулачках" and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "В кулачках" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "В кулачках" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "В кулачках с разрезн. втул." and self.content.edit_2.currentText() == "-" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            ##
            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках сцентр. люнет." and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")
            #
            ##
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В центрах с крепл. кулач." and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
            ##
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "-" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "-" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "Без крепления":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "С креп. гайкой и шайбой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("Быстросъемной")
                self.content.edit_4.addItem("Простой")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "С поджатием задним центр.":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("Без крепления")
                self.content.edit_4.addItem("С креплением гайкой")

            #
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На резьб. оправке" and self.content.edit_3.currentText() == "Без контрогайки":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На резьб. оправке" and self.content.edit_3.currentText() == "С контрогайкой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с зажим." and self.content.edit_3.currentText() == "Центром задн. бабки":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с зажим." and self.content.edit_3.currentText() == "Болтом или гайкой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "При свободном надевании дет.":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "При тугом надевании дет.":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На оправке с креп. гайкой" and self.content.edit_3.currentText() == "С быстросъёмной шайбой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На оправке с креп. гайкой" and self.content.edit_3.currentText() == "С простой шайбой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с креп. гайкой." and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С центр. приспособ. без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С центр. приспособ. без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. цилиндр. формы" and self.content.edit_2.currentText() == "С выверкой по диам. и торц." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в одн. плоскости" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "Дет. фасонной и короб. формы" and self.content.edit_2.currentText() == "С выв. в двух плоскостях" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "Без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")

            if self.content.edit.currentText() == "В в 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В в 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с центр. люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")
            #
            #
            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках с люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках c люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках c люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках c люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")

            if self.content.edit.currentText() == "В 4х кулачковом патроне" and self.content.edit_1.currentText() == "В кулачках c люнет." and self.content.edit_2.currentText() == "С выверкой по диам." and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("1000")
                self.content.edit_4.addItem("3000")
                self.content.edit_4.addItem("5000")
                self.content.edit_4.addItem("10000")
                self.content.edit_4.addItem("15000")
            ##
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "-" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут." and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С надев. хомут. люнет." and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "-" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут" and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "1000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "2000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "3000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "5000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "Без надев. хомут. люнет." and self.content.edit_2.currentText() == "10000" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "Без крепления":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "С креп. гайкой и шайбой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("Быстросъемной")
                self.content.edit_4.addItem("Простой")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "С поджатием задним центр.":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("Без крепления")
                self.content.edit_4.addItem("С креп. гайкой и шайбой")

            #
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На резьб. оправке" and self.content.edit_3.currentText() == "Без контрогайки":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На резьб. оправке" and self.content.edit_3.currentText() == "С контрогайкой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с зажим." and self.content.edit_3.currentText() == "Центром задн. бабки":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На концевой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с зажим." and self.content.edit_3.currentText() == "Болтом или гайкой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "При свободном надевании дет.":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На гладк. или шлиц. оправке" and self.content.edit_3.currentText() == "При тугом надевании дет.":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На оправке с креп. гайкой" and self.content.edit_3.currentText() == "С быстросъёмной шайбой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На оправке с креп. гайкой" and self.content.edit_3.currentText() == "С простой шайбой":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "На центровой оправке" and self.content.edit_2.currentText() == "На разжим. оправке с креп. гайкой." and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            ##
            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С центр. приспособ. без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            #
            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С центр. приспособ. без выверки" and self.content.edit_3.currentText() == "-":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в одн. плоскости" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")
            #
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "1.0":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.5":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.1":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.05":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками" and self.content.edit_2.currentText() == "С выверкой в двух плоскостях" and self.content.edit_3.currentText() == "0.01":
                print(self.content.edit.currentText())
                self.content.edit_4.clear()
                self.content.edit_4.addItem("-")

            val = self.evalImplementation()
            return val

        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def onInputChanged_1(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval_1()

    def onInputChanged_2(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval_2()

    def onInputChanged_3(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval_3()

    def onInputChanged_4(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval_4()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        res["value"] = self.content.edit.currentIndex()
        res["value2"] = self.content.edit_1.currentIndex()
        res["value3"] = self.content.edit_2.currentIndex()
        res["value4"] = self.content.edit_3.currentIndex()
        res["value5"] = self.content.edit_4.currentIndex()
        res["val_res"] = self.value
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
        try:
            val_res = data['val_res']
            value = data['value']
            value2 = data['value2']
            value3 = data['value3']
            value4 = data['value4']
            value5 = data['value5']
            print(value)
            self.content.edit.setCurrentIndex(value)
            self.content.edit_1.setCurrentIndex(value2)
            self.content.edit_2.setCurrentIndex(value3)
            self.content.edit_3.setCurrentIndex(value4)
            self.content.edit_4.setCurrentIndex(value5)
            self.value = val_res
            return True & res

        except Exception as e:
            dumpException(e)
        return res
