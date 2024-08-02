import math
from prettytable import PrettyTable as PT

sp = 0
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
    global sp
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
        sp = spindle_speed
        #print(round(spindle_speed))

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


d_list = [20, 50, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1250, 1500, 2000]
v_list = [63, 99, 79, 63, 99, 79, 63, 50, 94, 75, 59, 47, 101, 79, 63, 50, 98, 79, 63, 49, 94, 75, 59, 47, 96, 79, 63, 48, 99, 60, 50, 42, 90, 75, 64, 57, 101, 75, 60, 50, 94, 75, 63, 51, 90, 75, 61, 47, 101, 82, 63, 50]
s_list = [0.26, 0.28, 0.26, 0.23, 0.30, 0.28, 0.26, 0.23, 0.33, 0.30, 0.28, 0.26, 0.36, 0.33, 0.30, 0.28, 0.38, 0.36, 0.33, 0.30, 0.40, 0.38, 0.36, 0.33, 0.46, 0.40, 0.38, 0.36, 0.51, 0.46, 0.40, 0.38, 0.61, 0.51, 0.46, 0.40, 0.66, 0.51, 0.46, 0.40, 0.71, 0.51, 0.46, 0.40, 0.71, 0.51, 0.46, 0.40, 0.71, 0.51, 0.46, 0.40]
or_list = [10, 13, 18, 23]
t_list = [3, 5, 10, 15]
l_list = [10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 8000]
stst = []
ta = []

#print(len(v_list), len(s_list))
cont = 0
cont2 = 0

table_1 = PT()
table_1.field_names = ['D', 't', 'L', 10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 8000, "S", "N", "V"]


for i in range(len(d_list)):
    cont += 1
    for j in range(len(t_list)):
        if d_list[cont-1] == 20 and t_list[j] != 3:
            continue
        elif d_list[cont-1] == 50 and t_list[j] == 15:
            continue
        else:
            # print(d_list[cont-1], end=" ")
            # print(t_list[j], end=" ")
            # print(or_list[j], end=" ")
            # print(v_list[j], end=" ")
            # print(s_list[j], "\n")
            initial_diameter = d_list[cont-1] + t_list[j]  # начальный диаметр в мм
            final_diameter = d_list[cont-1]  # конечный диаметр в мм
            depth_of_cut = t_list[j] / 2  # глубина резания в мм (на сторону)
            cutting_speed = round(v_list[cont2])  # скорость резания в м/мин
            feed_rate_per_revolution = s_list[cont2]  # подача на один оборот в мм/об
            overrun = or_list[j]  # перебег резца в мм
            rapid_traverse_rate = 2000.0  # скорость возврата на ускоренной подаче в мм/мин
            stst.append(d_list[cont-1])
            stst.append(t_list[j])
            stst.append(or_list[j])
            for k in range(len(l_list)):
                #print(l_list[k], end="")
                length_of_workpiece = l_list[k]  # длина вала в мм
                time_required = calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, cutting_speed, feed_rate_per_revolution, overrun, rapid_traverse_rate) * 1.1
                #print(f"Во:{time_required:.2f}м", end=" ")
                # stst.append(d_list[cont-1])
                # stst.append(t_list[j])
                # stst.append(or_list[j])


                stst.append(round(time_required, 2))

            stst.append(feed_rate_per_revolution)
            stst.append(round(sp))
            stst.append(cutting_speed)
            cont2 += 1
            table_1.add_row(stst)
            #print(stst)
            stst.clear()




            #print("\n")



print(table_1)
input("для завершения нажмите 'Enter' ")
# for i in range(len(d_list)):
#     for j in range(len(t_list)):
#         #print(d_list[j])
#         if d_list[i] == 20 and t_list[j] != 3:
#             continue
#         elif d_list[i] == 50 and t_list[j] == 15:
#             continue
#         else:
#             pass
            #print(j)
            #depth_of_cut = t_list[j] / 2
            #print(depth_of_cut * 2)
            #initial_diameter = d_list[j]


            #time_required = calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, cutting_speed, feed_rate_per_revolution, overrun, rapid_traverse_rate) * 1.1


# initial_diameter = 200.0  # начальный диаметр в мм
# final_diameter = 197.0  # конечный диаметр в мм
# depth_of_cut = 1.5  # глубина резания в мм (на сторону)
# length_of_workpiece = 500.0  # длина вала в мм
# cutting_speed = 101  # скорость резания в м/мин
# feed_rate_per_revolution = 0.36  # подача на один оборот в мм/об
# overrun = 10.0  # перебег резца в мм
# rapid_traverse_rate = 2000.0  # скорость возврата на ускоренной подаче в мм/мин




#time_required = calculate_turning_time(initial_diameter, final_diameter, depth_of_cut, length_of_workpiece, cutting_speed, feed_rate_per_revolution, overrun, rapid_traverse_rate) * 1.1
#print(f"Время обработки: {time_required:.2f} минут")
