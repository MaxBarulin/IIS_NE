from example_calculator.calc_conf import (
    register_node,
    OP_NODE_ADD,
    OP_NODE_SUB,
    OP_NODE_MUL,
    OP_NODE_DIV,
    OP_NODE_TABLE_6,
    OP_NODE_TABLE_1,
    OP_NODE_TABLE_3,
    OP_NODE_TABLE_4,
    OP_NODE_TABLE_7,
    OP_NODE_TABLE_2,
    OP_NODE_TABLE_5,
    OP_NODE_TABLE_8,
    OP_NODE_TABLE_9,
    OP_NODE_GROUP,
    OP_NODE_GROUP1,
    OP_NODE_TABLE_T1,
    OP_NODE_FORMULA,
    OP_NODE_PEREMEN,
    OP_NODE_TURN1
)
from example_calculator.calc_node_base import CalcNode, CalcTable, CalcNode_lbl, CalcNodeMulti, CalcNodeMulti1, CalcNodeFormula, CalcNodePerem, CalcNodeTURN1
from example_calculator.table import create_tables, create_tables_turning
import os

open_img_add = "add.ico"
open_img_sub = "sub.ico"
open_img_mul = "mul.ico"
open_img_div = "div.ico"
open_img_tab = "table.ico"
open_img_com = "com.ico"

put = os.path.dirname(__file__)

path_img_add = f"{put}\\icons\\{open_img_add}"
path_img_sub = f"{put}\\icons\\{open_img_sub}"
path_img_mul = f"{put}\\icons\\{open_img_mul}"
path_img_div = f"{put}\\icons\\{open_img_div}"
path_img_tab = f"{put}\\icons\\{open_img_tab}"
path_img_com = f"{put}\\icons\\{open_img_com}"


@register_node(OP_NODE_TURN1)
class CalcNode_Group3(CalcNodeTURN1):
    icon = path_img_mul
    op_code = OP_NODE_TURN1
    op_title = "ДЛЯ ТЕСТА"
    content_label = "нач Д"
    content_label_1 = "кон Д"
    content_label_2 = "asd"
    content_label_objname = "calc_node_TURN1"

    def __init__(self, scene):
        super().__init__(scene)
        self.eval()

    def evalOperation(self, input1, input2):
        return input1 + input2

@register_node(OP_NODE_PEREMEN)
class CalcNode_Group2(CalcNodePerem):
    icon = path_img_mul
    op_code = OP_NODE_PEREMEN
    op_title = "Переменные"
    content_label = "буква=число"
    content_label_objname = "calc_node_perem"

    def __init__(self, scene):
        super().__init__(scene)
        self.eval()

    def evalOperation(self, inputs):
        print(f"+++{inputs}")
        # Логика для выполнения группировки
        return str(inputs)


@register_node(OP_NODE_GROUP1)
class CalcNode_Group1(CalcNodeMulti1):
    icon = path_img_mul
    op_code = OP_NODE_GROUP1
    op_title = "Умножение+"
    content_label = "число"
    content_label_objname = "calc_node_group"

    def __init__(self, scene):
        super().__init__(scene)
        self.eval()

    def evalOperation(self, inputs):
        # Логика для выполнения группировки
        return str(inputs)


@register_node(OP_NODE_GROUP)
class CalcNode_Group(CalcNodeMulti):
    icon = path_img_add
    op_code = OP_NODE_GROUP
    op_title = "Сложение+"
    content_label = "число"
    content_label_objname = "calc_node_group"

    def __init__(self, scene):
        super().__init__(scene)
        self.eval()

    def evalOperation(self, inputs):
        # Логика для выполнения группировки
        return str(inputs)


@register_node(OP_NODE_FORMULA)
class CalcNode_Formula(CalcNodeFormula):
    icon = path_img_add
    op_code = OP_NODE_FORMULA
    op_title = "Формула"
    content_label = "переменные"
    content_label_objname = "calc_node_formula"

    def __init__(self, scene):
        super().__init__(scene)
        self.eval()

    def evalOperation(self, input):
        no_spase = str(input).replace(" ", "")
        string_to_list = str(no_spase).split(",")
        print(string_to_list)

        def fun(args, string):
            print(f"===={args}")
            for i in args:
                re = i.split("=")
                print(re[0], "111111", re[1])

                s = string.replace(f"{re[0]}", f"{re[1]}")
                string = s
            return(string)

        label_text = self.content.edit.text()
        #print(label_text)
        dee = eval(fun(string_to_list, label_text))

        #label_text = self.content.edit.text()
        #print(label_text)
        # Логика для выполнения группировки

        return str(dee)


@register_node(OP_NODE_ADD)
class CalcNode_Add(CalcNode):
    icon = path_img_add
    op_code = OP_NODE_ADD
    op_title = "Сложение"
    content_label = "+"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):

        return float(input1) + float(input2)


@register_node(OP_NODE_SUB)
class CalcNode_Sub(CalcNode):
    icon = path_img_sub
    op_code = OP_NODE_SUB
    op_title = "Вычитание"
    content_label = "-"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return input1 - input2


@register_node(OP_NODE_MUL)
class CalcNode_Mul(CalcNode):
    icon = path_img_mul
    op_code = OP_NODE_MUL
    op_title = "Умножение"
    content_label = "*"
    content_label_objname = "calc_node_mul"

    def evalOperation(self, input1, input2):
        input1 = float(input1)
        input2 = float(input2)
        return input1 * input2


@register_node(OP_NODE_DIV)
class CalcNode_Div(CalcNode):
    icon = path_img_div
    op_code = OP_NODE_DIV
    op_title = "Деление"
    content_label = "/"
    content_label_objname = "calc_node_div"

    def evalOperation(self, input1, input2):
        return float(input1) / float(input2)


@register_node(OP_NODE_TABLE_6)
class CalcNode_table_4(CalcTable):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_6
    op_title = "К4 Св сквозных отв+"
    content_label = "кол-во отв. в дет."
    content_label_1 = "диаметр"
    content_label_2 = "глубина"
    content_label_3 = "Н/Ч"
    content_label_objname = "calc_node_bg_1"

    def evalOperation(self, input1, input2, input3):
        table = create_tables()[14]
        print(table)
        value1 = int(input1)
        if 1 <= value1 <= 2:
            value1 = 0
        elif 3 <= value1 <= 3:
            value1 = 1
        elif 4 <= value1 <= 4:
            value1 = 2
        elif 5 <= value1 <= 6:
            value1 = 3
        elif 7 <= value1 <= 8:
            value1 = 4
        elif 9 <= value1 <= 12:
            value1 = 5
        elif 13 <= value1 <= 16:
            value1 = 6
        elif 17 <= value1 <= 20:
            value1 = 7
        elif 21 <= value1 <= 24:
            value1 = 8
        elif 25 <= value1 <= 28:
            value1 = 9
        elif 29 <= value1 <= 32:
            value1 = 10

        value2 = int(input2)
        print(value2)
        if 5 <= value2 < 11:
            value2 = "5-10,9"
        elif 11 <= value2 < 18:
            value2 = "11-17,9"
        elif 18 <= value2 < 22:
            value2 = "18-21,9"
        elif 22 <= value2 < 27:
            value2 = "22-26,9"
        elif 27 <= value2 < 31:
            value2 = "27-30,8"
        elif 31 <= value2 < 45:
            value2 = "31-44,8"

        value3 = int(input3)
        print(value3)
        if 1 <= value3 <= 10:
            value3 = "10"
        elif 10 < value3 <= 15:
            value3 = "15"
        elif 15 < value3 <= 20:
            value3 = "20"
        elif 20 < value3 <= 30:
            value3 = "30"
        elif 30 < value3 <= 40:
            value3 = "40"
        elif 40 < value3 <= 50:
            value3 = "50"

        result_3 = table.get(value2, "Р-")
        print(result_3)
        if result_3 == "Р-":
            res = result_3
        else:
            # print(f'---{value1}')
            result_2 = result_3.get(value3, "Р-")
            if result_2 == "Р-":
                res = result_2
            else:
                # print(result_2)
                result_1 = result_2[value1]
                # print(result_1)

                # result = self.tables[14].get((value2, value3, value1), "Результат не найден")
                res = result_1
                # with open("results.txt", "a") as file:
                #    file.write(f"Карта 4: {res}\n")

        return res


@register_node(OP_NODE_TABLE_7)
class CalcNode_table_4(CalcTable):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_7
    op_title = "К5 Нарез в сквоз"
    content_label = "кол-во отв. в дет."
    content_label_1 = "диаметр"
    content_label_2 = "глубина"
    content_label_3 = "Н/Ч"
    content_label_objname = "calc_node_bg_2"

    def evalOperation(self, input1, input2, input3):
        table = create_tables()[15]
        value1 = int(input1)
        if value1 == 1:
            value1 = 0
        elif value1 == 2:
            value1 = 1
        elif 3 <= value1 <= 4:
            value1 = 2
        elif 5 <= value1 <= 6:
            value1 = 3
        elif 7 <= value1 <= 8:
            value1 = 4
        elif 9 <= value1 <= 12:
            value1 = 5
        elif 13 <= value1 <= 16:
            value1 = 6
        elif 17 <= value1 <= 20:
            value1 = 7
        elif 21 <= value1 <= 24:
            value1 = 8
        elif 25 <= value1 <= 28:
            value1 = 9
        elif 29 <= value1 <= 32:
            value1 = 10

        value2 = int(input2)
        print(value2)
        if 6 <= value2 < 11:
            value2 = "6-10"
        elif 11 <= value2 < 18:
            value2 = "12-16"
        elif 18 <= value2 < 22:
            value2 = "18-22"
        elif 22 <= value2 < 27:
            value2 = "24-27"
        elif 27 <= value2 < 31:
            value2 = "30-33"
        elif 31 <= value2 < 45:
            value2 = "36-45"

        value3 = int(input3)
        print(value3)
        if 1 <= value3 <= 10:
            value3 = "10"
        elif 10 < value3 <= 15:
            value3 = "15"
        elif 15 < value3 <= 20:
            value3 = "20"
        elif 20 < value3 <= 25:
            value3 = "25"
        elif 25 < value3 <= 30:
            value3 = "30"
        elif 30 < value3 <= 40:
            value3 = "40"
        elif 40 < value3 <= 50:
            value3 = "50"

        result_3 = table.get(value2, "Р-")
        print(result_3)
        if result_3 == "Р-":
            res = result_3
        else:
            # print(f'---{value1}')
            result_2 = result_3.get(value3, "Р-")
            if result_2 == "Р-":
                res = result_2
            else:
                # print(result_2)
                result_1 = result_2[value1]
                # print(result_1)

                # result = self.tables[14].get((value2, value3, value1), "Результат не найден")
                res = result_1
                # with open("results.txt", "a") as file:
                #    file.write(f"Карта 4: {res}\n")

        return res


@register_node(OP_NODE_TABLE_4)
class CalcContent(CalcNode_lbl):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_4
    op_title = "К3 Св сквозных отв"
    content_label = "диаметр"
    content_label_1 = "глубина"
    content_label_2 = "Н/Ч"

    content_label_objname = "calc_node_bg_3"

    def evalOperation(self, input1, input2):
        table = create_tables()[3]
        print(table)
        value1 = float(input1)
        if 0 < value1 <= 10:
            value1 = 1
        if 10 < value1 <= 17:
            value1 = 2
        if 17 < value1 <= 21:
            value1 = 3
        if 21 < value1 <= 26:
            value1 = 4
        if 26 < value1 <= 30:
            value1 = 5
        if 30 < value1 <= 44:
            value1 = 6
        if 44 < value1 <= 54:
            value1 = 7
        if 54 < value1 <= 62:
            value1 = 8
        if 62 < value1:
            value1 = 8

        value2 = float(input2)
        if 0 < value2 <= 10:
            value2 = 10
        if 10 < value2 <= 15:
            value2 = 15
        if 15 < value2 <= 20:
            value2 = 20
        if 20 < value2 <= 30:
            value2 = 30
        if 30 < value2 <= 40:
            value2 = 40
        if 40 < value2 <= 50:
            value2 = 50
        if 50 < value2 <= 60:
            value2 = 60
        if 60 < value2 <= 80:
            value2 = 80
        if 80 < value2 <= 100:
            value2 = 100
        if 100 < value2 <= 125:
            value2 = 125
        if 125 < value2 <= 150:
            value2 = 150

        res = table.get((value1, value2), "Значение за пределами таблицы")

        return res


@register_node(OP_NODE_TABLE_1)
class CalcNode_table_1(CalcNode_lbl):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_1
    op_title = "К1 Коэф партии"
    content_label = "Кол-во шт."
    content_label_1 = "Н/Ч"
    content_label_2 = "Коэф."
    content_label_objname = "calc_node_bg_4"

    def evalOperation(self, input1, input2):
        table = create_tables()[0]

        if 0 < input1 <= 2:
            input1 = 1
        elif 2 < input1 <= 5:
            input1 = 2
        elif 5 < input1 <= 10:
            input1 = 3
        elif 10 < input1 <= 20:
            input1 = 4
        elif 20 < input1 <= 40:
            input1 = 5
        elif 40 < input1 <= 60:
            input1 = 6
        elif 60 < input1:
            input1 = 7

        if 0 < input2 <= 0.25:
            input2 = 1
            # print('1')
        elif 0.25 < input2 <= 0.5:
            input2 = 2
            # print('2')
        elif 0.5 < input2 <= 1:
            input2 = 3
        elif 1 < input2 <= 2:
            input2 = 4
        elif 2 < input2:
            input2 = 5

        result = table.get((input1, input2), "Р-")
        print(result)

        return result


@register_node(OP_NODE_TABLE_T1)
class CalcNode_table_1(CalcNode_lbl):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_T1
    op_title = "T2 Коэф партии"
    content_label = "Кол-во шт."
    content_label_1 = "Н/Ч"
    content_label_2 = "Коэф."
    content_label_objname = "calc_node_bg_4"

    def evalOperation(self, input1, input2):
        table = create_tables_turning()[0]

        if 0 < input1 <= 2:
            input1 = 1
        elif 2 < input1 <= 5:
            input1 = 2
        elif 5 < input1 <= 10:
            input1 = 3
        elif 10 < input1 <= 20:
            input1 = 4
        elif 20 < input1 <= 40:
            input1 = 5
        elif 40 < input1 <= 60:
            input1 = 6
        elif 60 < input1:
            input1 = 7

        if 0 < input2 <= 0.25:
            input2 = 1
            # print('1')
        elif 0.25 < input2 <= 0.5:
            input2 = 2
            # print('2')
        elif 0.5 < input2 <= 1:
            input2 = 3
        elif 1 < input2 <= 2:
            input2 = 4
        elif 2 < input2:
            input2 = 5

        result = table.get((input1, input2), "Р-")
        print(result)

        return result



@register_node(OP_NODE_TABLE_3)
class CalcNode_table_4(CalcTable):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_3
    op_title = "К6 Св и нарез в сквоз"
    content_label = "кол-во отв. в дет."
    content_label_1 = "диаметр"
    content_label_2 = "глубина"
    content_label_3 = "Н/Ч"
    content_label_objname = "calc_node_bg_5"

    def evalOperation(self, input1, input2, input3):
        table = create_tables()[16]
        print(table)
        value1 = int(input1)
        if value1 == 1:
            value1 = 0
        elif value1 == 2:
            value1 = 1
        elif value1 == 3:
            value1 = 2
        elif value1 == 4:
            value1 = 3
        elif 5 <= value1 <= 6:
            value1 = 4
        elif 7 <= value1 <= 8:
            value1 = 5
        elif 9 <= value1 <= 12:
            value1 = 6
        elif 13 <= value1 <= 16:
            value1 = 7
        elif 17 <= value1 <= 20:
            value1 = 8
        elif 21 <= value1 <= 24:
            value1 = 9
        elif 25 <= value1 <= 28:
            value1 = 10
        elif 29 <= value1 <= 32:
            value1 = 11

        value2 = int(input2)
        print(value2)
        if 6 <= value2 < 11:
            value2 = "6м-10м"
        elif 11 <= value2 < 18:
            value2 = "12м-16м"
        elif 18 <= value2 < 22:
            value2 = "18м-22м"
        elif 22 <= value2 < 27:
            value2 = "24м-27м"
        elif 27 <= value2 < 31:
            value2 = "30м-33м"
        elif 31 <= value2 < 45:
            value2 = "36м-45м"

        value3 = int(input3)
        print(value3)
        if 1 <= value3 <= 10:
            value3 = "10"
        elif 10 < value3 <= 15:
            value3 = "15"
        elif 15 < value3 <= 20:
            value3 = "20"
        elif 20 < value3 <= 25:
            value3 = "25"
        elif 25 < value3 <= 30:
            value3 = "30"
        elif 30 < value3 <= 40:
            value3 = "40"
        elif 40 < value3 <= 50:
            value3 = "50"

        result_3 = table.get(value2, "Р-")
        print(result_3)
        if result_3 == "Р-":
            res = result_3
        else:
            # print(f'---{value1}')
            result_2 = result_3.get(value3, "Р-")
            if result_2 == "Р-":
                res = result_2
            else:
                # print(result_2)
                result_1 = result_2[value1]
                # print(result_1)

                # result = self.tables[14].get((value2, value3, value1), "Результат не найден")
                res = result_1
                # with open("results.txt", "a") as file:
                #    file.write(f"Карта 4: {res}\n")

        return res


@register_node(OP_NODE_TABLE_2)
class CalcContent(CalcNode_lbl):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_2
    op_title = "К7 Св глух"
    content_label = "диаметр"
    content_label_1 = "глубина"
    content_label_2 = "Н/Ч"

    content_label_objname = "calc_node_bg_6"

    def evalOperation(self, input1, input2):
        table = create_tables()[17]
        print(table)
        value1 = float(input1)
        if 5 <= value1 <= 10.9:
            value1 = 1
        if 10.9 < value1 <= 17.9:
            value1 = 2
        if 17.9 < value1 <= 21.9:
            value1 = 3
        if 21.9 < value1 <= 26.9:
            value1 = 4
        if 26.9 < value1 <= 30.8:
            value1 = 5
        if 30.8 < value1 <= 44.8:
            value1 = 6
        if 44.8 < value1 <= 54:
            value1 = 7
        if 54 < value1 <= 62:
            value1 = 8
        if 62 < value1:
            value1 = 8

        value2 = float(input2)
        if 0 < value2 <= 10:
            value2 = 10
        if 10 < value2 <= 15:
            value2 = 15
        if 15 < value2 <= 20:
            value2 = 20
        if 20 < value2 <= 30:
            value2 = 30
        if 30 < value2 <= 40:
            value2 = 40
        if 40 < value2 <= 50:
            value2 = 50
        if 50 < value2 <= 60:
            value2 = 60
        if 60 < value2 <= 80:
            value2 = 80
        if 80 < value2 <= 100:
            value2 = 100
        if 100 < value2 <= 125:
            value2 = 125
        if 125 < value2 <= 150:
            value2 = 150

        res = table.get((value1, value2), "Значение за пределами таблицы")

        return res


@register_node(OP_NODE_TABLE_5)
class CalcNode_table_4(CalcTable):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_5
    op_title = "К8 Св глух+"
    content_label = "кол-во отв. в дет."
    content_label_1 = "диаметр"
    content_label_2 = "глубина"
    content_label_3 = "Н/Ч"
    content_label_objname = "calc_node_bg_7"

    def evalOperation(self, input1, input2, input3):
        table = create_tables()[18]
        print(table)
        value1 = int(input1)
        if 1 <= value1 <= 2:
            value1 = 0
        elif 3 <= value1 <= 3:
            value1 = 1
        elif 4 <= value1 <= 4:
            value1 = 2
        elif 5 <= value1 <= 6:
            value1 = 3
        elif 7 <= value1 <= 8:
            value1 = 4
        elif 9 <= value1 <= 12:
            value1 = 5
        elif 13 <= value1 <= 16:
            value1 = 6
        elif 17 <= value1 <= 20:
            value1 = 7
        elif 21 <= value1 <= 24:
            value1 = 8
        elif 25 <= value1 <= 28:
            value1 = 9
        elif 29 <= value1 <= 32:
            value1 = 10

        value2 = int(input2)
        print(value2)
        if 5 <= value2 < 11:
            value2 = "5-10,9"
        elif 11 <= value2 < 18:
            value2 = "11-17,9"
        elif 18 <= value2 < 22:
            value2 = "18-21,9"
        elif 22 <= value2 < 27:
            value2 = "22-26,9"
        elif 27 <= value2 < 31:
            value2 = "27-30,8"
        elif 31 <= value2 < 45:
            value2 = "31-44,8"

        value3 = int(input3)
        print(value3)
        if 1 <= value3 <= 10:
            value3 = "10"
        elif 10 < value3 <= 15:
            value3 = "15"
        elif 15 < value3 <= 20:
            value3 = "20"
        elif 20 < value3 <= 30:
            value3 = "30"
        elif 30 < value3 <= 40:
            value3 = "40"
        elif 40 < value3 <= 50:
            value3 = "50"

        result_3 = table.get(value2, "Р-")
        print(result_3)
        if result_3 == "Р-":
            res = result_3
        else:
            # print(f'---{value1}')
            result_2 = result_3.get(value3, "Р-")
            if result_2 == "Р-":
                res = result_2
            else:
                # print(result_2)
                result_1 = result_2[value1]
                # print(result_1)

                # result = self.tables[14].get((value2, value3, value1), "Результат не найден")
                res = result_1
                # with open("results.txt", "a") as file:
                #    file.write(f"Карта 4: {res}\n")

        return res


@register_node(OP_NODE_TABLE_8)
class CalcNode_table_4(CalcTable):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_8
    op_title = "К9 Св и нарез в глух"
    content_label = "кол-во отв. в дет."
    content_label_1 = "диаметр"
    content_label_2 = "глубина"
    content_label_3 = "Н/Ч"
    content_label_objname = "calc_node_bg_8"

    def evalOperation(self, input1, input2, input3):
        table = create_tables()[19]
        print(table)
        value1 = int(input1)
        if value1 == 1:
            value1 = 0
        elif value1 == 2:
            value1 = 1
        elif value1 == 3:
            value1 = 2
        elif value1 == 4:
            value1 = 3
        elif 5 <= value1 <= 6:
            value1 = 4
        elif 7 <= value1 <= 8:
            value1 = 5
        elif 9 <= value1 <= 12:
            value1 = 6
        elif 13 <= value1 <= 16:
            value1 = 7
        elif 17 <= value1 <= 20:
            value1 = 8
        elif 21 <= value1 <= 24:
            value1 = 9
        elif 25 <= value1 <= 28:
            value1 = 10
        elif 29 <= value1 <= 32:
            value1 = 11

        value2 = int(input2)
        print(value2)
        if 6 <= value2 < 11:
            value2 = "6м-10м"
        elif 11 <= value2 < 18:
            value2 = "12м-16м"
        elif 18 <= value2 < 22:
            value2 = "18м-22м"
        elif 22 <= value2 < 27:
            value2 = "24м-27м"
        elif 27 <= value2 < 31:
            value2 = "30м-33м"
        elif 31 <= value2 < 45:
            value2 = "36м-45м"

        value3 = int(input3)
        print(value3)
        if 1 <= value3 <= 10:
            value3 = "10"
        elif 10 < value3 <= 15:
            value3 = "15"
        elif 15 < value3 <= 20:
            value3 = "20"
        elif 20 < value3 <= 30:
            value3 = "30"
        elif 30 < value3 <= 40:
            value3 = "40"
        elif 40 < value3 <= 50:
            value3 = "50"

        result_3 = table.get(value2, "Р-")
        print(result_3)
        if result_3 == "Р-":
            res = result_3
        else:
            # print(f'---{value1}')
            result_2 = result_3.get(value3, "Р-")
            if result_2 == "Р-":
                res = result_2
            else:
                # print(result_2)
                result_1 = result_2[value1]
                # print(result_1)

                # result = self.tables[14].get((value2, value3, value1), "Результат не найден")
                res = result_1
                # with open("results.txt", "a") as file:
                #    file.write(f"Карта 4: {res}\n")

        return res


@register_node(OP_NODE_TABLE_9)
class CalcNode_table_4(CalcTable):
    icon = path_img_tab
    op_code = OP_NODE_TABLE_9
    op_title = "К10 Обр Сквоз отв"
    content_label = "диаметр"
    content_label_1 = "глубина"
    content_label_2 = "Класс точности"
    content_label_3 = "Н/Ч"
    content_label_objname = "calc_node_bg_9"

    def evalOperation(self, input1, input2, input3):
        table = create_tables()[20]
        print(table)
        value1 = int(input2)
        if 0 < value1 <= 10:
            value1 = 0
        elif 10 < value1 <= 20:
            value1 = 1
        elif 20 < value1 <= 30:
            value1 = 2
        elif 30 < value1 <= 40:
            value1 = 3
        elif 40 <= value1 <= 50:
            value1 = 4
        elif 50 <= value1 <= 60:
            value1 = 5
        elif 60 <= value1 <= 80:
            value1 = 6
        elif 80 <= value1 <= 100:
            value1 = 7
        elif 100 <= value1 <= 125:
            value1 = 8
        elif 125 <= value1 <= 150:
            value1 = 9
        elif 150 <= value1 <= 175:
            value1 = 10
        elif 175 <= value1 <= 200:
            value1 = 11

        value2 = int(input1)
        print(value2)
        if 0 < value2 <= 12:
            value2 = "12"
        elif 12 < value2 <= 15:
            value2 = "15"
        elif 15 < value2 <= 20:
            value2 = "20"
        elif 20 < value2 <= 25:
            value2 = "25"
        elif 25 < value2 <= 30:
            value2 = "30"
        elif 30 < value2 <= 40:
            value2 = "40"
        elif 40 < value2 <= 50:
            value2 = "50"
        elif 50 < value2 <= 60:
            value2 = "60"

        value3 = str(input3).upper()
        print(value3)
        if value3 == "А" or value3 == "1.0" or value3 == "A":
            value3 = "A"
        elif value3 == "Б" or value3 == "2.0" or value3 == "B":
            value3 = "B"
        elif value3 == "В" or value3 == "3.0" or value3 == "C":
            value3 = "C"

        result_3 = table.get(value2, "Р-")
        print(result_3)
        if result_3 == "Р-":
            res = result_3
        else:
            # print(f'---{value1}')
            result_2 = result_3.get(value3, "Р-")
            if result_2 == "Р-":
                res = result_2
            else:
                # print(result_2)
                result_1 = result_2[value1]
                # print(result_1)

                # result = self.tables[14].get((value2, value3, value1), "Результат не найден")
                res = result_1
                # with open("results.txt", "a") as file:
                #    file.write(f"Карта 4: {res}\n")

        return res


# way how to register by function call
# register_node_now(OP_NODE_ADD, CalcNode_Add)
