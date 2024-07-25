from qtpy.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit
from qtpy.QtCore import Qt, QRect
from example_calculator.calc_conf import register_node, OP_NODE_INPUT, OP_NODE_INPUT_1, OP_NODE_INPUT_2, \
    OP_NODE_INPUT_TEXT, OP_NODE_INPUT_3, OP_NODE_INPUT_5
from example_calculator.calc_node_base import CalcNode, CalcTable2, CalcTable3, CalcGraphicsNode, \
    CalcGraphicsNodeComboBox, CalcGraphicsNodeComboBox_2, CalcGraphicsText, CalcNodeText, CalcNodeResult, CalcTable5, \
    CalcGraphicsNodeComboBox_4
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.utils import dumpException
import os
from example_calculator.table import create_tables, create_tables_turning

open_img_in = "in_1.ico"
open_img_tab = "table.ico"
open_img_com = "com.ico"

put = os.path.dirname(__file__)

path_img_in = f'{put}\icons\{open_img_in}'
path_img_tab = f'{put}\icons\{open_img_tab}'
path_img_com = f'{put}\icons\{open_img_com}'

style = '''
QPlainTextEdit {
    color: #000000;    
}
QComboBox {
    color: #000000;    
    background-color: #666;
    padding: 4px;
    border: 0px solid rgb(#fff);
    border-radius: 0px;
    padding-left: 5px;
    padding-right: 5px;
    selection-background-color: rgb(66, 66, 66);
}
QComboBox QAbstractItemView {
    color: #000000;    
    background-color: #666;
    padding: 4px;
    border: 0px solid rgb(#fff);
    border-radius: 0px;
    padding-left: 5px;
    padding-right: 5px;
    selection-background-color: rgb(66, 66, 66);
}
'''


class CalcInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("", self)
        self.edit.setGeometry(0, 0, 150, 45)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setObjectName(self.node.content_label_objname)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcInputContentText(QDMNodeContentWidget):
    def initUI(self):
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QRect(0, 0, 160, 136))
        self.plainTextEdit.setStyleSheet(style)
        self.plainTextEdit.setPlainText('')
        #self.edit = QLineEdit("1", self)
        # self.edit.setAlignment(Qt.AlignRight)
        # self.edit.setObjectName(self.node.content_label_objname)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.plainTextEdit.toPlainText()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.plainTextEdit.setPlainText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcInputContent_1(QDMNodeContentWidget):
    def initUI(self):
        #self.edit = QLineEdit("1", self)
        self.edit = QComboBox(self)
        self.edit.setGeometry(0, 4, 240, 30)
        self.edit.addItem('АЛ-2, DIAM, DI6AM')
        self.edit.addItem('ЛС69-1, АМГ3, АМГ5')
        self.edit.addItem('Бронза, фторопласт, графит, текстолит')
        self.edit.addItem('Ст 3, 4, 5, 10, 15, 45, 25Л, 35Л')
        self.edit.addItem('15Х, 35Х, 40ХМ, 38ХМА, У10А, У12А')
        self.edit.addItem('10XCД, 18ХГТ, ОСГА-6, 18ХНВА')
        self.edit.addItem('90ХГСА, 38ХНВА, ХВГ')
        self.edit.addItem('12Х13, 20Х13, 40Х13')
        self.edit.addItem('АК25, АК27, АК29, АК29ПК')
        self.edit.addItem('АК32, АК35, АК32, ПК')
        self.edit.addItem('АК33, АК34, АК36, АК37')
        self.edit.addItem('14Х17Н2, 2Х17Н2')
        self.edit.addItem('ОХ18Н9Т, 12Х18Н9Т')
        self.edit.addItem('ВТ-1, ВТ-8, 52КФ, ВНМ5-3')
        self.edit.addItem('3, 3В, 3М')
        self.edit.addItem('45Г17, ЮЗ, ЮЗХ')
        self.edit.currentText()
        self.edit.setStyleSheet(style)

        self.edit_1 = QComboBox(self)
        self.edit_1.setGeometry(0, 35, 240, 30)
        self.edit_1.addItem('Сверление, рассверливание')
        self.edit_1.addItem('Зенкование, развертывание')
        self.edit_1.addItem('Нарезание резьбы')
        self.edit_1.addItem('По корке, вырезка')
        self.edit_1.addItem('Поковка')
        self.edit_1.addItem('Отливка')
        self.edit_1.currentText()
        self.edit_1.setStyleSheet(style)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.currentText()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.currentText()
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcInputContent_tur1(QDMNodeContentWidget):
    def initUI(self):
        #self.edit = QLineEdit("1", self)
        self.edit = QComboBox(self)
        self.edit.setGeometry(0, 4, 240, 30)
        self.edit.addItem('АЛ-2, Текстолит, эбонит, фенопласт')
        self.edit.addItem('АМГ-6, ЛС-59, ЛО-62, М-3, ЛМЦ58-2')
        self.edit.addItem('АМЦ9-2, Л-96, оргстекло, фторопласт')
        self.edit.addItem('Ст 3, 4, 5, 10, 15-50, 45, 25Л, 35Л')
        self.edit.addItem('У10А, У12А, 40ХН, 38ХА')
        self.edit.addItem('18ХГТ, 18Х2Н4, МА, 10ХНСД')
        self.edit.addItem('90ХГСА, 38ХНВА, ХВГ')
        self.edit.addItem('30ХГСА, ХГВ, 38ХНВА, 16ГДНМ')
        self.edit.addItem('12Х13, 20Х13, 30Х13')
        self.edit.addItem('АК25, АК27, АК29, АК29ПК')
        self.edit.addItem('АК32, АК35, АК32ПК')
        self.edit.addItem('АК33, АК34, АК36, АК37')
        self.edit.addItem('14Х17Н2, 2Х17Н2')
        self.edit.addItem('ОХ18Н10Т')
        self.edit.addItem('ВТ-3, ВТ-5, СПЛ.-19')
        self.edit.addItem('3, 3В, 3М')
        self.edit.addItem('ММЛ-1')
        self.edit.addItem('ММЛ-2')
        self.edit.addItem('45Г17, ЮЗ, ЮЗХБ ММЛ-3')
        self.edit.currentText()
        self.edit.setStyleSheet(style)

        self.edit_1 = QComboBox(self)
        self.edit_1.setGeometry(0, 35, 240, 30)
        self.edit_1.addItem('Точение')
        self.edit_1.addItem('Доводка, шлифовка')
        self.edit_1.addItem('По корке, вырезка')
        self.edit_1.addItem('По корке, поковка')
        self.edit_1.addItem('По корке, отливка')
        self.edit_1.addItem('На удар')
        self.edit_1.addItem('Тонкостенные')
        self.edit_1.currentText()
        self.edit_1.setStyleSheet(style)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.currentText()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.currentText()
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcInputContent_2(QDMNodeContentWidget):
    def initUI(self):
        #self.edit = QLineEdit("1", self)
        self.edit = QComboBox(self)
        self.edit.setGeometry(0, 4, 260, 30)
        self.edit.addItem("На столе или плите без крепления (с упором)")
        self.edit.addItem("В тисках")
        self.edit.addItem("В кулачках самоцентрирующего патрона")
        self.edit.addItem("На столе с пневмоприводом")
        self.edit.addItem("На столе с креплением 2-я болтами и планками")
        self.edit.addItem("Сбоку стола с выверкой")

        self.edit.setStyleSheet(style)
        self.edit_1 = QComboBox(self)
        self.edit_1.setGeometry(0, 35, 260, 30)
        self.edit_1.addItem("С выверкой")
        self.edit_1.addItem("Без выверки")
        self.edit_1.setStyleSheet(style)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.currentIndex()
        res['value2'] = self.edit_1.currentIndex()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = self.edit.currentIndex()
            value2 = self.edit_1.currentIndex()
            print(value)
            #self.edit.setText(value)
            self.edit.setCurrentIndex(value)
            self.edit_1.setCurrentIndex(value2)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcInputContent_4(QDMNodeContentWidget):
    def initUI(self):
        #self.edit = QLineEdit("1", self)
        self.edit = QComboBox(self)
        self.edit.setGeometry(0, 4, 260, 30)
        self.edit.addItem("В самоцентр. патроне")
        self.edit.addItem("В 4х кулачковом патроне")
        self.edit.addItem("В центрах")
        self.edit.addItem("На оправке")
        self.edit.addItem("На планшайбе с угол.")
        self.edit.setStyleSheet(style)
        self.edit_1 = QComboBox(self)
        self.edit_1.setGeometry(0, 35, 260, 30)
        self.edit_1.addItem("В кулачках")
        self.edit_1.addItem("В кулачках с центр.")
        self.edit_1.addItem("В кулачках с центр. люнет.")
        self.edit_1.addItem("В кулачках с люнет.")
        self.edit_1.addItem("В кулачках с разрезн. втул.")
        self.edit_1.setStyleSheet(style)
        self.edit_2 = QComboBox(self)
        self.edit_2.setGeometry(0, 66, 260, 30)
        self.edit_2.addItem("Без выверки")
        self.edit_2.setStyleSheet(style)
        self.edit_3 = QComboBox(self)
        self.edit_3.setGeometry(0, 97, 260, 30)
        self.edit_3.addItem("-")
        self.edit_3.setStyleSheet(style)
        self.edit_4 = QComboBox(self)
        self.edit_4.setGeometry(0, 128, 260, 30)
        self.edit_4.addItem("-")
        self.edit_4.setStyleSheet(style)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.currentIndex()
        res['value2'] = self.edit_1.currentIndex()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            value2 = data['value2']
            #value = self.edit.currentIndex()
            #value2 = self.edit_1.currentIndex()
            print(value)
            self.edit.setCurrentIndex(value)
            self.edit_1.setCurrentIndex(value2)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


@register_node(OP_NODE_INPUT)
class CalcNode_Input(CalcNodeResult):
    icon = path_img_in
    op_code = OP_NODE_INPUT
    op_title = "Значение"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContent(self)
        self.grNode = CalcGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        try:
            s_value = float(u_value.replace(',', '.'))
        except:
            s_value = str(u_value)

        self.value = s_value
        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()

        return self.value


@register_node(OP_NODE_INPUT_TEXT)
class CalcNode_Input(CalcNodeText):
    icon = path_img_com
    op_code = OP_NODE_INPUT_TEXT
    op_title = "Комментарий"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContentText(self)
        self.grNode = CalcGraphicsText(self)
        self.content.plainTextEdit.textChanged.connect(self.onInputChanged)  #edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()

        return self.value


@register_node(OP_NODE_INPUT_1)
class CalcNode_Input_1(CalcTable2):
    icon = path_img_tab
    op_code = OP_NODE_INPUT_1
    op_title = "К1а Коэф мат"
    content_label_objname = "calc_node_input_1"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContent_1(self)
        self.grNode = CalcGraphicsNodeComboBox(self)
        self.content.edit.currentTextChanged.connect(self.onInputChanged)  #textChanged.connect(self.onInputChanged)
        self.content.edit_1.currentTextChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.currentText()
        s_value = u_value
        #print(u_value)

        u_value_1 = self.content.edit_1.currentText()
        s_value_1 = u_value_1

        table = create_tables()[13]
        #print(table)
        #print(u_value_1)
        res_1 = table.get(u_value_1, "Р-")
        #print(res_1)
        res = res_1.get(u_value, "Р-")
        res_f = float(f'{res[0]}.{res[1]}')
        print(res_f)
        self.value = res_f

        #self.value_1 = s_value_1

        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()
        return self.value


@register_node(OP_NODE_INPUT_2)
class CalcNode_Input_2(CalcTable3):
    icon = path_img_tab
    op_code = OP_NODE_INPUT_2
    op_title = "К2 Уст и снят детали"
    content_label_objname = "calc_node_input_2"

    def __init__(self, scene):
        super().__init__(scene, inputs=[2], outputs=[1])
        self.eval()

    def initInnerClasses(self):

        self.content = CalcInputContent_2(self)
        self.grNode = CalcGraphicsNodeComboBox_2(self)
        self.content.edit.currentTextChanged.connect(self.onInputChanged_1)  #textChanged.connect(self.onInputChanged)
        self.content.edit_1.currentTextChanged.connect(self.onInputChanged)

    def evalImplementation_1(self):
        u_value = self.content.edit.currentText()
        u_value_1 = self.content.edit_1.currentText()
        # s_value_1 = u_value_1
        table = create_tables()[2]
        res_1 = table.get(u_value, "Р-")
        res = res_1.get(u_value_1, "Р-")

        i1 = self.getInput(0)
        try:
            val32 = i1.eval()
        except:
            val32 = 0

        if 0 < val32 <= 0.3:
            val32 = 0
        if 0.3 < val32 <= 1:
            val32 = 1
        if 1 < val32 <= 3:
            val32 = 2
        if 3 < val32 <= 5:
            val32 = 3
        if 5 < val32 <= 8:
            val32 = 4
        if 8 < val32 <= 12:
            val32 = 5
        if 12 < val32 <= 20:
            val32 = 6
        if 20 < val32 <= 30:
            val32 = 7
        if 30 < val32 <= 50:
            val32 = 8
        if 50 < val32 <= 100:
            val32 = 9
        if 100 < val32 <= 200:
            val32 = 10
        if 200 < val32 <= 500:
            val32 = 11
        if 500 < val32 <= 1000:
            val32 = 12
        if 1000 < val32 <= 2000:
            val32 = 13
        if 2000 < val32 <= 3000:
            val32 = 14

        self.value = res[val32]

        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()
        return self.value

    def evalImplementation(self):
        u_value = self.content.edit.currentText()
        u_value_1 = self.content.edit_1.currentText()
        #s_value_1 = u_value_1
        table = create_tables()[2]
        res_1 = table.get(u_value, "Р-")
        res = res_1.get(u_value_1, "Р-")

        i1 = self.getInput(0)
        try:
            val32 = i1.eval()
        except:
            val32 = 0

        if 0 < val32 <= 0.3:
            val32 = 0
        if 0.3 < val32 <= 1:
            val32 = 1
        if 1 < val32 <= 3:
            val32 = 2
        if 3 < val32 <= 5:
            val32 = 3
        if 5 < val32 <= 8:
            val32 = 4
        if 8 < val32 <= 12:
            val32 = 5
        if 12 < val32 <= 20:
            val32 = 6
        if 20 < val32 <= 30:
            val32 = 7
        if 30 < val32 <= 50:
            val32 = 8
        if 50 < val32 <= 100:
            val32 = 9
        if 100 < val32 <= 200:
            val32 = 10
        if 200 < val32 <= 500:
            val32 = 11
        if 500 < val32 <= 1000:
            val32 = 12
        if 1000 < val32 <= 2000:
            val32 = 13
        if 2000 < val32 <= 3000:
            val32 = 14

        self.value = res[val32]

        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()
        return self.value


@register_node(OP_NODE_INPUT_3)
class CalcNode_Input_1(CalcTable2):
    icon = path_img_tab
    op_code = OP_NODE_INPUT_3
    op_title = "Т1 Коэф мат"
    content_label_objname = "calc_node_input_1"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[1])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContent_tur1(self)
        self.grNode = CalcGraphicsNodeComboBox(self)
        self.content.edit.currentTextChanged.connect(self.onInputChanged)  #textChanged.connect(self.onInputChanged)
        self.content.edit_1.currentTextChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.currentText()
        s_value = u_value
        #print(u_value)

        u_value_1 = self.content.edit_1.currentText()
        s_value_1 = u_value_1

        table = create_tables_turning()[4]
        #print(table)
        #print(u_value_1)
        res_1 = table.get(u_value_1, "Р-")
        #print(res_1)
        res = res_1.get(u_value, "Р-")
        res_f = float(f'{res[0]}.{res[1]}')
        print(res_f)
        self.value = res_f

        #self.value_1 = s_value_1

        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()
        return self.value


@register_node(OP_NODE_INPUT_5)
class CalcNode_Input_5(CalcTable5):
    icon = path_img_tab
    op_code = OP_NODE_INPUT_5
    op_title = "Т4 Уст и снят детали"
    content_label_objname = "calc_node_input_4"

    def __init__(self, scene):
        super().__init__(scene, inputs=[2], outputs=[1])
        self.eval()

    def initInnerClasses(self):

        self.content = CalcInputContent_4(self)
        self.grNode = CalcGraphicsNodeComboBox_4(self)
        self.content.edit.currentTextChanged.connect(self.onInputChanged_1)  #textChanged.connect(self.onInputChanged)
        self.content.edit_1.currentTextChanged.connect(self.onInputChanged_2)
        self.content.edit_2.currentTextChanged.connect(self.onInputChanged_3)
        self.content.edit_3.currentTextChanged.connect(self.onInputChanged_4)
        self.content.edit_4.currentTextChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.currentText()
        u_value_1 = self.content.edit_1.currentText()
        u_value_2 = self.content.edit_2.currentText()
        u_value_3 = self.content.edit_3.currentText()
        u_value_4 = self.content.edit_4.currentText()
        print(u_value, u_value_1, u_value_2, u_value_3, u_value_4)
        res = ""

        if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с разрезн. втул.":
            table = create_tables_turning()[1]
            res = table.get(u_value_1, "Р-")
            print(f"---{res}")

            i1 = self.getInput(0)
            try:
                val32 = float(i1.eval())
            except:
                val32 = 0

            if 0 < val32 <= 1:
                val32 = 0
            if 1 < val32 <= 3:
                val32 = 1
            if 3 < val32 <= 5:
                val32 = 2
            if 5 < val32 <= 10:
                val32 = 3
            if 10 < val32 <= 20:
                val32 = 4
            if 20 < val32 <= 30:
                val32 = 5
            if 30 < val32 <= 50:
                val32 = 6
            if 50 < val32 <= 100:
                val32 = 7
            if 100 < val32 <= 200:
                val32 = 8
            if 200 < val32 <= 400:
                val32 = 9
            if 400 < val32 <= 800:
                val32 = 10
            if 800 < val32 <= 1500:
                val32 = 11
            if 1500 < val32 <= 3000:
                val32 = 12
            try:
                self.value = res[val32]
            except:
                self.value = "-"

            self.markDirty(False)
            self.markInvalid(False)

            self.markDescendantsInvalid(False)
            self.markDescendantsDirty()

            self.grNode.setToolTip("")
            self.eval()
            self.evalChildren()
            return self.value

        if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() != "В кулачках с разрезн. втул.":
            table = create_tables_turning()[1]
            res_11 = table.get(u_value_1, "Р-")
            res_1 = res_11.get(u_value_2, "Р-")
            res = res_1.get(u_value_3, "Р-")
            print(f"---{res}")

            i1 = self.getInput(0)
            try:
                val32 = float(i1.eval())
            except:
                val32 = 0

            if 0 < val32 <= 1:
                val32 = 0
            if 1 < val32 <= 3:
                val32 = 1
            if 3 < val32 <= 5:
                val32 = 2
            if 5 < val32 <= 10:
                val32 = 3
            if 10 < val32 <= 20:
                val32 = 4
            if 20 < val32 <= 30:
                val32 = 5
            if 30 < val32 <= 50:
                val32 = 6
            if 50 < val32 <= 100:
                val32 = 7
            if 100 < val32 <= 200:
                val32 = 8
            if 200 < val32 <= 400:
                val32 = 9
            if 400 < val32 <= 800:
                val32 = 10
            if 800 < val32 <= 1500:
                val32 = 11
            if 1500 < val32 <= 3000:
                val32 = 12
            try:
                self.value = res[val32]
            except:
                self.value = "-"

            self.markDirty(False)
            self.markInvalid(False)

            self.markDescendantsInvalid(False)
            self.markDescendantsDirty()

            self.grNode.setToolTip("")
            self.eval()
            self.evalChildren()
            return self.value

        if self.content.edit.currentText() == "В 4х кулачковом патроне":
            table = create_tables_turning()[2]
            res_111 = table.get(u_value_1, "Р-")
            res_11 = res_111.get(u_value_2, "Р-")
            res_1 = res_11.get(u_value_3, "Р-")
            res = res_1.get(u_value_4, "Р-")
            print(f"---{table}")

            i1 = self.getInput(0)
            try:
                val32 = float(i1.eval())
            except:
                val32 = 0

            if 0 < val32 <= 3:
                val32 = 0
            if 3 < val32 <= 5:
                val32 = 1
            if 5 < val32 <= 10:
                val32 = 2
            if 10 < val32 <= 20:
                val32 = 3
            if 20 < val32 <= 30:
                val32 = 4
            if 30 < val32 <= 50:
                val32 = 5
            if 50 < val32 <= 100:
                val32 = 6
            if 100 < val32 <= 200:
                val32 = 7
            if 200 < val32 <= 400:
                val32 = 8
            if 400 < val32 <= 800:
                val32 = 9
            if 800 < val32 <= 1500:
                val32 = 10
            if 1500 < val32 <= 3000:
                val32 = 11
            if 3000 < val32 <= 5000:
                val32 = 12
            if 5000 < val32 <= 10000:
                val32 = 13
            if 10000 < val32 <= 20000:
                val32 = 14
            if 20000 < val32 <= 40000:
                val32 = 15
            if 40000 < val32 <= 75000:
                val32 = 16
            if 75000 < val32 <= 100000:
                val32 = 17
            if 100000 < val32:
                val32 = 18

            try:
                self.value = res[val32]
            except:
                self.value = "-"

            self.markDirty(False)
            self.markInvalid(False)

            self.markDescendantsInvalid(False)
            self.markDescendantsDirty()

            self.grNode.setToolTip("")
            self.eval()
            self.evalChildren()
            return self.value

        if self.content.edit.currentText() == "В центрах":
            table = create_tables_turning()[2]
            res_1 = table.get(u_value_1, "Р-")
            res = res_1.get(u_value_2, "Р-")
            # res_1 = res_11.get(u_value_3, "Р-")
            # res = res_1.get(u_value_4, "Р-")
            print(f"---{res}")

            i1 = self.getInput(0)
            try:
                val32 = float(i1.eval())
            except:
                val32 = 0

            if 0 < val32 <= 1:
                val32 = 0
            if 1 < val32 <= 3:
                val32 = 1
            if 3 < val32 <= 5:
                val32 = 2
            if 5 < val32 <= 10:
                val32 = 3
            if 10 < val32 <= 20:
                val32 = 4
            if 20 < val32 <= 30:
                val32 = 5
            if 30 < val32 <= 50:
                val32 = 6
            if 50 < val32 <= 100:
                val32 = 7
            if 100 < val32 <= 200:
                val32 = 8
            if 200 < val32 <= 400:
                val32 = 9
            if 400 < val32 <= 800:
                val32 = 10
            if 800 < val32 <= 1500:
                val32 = 11
            if 1500 < val32 <= 3000:
                val32 = 12

            try:
                self.value = res[val32]
            except:
                self.value = "-"

            self.markDirty(False)
            self.markInvalid(False)

            self.markDescendantsInvalid(False)
            self.markDescendantsDirty()

            self.grNode.setToolTip("")
            self.eval()
            self.evalChildren()
            return self.value

        if self.content.edit.currentText() == "На планшайбе с угол.":
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками":
                if self.content.edit_2.currentText() == "С выверкой в одн. плоскости":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"---{res}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7
                    if 100 < val32 <= 200:
                        val32 = 8
                    if 200 < val32 <= 400:
                        val32 = 9
                    if 400 < val32 <= 800:
                        val32 = 10
                    if 800 < val32 <= 1500:
                        val32 = 11

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

                if self.content.edit_2.currentText() == "С угол. с крепл. болтами и планками":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"---{res}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7
                    if 100 < val32 <= 200:
                        val32 = 8
                    if 200 < val32 <= 400:
                        val32 = 9
                    if 400 < val32 <= 800:
                        val32 = 10
                    if 800 < val32 <= 1500:
                        val32 = 11

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

        if self.content.edit.currentText() == "На планшайбе с угол.":
            if self.content.edit_1.currentText() == "С угол. с крепл. болтами и планками":
                if self.content.edit_2.currentText() == "С центр. приспособ. без выверки":
                    table = create_tables_turning()[2]
                    res_1 = table.get(u_value_1, "Р-")
                    res = res_1.get(u_value_2, "Р-")
                    print(f"---{res}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7
                    if 100 < val32 <= 200:
                        val32 = 8
                    if 200 < val32 <= 400:
                        val32 = 9
                    if 400 < val32 <= 800:
                        val32 = 10
                    if 800 < val32 <= 1500:
                        val32 = 11

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value


        if self.content.edit.currentText() == "На планшайбе с угол.":
            if self.content.edit_1.currentText() == "С крепл. болтами и планками":
                if self.content.edit_2.currentText() == "С выверкой в одн. плоскости":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"---{res}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7
                    if 100 < val32 <= 200:
                        val32 = 8
                    if 200 < val32 <= 400:
                        val32 = 9
                    if 400 < val32 <= 800:
                        val32 = 10
                    if 800 < val32 <= 1500:
                        val32 = 11

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

                if self.content.edit_2.currentText() == "С выверкой в двух плоскостях":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"---{res}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7
                    if 100 < val32 <= 200:
                        val32 = 8
                    if 200 < val32 <= 400:
                        val32 = 9
                    if 400 < val32 <= 800:
                        val32 = 10
                    if 800 < val32 <= 1500:
                        val32 = 11

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value



        if self.content.edit.currentText() == "На планшайбе с угол.":
            if self.content.edit_1.currentText() == "С крепл. болтами и планками":
                if self.content.edit_2.currentText() == "С центр. приспособ. без выверки":
                    table = create_tables_turning()[2]
                    res_1 = table.get(u_value_1, "Р-")
                    res = res_1.get(u_value_2, "Р-")
                    print(f"---{res}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7
                    if 100 < val32 <= 200:
                        val32 = 8
                    if 200 < val32 <= 400:
                        val32 = 9
                    if 400 < val32 <= 800:
                        val32 = 10
                    if 800 < val32 <= 1500:
                        val32 = 11

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value


        if self.content.edit.currentText() == "На оправке":
            if self.content.edit_1.currentText() == "На концевой оправке":
                if self.content.edit_2.currentText() == "На гладк. или шлиц. оправке":
                    if self.content.edit_3.currentText() == "С креп. гайкой и шайбой":
                        table = create_tables_turning()[2]
                        res_111 = table.get(u_value_1, "Р-")
                        res_11 = res_111.get(u_value_2, "Р-")
                        res_1 = res_11.get(u_value_3, "Р-")
                        res = res_1.get(u_value_4, "Р-")
                        print(f"---{res}")

                        i1 = self.getInput(0)
                        try:
                            val32 = float(i1.eval())
                        except:
                            val32 = 0

                        if 0 < val32 <= 1:
                            val32 = 0
                        if 1 < val32 <= 3:
                            val32 = 1
                        if 3 < val32 <= 5:
                            val32 = 2
                        if 5 < val32 <= 10:
                            val32 = 3
                        if 10 < val32 <= 20:
                            val32 = 4
                        if 20 < val32 <= 30:
                            val32 = 5
                        if 30 < val32 <= 50:
                            val32 = 6
                        if 50 < val32 <= 100:
                            val32 = 7

                        try:
                            self.value = res[val32]
                        except:
                            self.value = "-"

                        self.markDirty(False)
                        self.markInvalid(False)

                        self.markDescendantsInvalid(False)
                        self.markDescendantsDirty()

                        self.grNode.setToolTip("")
                        self.eval()
                        self.evalChildren()
                        return self.value

                    if self.content.edit_3.currentText() == "С поджатием задним центр.":
                        table = create_tables_turning()[2]
                        res_111 = table.get(u_value_1, "Р-")
                        res_11 = res_111.get(u_value_2, "Р-")
                        res_1 = res_11.get(u_value_3, "Р-")
                        res = res_1.get(u_value_4, "Р-")
                        print(f"---{res}")

                        i1 = self.getInput(0)
                        try:
                            val32 = float(i1.eval())
                        except:
                            val32 = 0

                        if 0 < val32 <= 1:
                            val32 = 0
                        if 1 < val32 <= 3:
                            val32 = 1
                        if 3 < val32 <= 5:
                            val32 = 2
                        if 5 < val32 <= 10:
                            val32 = 3
                        if 10 < val32 <= 20:
                            val32 = 4
                        if 20 < val32 <= 30:
                            val32 = 5
                        if 30 < val32 <= 50:
                            val32 = 6
                        if 50 < val32 <= 100:
                            val32 = 7

                        try:
                            self.value = res[val32]
                        except:
                            self.value = "-"

                        self.markDirty(False)
                        self.markInvalid(False)

                        self.markDescendantsInvalid(False)
                        self.markDescendantsDirty()

                        self.grNode.setToolTip("")
                        self.eval()
                        self.evalChildren()
                        return self.value

        if self.content.edit.currentText() == "На оправке":
            if self.content.edit_1.currentText() == "На концевой оправке":
                if self.content.edit_2.currentText() == "С поджатием задним центр.":
                    if self.content.edit_3.currentText() == "Без крепления":
                        table = create_tables_turning()[2]
                        res_11 = table.get(u_value_1, "Р-")
                        res_1 = res_11.get(u_value_2, "Р-")
                        res = res_1.get(u_value_3, "Р-")
                        print(f"---{res}")

                        i1 = self.getInput(0)
                        try:
                            val32 = float(i1.eval())
                        except:
                            val32 = 0

                        if 0 < val32 <= 1:
                            val32 = 0
                        if 1 < val32 <= 3:
                            val32 = 1
                        if 3 < val32 <= 5:
                            val32 = 2
                        if 5 < val32 <= 10:
                            val32 = 3
                        if 10 < val32 <= 20:
                            val32 = 4
                        if 20 < val32 <= 30:
                            val32 = 5
                        if 30 < val32 <= 50:
                            val32 = 6
                        if 50 < val32 <= 100:
                            val32 = 7

                        try:
                            self.value = res[val32]
                        except:
                            self.value = "-"

                        self.markDirty(False)
                        self.markInvalid(False)

                        self.markDescendantsInvalid(False)
                        self.markDescendantsDirty()

                        self.grNode.setToolTip("")
                        self.eval()
                        self.evalChildren()
                        return self.value

                    if self.content.edit_3.currentText() == "С креп. гайкой и шайбой":
                        table = create_tables_turning()[2]
                        res_11 = table.get(u_value_1, "Р-")
                        res_1 = res_11.get(u_value_2, "Р-")
                        res = res_1.get(u_value_3, "Р-")
                        print(f"---{res}")

                        i1 = self.getInput(0)
                        try:
                            val32 = float(i1.eval())
                        except:
                            val32 = 0

                        if 0 < val32 <= 1:
                            val32 = 0
                        if 1 < val32 <= 3:
                            val32 = 1
                        if 3 < val32 <= 5:
                            val32 = 2
                        if 5 < val32 <= 10:
                            val32 = 3
                        if 10 < val32 <= 20:
                            val32 = 4
                        if 20 < val32 <= 30:
                            val32 = 5
                        if 30 < val32 <= 50:
                            val32 = 6
                        if 50 < val32 <= 100:
                            val32 = 7

                        try:
                            self.value = res[val32]
                        except:
                            self.value = "-"

                        self.markDirty(False)
                        self.markInvalid(False)

                        self.markDescendantsInvalid(False)
                        self.markDescendantsDirty()

                        self.grNode.setToolTip("")
                        self.eval()
                        self.evalChildren()
                        return self.value

        if self.content.edit.currentText() == "На оправке":
            if self.content.edit_1.currentText() == "На концевой оправке":
                if self.content.edit_2.currentText() == "На гладк. или шлиц. оправке":
                    if self.content.edit_3.currentText() == "Без крепления":
                        table = create_tables_turning()[2]
                        res_11 = table.get(u_value_1, "Р-")
                        res_1 = res_11.get(u_value_2, "Р-")
                        res = res_1.get(u_value_3, "Р-")
                        print(f"---{res}")

                        i1 = self.getInput(0)
                        try:
                            val32 = float(i1.eval())
                        except:
                            val32 = 0

                        if 0 < val32 <= 1:
                            val32 = 0
                        if 1 < val32 <= 3:
                            val32 = 1
                        if 3 < val32 <= 5:
                            val32 = 2
                        if 5 < val32 <= 10:
                            val32 = 3
                        if 10 < val32 <= 20:
                            val32 = 4
                        if 20 < val32 <= 30:
                            val32 = 5
                        if 30 < val32 <= 50:
                            val32 = 6
                        if 50 < val32 <= 100:
                            val32 = 7

                        try:
                            self.value = res[val32]
                        except:
                            self.value = "-"

                        self.markDirty(False)
                        self.markInvalid(False)

                        self.markDescendantsInvalid(False)
                        self.markDescendantsDirty()

                        self.grNode.setToolTip("")
                        self.eval()
                        self.evalChildren()
                        return self.value

        if self.content.edit.currentText() == "На оправке":
            if self.content.edit_1.currentText() == "На концевой оправке":
                if self.content.edit_2.currentText() == "На резьб. оправке":
                    if self.content.edit_3.currentText() == "Без контрогайки":
                        table = create_tables_turning()[2]
                        res_11 = table.get(u_value_1, "Р-")
                        res_1 = res_11.get(u_value_2, "Р-")
                        res = res_1.get(u_value_3, "Р-")
                        print(f"---{res_11}")

                        i1 = self.getInput(0)
                        try:
                            val32 = float(i1.eval())
                        except:
                            val32 = 0

                        if 0 < val32 <= 1:
                            val32 = 0
                        if 1 < val32 <= 3:
                            val32 = 1
                        if 3 < val32 <= 5:
                            val32 = 2
                        if 5 < val32 <= 10:
                            val32 = 3
                        if 10 < val32 <= 20:
                            val32 = 4
                        if 20 < val32 <= 30:
                            val32 = 5
                        if 30 < val32 <= 50:
                            val32 = 6
                        if 50 < val32 <= 100:
                            val32 = 7

                        try:
                            self.value = res[val32]
                        except:
                            self.value = "-"

                        self.markDirty(False)
                        self.markInvalid(False)

                        self.markDescendantsInvalid(False)
                        self.markDescendantsDirty()

                        self.grNode.setToolTip("")
                        self.eval()
                        self.evalChildren()
                        return self.value

                if self.content.edit_3.currentText() == "С контрогайкой":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"-*-{res_11}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

        if self.content.edit.currentText() == "На оправке":
            if self.content.edit_1.currentText() == "На центровой оправке":
                if self.content.edit_2.currentText() == "На гладк. или шлиц. оправке":
                    if self.content.edit_3.currentText() == "При свободном надевании дет.":
                        table = create_tables_turning()[2]
                        res_11 = table.get(u_value_1, "Р-")
                        res_1 = res_11.get(u_value_2, "Р-")
                        res = res_1.get(u_value_3, "Р-")
                        print(f"---{res_11}")

                        i1 = self.getInput(0)
                        try:
                            val32 = float(i1.eval())
                        except:
                            val32 = 0

                        if 0 < val32 <= 1:
                            val32 = 0
                        if 1 < val32 <= 3:
                            val32 = 1
                        if 3 < val32 <= 5:
                            val32 = 2
                        if 5 < val32 <= 10:
                            val32 = 3
                        if 10 < val32 <= 20:
                            val32 = 4
                        if 20 < val32 <= 30:
                            val32 = 5
                        if 30 < val32 <= 50:
                            val32 = 6
                        if 50 < val32 <= 100:
                            val32 = 7

                        try:
                            self.value = res[val32]
                        except:
                            self.value = "-"

                        self.markDirty(False)
                        self.markInvalid(False)

                        self.markDescendantsInvalid(False)
                        self.markDescendantsDirty()

                        self.grNode.setToolTip("")
                        self.eval()
                        self.evalChildren()
                        return self.value

                if self.content.edit_3.currentText() == "При тугом надевании дет.":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"-*-{res_11}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

            if self.content.edit_2.currentText() == "На оправке с креп. гайкой":
                if self.content.edit_3.currentText() == "С быстросъёмной шайбой":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"-*-{res_11}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

                if self.content.edit_3.currentText() == "С простой шайбой":
                    table = create_tables_turning()[2]
                    res_11 = table.get(u_value_1, "Р-")
                    res_1 = res_11.get(u_value_2, "Р-")
                    res = res_1.get(u_value_3, "Р-")
                    print(f"-*-{res_11}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

        if self.content.edit.currentText() == "На оправке":
            if self.content.edit_1.currentText() == "На центровой оправке":
                if self.content.edit_2.currentText() == "На разжим. оправке с креп. гайкой.":
                    table = create_tables_turning()[2]
                    res_1 = table.get(u_value_1, "Р-")
                    res = res_1.get(u_value_2, "Р-")
                    #res = res_1.get(u_value_3, "Р-")
                    print(f"-*-{res}")

                    i1 = self.getInput(0)
                    try:
                        val32 = float(i1.eval())
                    except:
                        val32 = 0

                    if 0 < val32 <= 1:
                        val32 = 0
                    if 1 < val32 <= 3:
                        val32 = 1
                    if 3 < val32 <= 5:
                        val32 = 2
                    if 5 < val32 <= 10:
                        val32 = 3
                    if 10 < val32 <= 20:
                        val32 = 4
                    if 20 < val32 <= 30:
                        val32 = 5
                    if 30 < val32 <= 50:
                        val32 = 6
                    if 50 < val32 <= 100:
                        val32 = 7

                    try:
                        self.value = res[val32]
                    except:
                        self.value = "-"

                    self.markDirty(False)
                    self.markInvalid(False)

                    self.markDescendantsInvalid(False)
                    self.markDescendantsDirty()

                    self.grNode.setToolTip("")
                    self.eval()
                    self.evalChildren()
                    return self.value

        # if self.content.edit.currentText() == "В самоцентр. патроне" and self.content.edit_1.currentText() == "В кулачках с люнет." and self.content.edit_2.currentText() == "С выверкой по диам.":
        #     table = create_tables_turning()[1]
        #     res_11 = table.get(u_value_1, "Р-")
        #     res_1 = res_11.get(u_value_2, "Р-")
        #     res = res_1.get(u_value_3, "Р-")
        #     print(f"---{res}")

        # i1 = self.getInput(0)
        # try:
        #     val32 = float(i1.eval())
        # except:
        #     val32 = 0
        #
        # if 0 < val32 <= 1:
        #     val32 = 0
        # if 1 < val32 <= 3:
        #     val32 = 1
        # if 3 < val32 <= 5:
        #     val32 = 2
        # if 5 < val32 <= 10:
        #     val32 = 3
        # if 10 < val32 <= 20:
        #     val32 = 4
        # if 20 < val32 <= 30:
        #     val32 = 5
        # if 30 < val32 <= 50:
        #     val32 = 6
        # if 50 < val32 <= 100:
        #     val32 = 7
        # if 100 < val32 <= 200:
        #     val32 = 8
        # if 200 < val32 <= 400:
        #     val32 = 9
        # if 400 < val32 <= 800:
        #     val32 = 10
        # if 800 < val32 <= 1500:
        #     val32 = 11
        # if 1500 < val32 <= 3000:
        #     val32 = 12
        # try:
        #     self.value = res[val32]
        # except:
        #     self.value = "-"
        #
        # self.markDirty(False)
        # self.markInvalid(False)
        #
        # self.markDescendantsInvalid(False)
        # self.markDescendantsDirty()
        #
        # self.grNode.setToolTip("")
        # self.eval()
        # self.evalChildren()
        # return self.value

            # elif self.content.edit.currentText() == "В 4х кулачковом патроне":
            #     if 0 < val32 <= 0.3:
            #         val32 = 0
            #     if 0.3 < val32 <= 0.5:
            #         val32 = 1
            #     if 0.5 < val32 <= 10:
            #         val32 = 2
            #     if 10 < val32 <= 20:
            #         val32 = 3
            #     if 20 < val32 <= 30:
            #         val32 = 4
            #     if 30 < val32 <= 50:
            #         val32 = 5
            #     if 50 < val32 <= 100:
            #         val32 = 6
            #     if 100 < val32 <= 200:
            #         val32 = 7
            #     if 200 < val32 <= 400:
            #         val32 = 8
            #     if 400 < val32 <= 800:
            #         val32 = 9
            #     if 800 < val32 <= 1500:
            #         val32 = 10
            #     if 1500 < val32 <= 3000:
            #         val32 = 11
            #     if 3000 < val32 <= 5000:
            #         val32 = 12
            #     if 5000 < val32 <= 10000:
            #         val32 = 13
            #     if 10000 < val32 <= 20000:
            #         val32 = 14
            #     if 20000 < val32 <= 40000:
            #         val32 = 15
            #     if 40000 < val32 <= 75000:
            #         val32 = 16
            #     if 75000 < val32 <= 100000:
            #         val32 = 17
            #     if 100000 < val32:
            #         val32 = 18
            #
            # elif self.content.edit.currentText() == "В центрах":
            #     if 0 < val32 <= 0.1:
            #         val32 = 0
            #     if 0.1 < val32 <= 3:
            #         val32 = 1
            #     if 3 < val32 <= 5:
            #         val32 = 2
            #     if 5 < val32 <= 10:
            #         val32 = 3
            #     if 10 < val32 <= 20:
            #         val32 = 4
            #     if 20 < val32 <= 30:
            #         val32 = 5
            #     if 30 < val32 <= 50:
            #         val32 = 6
            #     if 50 < val32 <= 100:
            #         val32 = 7
            #     if 100 < val32 <= 200:
            #         val32 = 8
            #     if 200 < val32 <= 400:
            #         val32 = 9
            #     if 400 < val32 <= 800:
            #         val32 = 10
            #     if 800 < val32 <= 1500:
            #         val32 = 11
            #     if 1500 < val32 <= 3000:
            #         val32 = 12
            #     if 3000 < val32 <= 5000:
            #         val32 = 13
            #     if 5000 < val32 <= 10000:
            #         val32 = 14
            #
            # elif self.content.edit.currentText() == "На оправке":
            #     if 0 < val32 <= 1:
            #         val32 = 0
            #     if 1 < val32 <= 3:
            #         val32 = 1
            #     if 3 < val32 <= 5:
            #         val32 = 2
            #     if 5 < val32 <= 10:
            #         val32 = 3
            #     if 10 < val32 <= 20:
            #         val32 = 4
            #     if 20 < val32 <= 30:
            #         val32 = 5
            #     if 30 < val32 <= 50:
            #         val32 = 6
            #     if 50 < val32 <= 100:
            #         val32 = 7
            #
            # elif self.content.edit.currentText() == "На планшайбе с угол.":
            #     if 0 < val32 <= 1:
            #         val32 = 0
            #     if 1 < val32 <= 3:
            #         val32 = 1
            #     if 3 < val32 <= 5:
            #         val32 = 2
            #     if 5 < val32 <= 10:
            #         val32 = 3
            #     if 10 < val32 <= 20:
            #         val32 = 4
            #     if 20 < val32 <= 30:
            #         val32 = 5
            #     if 30 < val32 <= 50:
            #         val32 = 6
            #     if 50 < val32 <= 100:
            #         val32 = 7
            #     if 100 < val32 <= 200:
            #         val32 = 8
            #     if 200 < val32 <= 400:
            #         val32 = 9
            #     if 400 < val32 <= 800:
            #         val32 = 10
            #     if 800 < val32 <= 1500:
            #         val32 = 11

