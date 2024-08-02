import math
import time


def calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, cutting_speed,
                           feed_rate_per_revolution, overrun, rapid_traverse_rate):
    """
    Рассчитывает время обработки вала с учетом перебега резца и возврата на ускоренной подаче.

    :param initial_diameter: начальный диаметр вала (мм)
    :param final_diameter: конечный диаметр вала (мм)
    :param depth_of_cut: глубина резания (мм)
    :param length_of_workpiece: длина вала (мм)
    :param cutting_speed: скорость резания (м/мин)
    :param feed_rate_per_revolution: подача на один оборот (мм/об)
    :param overrun: перебег резца (мм)
    :param rapid_traverse_rate: скорость возврата на ускоренной подаче (мм/мин)
    :return: время обработки в минутах
    """

    # Определение количества проходов
    total_depth = (initial_diameter - final_diameter) / 2
    number_of_passes = math.ceil(total_depth / depth_of_cut)

    # Общее время обработки
    total_time = 0

    for i in range(number_of_passes):
        # Диаметр после текущего прохода
        current_diameter = initial_diameter - 2 * depth_of_cut * (i + 1)
        #print(current_diameter)

        # Проверка, чтобы диаметр не стал меньше конечного
        if current_diameter < final_diameter:
            current_diameter = final_diameter


        # Пересчет частоты вращения шпинделя для текущего диаметра
        spindle_speed = (cutting_speed * 1000) / (math.pi * current_diameter)  # частота вращения в об/мин
        print(spindle_speed)

        # Подача инструмента в мм/мин
        feed_per_minute = feed_rate_per_revolution * spindle_speed

        # Длина прохода с учетом перебега
        total_length = length_of_workpiece + overrun

        # Время обработки для текущего прохода
        pass_time = total_length / feed_per_minute
        total_time += pass_time

        # Время возврата на ускоренной подаче
        return_time = (length_of_workpiece + overrun) / rapid_traverse_rate
        total_time += return_time

    return total_time



initial_diameter = 200.0  # начальный диаметр в мм
final_diameter = 197.0  # конечный диаметр в мм
depth_of_cut = 1.5  # глубина резания в мм (на сторону)
length_of_workpiece = 500.0  # длина вала в мм
cutting_speed = 101  # скорость резания в м/мин
feed_rate_per_revolution = 0.36  # подача на один оборот в мм/об
overrun = 10.0  # перебег резца в мм
rapid_traverse_rate = 2000.0  # скорость возврата на ускоренной подаче в мм/мин


# Пример использования функции
D = input("начальный диаметр в мм: ")
if D == "-":
    D = initial_diameter
else:
    D = float(D)

d = input("конечный диаметр в мм: ")
if d == "-":
    d = final_diameter
else:
    d = float(d)

t = input("глубина резания в мм (на сторону): ")
if t == "-":
    t = depth_of_cut
else:
    t = float(t)

L = input("длина вала в мм: ")
if L == "-":
    L = length_of_workpiece
else:
    L = float(L)

V = input("скорость резания в м/мин: ")
if V == "-":
    V = cutting_speed
else:
    V = float(V)

s = input("подача на один оборот в мм/об: ")
if s == "-":
    s = feed_rate_per_revolution
else:
    s = float(s)

LR = input("перебег резца в мм: ")
if LR == "-":
    LR = overrun
else:
    LR = float(LR)

SPEED = input("скорость возврата на ускоренной подаче в мм/мин: ")
if SPEED == "-":
    SPEED = rapid_traverse_rate
else:
    SPEED = float(SPEED)

time_required = calculate_turning_time(D, d, t, L, V, s, LR, SPEED) * 1.1
print(f"Время обработки: {time_required:.2f} минут")
input("для завершения нажмите 'Enter' ")
