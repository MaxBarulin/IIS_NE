from PyQt5.QtWidgets import QVBoxLayout, QLabel, QButtonGroup, QRadioButton, QSpacerItem, QSizePolicy, QHBoxLayout, \
    QWidget
from qtpy.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit
from qtpy.QtCore import Qt, QRect
from example_calculator.calc_conf import register_node, OP_NODE_INPUT, OP_NODE_INPUT_1, OP_NODE_INPUT_2, \
    OP_NODE_INPUT_TEXT, OP_NODE_INPUT_3, OP_NODE_INPUT_5, OP_NODE_TEST, OP_NODE_TURNING_2, OP_NODE_TURNING_3
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
        lbl.setGeometry(8, 12, 100, 14)

        lbl_1 = QLabel(self.node.content_label_1, self)
        lbl_1.setObjectName(self.node.content_label_objname)
        lbl_1.setGeometry(8, 34, 100, 14)

        lbl_2 = QLabel(self.node.content_label_2, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(100, 33, 50, 14)
        lbl_2.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        lbl_2 = QLabel(self.node.content_label_3, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(8, 56, 100, 14)

        # Метка для отображения текущего значения
        self.label = QLabel("12.5 + 3", self)
        self.label.setGeometry(44, -2, 150, 20)  # Увеличен размер для отображения текста

        self.value = 1
        self.ra = 1

        # Создаём основные радиокнопки
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
            radio_button.setGeometry(24, y_start + i * spacing, 50, 20)
            radio_button.clicked.connect(self.on_main_radio_changed)  # Подключаем сигнал

        # Создаём дополнительные радиокнопки заранее
        self.create_additional_radios()

        # При инициализации устанавливаем дополнительные радиокнопки
        self.update_additional_radios(1)


    def create_additional_radios(self):
        """Создаёт все дополнительные радиокнопки с фиксированным позиционированием."""
        # Дополнительные радиокнопки для опции 1 (4 радиокнопки)
        self.additional_radio_1_1 = QRadioButton("3", self)
        self.additional_radio_1_1.setGeometry(76, 18, 100, 20)
        self.additional_radio_1_1.setChecked(True)  # Выбираем по умолчанию
        self.additional_radio_1_1.clicked.connect(self.on_additional_radio_changed)

        self.additional_radio_1_2 = QRadioButton("5", self)
        self.additional_radio_1_2.setGeometry(76, 34, 100, 20)
        self.additional_radio_1_2.clicked.connect(self.on_additional_radio_changed)

        self.additional_radio_1_3 = QRadioButton("10", self)
        self.additional_radio_1_3.setGeometry(76, 50, 100, 20)
        self.additional_radio_1_3.clicked.connect(self.on_additional_radio_changed)

        self.additional_radio_1_4 = QRadioButton("15", self)
        self.additional_radio_1_4.setGeometry(76, 66, 100, 20)
        self.additional_radio_1_4.clicked.connect(self.on_additional_radio_changed)

        # Дополнительные радиокнопки для опций 2 и 3 (по 1 радиокнопке каждая)
        self.additional_radio_2 = QRadioButton("1", self)
        self.additional_radio_2.setGeometry(76, 18, 100, 20)
        self.additional_radio_2.setChecked(True)  # Выбираем по умолчанию
        self.additional_radio_2.clicked.connect(self.on_additional_radio_changed)

        self.additional_radio_3 = QRadioButton("0.5", self)
        self.additional_radio_3.setGeometry(76, 18, 100, 20)
        self.additional_radio_3.setChecked(True)  # Выбираем по умолчанию
        self.additional_radio_3.clicked.connect(self.on_additional_radio_changed)

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

    def update_additional_radios(self, selected_option, set_default_checked=True):
        """
        Обновляет видимость и выбор дополнительных радиокнопок в зависимости от выбранной основной опции.
        :param selected_option: Значение выбранной основной радиокнопки (1, 2 или 3)
        :param set_default_checked: Если True, устанавливает первую дополнительную радиокнопку как выбранную по умолчанию
        """
        if selected_option == 1:
            self.additional_radio_1_1.show()
            self.additional_radio_1_2.show()
            self.additional_radio_1_3.show()
            self.additional_radio_1_4.show()
            self.additional_radio_2.hide()
            self.additional_radio_3.hide()
            if set_default_checked:
                self.additional_radio_1_1.setChecked(True)
        elif selected_option == 2:
            self.additional_radio_2.show()
            self.additional_radio_1_1.hide()
            self.additional_radio_1_2.hide()
            self.additional_radio_1_3.hide()
            self.additional_radio_1_4.hide()
            self.additional_radio_3.hide()
            if set_default_checked:
                self.additional_radio_2.setChecked(True)
        elif selected_option == 3:
            self.additional_radio_3.show()
            self.additional_radio_1_1.hide()
            self.additional_radio_1_2.hide()
            self.additional_radio_1_3.hide()
            self.additional_radio_1_4.hide()
            self.additional_radio_2.hide()
            if set_default_checked:
                self.additional_radio_3.setChecked(True)

        # Обновляем метку после изменения выбора
        self.update_label()

    def update_label(self):
        """
        Обновляет текст метки на основе выбранной основной и дополнительной радиокнопки.
        """
        # Определяем выбранную основную радиокнопку
        if self.radio_1.isChecked():
            selected_main = "12.5"
        elif self.radio_2.isChecked():
            selected_main = "6.3"
        else:
            selected_main = "1.6"

        # Определяем выбранную дополнительную радиокнопку
        additional_selected = self.get_selected_additional_option() or ""

        # Обновляем текст метки
        self.label.setText(f"{selected_main} + {additional_selected}")

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
        self.update_label()
        self.node.markDirty(True) ### ВАЖНО ПРИ ИЗМЕНЕНИИ НОДЫ!!!
        # Вызовите eval у узла для перерасчёта
        self.node.eval()

    def on_additional_radio_changed(self):
        """
        Обработчик изменения дополнительной радиокнопки.
        """
        self.update_label()
        self.node.markDirty(True)  ### ВАЖНО ПРИ ИЗМЕНЕНИИ НОДЫ!!!
        # Вызовите eval у узла для перерасчёта
        self.node.eval()

    def get_selected_additional_option(self):
        """
        Возвращает текст выбранной дополнительной радиокнопки или None, если ничего не выбрано.
        """
        if self.radio_1.isChecked():
            for button in self.additional_group_1.buttons():
                if button.isChecked():
                    return button.text()
        elif self.radio_2.isChecked():
            if self.additional_radio_2.isChecked():
                return self.additional_radio_2.text()
        elif self.radio_3.isChecked():
            if self.additional_radio_3.isChecked():
                return self.additional_radio_3.text()
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

            # Блокируем сигналы основных радиокнопок
            self.radio_group.blockSignals(True)
            if ra == 1:
                self.radio_1.setChecked(True)
            elif ra == 2:
                self.radio_2.setChecked(True)
            elif ra == 3:
                self.radio_3.setChecked(True)
            self.radio_group.blockSignals(False)

            additional_ra = data.get('additional_ra', None)

            # Обновляем дополнительные радиокнопки без установки значения по умолчанию
            self.update_additional_radios(ra, set_default_checked=False)

            # Блокируем сигналы дополнительных радиокнопок
            if ra == 1:
                for button in self.additional_group_1.buttons():
                    if button.text() == additional_ra:
                        button.blockSignals(True)
                        button.setChecked(True)
                        button.blockSignals(False)
                        break
            elif ra == 2:
                self.additional_radio_2.blockSignals(True)
                if self.additional_radio_2.text() == additional_ra:
                    self.additional_radio_2.setChecked(True)
                self.additional_radio_2.blockSignals(False)
            elif ra == 3:
                self.additional_radio_3.blockSignals(True)
                if self.additional_radio_3.text() == additional_ra:
                    self.additional_radio_3.setChecked(True)
                self.additional_radio_3.blockSignals(False)

            # Обновляем метку
            self.update_label()
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcInputContentTurning2(QDMNodeContentWidget):
    def initUI(self):
        # Основные метки
        lbl = QLabel(self.node.content_label, self)
        lbl.setObjectName(self.node.content_label_objname)
        lbl.setGeometry(8, 12, 100, 14)

        lbl_1 = QLabel(self.node.content_label_1, self)
        lbl_1.setObjectName(self.node.content_label_objname)
        lbl_1.setGeometry(8, 34, 100, 14)

        lbl_2 = QLabel(self.node.content_label_2, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(100, 33, 50, 14)
        lbl_2.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        lbl_2 = QLabel(self.node.content_label_3, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(8, 56, 100, 14)

        # Метка для отображения текущего значения
        self.label = QLabel("12.5 + 3", self)
        self.label.setGeometry(44, -2, 150, 20)  # Увеличен размер для отображения текста

        self.value = 1
        self.ra = 1

        # Создаём основные радиокнопки
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
            radio_button.setGeometry(24, y_start + i * spacing, 50, 20)
            radio_button.clicked.connect(self.on_main_radio_changed)  # Подключаем сигнал

        # Создаём дополнительные радиокнопки заранее
        self.create_additional_radios()

        # При инициализации устанавливаем дополнительные радиокнопки
        self.update_additional_radios(1)


    def create_additional_radios(self):
        """Создаёт все дополнительные радиокнопки с фиксированным позиционированием."""
        # Дополнительные радиокнопки для опции 1 (4 радиокнопки)
        self.additional_radio_1_1 = QRadioButton("3", self)
        self.additional_radio_1_1.setGeometry(76, 18, 100, 20)
        self.additional_radio_1_1.setChecked(True)  # Выбираем по умолчанию
        self.additional_radio_1_1.clicked.connect(self.on_additional_radio_changed)

        self.additional_radio_1_2 = QRadioButton("5", self)
        self.additional_radio_1_2.setGeometry(76, 34, 100, 20)
        self.additional_radio_1_2.clicked.connect(self.on_additional_radio_changed)

        self.additional_radio_1_3 = QRadioButton("10", self)
        self.additional_radio_1_3.setGeometry(76, 50, 100, 20)
        self.additional_radio_1_3.clicked.connect(self.on_additional_radio_changed)

        # self.additional_radio_1_4 = QRadioButton("15", self)
        # self.additional_radio_1_4.setGeometry(76, 66, 100, 20)
        # self.additional_radio_1_4.clicked.connect(self.on_additional_radio_changed)

        # Дополнительные радиокнопки для опций 2 и 3 (по 1 радиокнопке каждая)
        self.additional_radio_2 = QRadioButton("0.5", self)
        self.additional_radio_2.setGeometry(76, 18, 100, 20)
        self.additional_radio_2.setChecked(True)  # Выбираем по умолчанию
        self.additional_radio_2.clicked.connect(self.on_additional_radio_changed)

        self.additional_radio_3 = QRadioButton("0.3", self)
        self.additional_radio_3.setGeometry(76, 18, 100, 20)
        self.additional_radio_3.setChecked(True)  # Выбираем по умолчанию
        self.additional_radio_3.clicked.connect(self.on_additional_radio_changed)

        # Создаём группы для дополнительных радиокнопок
        self.additional_group_1 = QButtonGroup(self)
        self.additional_group_1.addButton(self.additional_radio_1_1)
        self.additional_group_1.addButton(self.additional_radio_1_2)
        self.additional_group_1.addButton(self.additional_radio_1_3)
        # self.additional_group_1.addButton(self.additional_radio_1_4)

        self.additional_group_2 = QButtonGroup(self)
        self.additional_group_2.addButton(self.additional_radio_2)

        self.additional_group_3 = QButtonGroup(self)
        self.additional_group_3.addButton(self.additional_radio_3)

    def update_additional_radios(self, selected_option, set_default_checked=True):
        """
        Обновляет видимость и выбор дополнительных радиокнопок в зависимости от выбранной основной опции.
        :param selected_option: Значение выбранной основной радиокнопки (1, 2 или 3)
        :param set_default_checked: Если True, устанавливает первую дополнительную радиокнопку как выбранную по умолчанию
        """
        if selected_option == 1:
            self.additional_radio_1_1.show()
            self.additional_radio_1_2.show()
            self.additional_radio_1_3.show()
            # self.additional_radio_1_4.show()
            self.additional_radio_2.hide()
            self.additional_radio_3.hide()
            if set_default_checked:
                self.additional_radio_1_1.setChecked(True)
        elif selected_option == 2:
            self.additional_radio_2.show()
            self.additional_radio_1_1.hide()
            self.additional_radio_1_2.hide()
            self.additional_radio_1_3.hide()
            # self.additional_radio_1_4.hide()
            self.additional_radio_3.hide()
            if set_default_checked:
                self.additional_radio_2.setChecked(True)
        elif selected_option == 3:
            self.additional_radio_3.show()
            self.additional_radio_1_1.hide()
            self.additional_radio_1_2.hide()
            self.additional_radio_1_3.hide()
            # self.additional_radio_1_4.hide()
            self.additional_radio_2.hide()
            if set_default_checked:
                self.additional_radio_3.setChecked(True)

        # Обновляем метку после изменения выбора
        self.update_label()

    def update_label(self):
        """
        Обновляет текст метки на основе выбранной основной и дополнительной радиокнопки.
        """
        # Определяем выбранную основную радиокнопку
        if self.radio_1.isChecked():
            selected_main = "12.5"
        elif self.radio_2.isChecked():
            selected_main = "6.3"
        else:
            selected_main = "1.6"

        # Определяем выбранную дополнительную радиокнопку
        additional_selected = self.get_selected_additional_option() or ""

        # Обновляем текст метки
        self.label.setText(f"{selected_main} + {additional_selected}")

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
        self.update_label()
        self.node.markDirty(True) ### ВАЖНО ПРИ ИЗМЕНЕНИИ НОДЫ!!!
        # Вызовите eval у узла для перерасчёта
        self.node.eval()

    def on_additional_radio_changed(self):
        """
        Обработчик изменения дополнительной радиокнопки.
        """
        self.update_label()
        self.node.markDirty(True)  ### ВАЖНО ПРИ ИЗМЕНЕНИИ НОДЫ!!!
        # Вызовите eval у узла для перерасчёта
        self.node.eval()

    def get_selected_additional_option(self):
        """
        Возвращает текст выбранной дополнительной радиокнопки или None, если ничего не выбрано.
        """
        if self.radio_1.isChecked():
            for button in self.additional_group_1.buttons():
                if button.isChecked():
                    return button.text()
        elif self.radio_2.isChecked():
            if self.additional_radio_2.isChecked():
                return self.additional_radio_2.text()
        elif self.radio_3.isChecked():
            if self.additional_radio_3.isChecked():
                return self.additional_radio_3.text()
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

            # Блокируем сигналы основных радиокнопок
            self.radio_group.blockSignals(True)
            if ra == 1:
                self.radio_1.setChecked(True)
            elif ra == 2:
                self.radio_2.setChecked(True)
            elif ra == 3:
                self.radio_3.setChecked(True)
            self.radio_group.blockSignals(False)

            additional_ra = data.get('additional_ra', None)

            # Обновляем дополнительные радиокнопки без установки значения по умолчанию
            self.update_additional_radios(ra, set_default_checked=False)

            # Блокируем сигналы дополнительных радиокнопок
            if ra == 1:
                for button in self.additional_group_1.buttons():
                    if button.text() == additional_ra:
                        button.blockSignals(True)
                        button.setChecked(True)
                        button.blockSignals(False)
                        break
            elif ra == 2:
                self.additional_radio_2.blockSignals(True)
                if self.additional_radio_2.text() == additional_ra:
                    self.additional_radio_2.setChecked(True)
                self.additional_radio_2.blockSignals(False)
            elif ra == 3:
                self.additional_radio_3.blockSignals(True)
                if self.additional_radio_3.text() == additional_ra:
                    self.additional_radio_3.setChecked(True)
                self.additional_radio_3.blockSignals(False)

            # Обновляем метку
            self.update_label()
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CalcInputContentTurning3(QDMNodeContentWidget):
    value: None

    def initUI(self):
        lbl = QLabel(self.node.content_label, self)
        lbl.setObjectName(self.node.content_label_objname)
        lbl.setGeometry(8, 12, 100, 14)

        lbl_1 = QLabel(self.node.content_label_1, self)
        lbl_1.setObjectName(self.node.content_label_objname)
        lbl_1.setGeometry(8, 34, 100, 14)

        lbl_2 = QLabel(self.node.content_label_2, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(100, 33, 50, 14)
        lbl_2.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        lbl_2 = QLabel(self.node.content_label_3, self)
        lbl_2.setObjectName(self.node.content_label_objname)
        lbl_2.setGeometry(8, 56, 100, 14)

    def serialize(self):
        res = super().serialize()
        #res['value'] = self.value
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            #value = data['value']
            #self.value = value
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
    content_label = "D"
    content_label_1 = "d"
    content_label_2 = "Н/Ч"
    content_label_3 = "L"
    content_label_objname = "calc_node_TEST"

    def __init__(self, scene):
        super().__init__(scene, inputs=[2, 2, 2], outputs=[1])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContentTest(self)
        self.grNode = CalcGraphicsNodeTest(self)

        # Подключаем сигнал изменения дополнительных радиокнопок к обработчику
        # Обработчики подключены внутри CalcInputContentTest через методы on_main_radio_changed и on_additional_radio_changed
    # def eval(self):
    #     val = self.evalImplementation()
    #     return val


    def evalImplementation(self):
        # additional_value = self.content.get_selected_additional_option()
        # print(f"Дополнительная опция: {additional_value}")
        global a, int_WW, res, Li
        list_num = []
        i1 = self.getInput(0)
        i2 = self.getInput(1)
        i3 = self.getInput(2)

        if i1 is None or i2 is None or i3 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            # Получаем выбранную дополнительную опцию
            additional_value = self.content.get_selected_additional_option()
            print(f"Дополнительная опция: {additional_value}")

            # Обновляем метку (уже сделано через сигналы)
            # self.content.update_label()

            try:
                W = float(i1.eval())
                Wa = W
                E = float(i2.eval())
                L = float(i3.eval())
            except ValueError:
                self.markInvalid()
                self.grNode.setToolTip("Invalid input values")
                return None

            # Ваши преобразования W и E с учётом additional_value
            # Например, вы можете использовать дополнительное значение для модификации W или E
            # Здесь показан простой пример использования additional_value в качестве множителя для W
            try:
                # Преобразуем дополнительное значение в число
                additional_multiplier = additional_value
            except (ValueError, TypeError):
                additional_multiplier = 1  # Значение по умолчанию, если дополнительное значение некорректно

            delta_W_E = W - E
            print(delta_W_E)
            num_i = delta_W_E / float(additional_multiplier)
            if 0 < num_i < 1:
                num_i = 1
            print(f"num_i = {int(num_i)}")
            for i in range(int(num_i)):
                W + float(additional_multiplier)
                W -= float(additional_multiplier)
                if additional_multiplier == "0.5":
                    int_W = float(W)
                else:
                    int_W = int(W)

                if 0 < int_W <= 20:
                    int_WW = f"20|{additional_multiplier}"
                elif 20 < int_W <= 50:
                    int_WW = f"50|{additional_multiplier}"
                elif 50 < int_W <= 100:
                    int_WW = f"100|{additional_multiplier}"
                elif 100 < int_W <= 150:
                    int_WW = f"150|{additional_multiplier}"
                elif 150 < int_W <= 200:
                    int_WW = f"200|{additional_multiplier}"
                elif 200 < int_W <= 250:
                    int_WW = f"250|{additional_multiplier}"
                elif 250 < int_W <= 300:
                    int_WW = f"300|{additional_multiplier}"
                elif 300 < int_W <= 400:
                    int_WW = f"400|{additional_multiplier}"
                elif 400 < int_W <= 500:
                    int_WW = f"500|{additional_multiplier}"
                elif 500 < int_W <= 750:
                    int_WW = f"750|{additional_multiplier}"
                elif 750 < int_W <= 1000:
                    int_WW = f"1000|{additional_multiplier}"
                elif 1000 < int_W <= 1250:
                    int_WW = f"1250|{additional_multiplier}"
                elif 1250 < int_W <= 1500:
                    int_WW = f"1500|{additional_multiplier}"
                elif 1500 < int_W <= 2000:
                    int_WW = f"2000|{additional_multiplier}"

                if 0 < L <= 10:
                    Li = 0
                elif 10 < L <= 20:
                    Li = 1
                elif 20 < L <= 50:
                    Li = 2
                elif 50 < L <= 100:
                    Li = 3
                elif 100 < L <= 200:
                    Li = 4
                elif 200 < L <= 300:
                    Li = 5
                elif 300 < L <= 400:
                    Li = 6
                elif 400 < L <= 500:
                    Li = 7
                elif 500 < L <= 600:
                    Li = 8
                elif 600 < L <= 700:
                    Li = 9
                elif 700 < L <= 800:
                    Li = 10
                elif 800 < L <= 1000:
                    Li = 11
                elif 1000 < L <= 1200:
                    Li = 12
                elif 1200 < L <= 1600:
                    Li = 13
                elif 1600 < L <= 2000:
                    Li = 14
                elif 2000 < L <= 2500:
                    Li = 15
                elif 2500 < L <= 3000:
                    Li = 16
                elif 3000 < L <= 4000:
                    Li = 17
                elif 4000 < L <= 5000:
                    Li = 18
                elif 5000 < L <= 6000:
                    Li = 19
                elif 7000 < L <= 8000:
                    Li = 20

                table = create_tables_turning_other()
                s_tab = table[0]
                if additional_multiplier == "3" or additional_multiplier == "5" or additional_multiplier == "10" or additional_multiplier == "15":
                    a = s_tab.get("k1")
                elif additional_multiplier == "1":
                    a = s_tab.get("k2")
                elif additional_multiplier == "0.5":
                    a = s_tab.get("k3")

                res_1 = a.get(str(int_WW), "Р-")
                print(res_1)
                print(Li)
                res = res_1[Li]
                list_num.append(res)
                print(f"append{list_num}")


                print("=======")
                print(int_W)
                print(int_WW)
                print(L)
                print(Li)
                print(res)
                print("=======")

                if int_W < E:
                    break

            # Модифицируем W и E на основе additional_multiplier
            # W1 = f"{W}.{additional_multiplier}"
            # print(W1)
            #E = E + additional_multiplier  # Пример изменения E

            # print(f"--- W после преобразования: {W}")
            # print(f"--- E после преобразования: {E}")
            # print(f"--- L после преобразования: {L}")
            #
            # # Далее следует ваша логика расчётов, используя преобразованные W и E
            # # Например:
            #
            # if 0 < Wa <= 20:
            #     Wa = "20"
            # elif 20 < Wa <= 50:
            #     Wa = "50"
            # elif 50 < Wa <= 100:
            #     Wa = "100"
            # elif 100 < Wa <= 150:
            #     Wa = "150"
            # elif 150 < Wa <= 200:
            #     Wa = "200"
            # elif 200 < Wa <= 250:
            #     Wa = "250"
            # elif 250 < Wa <= 300:
            #     Wa = "300"
            # elif 300 < Wa <= 400:
            #     Wa = "400"
            # elif 400 < Wa <= 500:
            #     Wa = "500"
            # elif 500 < Wa <= 750:
            #     Wa = "750"
            # elif 750 < Wa <= 1000:
            #     Wa = "1000"
            # elif 1000 < Wa <= 1250:
            #     Wa = "1250"
            # elif 1250 < Wa <= 1500:
            #     Wa = "1500"
            # elif 1500 < Wa <= 2000:
            #     Wa = "2000"
            #
            # print(f"---{Wa}")
            #
            # if 0 < L <= 10:
            #     L = 0
            # elif 10 < L <= 20:
            #     L = 1
            # elif 20 <L <= 50:
            #     L = 2
            # elif 50 < L <= 100:
            #     L = 3
            # elif 100 < L <= 200:
            #     L = 4
            # elif 200 < L <= 300:
            #     L = 5
            # elif 300 < L <= 400:
            #     L = 6
            # elif 400 < L <= 500:
            #     L = 7
            # elif 500 < L <= 600:
            #     L = 8
            # elif 600 < L <= 700:
            #     L = 9
            # elif 700 < L <= 800:
            #     L = 10
            # elif 800 < L <= 1000:
            #     L = 11
            # elif 1000 < L <= 1200:
            #     L = 12
            # elif 1200 < L <= 1600:
            #     L = 13
            # elif 1600 < L <= 2000:
            #     L = 14
            # elif 2000 < L <= 2500:
            #     L = 15
            # elif 2500 < L <= 3000:
            #     L = 16
            # elif 3000 < L <= 4000:
            #     L = 17
            # elif 4000 < L <= 5000:
            #     L = 18
            # elif 5000 < L <= 6000:
            #     L = 19
            # elif 7000 < L <= 8000:
            #     L = 20
            #
            # print(f"---s-{L}")
            # W1 = f"{Wa}|{additional_multiplier}"
            # print(W1)
            # table = create_tables_turning_other()
            # s_tab = table[0]
            # if additional_multiplier == "3" or additional_multiplier == "5" or additional_multiplier == "10" or additional_multiplier == "15":
            #     a = s_tab.get("k1")
            # elif additional_multiplier == "1":
            #     a = s_tab.get("k2")
            # elif additional_multiplier == "0.5":
            #     a = s_tab.get("k3")
            #
            # res_1 = a.get(str(W1), "Р-")
            # try:
            #     res = res_1[L]
            # except:
            #     res = "p-"
            #
            # print(f"Результат: {res}")

            # Устанавливаем значение узла
            print(list_num)
            resul = sum(list_num)
            print(f"{resul}******")

            self.value = round(resul, 2)
            self.markDirty(False)
            self.markInvalid(False)

            self.markDescendantsInvalid(False)
            self.markDescendantsDirty()

            self.grNode.setToolTip("")

            self.evalChildren()

            return self.value


@register_node(OP_NODE_TURNING_2)
class CalcNode_Turning_2(CalcNodeResultTest):
    icon = path_img_in
    op_code = OP_NODE_TURNING_2
    op_title = "Растачивание"
    content_label = "d"
    content_label_1 = "D"
    content_label_2 = "Н/Ч"
    content_label_3 = "L"
    content_label_objname = "calc_node_TURNING_2"

    def __init__(self, scene):
        super().__init__(scene, inputs=[2, 2, 2], outputs=[1])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContentTurning2(self)
        self.grNode = CalcGraphicsNodeTest(self)

        # Подключаем сигнал изменения дополнительных радиокнопок к обработчику
        # Обработчики подключены внутри CalcInputContentTest через методы on_main_radio_changed и on_additional_radio_changed
    # def eval(self):
    #     val = self.evalImplementation()
    #     return val


    def evalImplementation(self):
        # additional_value = self.content.get_selected_additional_option()
        # print(f"Дополнительная опция: {additional_value}")
        global a, int_WW, res, Li
        list_num = []
        i1 = self.getInput(0)
        i2 = self.getInput(1)
        i3 = self.getInput(2)

        if i1 is None or i2 is None or i3 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            # Получаем выбранную дополнительную опцию
            additional_value = self.content.get_selected_additional_option()
            print(f"Дополнительная опция: {additional_value}")

            # Обновляем метку (уже сделано через сигналы)
            # self.content.update_label()

            try:
                W = float(i1.eval())
                Wa = W
                E = float(i2.eval())
                L = float(i3.eval())
            except ValueError:
                self.markInvalid()
                self.grNode.setToolTip("Invalid input values")
                return None

            # Ваши преобразования W и E с учётом additional_value
            # Например, вы можете использовать дополнительное значение для модификации W или E
            # Здесь показан простой пример использования additional_value в качестве множителя для W
            try:
                # Преобразуем дополнительное значение в число
                additional_multiplier = additional_value
            except (ValueError, TypeError):
                additional_multiplier = 1  # Значение по умолчанию, если дополнительное значение некорректно

            delta_W_E = E - W
            print(delta_W_E)
            num_i = delta_W_E / float(additional_multiplier)
            if 0 < num_i < 1:
                num_i = 1
            print(f"num_i = {int(num_i)}")
            for i in range(int(num_i)):
                E + float(additional_multiplier)
                E -= float(additional_multiplier)
                if additional_multiplier == "0.5" or additional_multiplier == "0.3":
                    int_W = float(E)
                else:
                    int_W = int(E)

                if 0 < int_W <= 50:
                    int_WW = f"50|{additional_multiplier}"
                elif 50 < int_W <= 80:
                    int_WW = f"80|{additional_multiplier}"
                elif 80 < int_W <= 100:
                    int_WW = f"100|{additional_multiplier}"
                elif 100 < int_W <= 150:
                    int_WW = f"150|{additional_multiplier}"
                elif 150 < int_W <= 200:
                    int_WW = f"200|{additional_multiplier}"
                elif 200 < int_W <= 250:
                    int_WW = f"250|{additional_multiplier}"
                elif 250 < int_W <= 300:
                    int_WW = f"300|{additional_multiplier}"
                elif 300 < int_W <= 400:
                    int_WW = f"400|{additional_multiplier}"
                elif 400 < int_W <= 500:
                    int_WW = f"500|{additional_multiplier}"
                elif 500 < int_W <= 750:
                    int_WW = f"750|{additional_multiplier}"
                elif 750 < int_W <= 1000:
                    int_WW = f"1000|{additional_multiplier}"
                elif 1000 < int_W <= 1250:
                    int_WW = f"1250|{additional_multiplier}"
                elif 1250 < int_W <= 1500:
                    int_WW = f"1500|{additional_multiplier}"
                elif 1500 < int_W <= 2000:
                    int_WW = f"2000|{additional_multiplier}"

                if 0 < L <= 10:
                    Li = 0
                elif 10 < L <= 20:
                    Li = 1
                elif 20 < L <= 50:
                    Li = 2
                elif 50 < L <= 80:
                    Li = 3
                elif 80 < L <= 100:
                    Li = 4
                elif 100 < L <= 150:
                    Li = 5
                elif 150 < L <= 200:
                    Li = 6
                elif 200 < L <= 250:
                    Li = 7
                elif 250 < L <= 300:
                    Li = 8
                elif 300 < L <= 400:
                    Li = 9
                elif 400 < L <= 500:
                    Li = 10
                elif 500 < L <= 600:
                    Li = 11
                elif 600 < L <= 700:
                    Li = 12
                elif 700 < L <= 800:
                    Li = 13
                elif 800 < L <= 1000:
                    Li = 14
                elif 1000 < L <= 1200:
                    Li = 15
                elif 1200 < L <= 1500:
                    Li = 16
                elif 1500 < L <= 2000:
                    Li = 17
                elif 2000 < L <= 2500:
                    Li = 18
                elif 2500 < L <= 3000:
                    Li = 19
                elif 3000 < L <= 3500:
                    Li = 20
                elif 3500 < L <= 4000:
                    Li = 21

                table = create_tables_turning_other()
                s_tab = table[0]
                if additional_multiplier == "3" or additional_multiplier == "5" or additional_multiplier == "10":
                    a = s_tab.get("k4")
                elif additional_multiplier == "0.5":
                    a = s_tab.get("k5")
                elif additional_multiplier == "0.3":
                    a = s_tab.get("k6")

                res_1 = a.get(str(int_WW), "Р-")
                print(res_1)
                print(Li)
                res = res_1[Li]
                list_num.append(res)
                print(f"append{list_num}")


                print("=======")
                print(int_W)
                print(int_WW)
                print(L)
                print(Li)
                print(res)
                print("=======")

                if int_W < E:
                    break

            # Модифицируем W и E на основе additional_multiplier
            # W1 = f"{W}.{additional_multiplier}"
            # print(W1)
            #E = E + additional_multiplier  # Пример изменения E

            # print(f"--- W после преобразования: {W}")
            # print(f"--- E после преобразования: {E}")
            # print(f"--- L после преобразования: {L}")
            #
            # # Далее следует ваша логика расчётов, используя преобразованные W и E
            # # Например:
            #
            # if 0 < Wa <= 20:
            #     Wa = "20"
            # elif 20 < Wa <= 50:
            #     Wa = "50"
            # elif 50 < Wa <= 100:
            #     Wa = "100"
            # elif 100 < Wa <= 150:
            #     Wa = "150"
            # elif 150 < Wa <= 200:
            #     Wa = "200"
            # elif 200 < Wa <= 250:
            #     Wa = "250"
            # elif 250 < Wa <= 300:
            #     Wa = "300"
            # elif 300 < Wa <= 400:
            #     Wa = "400"
            # elif 400 < Wa <= 500:
            #     Wa = "500"
            # elif 500 < Wa <= 750:
            #     Wa = "750"
            # elif 750 < Wa <= 1000:
            #     Wa = "1000"
            # elif 1000 < Wa <= 1250:
            #     Wa = "1250"
            # elif 1250 < Wa <= 1500:
            #     Wa = "1500"
            # elif 1500 < Wa <= 2000:
            #     Wa = "2000"
            #
            # print(f"---{Wa}")
            #
            # if 0 < L <= 10:
            #     L = 0
            # elif 10 < L <= 20:
            #     L = 1
            # elif 20 <L <= 50:
            #     L = 2
            # elif 50 < L <= 100:
            #     L = 3
            # elif 100 < L <= 200:
            #     L = 4
            # elif 200 < L <= 300:
            #     L = 5
            # elif 300 < L <= 400:
            #     L = 6
            # elif 400 < L <= 500:
            #     L = 7
            # elif 500 < L <= 600:
            #     L = 8
            # elif 600 < L <= 700:
            #     L = 9
            # elif 700 < L <= 800:
            #     L = 10
            # elif 800 < L <= 1000:
            #     L = 11
            # elif 1000 < L <= 1200:
            #     L = 12
            # elif 1200 < L <= 1600:
            #     L = 13
            # elif 1600 < L <= 2000:
            #     L = 14
            # elif 2000 < L <= 2500:
            #     L = 15
            # elif 2500 < L <= 3000:
            #     L = 16
            # elif 3000 < L <= 4000:
            #     L = 17
            # elif 4000 < L <= 5000:
            #     L = 18
            # elif 5000 < L <= 6000:
            #     L = 19
            # elif 7000 < L <= 8000:
            #     L = 20
            #
            # print(f"---s-{L}")
            # W1 = f"{Wa}|{additional_multiplier}"
            # print(W1)
            # table = create_tables_turning_other()
            # s_tab = table[0]
            # if additional_multiplier == "3" or additional_multiplier == "5" or additional_multiplier == "10" or additional_multiplier == "15":
            #     a = s_tab.get("k1")
            # elif additional_multiplier == "1":
            #     a = s_tab.get("k2")
            # elif additional_multiplier == "0.5":
            #     a = s_tab.get("k3")
            #
            # res_1 = a.get(str(W1), "Р-")
            # try:
            #     res = res_1[L]
            # except:
            #     res = "p-"
            #
            # print(f"Результат: {res}")

            # Устанавливаем значение узла
            print(list_num)
            resul = sum(list_num)
            print(f"{resul}******")

            self.value = round(resul, 2)
            self.markDirty(False)
            self.markInvalid(False)

            self.markDescendantsInvalid(False)
            self.markDescendantsDirty()

            self.grNode.setToolTip("")

            self.evalChildren()

            return self.value


@register_node(OP_NODE_TURNING_3)
class CalcNode_Turning_3(CalcNodeResult):
    icon = path_img_in
    op_code = OP_NODE_TURNING_3
    op_title = "Отрезание/канавки"
    content_label = "D"
    content_label_1 = "t"
    content_label_2 = "Н/Ч"
    content_label_3 = "L"
    content_label_objname = "calc_node_TURNING_3"

    def __init__(self, scene):
        super().__init__(scene, inputs=[2,2,2], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContentTurning3(self)
        self.grNode = CalcGraphicsNodeTest(self)
        #self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        # additional_value = self.content.get_selected_additional_option()
        # print(f"Дополнительная опция: {additional_value}")
        global t, Wu, Li
        list_num = []
        i1 = self.getInput(0)
        i2 = self.getInput(1)
        i3 = self.getInput(2)

        if i1 is None or i2 is None or i3 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            try:
                W = float(i1.eval())
                E = float(i2.eval())
                L = float(i3.eval())
            except ValueError:
                self.markInvalid()
                self.grNode.setToolTip("Invalid input values")
                return None

            print("******")
            print(f"вход знач{W}")
            print("******")

            if 0 < W <= 20:
                W = f"20"
                t = 2
            elif 20 < W <= 50:
                W = f"50"
                t = 5
            elif 50 < W <= 80:
                W = f"80"
                t = 5
            elif 80 < W <= 100:
                W = f"100"
                t = 5
            elif 100 < W <= 150:
                W = f"150"
                t = 5
            elif 150 < W <= 200:
                W = f"200"
                t = 5
            elif 200 < W <= 250:
                W = f"250"
                t = 5
            elif 250 < W <= 300:
                W = f"300"
                t = 5
            elif 300 < W <= 400:
                W = f"400"
                t = 5
            elif 400 < W <= 500:
                W = f"500"
                t = 5
            elif 500 < W <= 750:
                W = f"750"
                t = 7
            elif 750 < W <= 1000:
                W = f"1000"
                t = 7
            elif 1000 < W <= 1250:
                W = f"1250"
                t = 7
            elif 1250 < W <= 1500:
                W = f"1500"
                t = 7
            elif 1500 < W <= 2000:
                W = f"2000"
                t = 7

            print("******")
            print(f"запрос в таблицу{W}")
            print("******")

            Lii = L / t

            if 0 < E <= 2:
                E = 0
            elif 2 < E <= 3:
                E = 1
            elif 3 < E <= 5:
                E = 2
            elif 5 < E <= 10:
                E = 3
            elif 10 < E <= 15:
                E = 4
            elif 15 < E <= 20:
                E = 5
            elif 20 < E <= 25:
                E = 6
            elif 25 < E <= 30:
                E = 7
            elif 30 < E <= 40:
                E = 8
            elif 40 < E <= 50:
                E = 9
            elif 50 < E <= 60:
                E = 10
            elif 60 < E <= 70:
                E = 11
            elif 70 < E <= 80:
                E = 12
            elif 80 < E <= 90:
                E = 13
            elif 90 < E <= 100:
                E = 14
            elif 100 < E <= 120:
                E = 15
            elif 120 < E <= 150:
                E = 16
            elif 150 < E <= 200:
                E = 17
            elif 200 < E <= 250:
                E = 18
            elif 250 < E <= 300:
                E = 19
            elif 300 < E <= 350:
                E = 20
            elif 350 < E <= 400:
                E = 21

            print(f"W = {W}, E = {E}")

            table = create_tables_turning_other()
            s_tab = table[0]
            a = s_tab.get("k7")
            res_1 = a.get(str(W), "Р-")
            res = res_1[E]
            full_res = int(int(res*Lii) + 1)
            print(res)

            print(f"{full_res}")

            self.value = full_res
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
                try:
                    self.value = float(res[val32])
                except:
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

