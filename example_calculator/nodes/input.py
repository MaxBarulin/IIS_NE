from PyQt5.QtWidgets import QVBoxLayout, QLabel, QButtonGroup, QRadioButton, QSpacerItem, QSizePolicy, QHBoxLayout
from qtpy.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit
from qtpy.QtCore import Qt, QRect
from example_calculator.calc_conf import register_node, OP_NODE_INPUT, OP_NODE_INPUT_1, OP_NODE_INPUT_2, \
    OP_NODE_INPUT_TEXT, OP_NODE_INPUT_3, OP_NODE_INPUT_5, OP_NODE_TEST
from example_calculator.calc_node_base import CalcNode, CalcTable2, CalcTable3, CalcGraphicsNode, \
    CalcGraphicsNodeComboBox, CalcGraphicsNodeComboBox_2, CalcGraphicsText, CalcNodeText, CalcNodeResult, CalcTable5, \
    CalcGraphicsNodeComboBox_4, CalcGraphicsNodeTest, CalcNodeResultTest
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.utils import dumpException
import os
from example_calculator.table import create_tables, create_tables_turning, create_tables_turning_other

open_img_in = "in_1.ico"
open_img_tab = "table.ico"
open_img_com = "com.ico"

put = os.path.dirname(__file__)

path_img_in = f'{put}\icons\{open_img_in}'
path_img_tab = f'{put}\icons\{open_img_tab}'
path_img_com = f'{put}\icons\{open_img_com}'

#для белой темы
style = '''
QPlainTextEdit {
    color: #000000; 
}
QComboBox {
    color: #000000;    
    background-color: #f2f2f2;
    padding: 4px;
    border: 0px solid rgb(#fff);
    border-radius: 0px;
    padding-left: 5px;
    padding-right: 5px;
    selection-background-color: #dfdfdf;
}
QComboBox QAbstractItemView {
    color: #000000;    
    background-color: #f2f2f2;
    padding: 4px;
    border: 0px solid rgb(#fff);
    border-radius: 0px;
    padding-left: 5px;
    padding-right: 5px;
    selection-background-color: #dfdfdf;
}
'''

class CalcInputContentTest(QDMNodeContentWidget):
    def initUI(self):
        # Основные метки
        lbl = QLabel(self.node.content_label, self)
        lbl.setObjectName(self.node.content_label_objname)
        lbl.setGeometry(8, 22, 100, 14)

        lbl_1 = QLabel(self.node.content_label_1, self)
        lbl_1.setObjectName(self.node.content_label_objname)
        lbl_1.setGeometry(8, 44, 100, 14)

        lbl_2 = QLabel(self.node.content_label_2, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(140, 33, 50, 14)
        lbl_2.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        # Метка для отображения текущего значения
        self.label = QLabel("12.5 + 3", self)
        self.label.setGeometry(70, -2, 150, 20)  # Увеличен размер для отображения текста

        self.value = 1
        self.ra = 1

        # Создаём QButtonGroup для обеспечения выбора только одной основной радиокнопки
        self.radio_group = QButtonGroup(self)
        self.radio_1 = QRadioButton("12.5", self)
        self.radio_2 = QRadioButton("6.3", self)
        self.radio_3 = QRadioButton("1.6", self)

        # Добавляем основные радиокнопки в группу
        self.radio_group.addButton(self.radio_1)
        self.radio_group.addButton(self.radio_2)
        self.radio_group.addButton(self.radio_3)

        self.radio_1.setChecked(True)

        # Позиционируем основные радиокнопки вручную
        y_start = 18  # Начальная позиция по оси Y
        spacing = 16  # Расстояние между радиокнопками
        for i, radio_button in enumerate([self.radio_1, self.radio_2, self.radio_3]):
            radio_button.setGeometry(70, y_start + i * spacing, 50, 20)

        # Создаём дополнительные радиокнопки заранее
        self.create_additional_radios()

        # Подключаем сигнал изменения основной радиокнопки к обработчику
        self.radio_group.buttonClicked.connect(self.on_main_radio_changed)

        # Подключаем сигналы дополнительных радиокнопок к обновлению метки
        self.additional_group_1.buttonClicked.connect(self.update_label)
        self.additional_group_2.buttonClicked.connect(self.update_label)
        self.additional_group_3.buttonClicked.connect(self.update_label)

        # При инициализации устанавливаем дополнительные радиокнопки
        self.update_additional_radios(1)

    def create_additional_radios(self):
        """Создаёт все дополнительные радиокнопки с фиксированным позиционированием."""
        # Дополнительные радиокнопки для опции 1 (4 радиокнопки)
        self.additional_radio_1_1 = QRadioButton("3", self)
        self.additional_radio_1_1.setGeometry(122, 18, 100, 20)
        self.additional_radio_1_1.setChecked(True)  # Выбираем по умолчанию

        self.additional_radio_1_2 = QRadioButton("5", self)
        self.additional_radio_1_2.setGeometry(122, 34, 100, 20)

        self.additional_radio_1_3 = QRadioButton("10", self)
        self.additional_radio_1_3.setGeometry(122, 50, 100, 20)

        self.additional_radio_1_4 = QRadioButton("15", self)
        self.additional_radio_1_4.setGeometry(122, 66, 100, 20)

        # Дополнительные радиокнопки для опций 2 и 3 (по 1 радиокнопке каждая)
        self.additional_radio_2 = QRadioButton("1", self)
        self.additional_radio_2.setGeometry(122, 18, 100, 20)
        self.additional_radio_2.setChecked(True)  # Выбираем по умолчанию

        self.additional_radio_3 = QRadioButton("0.5", self)
        self.additional_radio_3.setGeometry(122, 18, 100, 20)
        self.additional_radio_3.setChecked(True)  # Выбираем по умолчанию

        # Создаём группы для дополнительных радиокнопок
        self.additional_group_1 = QButtonGroup(self)
        self.additional_group_1.addButton(self.additional_radio_1_1)
        self.additional_group_1.addButton(self.additional_radio_1_2)
        self.additional_group_1.addButton(self.additional_radio_1_3)
        self.additional_group_1.addButton(self.additional_radio_1_4)

        self.additional_group_2 = QButtonGroup(self)
        self.additional_group_2.addButton(self.additional_radio_2)

        self.additional_group_3 = QButtonGroup(self)
        self.additional_group_3.addButton(self.additional_radio_3)

    def update_additional_radios(self, selected_option):
        """
        Обновляет выбор дополнительных радиокнопок в зависимости от выбранной основной опции.
        :param selected_option: Значение выбранной основной радиокнопки (1, 2 или 3)
        """
        if selected_option == 1:
            self.additional_radio_1_1.show()
            self.additional_radio_1_2.show()
            self.additional_radio_1_3.show()
            self.additional_radio_1_4.show()
            self.additional_radio_2.hide()
            self.additional_radio_3.hide()

            self.additional_radio_1_1.setChecked(True)
            # При выборе опции 1 выбираем первую дополнительную радиокнопку
        elif selected_option == 2:
            self.additional_radio_2.show()
            self.additional_radio_1_1.hide()
            self.additional_radio_1_2.hide()
            self.additional_radio_1_3.hide()
            self.additional_radio_1_4.hide()
            self.additional_radio_3.hide()
            self.additional_radio_2.setChecked(True)
            # При выборе опции 2 выбираем дополнительную радиокнопку 2.1
        elif selected_option == 3:
            self.additional_radio_3.show()
            self.additional_radio_1_1.hide()
            self.additional_radio_1_2.hide()
            self.additional_radio_1_3.hide()
            self.additional_radio_1_4.hide()
            self.additional_radio_2.hide()
            self.additional_radio_3.setChecked(True)
            # При выборе опции 3 выбираем дополнительную радиокнопку 3.1

        # Обновляем метку после изменения выбора
        self.update_label()

    def update_label(self):
        """
        Обновляет текст метки на основе выбранной основной и дополнительной радиокнопки.
        """
        selected_main = "12.5" if self.radio_1.isChecked() else "6.3" if self.radio_2.isChecked() else "1.6"

        # Находим выбранную дополнительную радиокнопку
        additional_selected = ""
        if self.radio_1.isChecked():
            additional_selected = next((btn.text() for btn in self.additional_group_1.buttons() if btn.isChecked()), "")
        elif self.radio_2.isChecked():
            additional_selected = self.additional_radio_2.text() if self.additional_radio_2.isChecked() else ""
        elif self.radio_3.isChecked():
            additional_selected = self.additional_radio_3.text() if self.additional_radio_3.isChecked() else ""

        # Обновляем текст метки
        self.label.setText(f"{selected_main}.{additional_selected}")

    def on_main_radio_changed(self):
        """
        Обработчик изменения основной радиокнопки.
        """
        if self.radio_1.isChecked():
            selected = 1
        elif self.radio_2.isChecked():
            selected = 2
        elif self.radio_3.isChecked():
            selected = 3
        else:
            selected = None

        # Обновляем дополнительные радиокнопки при изменении основной
        self.update_additional_radios(selected)

        # Вызовите eval у узла для перерасчёта
        self.node.eval()

    def get_selected_additional_option(self):
        """
        Возвращает текст выбранной дополнительной радиокнопки или None, если ничего не выбрано.
        """
        # Проверяем группу 1
        for button in self.additional_group_1.buttons():
            if button.isChecked():
                return button.text()
        # Проверяем группу 2
        for button in self.additional_group_2.buttons():
            if button.isChecked():
                return button.text()
        # Проверяем группу 3
        for button in self.additional_group_3.buttons():
            if button.isChecked():
                return button.text()
        return None

    def serialize(self):
        res = super().serialize()
        if self.radio_1.isChecked():
            self.ra = 1
        elif self.radio_2.isChecked():
            self.ra = 2
        elif self.radio_3.isChecked():
            self.ra = 3
        res['ra'] = self.ra

        # Сохраняем состояние дополнительных радиокнопок
        additional_selected = self.get_selected_additional_option()
        res['additional_ra'] = additional_selected
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            ra = data.get('ra', 1)
            if ra == 1:
                self.radio_1.setChecked(True)
            elif ra == 2:
                self.radio_2.setChecked(True)
            elif ra == 3:
                self.radio_3.setChecked(True)

            self.update_additional_radios(ra)

            # Восстанавливаем состояние дополнительных радиокнопок
            additional_ra = data.get('additional_ra', None)
            if additional_ra:
                for group in [self.additional_group_1, self.additional_group_2, self.additional_group_3]:
                    for button in group.buttons():
                        if button.text() == additional_ra:
                            button.setChecked(True)
                            break

            return True & res
        except Exception as e:
            dumpException(e)
        return res


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


@register_node(OP_NODE_TEST)
class CalcNode_Test(CalcNodeResultTest):
    icon = path_img_in
    op_code = OP_NODE_TEST
    op_title = "Точение"
    content_label = "Диаметр"
    content_label_1 = "Длина"
    content_label_2 = "Н/Ч"
    content_label_objname = "calc_node_TEST"

    def __init__(self, scene):
        super().__init__(scene, inputs=[2, 2], outputs=[1])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContentTest(self)
        self.grNode = CalcGraphicsNodeTest(self)

        # Подключаем сигнал изменения дополнительных радиокнопок к обработчику
        self.content.additional_group_1.buttonClicked.connect(self.on_input_changed)
        self.content.additional_group_2.buttonClicked.connect(self.on_input_changed)
        self.content.additional_group_3.buttonClicked.connect(self.on_input_changed)

        # Также основные радиокнопки уже подключены внутри CalcInputContentTest

    def on_input_changed(self):
        """
        Обработчик изменения выбора радиокнопок (основных и дополнительных).
        """
        # Обновляем метку отображения уже сделано в CalcInputContentTest
        # Поэтому здесь нужно просто вызвать перерасчёт
        self.eval()

    def evalImplementation(self):
        i1 = self.getInput(0)
        i2 = self.getInput(1)
        print(f"----+++++{self.content.ra}")
        print(self.content.label.text())

        if i1 is None or i2 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            if self.content.radio_1.isChecked():
                self.content.label.setText("")
                print(f"!")
            elif self.content.radio_2.isChecked():
                self.content.label.setText("")
                print(f"!!")
            elif self.content.radio_3.isChecked():
                self.content.label.setText("")
                print(f"!!!")

            # Получаем выбранную дополнительную опцию
            additional_value = self.content.get_selected_additional_option()
            print(f"Дополнительная опция: {additional_value}")

            # Продолжение вашей логики расчётов...
            # Например, использование additional_value в расчётах
            self.content.update_label()
            try:
                W = float(i1.eval())
                E = float(i2.eval())
            except ValueError:
                self.markInvalid()
                self.grNode.setToolTip("Invalid input values")
                return None


            # Ваши преобразования W и E
            if 0 < W <= 20:
                W = "20.3"
            elif 20 < W <= 50:
                W = "50.3"
            elif 50 < W <= 100:
                W = "100.3"
            elif 100 < W <= 150:
                W = "150.3"
            elif 150 < W <= 200:
                W = "200.3"
            elif 200 < W <= 250:
                W = "250.3"
            elif 250 < W <= 300:
                W = "300.3"
            elif 300 < W <= 400:
                W = "400.3"
            elif 400 < W <= 500:
                W = "500.3"
            elif 500 < W <= 750:
                W = "750.3"
            elif 750 < W <= 1000:
                W = "1000.3"
            elif 1000 < W <= 1250:
                W = "1250.3"
            elif 1250 < W <= 1500:
                W = "1500.3"
            elif 1500 < W <= 2000:
                W = "2000.3"

            print(f"---{W}")

            if 0 < E <= 10:
                E = 0
            elif 10 < E <= 20:
                E = 1
            elif 20 < E <= 50:
                E = 2
            elif 50 < E <= 100:
                E = 3
            elif 100 < E <= 200:
                E = 4
            elif 200 < E <= 300:
                E = 5
            elif 300 < E <= 400:
                E = 6
            elif 400 < E <= 500:
                E = 7
            elif 500 < E <= 600:
                E = 8
            elif 600 < E <= 700:
                E = 9
            elif 700 < E <= 800:
                E = 10
            elif 800 < E <= 1000:
                E = 11
            elif 1000 < E <= 1200:
                E = 12
            elif 1200 < E <= 1600:
                E = 13
            elif 1600 < E <= 2000:
                E = 14
            elif 2000 < E <= 2500:
                E = 15
            elif 2500 < E <= 3000:
                E = 16
            elif 3000 < E <= 4000:
                E = 17
            elif 4000 < E <= 5000:
                E = 18
            elif 5000 < E <= 6000:
                E = 19
            elif 7000 < E <= 8000:
                E = 20

            print(f"---{E}")

            table = create_tables_turning_other()
            s = table[0]
            a = s.get("k1")
            res_1 = a.get(str(W), "Р-")
            res = res_1[E]

            print(f"rrrrrrrrrr{res}")

            self.value = float(res)
            self.markDirty(False)
            self.markInvalid(False)

            self.markDescendantsInvalid(False)
            self.markDescendantsDirty()

            self.grNode.setToolTip("")

            self.evalChildren()

            return self.value


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

